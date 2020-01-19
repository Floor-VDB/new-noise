Dim WShell
Set WShell = CreateObject("WScript.Shell")
WShell.Run "c:\Windows\newnoise.exe", 0
Set WShell = Nothing