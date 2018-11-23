# coding=utf-8
import os
import socket as sk
import sys
import time as tm
import yan_zheng as Yz
import zhu_ce as Zc
import deng_lu as Dl


def di_zhi():
    #    host = input('输入地址：')
    #    port = input('输入端口：')
    host = '127.0.0.1'
    port = input('输入端口：')

    addr_port = (host, int(port))
    sockfd = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    Dl.deng_lu(sockfd, addr_port)


if __name__ == "__main__":
    di_zhi()
