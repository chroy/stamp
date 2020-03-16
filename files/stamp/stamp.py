import time
import socket
import datetime
from pathlib import Path
from SMWinservice import SMWinservice

class PythonCornerExample(SMWinservice):
    _svc_name_ = "Stamp"
    _svc_display_name_ = "Log Stamp"
    _svc_description_ = "Stamp a log file with hostname and time stamp"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        i = 0
        while self.isrunning:
            f=open("c:\stamp\stamp.log", "a+")
            f.write(socket.gethostname() + " " + str(datetime.datetime.now()).split('.')[0] + "\n")
            f.close()
            time.sleep(5)

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()
