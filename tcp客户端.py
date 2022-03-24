"""
TCP客户端基础代码
"""
from socket import *


class TcpClient:

    @staticmethod
    def client():
        # 创建套接字
        tcp_socket = socket()

        # 发起连接  连接服务端
        tcp_socket.connect(('127.0.0.1', 8888))
        while True:
            # 发送消息
            msg = input(">>")
            if not msg:
                break

            tcp_socket.send(msg.encode())  # 发送字节串

            data = tcp_socket.recv(1024)
            print(data.decode())

        tcp_socket.close()


if __name__ == '__main__':
    TcpClient.client()