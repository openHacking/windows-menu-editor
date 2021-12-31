@REM Modify the registration form and add a piece of registration information
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f

@REM Kill file explorer
taskkill /IM explorer.exe /F

@REM Start windows explorer
start "" c:\windows\explorer.exe&exit

