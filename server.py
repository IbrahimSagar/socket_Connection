import socket
import time
HeaderSize = 20

s =socket.socket()
s.bind((socket.gethostname(),1028))
s.listen(5)
print("Waiting for Connection.....!!!")
while True:
    clt,adr =s.accept()
    print(f"Connection to {adr} has been established")
    #Buffer
    msg = "Welcome To My World"
    msg = f'{len(msg):<{HeaderSize}}' + msg

    clt.send(bytes(msg,"utf-8"))
    #clt.close()

    #sending time exmp is streeming
    while True:
        time.sleep(3)
        msg = f"The time is : {time.time()}"
        msg = f'{len(msg):<{HeaderSize}}' + msg
        clt.send(bytes(msg, "utf-8"))
