import os
import subprocess
import sys
from socket import socket, AF_INET, SOCK_STREAM

sys.path.append(os.path.join(os.getcwd(), '..'))
process = subprocess.Popen(['python', 'run_test_server.py'], shell=True)
print(f'Process ID: {process.pid}, Process: {process}')
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('localhost', 7777))
client_socket.close()

process.kill()
print(f'Process ID: {process.pid}')
print(f'Process ID: {process.pid}, Process: {process}')
