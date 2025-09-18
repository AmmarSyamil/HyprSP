# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('images', 'images'),
        ('ui', 'ui'),
        ('todos.json', '.'),
        ('compiled', 'compiled'),
        ('list_todo.py', '.'),
    ],
    hiddenimports=[
        'PySide6.QtWebEngineWidgets',
        'qfluentwidgets',
        'qframelesswindow.webengine',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        'numpy',
        'pandas',
        'matplotlib',
        'tkinter',
        'jupyter',
        'notebook',
        'mpl_toolkits',
        'sklearn',
        'seaborn',
        'torch',
        'tensorflow',
        'cv2',
        'boto3',
        'botocore',
        'requests',
        'urllib3',
        'openpyxl',
        'xlrd',
        'xlwt',
        'lxml',
        'bs4',
        'sqlalchemy',
        'psycopg2',
        'mysql',
        'mysqlclient',
        'pymongo',
        'dateutil',
        'cryptography',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='HypSP',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='HypSP',
)
