from __future__ import annotations

from typing import Dict, Any, List, Tuple

import csv
import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QPlainTextEdit,
    QLabel,
    QFileDialog,
    QMessageBox,
    QTabWidget,
)
from PySide6.QtGui import QColor, QPainter
from PySide6.QtCharts import (
    QChartView,
    QChart,
    QPieSeries,
    QBarSeries,
    QBarSet,
    QBarCategoryAxis,
    QValueAxis,
)

from eml_forensic_suite.core.statistics import compute_forensic_stats, ForensicStats
from eml_forensic_suite.ui.i18n import t


class DashboardTab(QWidget):

    def retranslate(self, lang: str) -> None:
        self.lang = lang

        if self.btn_use_last is not None:
            self.btn_use_last.setText(t("dashboard.use_last_index", self.lang))
        if self.btn_open_csv is not None:
            self.btn_open_csv.setText(t("dashboard.open_csv", self.lang))
        if self.text_summary is not None:
            self.text_summary.setPlaceholderText(t("dashboard.placeholder", self.lang))

    def __init__(self, shared_state: Dict[str, Any], parent: QWidget | None = None):
        super().__init__(parent)
        self.shared_state = shared_state
        self.lang = str(shared_state.get("language", "fr"))

        self.current_entries: list[Dict[str, Any]] = []
        self.current_stats: ForensicStats | None = None

        self.text_summary: QPlainTextEdit | None = None
        self.label_source: QLabel | None = None

        self.chart_suspicion_view: QChartView | None = None
        self.chart_folders_view: QChartView | None = None
        self.chart_domains_view: QChartView | None = None
        self.chart_attachments_view: QChartView | None = None

        self._build_ui()
        self._load_initial_entries()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(8)

        btn_row = QHBoxLayout()

        self.btn_use_last = QPushButton(t("dashboard.use_last_index", self.lang), self)
        self.btn_use_last.clicked.connect(self._use_last_index)
        btn_row.addWidget(self.btn_use_last)

        self.btn_open_csv = QPushButton(t("dashboard.open_csv", self.lang), self)
        self.btn_open_csv.clicked.connect(self._open_csv)
        btn_row.addWidget(self.btn_open_csv)

        btn_row.addStretch(1)
        layout.addLayout(btn_row)

        self.label_source = QLabel("", self)
        layout.addWidget(self.label_source)

        self.tabs = QTabWidget(self)
        layout.addWidget(self.tabs, 1)

        tab_text = QWidget(self.tabs)
        text_layout = QVBoxLayout(tab_text)
        text_layout.setSpacing(6)

        self.text_summary = QPlainTextEdit(tab_text)
        self.text_summary.setReadOnly(True)
        self.text_summary.setPlaceholderText(t("dashboard.placeholder", self.lang))
        text_layout.addWidget(self.text_summary, 1)

        self.tabs.addTab(tab_text, t("dashboard.tab_text", self.lang))

        tab_graphs = QWidget(self.tabs)
        graphs_layout = QVBoxLayout(tab_graphs)
        graphs_layout.setSpacing(8)

        row1 = QHBoxLayout()
        self.chart_suspicion_view = self._create_chart_view()
        self.chart_folders_view = self._create_chart_view()
        row1.addWidget(self.chart_suspicion_view, 1)
        row1.addWidget(self.chart_folders_view, 1)
        graphs_layout.addLayout(row1)

        row2 = QHBoxLayout()
        self.chart_domains_view = self._create_chart_view()
        self.chart_attachments_view = self._create_chart_view()
        row2.addWidget(self.chart_domains_view, 1)
        row2.addWidget(self.chart_attachments_view, 1)
        graphs_layout.addLayout(row2)

        self.tabs.addTab(tab_graphs, t("dashboard.tab_graphs", self.lang))

    def _create_chart_view(self) -> QChartView:
        view = QChartView()
        view.setRenderHint(QPainter.Antialiasing, True)
        return view

    def _load_initial_entries(self) -> None:
        entries = self.shared_state.get("last_index_entries") or []
        if entries:
            self.current_entries = entries
            source = self.shared_state.get("last_index_csv") or ""
            if not source:
                self.label_source.setText(t("dashboard.source_memory", self.lang))
            else:
                self.label_source.setText(
                    t("dashboard.source_csv", self.lang, path=str(source))
                )
            self._recompute()

    def _use_last_index(self) -> None:
        entries = self.shared_state.get("last_index_entries") or []
        if not entries:
            QMessageBox.information(
                self,
                t("dashboard.no_index_title", self.lang),
                t("dashboard.no_index_body", self.lang),
            )
            return

        self.current_entries = entries
        source = self.shared_state.get("last_index_csv") or ""
        if not source:
            self.label_source.setText(t("dashboard.source_memory", self.lang))
        else:
            self.label_source.setText(
                t("dashboard.source_csv", self.lang, path=str(source))
            )
        self._recompute()

    def _open_csv(self) -> None:
        csv_path, _ = QFileDialog.getOpenFileName(
            self,
            t("dashboard.dialog_open_csv", self.lang),
            "",
            "Fichiers CSV (*.csv);;Tous les fichiers (*.*)",
        )
        if not csv_path:
            return

        if not os.path.isfile(csv_path):
            QMessageBox.warning(
                self,
                t("dashboard.error_csv_missing_title", self.lang),
                t("dashboard.error_csv_missing_body", self.lang, path=csv_path),
            )
            return

        try:
            entries: list[Dict[str, Any]] = []
            with open(csv_path, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    entries.append(dict(row))
        except Exception as e:
            QMessageBox.critical(
                self,
                t("dashboard.error_csv_read_title", self.lang),
                f"{t('dashboard.error_csv_read_body', self.lang, path=csv_path)}\n\n{e}",
            )
            return

        if not entries:
            QMessageBox.information(
                self,
                t("dashboard.empty_csv_title", self.lang),
                t("dashboard.empty_csv_body", self.lang),
            )
            return

        self.current_entries = entries
        self.label_source.setText(
            t("dashboard.source_csv", self.lang, path=str(csv_path))
        )
        self._recompute()

    def _recompute(self) -> None:
        if not self.current_entries:
            if self.text_summary:
                self.text_summary.clear()
                self.text_summary.setPlainText(t("dashboard.no_data", self.lang))
            self._clear_charts()
            return

        stats = compute_forensic_stats(self.current_entries)
        self.current_stats = stats

        self._update_text_summary(stats)
        self._update_charts(stats)

    def _update_text_summary(self, stats: ForensicStats) -> None:
        lines: list[str] = []

        lines.append("=== " + t("dashboard.section_overview", self.lang) + " ===")
        lines.append(
            t(
                "dashboard.overview_line",
                self.lang,
                total=stats.total_emails,
                senders=stats.distinct_senders,
            )
        )

        if stats.date_min and stats.date_max:
            lines.append(
                t(
                    "dashboard.dates_line",
                    self.lang,
                    date_min=stats.date_min,
                    date_max=stats.date_max,
                )
            )
        else:
            lines.append(t("dashboard.dates_unknown", self.lang))

        lines.append("")

        lines.append("=== " + t("dashboard.section_folders", self.lang) + " ===")
        for folder, count in stats.per_folder.items():
            lines.append(f"- {folder}: {count}")
        if not stats.per_folder:
            lines.append(t("dashboard.no_folders", self.lang))
        lines.append("")

        lines.append("=== " + t("dashboard.section_domains", self.lang) + " ===")
        top_domains = list(stats.per_domain.items())[:20]
        for domain, count in top_domains:
            lines.append(f"- {domain}: {count}")
        if not top_domains:
            lines.append(t("dashboard.no_domains", self.lang))
        lines.append("")

        lines.append("=== " + t("dashboard.section_attachments", self.lang) + " ===")
        lines.append(
            t(
                "dashboard.attachments_line",
                self.lang,
                with_att=stats.total_with_attachments,
                total=stats.total_emails,
                total_att=stats.total_attachments,
            )
        )
        lines.append("")

        lines.append("=== " + t("dashboard.section_auth", self.lang) + " ===")
        lines.append(t("dashboard.auth_header_dkim", self.lang))
        for k, v in stats.dkim_counts.items():
            lines.append(f"  - {k}: {v}")
        lines.append(t("dashboard.auth_header_spf", self.lang))
        for k, v in stats.spf_counts.items():
            lines.append(f"  - {k}: {v}")
        lines.append(t("dashboard.auth_header_dmarc", self.lang))
        for k, v in stats.dmarc_counts.items():
            lines.append(f"  - {k}: {v}")
        lines.append("")

        lines.append("=== " + t("dashboard.section_integrity", self.lang) + " ===")
        if stats.integrity_flag_counts:
            lines.append(t("dashboard.integrity_flags_title", self.lang))
            for flag, count in stats.integrity_flag_counts.items():
                lines.append(f"  - {flag}: {count}")
        else:
            lines.append(t("dashboard.no_integrity_flags", self.lang))

        lines.append("")
        lines.append("=== " + t("dashboard.section_received", self.lang) + " ===")
        if stats.received_anomaly_counts:
            for flag, count in stats.received_anomaly_counts.items():
                lines.append(f"  - {flag}: {count}")
        else:
            lines.append(t("dashboard.no_received_anomalies", self.lang))

        lines.append("")
        lines.append("=== " + t("dashboard.section_suspicion", self.lang) + " ===")

        if stats.suspicion_score_min is None:
            lines.append(t("dashboard.no_suspicion_data", self.lang))
        else:
            avg_str = (
                f"{stats.suspicion_score_avg:.1f}"
                if stats.suspicion_score_avg is not None
                else "N/A"
            )

            lines.append(
                t(
                    "dashboard.suspicion_scores_line",
                    self.lang,
                    min=stats.suspicion_score_min,
                    max=stats.suspicion_score_max,
                    avg=avg_str,
                )
            )

            if stats.suspicion_level_counts:
                lines.append(t("dashboard.suspicion_levels_title", self.lang))
                for level, count in stats.suspicion_level_counts.items():
                    lines.append(f"  - {level}: {count}")
            else:
                lines.append(t("dashboard.no_suspicion_levels", self.lang))

        if self.text_summary:
            self.text_summary.setPlainText("\n".join(lines))

    def _clear_charts(self) -> None:
        for view in [
            self.chart_suspicion_view,
            self.chart_folders_view,
            self.chart_domains_view,
            self.chart_attachments_view,
        ]:
            if view is not None:
                view.setChart(QChart())

    def _update_charts(self, stats: ForensicStats) -> None:
        if self.chart_suspicion_view:
            self.chart_suspicion_view.setChart(self._build_suspicion_chart(stats))
        if self.chart_folders_view:
            self.chart_folders_view.setChart(self._build_folders_chart(stats))
        if self.chart_domains_view:
            self.chart_domains_view.setChart(self._build_domains_chart(stats))
        if self.chart_attachments_view:
            self.chart_attachments_view.setChart(self._build_attachments_chart(stats))

    def _build_suspicion_chart(self, stats: ForensicStats) -> QChart:
        chart = QChart()
        chart.setTitle(t("dashboard.chart_suspicion_title", self.lang))
        chart.setAnimationOptions(QChart.AllAnimations)

        series = QPieSeries()

        if not stats.suspicion_level_counts:
            slice_unknown = series.append(t("dashboard.suspicion_unknown", self.lang), 1)
            slice_unknown.setBrush(QColor("#BDBDBD"))
        else:
            ordered_levels: List[Tuple[str, str, str]] = [
                ("HIGH", "🔴", "#e53935"),
                ("MEDIUM", "🟠", "#fb8c00"),
                ("LOW", "🟢", "#43a047"),
            ]

            used_levels = set()

            for level_key, emoji, color in ordered_levels:
                count = stats.suspicion_level_counts.get(level_key, 0)
                if count <= 0:
                    continue
                used_levels.add(level_key)
                label = f"{emoji} {level_key} ({count})"
                slice_ = series.append(label, count)
                slice_.setBrush(QColor(color))

            for raw_level, count in stats.suspicion_level_counts.items():
                level = (raw_level or "").upper()
                if level in used_levels or count <= 0:
                    continue
                label = f"{level} ({count})"
                slice_ = series.append(label, count)
                slice_.setBrush(QColor("#9e9e9e"))

        chart.addSeries(series)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        return chart

    def _build_folders_chart(self, stats: ForensicStats) -> QChart:
        chart = QChart()
        chart.setTitle(t("dashboard.chart_folders_title", self.lang))
        chart.setAnimationOptions(QChart.SeriesAnimations)

        if not stats.per_folder:
            return chart

        items = list(stats.per_folder.items())
        items.sort(key=lambda kv: kv[1], reverse=True)
        top = items[:10]

        series = QBarSeries()
        bar_set = QBarSet(t("dashboard.chart_folders_serie", self.lang))

        categories: List[str] = []
        for folder, count in top:
            bar_set.append(count)
            categories.append(folder or "(?)")

        bar_set.setColor(QColor("#1e88e5"))
        series.append(bar_set)

        chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        axis_x.setLabelsAngle(45)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setLabelFormat("%d")
        axis_y.setTitleText(t("dashboard.chart_axis_count", self.lang))
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        chart.legend().setVisible(False)

        return chart

    def _build_domains_chart(self, stats: ForensicStats) -> QChart:
        chart = QChart()
        chart.setTitle(t("dashboard.chart_domains_title", self.lang))
        chart.setAnimationOptions(QChart.SeriesAnimations)

        if not stats.per_domain:
            return chart

        items = list(stats.per_domain.items())
        items.sort(key=lambda kv: kv[1], reverse=True)
        top = items[:10]

        series = QBarSeries()
        bar_set = QBarSet(t("dashboard.chart_domains_serie", self.lang))

        categories: List[str] = []
        for domain, count in top:
            bar_set.append(count)
            categories.append(domain or "(?)")

        bar_set.setColor(QColor("#8e24aa"))
        series.append(bar_set)

        chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        axis_x.setLabelsAngle(45)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setLabelFormat("%d")
        axis_y.setTitleText(t("dashboard.chart_axis_count", self.lang))
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        chart.legend().setVisible(False)

        return chart

    def _build_attachments_chart(self, stats: ForensicStats) -> QChart:
        chart = QChart()
        chart.setTitle(t("dashboard.chart_attachments_title", self.lang))
        chart.setAnimationOptions(QChart.AllAnimations)

        series = QPieSeries()

        if stats.total_emails <= 0:
            chart.addSeries(series)
            return chart

        with_att = stats.total_with_attachments
        without_att = max(stats.total_emails - with_att, 0)

        slice_with = series.append(
            t("dashboard.chart_attachments_with", self.lang),
            with_att,
        )
        slice_with.setBrush(QColor("#43a047"))

        slice_without = series.append(
            t("dashboard.chart_attachments_without", self.lang),
            without_att,
        )
        slice_without.setBrush(QColor("#757575"))

        chart.addSeries(series)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        return chart
