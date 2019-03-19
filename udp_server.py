# coding=utf-8
import os
import socket as sk
import sys
import time as tm


def main():
    host = '0.0.0.0'
    port = input('端口：')
    addr_port = (host, int(port))
    buffersize = 2048
    sockfd = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    sockfd.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
    sockfd.bind(addr_port)
    print('服务器开启成功')

    l = []
    while True:
        data, addr = sockfd.recvfrom(buffersize)

        if addr not in l:
            l.append(addr)
        data = data.decode()
        send = data
        t_recv = tm.ctime()
        send += '     #' + t_recv
        if data == 'quit':
            print('管理员关闭了聊天室')
            for i in l:
                if i != addr:
                    sockfd.sendto('管理员关闭了聊天室！'.encode(), i)
            return
        elif '_quit' in data:
            lq = data.split('_')
            print(lq[0], '退出服务')
            for i in l:
                if i != addr:
                    sockfd.sendto((lq[0] + '退出群聊').encode(), i)
        else:
            print('来自 %s：' % str(addr), data, '    #', t_recv)
            for i in l:
                if i != addr:
                    sockfd.sendto(send.encode(), i)


if __name__ == '__main__':
    main()
