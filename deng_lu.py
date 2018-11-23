# coding=utf-8
import os
import socket as sk
import sys
import time as tm
import yan_zheng as Yz
import zhu_ce as Zc
import multiprocessing as MP


# P_pid = 0
def deng_lu(sockfd, addr_port):
    name = input('请输入登录用户名：')
    passwd = input('密码：')
    jieshu = False
    if Yz.yanzheng(name, passwd) == 'userroot':
        print('登录成功！欢迎您，管理员！')
        '''
        p1 = MP.Process(name = 'jieshou', target = jie_shou, args = (sockfd,))
        p2 = MP.Process(name = 'fasong', target = fa_song, args = (sockfd, addr_port, name))
        
        p1.daemon = True
        p2.daemon = True
        
        p1.start()
        p2.start()
        '''
        pid = os.fork()
        if pid < 0:
            print('程序线程出错，关闭系统')
            sys.exit()
        elif pid > 0:
            sockfd.sendto(('%s进入聊天室！' % name).encode(), addr_port)
            ToF = fa_song(sockfd, addr_port, name)
            if ToF:
                return
        elif pid == 0:  # 子进程
            # global P_pid
            # P_pid = os.getppid()
            jie_shou(sockfd)

    elif Yz.yanzheng(name, passwd) == 'user':
        print('登录成功！欢迎')
        '''
        p1 = MP.Process(name = 'jieshou', target = jie_shou, args = (sockfd,))
        p2 = MP.Process(name = 'fasong', target = fa_song, args = (sockfd, addr_port, name))
        
        p1.daemon = True
        p2.daemon = True
        
        p1.start()
        p2.start()
        '''
        pid = os.fork()
        if pid < 0:
            print('程序线程出错，关闭系统')
            sys.exit()
        elif pid > 0:
            #            sockfd.sendto(('%s进入聊天室！'%name).encode(), addr_port)
            fa_song(sockfd, addr_port, name)
        elif pid == 0:  # 子进程
            #            global P_pid
            #            P_pid = os.getppid()
            jie_shou(sockfd)

    else:
        print('登录失败!重输验证信息请输入r, 注册新用户z:')
        xuanze = input('请输入：')
        if xuanze == 'r':
            return deng_lu(sockfd, addr_port)
        elif xuanze == 'z':
            yon = Zc.zhu_ce()
            if yon == 'denglu':
                return deng_lu(sockfd, addr_port)
            else:
                print(yon)
                deng_lu(sockfd, addr_port)


def fa_song(sockfd, addr_port, name):
    sockfd.sendto(('%s进入聊天室！' % name).encode(), addr_port)
    #    print('发送开始')
    while True:
        s = input()
        if name == 'root' and s == 'quit':
            sockfd.sendto('quit'.encode(), addr_port)
            print('关闭聊天室，退出群聊')
            #            global jieshu
            #            jieshu = True
            return True
        elif name != 'root' and s == 'quit':
            sockfd.sendto(('%s_quit' % name).encode(), addr_port)
            print('退出群聊')
            #            global jieshu
            #            jieshu = True
            return True
        else:
            #            global jieshu
            #            jieshu = False
            s = name + ': ' + s
            sockfd.sendto(s.encode(), addr_port)


def jie_shou(sockfd):
    #    print('接收开始')
    buffersize = 2048
    P_pid = os.getppid()
    while 1:
        ppid = os.getppid()
        #        print('ppid',ppid,'P_pid',P_pid)
        if ppid == P_pid:
            #            print('ppid: ',ppid)
            data, addr = sockfd.recvfrom(buffersize)
            data = data.decode()
            if data == '管理员关闭了聊天室！':
                print(data)
                return
            else:
                print(data)
        else:
            return
