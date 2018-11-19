import json
from pip._internal.operations.freeze import freeze
from platform import python_version
import site
import subprocess
import sys
import yaml


def info():
    packgs = []
    for requirement in freeze(local_only=True):
        packgs.append(requirement)
    get_info = {
        '1': python_version(),
        '2': sys.prefix,
        '3': sys.executable,
        '4': str(subprocess.check_output("which pip", shell=True)),
        '5': sys.path,
        '6': packgs,
        '7': site.getsitepackages()}
    get_info['Python version'] = get_info.pop('1')
    get_info['Virtual env'] = get_info.pop('2')
    get_info['Python executable location'] = get_info.pop('3')
    get_info['Pip location'] = get_info.pop('4')
    get_info['PYTHONPATH'] = get_info.pop('5')
    get_info['Installed packages'] = get_info.pop('6')
    get_info['Site-packages location'] = get_info.pop('7')
    return get_info


with open('outfile_y.yml', 'w') as f:
    yaml.dump(info(), f, default_flow_style=False)

with open('outfile_j.json', 'w') as r:
    json.dump(info(), r, ensure_ascii=False, sort_keys=True, indent=4)
