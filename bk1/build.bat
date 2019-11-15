pyinstaller --onefile start.py
cd dist
copy start.exe ..
cd ..
@RD /S /Q dist
@RD /S /Q build