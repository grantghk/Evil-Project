for /f "tokens=*" %%x in (config.txt) do (
    set /a count+=1
    set var[!count!]=%%x
)
"C:\Windows\System32\cmd.exe" /k ping -t -l %var[2]% %var[1]%
exit