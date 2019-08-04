from sys import argv
import os
import sys

servergo = sys.path[0]

if len(argv) > 1:
    if argv[1] == '-h':
        print('格式：run.py [comm]')
        print('     输入 start 启动服务')
        print('     输入 stop 停止服务')
        print('     输入 restart 重启服务')

    fileo = argv[0][:-6]
    if argv[1] == 'start':
        os.system('cd ' + servergo + ' ; nohup java -jar halo-latest.jar > run.log & echo $! > run.pid &')

    if argv[1] == 'stop':
        os.system('pid=$(cat ' + servergo + '/run.pid) ; sudo kill -9 $pid')
        print('执行完成')
    if argv[1] == 'restart':
        os.system('pid=$(cat ' + servergo + '/run.pid) ; sudo kill -9 $pid')
        os.system('cd ' + servergo + ' ; nohup java -jar halo-latest.jar > run.log & echo $! > run.pid &')


else:
    print('Enter "-h" for help')
