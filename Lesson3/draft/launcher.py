import subprocess

processes = []

while True:
    action = input('Input: q - for exit, s - for start server & clients, x - to close all')
    if action == 'q':
        break;
    elif action == 's':
        processes.append(subprocess.Popen("python server.py",
                                          shell=True
                                          )
                         )
        for i in range(5):
            processes.append(subprocess.Popen('python client.py',
                                              shell=True
                                              )
                             )
    elif action == 'x':
        process = processes.pop()
        process.kill()

