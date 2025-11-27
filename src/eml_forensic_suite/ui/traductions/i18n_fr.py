from __future__ import annotations

from typing import Dict

TRANSLATIONS_FR: Dict[str, str] = {
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    "app.title": "Suite forensic EML / IMAP (lecture seule)",

    # ------------------------------------------------------------------
    # Menus
    # ------------------------------------------------------------------
    "menu.file": "Fichier",
    "menu.view": "Affichage",
    "menu.help": "Aide",

    "menu.file.settings": "Paramètres…",
    "menu.file.quit": "Quitter",

    "menu.view.theme.dark": "Thème sombre",
    "menu.view.theme.light": "Thème clair",

    "menu.help.about": "À propos…",

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------
    "tab.imap": "1. Export IMAP",
    "tab.index": "2. Indexation EML",
    "tab.viewer": "3. Viewer forensic",
    "tab.dashboard": "4. Dashboard forensic",

    # ------------------------------------------------------------------
    # Settings dialog
    # ------------------------------------------------------------------
    "settings.title": "Paramètres",
    "settings.reports_dir.label": "Dossier de travail / rapports :",
    "settings.reports_dir.browse": "Parcourir…",
    "settings.language.label": "Langue de l’interface :",
    "settings.reports_dir.dialog_title": "Choisir le dossier de travail / rapports",

    # ------------------------------------------------------------------
    # Divers / Status
    # ------------------------------------------------------------------
    "status.ready": "Prêt.",
    "status.settings.saved": "Paramètres enregistrés.",

    # ------------------------------------------------------------------
    # Index tab
    # ------------------------------------------------------------------
    "index.folder_label": "Dossier d’export EML :",
    "index.browse": "Parcourir…",
    "index.use_last_export": "Utiliser le dernier export IMAP",
    "index.log_placeholder": "Journal d’indexation EML (lecture seule)…",
    "index.start_button": "Lancer l’indexation EML",
    "index.dialog_select_folder": "Sélectionner le dossier d’export EML",
    "index.no_last_export": "Aucun export IMAP connu pour l’instant (onglet 1).",
    "index.error_already_running_title": "Indexation déjà en cours",
    "index.error_already_running_body": "Une indexation EML est déjà en cours.",
    "index.error_no_folder_title": "Dossier manquant",
    "index.error_no_folder_body": "Merci de sélectionner un dossier contenant les fichiers .eml.",
    "index.error_invalid_folder_title": "Dossier invalide",
    "index.error_invalid_folder_body": "Le dossier spécifié n’existe pas :\n{folder}",
    "index.status_selected_folder": "Dossier sélectionné pour indexation : {folder}",
    "index.error_indexing_title": "Erreur lors de l’indexation",
    "index.error_log": "❌ Erreur : {error}",
    "index.done_log_success": "\nIndexation terminée avec succès.",
    "index.done_log_path": "Chemin du CSV : {csv_path}",
    "index.done_log_count": "Nombre d’entrées indexées : {count}",
    "index.done_msg_title": "Indexation terminée",
    "index.done_msg_body": (
        "Indexation EML terminée.\n\nFichier CSV : {csv_path}\nEntrées : {count}"
    ),

    # ------------------------------------------------------------------
    # Dashboard tab (base)
    # ------------------------------------------------------------------
    "dashboard.use_last_index": "Utiliser le dernier index",
    "dashboard.open_csv": "Ouvrir un index CSV…",
    "dashboard.placeholder": "Résumé statistique forensic basé sur l’index EML…",
    "dashboard.source_memory": (
        "Source : index en mémoire (dernière indexation de la session)."
    ),
    "dashboard.source_csv": "Source : {path}",
    "dashboard.no_index_title": "Aucun index",
    "dashboard.no_index_body": (
        "Aucun index n’est disponible dans la session.\n"
        "Générez un index dans l’onglet 2 ou ouvrez un CSV manuellement."
    ),
    "dashboard.dialog_open_csv": "Ouvrir un fichier index CSV",
    "dashboard.error_csv_missing_title": "Fichier introuvable",
    "dashboard.error_csv_missing_body": "Le fichier spécifié n’existe pas :\n{path}",
    "dashboard.error_csv_read_title": "Erreur de lecture CSV",
    "dashboard.error_csv_read_body": "Impossible de lire le fichier CSV : {path}",
    "dashboard.empty_csv_title": "Index vide",
    "dashboard.empty_csv_body": "Le fichier CSV ne contient aucune entrée exploitable.",
    "dashboard.no_data": "Aucune donnée à analyser.",

    "dashboard.section_overview": "Vue d’ensemble",
    "dashboard.overview_line": (
        "Total emails : {total} – Expéditeurs distincts : {senders}"
    ),
    "dashboard.dates_line": "Période couverte : {date_min} → {date_max}",
    "dashboard.dates_unknown": "Dates non exploitables ou absentes.",

    "dashboard.section_folders": "Répartition par dossier IMAP",
    "dashboard.no_folders": "Aucun dossier IMAP détecté.",

    "dashboard.section_domains": "Répartition par domaine (expéditeur)",
    "dashboard.no_domains": "Aucun domaine détecté.",

    "dashboard.section_attachments": "Pièces jointes",
    "dashboard.attachments_line": (
        "Emails avec pièces jointes : {with_att}/{total} – Total de PJ estimé : {total_att}"
    ),

    "dashboard.section_auth": "Authentification (DKIM / SPF / DMARC)",
    "dashboard.auth_header_dkim": "Résultats DKIM :",
    "dashboard.auth_header_spf": "Résultats SPF :",
    "dashboard.auth_header_dmarc": "Résultats DMARC :",

    "dashboard.section_integrity": "Intégrité / en-têtes manquants",
    "dashboard.integrity_flags_title": "Flags d’intégrité détectés :",
    "dashboard.no_integrity_flags": "Aucun flag d’intégrité spécifique détecté.",

    "dashboard.section_received": "Anomalies sur la chaîne Received",
    "dashboard.no_received_anomalies": (
        "Aucune anomalie Received détectée (dans les règles actuelles)."
    ),

    # ------------------------------------------------------------------
    # Viewer tab – colonnes de base
    # ------------------------------------------------------------------
    "viewer.col.folder_imap": "Dossier IMAP",
    "viewer.col.sequence_number": "Séquence",
    "viewer.col.date_header": "Date",
    "viewer.col.from_header": "From",
    "viewer.col.to_header": "To",
    "viewer.col.cc_header": "Cc",
    "viewer.col.cci_header": "Cci",
    "viewer.col.subject": "Sujet",
    "viewer.col.message_id": "Message-ID",
    "viewer.col.sha256": "SHA-256",
    "viewer.col.has_attachments": "PJ ?",
    "viewer.col.attachment_count": "Nb PJ",
    "viewer.col.attachment_filenames": "Noms PJ",
    "viewer.col.dkim_result": "DKIM",
    "viewer.col.spf_result": "SPF",
    "viewer.col.dmarc_result": "DMARC",
    "viewer.col.auth_comment": "Authentication-Results (extrait)",
    "viewer.col.received_count": "Nb Received",
    "viewer.col.received_anomalies": "Anomalies Received",
    "viewer.col.integrity_flags": "Flags intégrité",
    "viewer.col.relative_path": "Chemin relatif",
    "viewer.col.filename": "Nom de fichier",

    # ------------------------------------------------------------------
    # Viewer tab – recherche + zones
    # ------------------------------------------------------------------
    "viewer.search_label": "Recherche :",
    "viewer.search_placeholder": "Filtrer dans l’index (toutes colonnes)…",
    "viewer.search_clear": "Effacer",

    "viewer.headers_label": "En-têtes",
    "viewer.headers_placeholder": "En-têtes du message sélectionné…",

    "viewer.body_label": "Corps (texte)",
    "viewer.body_placeholder": (
        "Corps text/plain (ou fallback HTML brut) du message sélectionné…"
    ),

    "viewer.btn_load_last": "Utiliser le dernier export IMAP",
    "viewer.btn_open_csv": "Ouvrir un index CSV...",
    "viewer.attachments_label": "Pièces jointes",

    # ------------------------------------------------------------------
    # Viewer – erreurs EML
    # ------------------------------------------------------------------
    "viewer.error_missing_eml_title": "Fichier EML introuvable",
    "viewer.error_missing_eml_body": (
        "Impossible de trouver le fichier EML sur le disque :\n{path}"
    ),
    "viewer.error_parse_eml_title": "Erreur de lecture EML",
    "viewer.error_parse_eml_body": (
        "Impossible de parser le fichier EML : {path}"
    ),

    # ------------------------------------------------------------------
    # Viewer – colonnes PJ
    # ------------------------------------------------------------------
    "viewer.attach.col.name": "Nom",
    "viewer.attach.col.mime": "MIME",
    "viewer.attach.col.size": "Taille (octets)",
    "viewer.attach.col.sha256": "SHA-256",
    "viewer.attach.col.suspicious": "Suspect ?",

    "viewer.attach.yes": "Oui",
    "viewer.attach.no": "Non",

    # ------------------------------------------------------------------
    # IMAP tab – connexion & champs
    # ------------------------------------------------------------------
    "imap.group.connection": "Serveur IMAP (source de preuve)",
    "imap.label.host": "Adresse du serveur IMAP",
    "imap.label.user": "Identifiant de la boîte analysée",
    "imap.label.password": "Mot de passe (jamais stocké)",
    "imap.label.date_start": "Date de début (filtre forensic)",
    "imap.label.date_end": "Date de fin (filtre forensic)",

    "imap.placeholder.host": "ex. imap.example.com",
    "imap.placeholder.user": "ex. incident@entreprise.be",
    "imap.placeholder.password": "Mot de passe du compte analysé",
    "imap.placeholder.date_start": "JJ/MM/AAAA (optionnel)",
    "imap.placeholder.date_end": "JJ/MM/AAAA (optionnel)",

    "imap.button.fetch_mailboxes": "Inspecter les dossiers IMAP…",
    "imap.button.start_export": "Lancer l’extraction forensic",
    "imap.button.cancel_export": "Annuler l’extraction",

    "imap.label.mailboxes_title": (
        "Dossiers IMAP à extraire (source de preuve) :"
    ),
    "imap.checkbox.select_all": "Sélectionner tous les dossiers",

    "imap.log.placeholder": (
        "Journal de l’extraction IMAP (lecture seule, horodaté)…"
    ),

    # ------------------------------------------------------------------
    # IMAP tab – erreurs / infos génériques
    # ------------------------------------------------------------------
    "imap.error.missing_fields.title": "Paramètres incomplets",
    "imap.error.missing_fields.body": (
        "Merci de renseigner le serveur IMAP, l’identifiant et le mot de passe."
    ),

    "imap.info.export_running.title": "Extraction déjà en cours",
    "imap.info.export_running.body": "Une extraction IMAP est déjà en cours.",

    "imap.error.date_invalid.title": "Date invalide",
    "imap.error.date_invalid.body": "Erreur dans les dates saisies : {error}",
    "imap.error.date_end_before_start.body": (
        "La date de fin ne peut pas être antérieure à la date de début."
    ),

    "imap.error.no_mailbox_selected.title": "Aucun dossier sélectionné",
    "imap.error.no_mailbox_selected.body": (
        "Merci de sélectionner au moins un dossier IMAP à extraire."
    ),

    "imap.error.fetch_mailboxes.title": "Erreur IMAP",
    "imap.error.fetch_mailboxes.body": (
        "Impossible de récupérer la liste des dossiers IMAP :\n{error}"
    ),

    "imap.info.generic.title": "Information",
    "imap.error.generic.title": "Erreur",

        # ------------------------------------------------------------------
    # IMAP exporter
    # ------------------------------------------------------------------
    "imap.log.connecting": "Connexion à {host}:{port} (SSL={use_ssl})...",
    "imap.log.connected": "Connecté au serveur IMAP.",
    "imap.log.select_folder": "Sélection du dossier « {folder} »...",
    "imap.log.folder_selected": "Dossier « {folder} » sélectionné.",
    "imap.log.message_count": "{count} messages à exporter.",
    "imap.log.fetching": "Récupération des messages IMAP...",
    "imap.log.export_done": "Export IMAP terminé.",
    "imap.log.saving_to": "Enregistrement des messages dans « {output_dir} »...",
    "imap.log.progress": "Export du message {current}/{total}...",
    "imap.log.skip_existing": "Le fichier « {path} » existe déjà, saut.",

    "imap.error.connect_failed": "Impossible de se connecter à {host}:{port} : {error}",
    "imap.error.login_failed": "Erreur d'authentification IMAP : {error}",
    "imap.error.select_failed": "Impossible de sélectionner le dossier « {folder} » : {error}",
    "imap.error.fetch_failed": "Erreur lors de la récupération des messages : {error}",
    "imap.error.generic": "Erreur lors de l'export IMAP : {error}",

        # ------------------------------------------------------------------
    # IMAP - Rapport d'export
    # ------------------------------------------------------------------
    "imap.report.title": "=== Rapport d'export IMAP (lecture seule) ===",
    "imap.report.tool_line": "Outil      : eml_forensic_suite – export IMAP",
    "imap.report.version_line": "Version    : {version}",
    "imap.report.folder_line": "Dossier    : {export_dir}",

    "imap.report.section_tool": "---- Informations sur l'outil ----",
    "imap.report.tool_path": "Chemin de l'outil       : {tool_path}",
    "imap.report.tool_hash": "SHA-256 de l'outil      : {tool_hash}",

    "imap.report.section_env": "---- Environnement d'exécution ----",
    "imap.report.env_os": "Système d'exploitation : {os_system} {os_release} ({os_version}) / {machine}",
    "imap.report.env_python": "Version Python          : {python_version}",

    "imap.report.section_context": "---- Contexte IMAP / compte ----",
    "imap.report.context_host": "Serveur IMAP : {host}",
    "imap.report.context_user": "Compte      : {user}",
    "imap.report.context_date_start": "Date début demandée : {date_start}",
    "imap.report.context_date_end": "Date fin demandée   : {date_end}",
    "imap.report.context_criteria": "Critères IMAP       : {search_criteria} (tels qu'envoyés au serveur)",

    "imap.report.selected_folders_title": "Dossiers sélectionnés :",
    "imap.report.selected_folder_item": "  - {folder}",

    "imap.report.section_server": "---- Informations serveur IMAP ----",
    "imap.report.server_greeting": "Bannière IMAP : {greeting}",
    "imap.report.server_capability": "CAPABILITY    : {capability}",

    "imap.report.section_timestamps": "---- Horodatage de l'analyse ----",
    "imap.report.timestamp_start_utc": "Début analyse (UTC)   : {dt}",
    "imap.report.timestamp_start_local": "Début analyse (local) : {dt}",
    "imap.report.timestamp_end_utc": "Fin analyse (UTC)     : {dt}",
    "imap.report.timestamp_end_local": "Fin analyse (local)   : {dt}",
    "imap.report.duration": "Durée totale          : {duration}",

    "imap.report.section_folders": "---- Dossiers analysés ----",
    "imap.report.folders_count": "Nombre de dossiers sélectionnés : {count}",

    "imap.report.folder_header": "Dossier : {name}",
    "imap.report.folder_messages": "  Messages trouvés (période) : {count}",
    "imap.report.folder_exported": "  Messages exportés          : {count}",
    "imap.report.folder_errors": "  Erreurs de fetch           : {count}",
    "imap.report.folder_bytes": "  Volume téléchargé          : {bytes} octets",
    "imap.report.folder_size_stats": "  Taille min / max / moyenne : {min_size} / {max_size} / {avg_size} octets",
    "imap.report.folder_period": "  Période couverte (INTERNALDATE) : {first} → {last}",
    "imap.report.folder_error_uids": "  UIDs en erreur (liste non exhaustive) : {uids}",

    "imap.report.section_totals": "---- Totaux globaux ----",
    "imap.report.total_messages": "Messages trouvés (tous dossiers) : {count}",
    "imap.report.total_exported": "Messages exportés                : {count}",
    "imap.report.total_errors": "Erreurs de fetch                 : {count}",
    "imap.report.total_bytes": "Volume total téléchargé          : {bytes} octets",

    "imap.report.section_forensic": "---- Méthodologie et garanties forensic ----",
    "imap.report.forensic_item_readonly": "- L'outil n'a utilisé que des commandes IMAP en lecture seule (SELECT en readonly, SEARCH, FETCH). Aucun message n'a été modifié, supprimé ou marqué comme lu pendant l'analyse.",
    "imap.report.forensic_item_eml": "- Les messages ont été exportés tels que fournis par le serveur IMAP, et écrits sur disque en format .eml sans altération du contenu.",
    "imap.report.forensic_item_hashes": "- Chaque message exporté est associé à un hash SHA-256, listé dans le fichier hashes.txt, ainsi qu'à un hash global calculé sur la concaténation de tous les hashes individuels.",
    "imap.report.forensic_item_report_hash": "- Le présent rapport d'analyse est lui-même hashé en SHA-256, et ce hash est ajouté à hashes.txt pour garantir l'intégrité du rapport.",

    "imap.report.hashes_report_header": "RAPPORT D'ANALYSE :",
    "imap.report.hashes_report_line": "{filename} : {file_hash}",

    # ------------------------------------------------------------------
    # IMAP - Worker d'export (logs, erreurs, résumé)
    # ------------------------------------------------------------------
    "imap.worker.error_no_folder_selected": "Aucun dossier sélectionné.",
    "imap.worker.log_export_dir": "Dossier d'export : {export_dir}",
    "imap.worker.tool_hash_error": "(erreur lors du calcul du hash de l'outil)",

    "imap.worker.log_connecting": "Connexion au serveur IMAP...",
    "imap.worker.greeting_not_available": "(bannière IMAP non disponible)",
    "imap.worker.log_auth_classic": "Authentification IMAP classique...",
    "imap.worker.error_auth_failed": "Erreur d'authentification IMAP : {error}",
    "imap.worker.capability_error": "(erreur lors de la commande CAPABILITY)",

    "imap.worker.log_date_start_inclusive": "Date de début (incluse) : {date} → IMAP SINCE {imap_since}",
    "imap.worker.log_date_start_unset": "Date de début : non renseignée → extraction depuis le premier message disponible.",
    "imap.worker.date_start_unset_label": "Premier message disponible (pas de limite basse)",

    "imap.worker.log_date_end_inclusive": "Date de fin (incluse) : {date} → IMAP BEFORE {imap_before}",
    "imap.worker.log_date_end_unset": "Date de fin : non renseignée → jusqu'à la dernière date disponible sur le serveur.",
    "imap.worker.date_end_unset_label": "Dernier message disponible (pas de limite haute)",

    "imap.worker.log_criteria": "Critères IMAP utilisés : {criteria}",
    "imap.worker.log_selected_folders_header": "Dossiers sélectionnés ({count}) :",
    "imap.worker.log_selected_folder_item": "  - {folder}",

    "imap.worker.log_stop_during_count": "Arrêt demandé pendant la phase de comptage.",
    "imap.worker.log_phase1_count": "[Phase 1] Comptage des messages dans {folder}...",
    "imap.worker.log_select_folder_failed": "  ⚠️ Impossible de sélectionner ce dossier, on passe au suivant.",
    "imap.worker.log_search_folder_failed": "  ⚠️ Erreur lors de la recherche dans ce dossier, on passe au suivant.",
    "imap.worker.log_messages_to_process": "  → {count} messages à traiter dans {folder}",

    "imap.worker.log_total_messages_to_download": "Nombre total de messages à télécharger (tous dossiers) : {count}",

    "imap.worker.log_stop_during_export": "Arrêt demandé : on interrompt l'extraction.",
    "imap.worker.log_folder_header": "=== Dossier : {folder} ===",
    "imap.worker.log_no_messages_in_period": "  Aucun message dans {folder} pour cette période.",
    "imap.worker.log_folder_message_count": "  Nombre de messages trouvés dans {folder} : {count}",
    "imap.worker.log_reselect_folder_failed": "  ⚠️ Impossible de re-sélectionner ce dossier, on passe au suivant.",

    "imap.worker.log_first_message_download": "  Téléchargement du premier message ({uid})...",
    "imap.worker.log_folder_progress": "  Progression dossier {folder} : {current}/{total} (dernier : {last_uid})",
    "imap.worker.log_fetch_error_message": "    ⚠️ Erreur lors du fetch du message {uid}, on continue.",
    "imap.worker.log_folder_end": "  Fin du dossier {folder}",

    "imap.worker.hashes_header": "Liste des fichiers exportés et leurs hashes SHA-256",
    "imap.worker.hashes_file_line": "{path} : {file_hash}",
    "imap.worker.hashes_global_header": "HASH GLOBAL (messages uniquement) :",

    "imap.worker.log_export_done_header": "=== Export terminé ===",
    "imap.worker.log_export_done_count": "Nombre total de messages exportés : {count}",
    "imap.worker.log_export_done_hashes_file": "Fichier des hashes : {path}",
    "imap.worker.log_export_done_hash": "HASH GLOBAL : {file_hash}",

    "imap.worker.summary": (
        "Extraction terminée.\n\n"
        "Messages exportés : {count}\n"
        "Dossier : {export_dir}\n\n"
        "Hash global (messages) :\n{file_hash}"
    ),

    "imap.worker.log_report_generated": "Rapport d'analyse généré et hashé (voir rapport_imap_export.txt et hashes.txt).",
    "imap.worker.log_report_failed": "⚠️ Impossible de générer le rapport d'analyse : {error}",

    "imap.worker.error_generic": "Une erreur est survenue : {error}",

        # ------------------------------------------------------------------
    # IMAP - Interface Tk (liste des dossiers)
    # ------------------------------------------------------------------
    "imap.tk.log_connecting": "Connexion au serveur IMAP...",
    "imap.tk.log_auth_classic": "Authentification IMAP classique...",
    "imap.tk.error_list_mailboxes_failed": "Impossible de lister les dossiers IMAP.",

    "imap.tk.log_folders_found_header": "Dossiers trouvés sur le serveur :",
    "imap.tk.log_folder_item": "  - {folder}",
    "imap.tk.log_folders_count": "Total dossiers IMAP : {count}",

    "imap.tk.msgbox_error_title": "Erreur",
    "imap.tk.msgbox_error_fetch_mailboxes": "Erreur lors de la récupération des dossiers IMAP : {error}",
    "imap.tk.log_error_fetch_mailboxes": "❌ Erreur lors de la récupération des dossiers : {error}",

        # ------------------------------------------------------------------
    # IMAP - Interface Tk (onglet complet)
    # ------------------------------------------------------------------
    "imap.tk.tab_title": "1. Export IMAP",

    "imap.tk.label_server": "Serveur IMAP :",
    "imap.tk.label_email": "Adresse e-mail :",
    "imap.tk.label_password": "Mot de passe :",
    "imap.tk.label_date_start": "Date de début (JJ/MM/AAAA, optionnelle) :",
    "imap.tk.label_date_end": "Date de fin (JJ/MM/AAAA, optionnelle) :",
    "imap.tk.label_log": "Journal :",
    "imap.tk.label_mailboxes": "Dossiers IMAP à exporter :",
    "imap.tk.checkbox_select_all": "Tout cocher / Tout décocher",
    "imap.tk.label_progress": "Progression :",

    "imap.tk.msgbox_missing_fields_title": "Champs manquants",
    "imap.tk.msgbox_missing_fields_text": "Merci de remplir le serveur, l'e-mail et le mot de passe.",

    "imap.tk.log_fetch_mailboxes_start": "Récupération des dossiers IMAP...",
    "imap.tk.log_no_mailboxes_or_error": "Aucun dossier trouvé ou erreur.",
    "imap.tk.log_select_mailboxes_hint": "Sélectionnez les dossiers à exporter.",

    "imap.tk.button_list_mailboxes": "Lister les dossiers IMAP",

    "imap.tk.msgbox_date_start_invalid_title": "Date de début invalide",
    "imap.tk.msgbox_date_start_invalid_text": "La date de début doit être au format JJ/MM/AAAA.",

    "imap.tk.msgbox_date_end_invalid_title": "Date de fin invalide",
    "imap.tk.msgbox_date_end_invalid_text": "La date de fin doit être au format JJ/MM/AAAA.",

    "imap.tk.msgbox_date_range_invalid_title": "Plage de dates invalide",
    "imap.tk.msgbox_date_range_invalid_text": (
        "La date de fin ne peut pas être antérieure à la date de début."
    ),

    "imap.tk.msgbox_no_mailbox_selected_title": "Aucun dossier sélectionné",
    "imap.tk.msgbox_no_mailbox_selected_text": (
        "Merci de sélectionner au moins un dossier IMAP (via 'Lister les dossiers IMAP')."
    ),

    "imap.tk.log_export_start": "Démarrage de l'extraction...",
    "imap.tk.button_run_export": "Lancer l'extraction (dossiers cochés)",

    "imap.tk.log_stop_requested": (
        "Arrêt demandé, l'extraction va se terminer proprement..."
    ),
    "imap.tk.button_stop_export": "Arrêter l'extraction",

    "imap.tk.msgbox_export_done_title": "Extraction terminée",




    # ------------------------------------------------------------------
    # IMAP tab – logs
    # ------------------------------------------------------------------
    "imap.log.connect_list": (
        "Connexion au serveur IMAP pour énumérer les dossiers…"
    ),
    "imap.log.fetch_error": "❌ Erreur lors de la récupération des dossiers :",
    "imap.log.no_mailboxes": "Aucun dossier IMAP trouvé sur ce compte.",
    "imap.log.mailboxes_found": "Dossiers trouvés sur le serveur :",
    "imap.log.mailboxes_total": "Total dossiers IMAP : {count}",
    "imap.log.mailboxes_select_hint": (
        "Sélectionnez les dossiers à extraire en lecture seule."
    ),
    "imap.log.start_export": (
        "Démarrage de l’extraction IMAP (mode forensic, lecture seule)…"
    ),
    "imap.log.cancel_requested": (
        "Demande d’annulation envoyée au worker IMAP…"
    ),
    "imap.log.export_dir_saved": "Dossier d’export enregistré : {path}",
    "imap.log.done": "Traitement IMAP terminé.",

    # ------------------------------------------------------------------
    # Dashboard v3 – sections / onglets
    # ------------------------------------------------------------------
    "dashboard.section_scoring": "Niveaux de suspicion",
    "dashboard.tab_text": "Résumé de l'index EML",
    "dashboard.tab_graphs": "Graphiques",
    "dashboard.section_charts": "Visualisations graphiques",

    "dashboard.chart_suspicion_title": "Répartition des niveaux de suspicion",
    "dashboard.chart_folders_title": "Messages par dossier IMAP",
    "dashboard.chart_domains_title": "Domaines d'expéditeur les plus fréquents",
    "dashboard.chart_attachments_title": "Présence de pièces jointes",
    "dashboard.chart_axis_count": "Nombre",
    "dashboard.chart_attachments_with": "Avec pièces jointes",
    "dashboard.chart_attachments_without": "Sans pièces jointes",

    # Légende / texte autour du scoring
    "dashboard.suspicion_distribution_line": (
        "Répartition des emails par niveau de suspicion :"
    ),
    "dashboard.suspicion_level.LOW": "Faible",
    "dashboard.suspicion_level.MEDIUM": "Moyen",
    "dashboard.suspicion_level.HIGH": "Élevé",
    "dashboard.suspicion_level.CRITICAL": "Critique",
    "dashboard.suspicion_level.UNKNOWN": "Inconnu",

    # Graphes – titres (nouvelle nomenclature)
    "dashboard.chart.folders.title": "Emails par dossier IMAP",
    "dashboard.chart.domains.title": "Top domaines expéditeurs",
    "dashboard.chart.attachments.title": "Présence de pièces jointes",
    "dashboard.chart.auth.title": "Résultats DKIM / SPF / DMARC",
    "dashboard.chart.suspicion.title": "Répartition par niveau de suspicion",

    # Graphes – libellés / états
    "dashboard.chart.no_data": (
        "Pas de données suffisantes pour tracer ce graphique."
    ),
    "dashboard.chart.axis.emails": "Nombre d’emails",
    "dashboard.chart.axis.folders": "Dossiers IMAP",
    "dashboard.chart.axis.domains": "Domaines",
    "dashboard.chart.axis.levels": "Niveaux",
    "dashboard.section_suspicion": "Scores de suspicion",
    "dashboard.suspicion_scores_line": (
        "Score de suspicion global : min {score_min}, max {score_max}, moyenne {score_avg:.1f}"
    ),
    "dashboard.suspicion_levels_title": "Répartition par niveau de suspicion",
    "dashboard.no_suspicion_data": "Pas de données de suspicion disponibles.",
    "dashboard.no_suspicion_levels": "Aucun niveau de suspicion distinct détecté.",
    "dashboard.suspicion_unknown": "Inconnu / non calculé",
    "dashboard.chart_folders_serie": "Emails par dossier",
    "dashboard.chart_domains_serie": "Emails par domaine",


    # Petite aide visuelle sur les couleurs
    "dashboard.legend.safe": "Zone considérée comme plutôt sûre",
    "dashboard.legend.suspicious": "Zone à examiner en priorité",

    # ------------------------------------------------------------------
    # Viewer – colonnes de scoring & suspicion
    # ------------------------------------------------------------------
    "viewer.col.suspicion_score": "Score suspicion",
    "viewer.col.suspicion_level": "Niveau",
    "viewer.col.suspicion_reasons": "Raisons (résumé)",

    # Tooltips scoring
    "viewer.score.tooltip.base": (
        "Score de suspicion global calculé à partir de DKIM/SPF/DMARC, "
        "anomalies Received, intégrité des en-têtes et pièces jointes."
    ),
    "viewer.score.level.LOW": (
        "Suspicion faible : rien d’anormal détecté selon les règles actuelles."
    ),
    "viewer.score.level.MEDIUM": (
        "Suspicion moyenne : quelques éléments à vérifier "
        "(headers, authentification ou pièces jointes)."
    ),
    "viewer.score.level.HIGH": (
        "Suspicion élevée : plusieurs indicateurs techniques sont incohérents ou dangereux."
    ),
    "viewer.score.level.CRITICAL": (
        "Suspicion critique : email très probablement malveillant ou falsifié."
    ),

    # ------------------------------------------------------------------
    # IMAP – OAuth / providers restrictions
    # ------------------------------------------------------------------
    "imap.info.oauth_restricted_body": (
        "Ce compte semble être géré par un fournisseur qui impose l'usage "
        "de mécanismes modernes (OAuth2, exports officiels) pour accéder "
        "aux messages (ex. Gmail, Outlook/Microsoft 365, Yahoo).\n\n"
        "Par souci de conformité et pour éviter de contourner ces règles, "
        "cette version de eml_forensic_suite ne réalise pas d'extraction IMAP "
        "directe pour ces services.\n\n"
        "Pour récupérer les messages de manière compatible :\n"
        "  • Gmail : utilisez Google Takeout pour exporter la boîte (MBOX),\n"
        "    ou un client comme Thunderbird pour créer une copie locale.\n"
        "  • Outlook / Microsoft 365 : utilisez l'export de votre client Outlook\n"
        "    (PST) ou les outils d'archivage de votre organisation.\n"
        "  • Yahoo, etc. : utilisez les outils d'export proposés par le fournisseur.\n\n"
        "Les futures versions de eml_forensic_suite viseront à analyser directement "
        "ces exports (MBOX, PST, etc.) pour rester compatibles avec ces plateformes."
    ),

    # ------------------------------------------------------------------
    # Viewer – mini langage de recherche
    # ------------------------------------------------------------------
    "viewer.search_tooltip": (
        "Mini-langage forensic :\n"
        "  from:alice@example.com\n"
        "  domain:banque.com\n"
        "  folder:\"INBOX/Important\"\n"
        "  attachment:true\n"
        "Opérateurs : AND implicite, OR, NOT, parenthèses."
    ),

    # ------------------------------------------------------------------
    # Viewer – CSV / index generic messages
    # ------------------------------------------------------------------
    "viewer.no_index_title": "Aucun index disponible",
    "viewer.no_index_body": (
        "Aucun index n'est disponible dans cette session.\n"
        "Générez un index dans l'onglet 2 ou ouvrez un CSV manuellement."
    ),
    "viewer.open_csv_title": "Ouvrir un fichier index CSV",
    "viewer.error_csv_title": "Erreur de lecture CSV",
    "viewer.error_csv_body": (
        "Impossible de lire le fichier CSV : {path}\n\n{error}"
    ),

    # ------------------------------------------------------------------
    # Viewer – preview (version finale, lecture seule)
    # ------------------------------------------------------------------
    "viewer.attach.preview": "Aperçu lecture seule",
    "viewer.attach.preview_failed_title": "Aperçu impossible",
    "viewer.attach.preview_failed_body": (
        "Impossible d'afficher un aperçu de cette pièce jointe."
    ),
    "viewer.attach.preview_unsupported_title": "Type non supporté",
    "viewer.attach.preview_unsupported_body": (
        "Aucun aperçu intégré n'est disponible pour ce type MIME : {mime}"
    ),

    # ------------------------------------------------------------------
    # Viewer – extraction PJ (version finale)
    # ------------------------------------------------------------------
    "viewer.attach.no_msg_title": "Aucun message",
    "viewer.attach.no_msg_body": "Aucun message n’est actuellement sélectionné.",
    "viewer.attach.no_selection_title": "Aucune pièce jointe sélectionnée",
    "viewer.attach.no_selection_body": (
        "Veuillez sélectionner une pièce jointe dans la liste."
    ),
    "viewer.attach.no_root_title": "Dossier de travail introuvable",
    "viewer.attach.no_root_body": (
        "Aucun dossier forensic / index n’est configuré pour l’extraction."
    ),
    "viewer.attach.extract_one_title": "Pièce jointe extraite",
    "viewer.attach.extract_one_body": (
        "La pièce jointe a été extraite vers :\n{path}"
    ),
    "viewer.attach.extract_all_title": "Pièces jointes extraites",
    "viewer.attach.extract_all_body": (
        "{count} pièces jointes ont été extraites :\n{paths}"
    ),

    # ------------------------------------------------------------------
    # Actions PJ (boutons)
    # ------------------------------------------------------------------
    "viewer.attach.extract_one": "Extraire la pièce sélectionnée",
    "viewer.attach.extract_all": "Extraire toutes les pièces",

    # ------------------------------------------------------------------
    # OAuth dialog
    # ------------------------------------------------------------------
    "oauth.title": "Connexion OAuth2",
    "oauth.choose_provider": "Choisissez le fournisseur pour l'authentification OAuth2 :",
    "oauth.btn_google": "Google (Gmail / Workspace)",
    "oauth.btn_microsoft": "Microsoft 365 / Outlook",
    "oauth.btn_yahoo": "Yahoo Mail",
    "common.cancel": "Annuler",

    "oauth.generic_title": "OAuth2",
    "oauth.google.success": "Connexion Google OAuth2 réussie.",
    "oauth.microsoft.success": "Connexion Microsoft OAuth2 réussie.",
    "oauth.yahoo.success": "Connexion Yahoo OAuth2 réussie.",
    "oauth.google.error_title": "Erreur OAuth2 Google",
    "oauth.microsoft.error_title": "Erreur OAuth2 Microsoft",
    "oauth.yahoo.error_title": "Erreur OAuth2 Yahoo",

    # ------------------------------------------------------------------
    # About box
    # ------------------------------------------------------------------
    "about.version_label": "Version :",
    "about.description": (
        "Outil de lecture seule pour l’analyse forensic d’emails EML/IMAP."
    ),
}
