import socket

HeaderSize = 20

c = socket.socket()
c.connect((socket.gethostname(),1028))
#Buffert code start
while True:
    full_msg = ''
    new_msg=True
    while True:
        msg = c.recv(1024)
        if new_msg:
            print(f'New massage length is :{msg[:HeaderSize]}')   #massage length
            msglen = int(msg[:HeaderSize])  #grab the length
            new_msg = False         #its not longer any msg becs it convert in length

        full_msg += msg.decode("utf-8")

        if len(full_msg)-HeaderSize == msglen:
            print("Full msg recvd")
            print(full_msg[HeaderSize:])
            new_msg = True
            full_msg = ''
    print(full_msg)

#Connection code
'''full_msg = ''
while True:
    msg = c.recv(1024)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
print(full_msg)
'''