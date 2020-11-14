import os
from multiprocessing import Process, Pool

PROCESSES = []
SERVER = 'each_server.py'
CLIENT_READ = 'each_client.py -m recv'
CLIENT_WRITE = 'each_client.py -m send'


def run_proc(proc):
    print('running subprocess')
    os.system('python {} &'.format(proc))

while True:
    action = input(
            "r -  Запуск процесса, "
            "q - выход. "
            )
    if action == 'r':
        PROCESSES.append(Process(target=run_proc, args=(SERVER,)))
        for i in range(4):
            if i < 2:
                PROCESSES.insert(0, Process(target=run_proc, args=(CLIENT_READ,)))
            else:
                PROCESSES.insert(0, Process(target=run_proc, args=(CLIENT_WRITE,)))

    elif action == 'q':
        for process in PROCESSES:
            process.terminate()
        break


    #
    # while True:
    #     choice = input(
    #         "q - запуск сервера, w - остановка сервера, e - запуск 4 клиентов, r - остановка клиентов, t - остановить все, y - остановить все и выйти")
    #
    #     if choice == "q":
    #         print("Запустили сервер")
    #         server = Popen(f"open -n -a Terminal.app '{pathToScriptServer}'", shell=True)
    #
    #     elif choice == "w":
    #         print("Убили сервер")
    #         server.kill()
    #     elif choice == "e":
    #         print("Запустили клиенты")
    #         for i in range(1, 3):
    #             clients.append(Popen(f"open -n -a Terminal.app '{pathToScriptClients}{i}'", shell=True))
    #             # Задержка для того, что бы отправляющий процесс успел зарегистрироваться на сервере, и потом в словаре имен клиентов
    #             # остался только слушающий клиент
    #             time.sleep(0.5)
    #             clients.append(Popen(f"open -n -a Terminal.app '{pathToScriptClients}{i}r'", shell=True))
    #
    #     elif choice == "r":
    #         for i in range(len(clients)):
    #             print(clients[i])
    #             clients[i].kill()
    #     elif choice == "y":
    #         for i in range(len(clients)):
    #             clients[i].kill()
    #         server.kill()
    #         break