import socket
mypro= socket.SOCK_DGRAM
myipf= socket.AF_INET
s= socket.socket(mypro, myipf)
ip="192.168.43.34"
port=1000
s.bind((ip,port))
def recv():
    while True:
        x=s.recvfrom(1024)
        client=x[1][0]
        msg=x[0]
        print(client+":"+ msg.decode())
        if( msg.decode()=="good bye"):
            exit(0)
        else:
            send()
def send():
    while True:
        msg= input("Chat-")
        s.sendto(msg.encode(),("192.168.43.249", 2000))
        recv()
recv()
send()
