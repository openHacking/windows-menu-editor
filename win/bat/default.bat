@REM Modify the registry, delete the record
reg.exe delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f

@REM Kill file explorer
taskkill /IM explorer.exe /F

@REM Start windows explorer
explorer

