# coding=utf-8
import os
import socket as sk
import sys
import time as tm
import yan_zheng as Yz
import zhu_ce as Zc
import deng_lu as Dl

def connect():
#     host = '127.0.0.1'
#     port = input('输入端口：')    
    host, port = di_zhi()
    addr_port = (host, int(port))
    sockfd = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    Dl.deng_lu(sockfd, addr_port)
    
def di_zhi():
    host = ""
    port = ""
    note = ""
    last_con = last_connection()
    if last_con:
        note = "直接回车重复上次连接 %s " % last_con
        host_port = input(note)
        if not host_port:
            host = last_con.split(":")[0]
            port = last_con.split(":")[1]
        else:
            host = host_port.split(":")[0]
            port = host_port.split(":")[1]
    else:
        host_port = input('输入服务器地址和端口（ host:port ） ')
        if host_port:
            host = host_port.split(":")[0]
            port = host_port.split(":")[1]
            save_con_file(host, port)last_connection
    if host and port:
        return host port
    else:
        print("参数有误，无法连接")

def last_connection():
    last_con = ""
    cons = open_con_file()
    if cons:
        last_con = cons[-1]
    return last_con
        
def is_connected(host, port):
    is_con = False
    now_con = host + ":" + port
    cons = open_con_file()
    if now_con in cons:
        is_con = True
    return is_con

def save_con_file(host, port):
    if host and port:
        con = host + ":" + port
        try:
            with open("connection_record.txt", "a") as wf:
                wf.write(con)
        except Exception as E:
            print("写入连接记录失败", E)

def open_con_file():
    con_file = []
    try:
        with open("connection_record.txt", "a+") as rf:
            cons = rf.read()
            con_file = cons.split("\n")
    except Exception as E:
        print("连接记录文件操作失败", E)
    return con_file

if __name__ == "__main__":
    connect()
