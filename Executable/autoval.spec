# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'val'],
             pathex=['C:\\Users\\Chris\\Documents\\Code\\Python\\auto-validate\\Executable'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'autoval.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=True )
