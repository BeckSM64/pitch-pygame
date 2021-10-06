# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Pitch.py'],
             binaries=[],
             datas=[],
             hiddenimports=["pygame", "pygame.locals"],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          Tree('./resources', prefix='resources/'),
          Tree('./game', prefix='game/'),
          Tree('./ui', prefix='ui/'),
          Tree('./network', prefix='network/'),
          a.zipfiles,
          a.datas,  
          [],
          name='Pitch',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
