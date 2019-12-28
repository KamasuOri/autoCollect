C:\python27-x64\Scripts\pyinstaller.exe --onefile update.py
cd dist
copy update.exe ..
cd ..
@RD /S /Q dist
@RD /S /Q build