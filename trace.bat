@echo off
set input_file=ips.txt

if not exist "%input_file%" (
    echo Input file "%input_file%" not found.
    exit /b 1
)

for /f "usebackq tokens=*" %%i in ("%input_file%") do (
    echo Traceroute to IP: %%i
    tracert -d -h 15 -w 50 %%i
    echo.
)

Make sure to replace "ips.txt" with the actual path to your input file containing IP addresses. This script will execute a traceroute to each IP address listed in the file.

Save the script with a .bat extension (e.g., traceroute_ips.bat) and run it in the MS-DOS environment. It will read each line of the input file, perform a traceroute to the corresponding IP address, and display the results.
