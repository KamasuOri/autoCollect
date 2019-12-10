C:\python27-x64\Scripts\pyinstaller.exe --onefile readDiskSector.py
cd dist
copy readDiskSector.exe ..
cd ..
@RD /S /Q dist
@RD /S /Q build