@echo off
setlocal EnableDelayedExpansion
set i=0
for %%a in (*.jpg) do (
    set /a i+=1
    ren "%%a" "!i!.jpeg"
)
ren *.jpg *.png