import sys
import subprocess
import platform

def get_os_ver() -> str:
    platform_name = sys.platform.lower()
    if "win" in platform_name:
    return get_os_windows()
    elif "linux" in platform_name:
    return get_os_linux()
    elif "darwin" in platform_name:
    return get_os_macos()

def get_os_windows() -> str:
    command = "Get-ComputerInfo | Select-Object -Property WindowsProductName, WindowsVersion, WindowsBuildLabEx"
    result = subprocess.run(
        ["powershell", "-Command", command],
        capture_output=True,
        text=True
    )
def get_os_linux() -> str:
    with open('/etc/os-release', 'r') as f:
        for line in f:
            if line.startswith('PRETTY_NAME='):
                # Ubuntu 24.04.1 LTS
                r =  line.split('=')[1].replace('\n', '').strip('"')
                print(r)
                return r
    return None
