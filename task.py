import psutil
import config
import json
from time import sleep
from datetime import datetime


with open("config.py", "w") as f:
    f.write('interval = 5')
    f.write('\noutput_type = "text"')
    f.write('\n\nif output_type == "json":')
    f.write('\n    file_name = "output.json"')
    f.write('\nelif output_type == "text":')
    f.write('\n    file_name = "output.txt"')


def status():
    get_info = {
        '1': str(psutil.cpu_percent(interval=1)) + '%',
        '2': str(psutil.virtual_memory().available / 1048576) + 'Mb',
        '3': str(psutil.virtual_memory().used / 1048576) + 'Mb',
        '4': str(psutil.disk_io_counters().write_time) + 'ms',
        '5': str(psutil.net_io_counters().bytes_sent) + 'b'}
    get_info['Overall CPU load'] = get_info.pop('1')
    get_info['Overall memory usage(available)'] = get_info.pop('2')
    get_info['Overall virtual memory usage'] = get_info.pop('3')
    get_info['IO information(write time)'] = get_info.pop('4')
    get_info['Network information(bytes sent)'] = get_info.pop('5')
    return get_info


if config.output_type == "text":
    counter = 1
    while True:
        get_status = status()
        output_file = open(config.file_name, "a")
        string1 = 'SNAPSHOT ' + str(counter) + ' : ' + str(datetime.today())
        for _ in get_status:
            output_file.write(string1 + ' ' + _ + ' : ' + get_status[_] + '\n')
        output_file.write("\n")
        output_file.close()
        get_status.clear()
        print("Snapshot is ready.")
        sleep(config.interval)
        counter += 1

if config.output_type == "json":
    get_status = {}
    counter = 1
    while True:
        get_status["Snapshot"] = "SNAPSHOT" + str(counter)
        get_status["timestamp"] = str(datetime.today())
        get_status["status"] = status()
        output_file = open(config.file_name, "a")
        output_file.write(json.dumps(get_status) + "\n\n")
        output_file.close()
        get_status.clear()
        print("Snapshot is ready.")
        sleep(config.interval)
        counter += 1
