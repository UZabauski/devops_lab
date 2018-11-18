import datetime
import json
import psutil
from time import sleep


class Config_file(object):
    def __init__(self, myfile):
        self = open(myfile, 'w')
        self.write('interval = 5')
        self.write('\noutput_type = "text"')
        self.write('\n\nif output_type == "json":')
        self.write('\n    file_name = "output.json"')
        self.write('\nelif output_type == "text":')
        self.write('\n    file_name = "output.txt"')
        self.close()


c1 = Config_file("config.py")
import config  # noqa


class Psutil_stat(object):
    def cpu(self):
        return str(psutil.cpu_percent(interval=1)) + '%'

    def vma(self):
        return str(psutil.virtual_memory().available / 1048576) + 'Mb'

    def vmu(self):
        return str(psutil.virtual_memory().used / 1048576) + 'Mb'

    def disk_io_c(self):
        return str(psutil.disk_io_counters().write_time) + 'ms'

    def net_io_c(self):
        return str(psutil.net_io_counters().bytes_sent) + 'b'


class Statistic_dict(object):
    def dict_st(self):
        get_info = {
            '1': c2.cpu(),
            '2': c2.vma(),
            '3': c2.vmu(),
            '4': c2.disk_io_c(),
            '5': c2.net_io_c()}
        return get_info


class Output_to_file(object):
    def wrt(self):
        if config.output_type == "text":
            counter = 1
            while True:
                get_status = c3.dict_st()
                get_1 = c3.dict_st().get('1')
                get_2 = c3.dict_st().get('2')
                get_3 = c3.dict_st().get('3')
                get_4 = c3.dict_st().get('4')
                get_5 = c3.dict_st().get('5')
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
                get_status["status"] = c3.dict_st()
                output_file = open(config.file_name, "a")
                output_file.write(json.dumps(get_status) + "\n\n")
                output_file.close()
                get_status.clear()
                print("Snapshot is ready.")
                sleep(config.interval)
                counter += 1


class Sleep_interval(object):
    def my_time(self):
        return str(datetime.datetime.now().replace(microsecond=0))


c2 = Psutil_stat()
c3 = Statistic_dict()
c4 = Output_to_file()
c5 = Sleep_interval()
c4.wrt()
