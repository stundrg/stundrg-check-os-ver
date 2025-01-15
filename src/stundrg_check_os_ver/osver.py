import sys
import subprocess
import platform

def get_os_ver() -> str:
    if sys.platform.lower() == "windows"
    return get_os_windows()

def get_os_windows() -> str:
    return f"{Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, WindowsBuildLabEx}"

def get_os_linux() -> str:
    with open('/etc/os-release', 'r') as f:
        for line in f:
            if line.startswith('PRETTY_NAME='):
                # Ubuntu 24.04.1 LTS
                r =  line.split('=')[1].replace('\n', '').strip('"')
                print(r)
                return r
    return None
