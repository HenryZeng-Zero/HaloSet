import os
import sys

path = sys.path[0]


def service(run):
    os.system("cd " + path + ";" + 'sudo rm start.sh')
    os.system("cd " + path + ";" + 'sudo rm restart.sh')
    os.system("cd " + path + ";" + 'sudo rm stop.sh')

    os.system("cd " + path + ";" + 'echo "#! /bin/bash" >> start.sh')
    os.system("cd " + path + ";" + 'echo "#! /bin/bash" >> restart.sh')
    os.system("cd " + path + ";" + 'echo "#! /bin/bash" >> stop.sh')

    os.system("cd " + path + ";" + 'echo "' + run + 'start' + '" >> start.sh')
    os.system("cd " + path + ";" + 'echo "' + run + 'restart' + '" >> restart.sh')
    os.system("cd " + path + ";" + 'echo "' + run + 'stop' + '" >> stop.sh')

    os.system("cd " + path + ";" + 'sudo chmod 777 start.sh')
    os.system("cd " + path + ";" + 'sudo chmod 777 restart.sh')
    os.system("cd " + path + ";" + 'sudo chmod 777 stop.sh')

    os.system("cd " + path + ";" + '''sudo rm halo.service''')
    os.system("cd " + path + ";" + '''echo '[Unit]' >> halo.service''')
    os.system("cd " + path + ";" + '''echo 'Description=Halo' >> halo.service''')
    os.system("cd " + path + ";" + '''echo 'After=network.target' >> halo.service''')
    os.system("cd " + path + ";" + '''echo '[Service]' >> halo.service''')
    os.system("cd " + path + ";" + '''echo 'Type=forking' >> halo.service''')
    os.system("cd " + path + ";" + '''echo 'ExecStart=''' + path + '/start.sh' + '''' >> halo.service''')
    os.system("cd " + path + ";" + '''echo 'ExecReload=''' + path + '/restart.sh' + '''' >> halo.service''')
    os.system("cd " + path + ";" + '''echo 'ExecStop=''' + path + '/stop.sh' + '''' >> halo.service''')
    os.system("cd " + path + ";" + '''echo 'PrivateTmp=true' >> halo.service''')
    os.system("cd " + path + ";" + '''echo '[Install]' >> halo.service''')
    os.system("cd " + path + ";" + '''echo 'WantedBy=multi-user.target' >> halo.service''')
    os.system("cd " + path + ";" + '''sudo mv halo.service /lib/systemd/system/''')
    os.system('sudo systemctl daemon-reload')


def delete():
    os.system('sudo systemctl stop halo.service')
    os.system("cd " + path + ";" + '''sudo rm /lib/systemd/system/halo.service''')
    os.system('sudo systemctl daemon-reload')
    os.system("cd " + path + ";" + 'sudo rm start.sh')
    os.system("cd " + path + ";" + 'sudo rm restart.sh')
    os.system("cd " + path + ";" + 'sudo rm stop.sh')


def check():
    print("===基本选项================================================================")
    print("1.自动安装Java")
    print("2.启用Tuna apt源[本脚本不支持删除源，请考虑清楚在启用]")
    print("3.查看上一次启动log")
    print("Q.退出")
    print("===不启用systemd管理=======================================================")
    print("4.启动Hale[不启用systemd管理]")
    print("5.关闭Hale[不启用systemd管理]")
    print("6.重启Hale[不启用systemd管理]")
    print("===启用systemd管理=========================================================")
    print("7.注册服务[如果你想使用systemd管理,必须先选这项]")
    print("8.删除服务")
    print("9.启动Hale")
    print("10.关闭Hale")
    print("11.重启Hale")
    print("12.设置开机启动")
    print("13.取消开机启动")
    print("==========================================================================")
    a = input("选择序号:")
    if (a == "Q"):
        exit()
    if (a == "1"):
        os.system('sudo apt install openjdk-8* openjfx')
    if (a == "2"):
        print("本项目使用Tuna官方镜像源添加工具[参数]")
        print("下载目录：" + path)
        os.system('sudo apt install wget')
        os.system("cd " + path + ";" + "sudo rm oh-my-tuna*")
        os.system("cd " + path + ";" + "wget https://tuna.moe/oh-my-tuna/oh-my-tuna.py")
        os.system('sudo apt install python')
        os.system("cd " + path + ";" + "sudo python oh-my-tuna.py --global")
    if (a == "3"):
        print("Log:")
        print("==========================================================================")
        os.system('cat ' + path + '/run.log')
        print("==========================================================================")
    if (a == "4"):
        os.system("cd " + path + ";" + "python3 run.py start")
        print('执行完成,一切正常的话会运行在http://127.0.1.1:8090上')
    if (a == "5"):
        os.system("cd " + path + ";" + "python3 run.py stop")
    if (a == "6"):
        os.system("cd " + path + ";" + "python3 run.py restart")
        print('执行完成,一切正常的话会运行在http://127.0.1.1:8090上')
    if (a == "7"):
        run = 'python3 ' + path + '/run.py '
        service(run)
        print("注册完成，你可以使用 systemctl [语句] halo.service 来操作Halo了")
    if (a == "8"):
        delete()
        print("删除完成，不启用服务")
    if (a == "9"):
        print("正在执行服务启动命令：sudo systemctl start halo.service")
        os.system("sudo systemctl start halo.service")
        print('执行完成,一切正常的话会运行在http://127.0.1.1:8090上')
    if (a == "10"):
        print("正在执行服务关闭命令：sudo systemctl stop halo.service")
        os.system("sudo systemctl stop halo.service")
        print("执行完成")
    if (a == "11"):
        print("正在执行服务重启命令：sudo systemctl restart halo.service")
        os.system("sudo systemctl restart halo.service")
        print('执行完成,一切正常的话会运行在http://127.0.1.1:8090上')
    if (a == "12"):
        print("正在注册开机启动服务：sudo systemctl enable halo.service")
        os.system("sudo systemctl enable halo.service")
        print("执行完成")
    if (a == "13"):
        print("正在执行服务重启命令：sudo systemctl disable halo.service")
        os.system("sudo systemctl disable halo.service")
        print("执行完成")


if __name__ == "__main__":
    check()
