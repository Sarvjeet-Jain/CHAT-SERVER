import socket
myif= socket.AF_INET
mypro= socket.SOCK_DGRAM
s= socket.socket( mypro, myif)
ip= "192.168.43.249"
port=2000
s.bind((ip,port))
def recv():
    while True:
         inp= s.recvfrom(1024)
         client= inp[1][0]
         msg= inp[0]
         print(client+":"+  msg.decode())
         if (msg.decode()=="good bye"):
             exit(0)
         else:
             send()
def send():
    while True:
        msg= input("Chat-")
        s.sendto(msg.encode(), ("192.168.43.34", 1000))
        if (msg.encode()=="good bye"):
            exit(0)
        recv()
send()
recv()
