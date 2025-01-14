from stundrg_check_os_ver.osver import get_os_pretty_name

def test_first():
    v = get_os_pretty_name()
    assert v == "Ubuntu 24.04.1 LTS"

