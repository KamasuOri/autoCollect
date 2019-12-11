C:\python27-x64\Scripts\pyinstaller.exe --onefile start.py
cd dist
copy start.exe ..
cd ..
@RD /S /Q dist
@RD /S /Q build