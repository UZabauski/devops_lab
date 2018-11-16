import datetime
import json
import psutil
from time import sleep


class Class1(object):
    def __init__(self, myfile):
        self = open(myfile, 'w')
        self.write('interval = 5')
        self.write('\noutput_type = "text"')
        self.write('\n\nif output_type == "json":')
        self.write('\n    file_name = "output.json"')
        self.write('\nelif output_type == "text":')
        self.write('\n    file_name = "output.txt"')
        self.close()


c1 = Class1("config.py")
import config  # noqa


class Class2(object):
    def status1(self):
        return str(psutil.cpu_percent(interval=1)) + '%'

    def status2(self):
        return str(psutil.virtual_memory().available / 1048576) + 'Mb'

    def status3(self):
        return str(psutil.virtual_memory().used / 1048576) + 'Mb'

    def status4(self):
        return str(psutil.disk_io_counters().write_time) + 'ms'

    def status5(self):
        return str(psutil.net_io_counters().bytes_sent) + 'b'


class Class3(object):
    def status(self):
        get_info = {
            '1': c2.status1(),
            '2': c2.status2(),
            '3': c2.status3(),
            '4': c2.status4(),
            '5': c2.status5()}
        return get_info


class Class4(object):
    def wrt(self):
        if config.output_type == "text":
            counter = 1
            while True:
                get_status = c3.status()
                get_1 = c3.status().get('1')
                get_2 = c3.status().get('2')
                get_3 = c3.status().get('3')
                get_4 = c3.status().get('4')
                get_5 = c3.status().get('5')
                get_6 = c5.my_time()
                out_file = open(config.file_name, "a")
                str0 = 'SNAPSHOT ' + str(counter) + ' : ' + str(get_6)
                str1 = ' Overall CPU load : '
                str2 = ' Overall memory usage(available) : '
                str3 = ' Overall virtual memory usage : '
                str4 = ' IO information(write time) : '
                str5 = ' Network information(bytes sent) : '
                out_file.write(str0 + str1 + str(get_1) + '\n')
                out_file.write(str0 + str2 + str(get_2) + '\n')
                out_file.write(str0 + str3 + str(get_3) + '\n')
                out_file.write(str0 + str4 + str(get_4) + '\n')
                out_file.write(str0 + str5 + str(get_5) + '\n')
                out_file.write("\n")
                out_file.close()
                get_status.clear()
                print("Snapshot is ready.")
                sleep(config.interval)
                counter += 1
        if config.output_type == "json":
            get_status = {}
            counter = 1
            while True:
                get_status["Snapshot"] = "SNAPSHOT" + str(counter)
                get_status["timestamp"] = str(c5.my_time())
                get_status["status"] = c3.status()
                output_file = open(config.file_name, "a")
                output_file.write(json.dumps(get_status) + "\n\n")
                output_file.close()
                get_status.clear()
                print("Snapshot is ready.")
                sleep(config.interval)
                counter += 1


class Class5(object):
    def my_time(self):
        return str(datetime.datetime.now().replace(microsecond=0))


c2 = Class2()
c3 = Class3()
c4 = Class4()
c5 = Class5()
c4.wrt()
