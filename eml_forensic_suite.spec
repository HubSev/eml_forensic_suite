# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['src/eml_forensic_suite/__main__.py'],
    pathex=['src'],
    binaries=[],
    datas=[
        ('src/eml_forensic_suite/icone.ico', 'eml_forensic_suite'),
        ('src/eml_forensic_suite/core/version.json', 'eml_forensic_suite/core'),
        ('src/eml_forensic_suite/ui/traductions/*.py', 'eml_forensic_suite/ui/traductions'),
    ],
    hiddenimports=['dkim'],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='eml_forensic_suite',
    icon='src/eml_forensic_suite/icone.ico',
    version='file_version_info.txt',
    console=False,
    upx=True,
)
