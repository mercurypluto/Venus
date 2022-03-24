"""
TCP 服务端基础代码（循环模型）
"""
from socket import *


class TcpServer:

    @staticmethod
    def server():
        # 创建套接字
        tcp_socket = socket(AF_INET, SOCK_STREAM)

        # 绑定套接字
        tcp_socket.bind(('0.0.0.0', 8888))

        # 设置监听（设置队列最大连接数）
        tcp_socket.listen(5)

        # 循环处理客户端连接，如果当前有客户端断开连接，那么等待接受下一个客户端进行连接
        while True:
            # 等待客户端连接
            print("waiting for connect")
            # 等待处理客户端连接accept
            connfd, addr = tcp_socket.accept()  # connfd连接的监听套接字，用accept处理
            print("connect from", addr)  # 打印客户端地址

            # 循环处理客户端发送消息
            while True:
                # 等待接收客户端消息
                data = connfd.recv(1024)
                # 如果客户端关闭就会断开，并不是发送空才断开
                if not data:
                    break
                print("recv", data.decode())
                # 回发
                connfd.send(bytes(f"服务端返回：{data}", encoding="UTF-8"))

            connfd.close()  # 关闭监听套接字  如果某个客户端退出连接下一个客户端连接

        tcp_socket.close()  # 关闭套接字


if __name__ == '__main__':
    TcpServer.server()