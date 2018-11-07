# -*- mode: python -*-

block_cipher = None


a = Analysis(['tic-tac-toe-gui.py'],
             pathex=['C:\\Users\\hp\\Anaconda3\\pkgs\\python-3.7.0-hea74fb7_0\\Basic_Python_Programs'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          a.zipfiles,
          a.datas,
          [],
          name='tic-tac-toe-gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
