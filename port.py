import socket

port = 80
ip = input("enter the ip address")
sock = socket.socket()
try:
  sock.connect((ip,port))
  print("port is open")
except:
    print("port is closed")
