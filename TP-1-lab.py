import os
import platform as pl
import getpass
import psutil as ps
import urllib.request as req
import json


data = {
    'system': pl.system(),
    'python_version': pl.python_version(),
    'user': getpass.getuser(),
    'architecture': pl.architecture()[0],
    'remote_ip': req.urlopen("https://api.ipify.org", timeout=2).read().decode('utf-8')
}

#параметры для Linux
if data['system'] == 'Linux':
    import pwd
    os_release = pl.freedesktop_os_release()
    data['distribution'] = os_release.get('PRETTY_NAME', os_release.get('NAME', 'Linux'))
    data['load_average_15min'] = ps.getloadavg()[2]
    data['pagefile_total_gb'] = round(ps.swap_memory().total / (1024**3), 2)
    data['all users'] = [user.pw_name for user in pwd.getpwall()]

#параметры для Windows
elif data['system'] == 'Windows':
    data['win_build'] = pl.win32_ver()[1]
    data['system_drive'] = os.environ.get('SystemDrive', 'C:')
    data['running_services'] = len([s for s in ps.win_service_iter() if s.status() == 'running'])
    data['pagefile_total_gb'] = round(ps.swap_memory().total / (1024**3), 2)
    data['all users'] = [u.name for u in ps.users()]

dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dir, 'system_info.json')

f = open(path, 'w', encoding='utf-8')
json.dump(data, f, indent=4)
f.close()