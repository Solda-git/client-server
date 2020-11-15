import os
from multiprocessing import Process, Pool

# PROCESSES = []
# SERVER = 'each_server.py'
# CLIENT_READ = 'each_client.py -m recv'
# CLIENT_WRITE = 'each_client.py -m send'
#
#
# def run_proc(proc):
#     print('running subprocess')
#     os.system('python {} &'.format(proc))
#
# while True:
#     action = input(
#             "r -  Запуск процесса, "
#             "q - выход. "
#             )
#     if action == 'r':
#         PROCESSES.append(Process(target=run_proc, args=(SERVER,)))
#         PROCESSES[0].start()
#         PROCESSES[0].join()
#         for i in range(4):
#             if i < 2:
#                 PROCESSES.insert(0, Process(target=run_proc, args=(CLIENT_READ,)))
#             else:
#                 PROCESSES.insert(0, Process(target=run_proc, args=(CLIENT_WRITE,)))
#
#     elif action == 'q':
#         # for process in PROCESSES:
#         #     process.terminate()
#         break



def run_process(process):
    print('RUN > python {}'.format(process))
    os.system('python {}'.format(process))


pool = Pool(processes=3)
pool.map(run_process, (
    'each_client.py -m recv',
    'each_client.py -m send',
    'each_client.py -m recv',
    'each_client.py -m send',
))
