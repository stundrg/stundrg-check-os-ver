def get_os_pretty_name() -> str:
    with open('/etc/os-release', 'r') as f:
        for line in f:
            if line.startswith('PRETTY_NAME='):
                return line.split('=')[1].replace('\n', '').strip('"')
    return None
