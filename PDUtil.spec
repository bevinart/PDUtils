# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['PDUtilities/__main__.py'],
    pathex=['myenv39/Lib/site-packages/'],
    binaries=[],
    datas=[('PDUtilities/ui_layouts/pd_gui_layout.ui', '.'), ('PDUtilities/ui_layouts/song_display_layout.ui', '.'), ('PDUtilities/midi_maps/*', 'midi_maps'), ('PDUtilities/drum_sets', 'drum_sets'), ('PDUtilities/assets/*', 'assets')],
    hiddenimports=['python-rtmidi', 'rtmidi-python', 'mido.backends.rtmidi'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='PDUtilities',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    icon='PDUtilities/assets/favicon.ico',
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PDUtilities',
)
