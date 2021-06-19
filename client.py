import socket
import pickle
#client1

ClientSocket = socket.socket()
host = "192.168.1.22"
port = 4000
Input = ""

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))


Response = ClientSocket.recv(1024).decode()
while True:
    Input = input('Client>')
    if(Input == 'update stock'):
        f = open("kalan.txt", "r")
        a = []
        stock = {'IceTea': 0, 'Soda': 0, 'Water': 0}

        for x in f:
            x = x.replace("'", "")
            x = x.replace("::", ":")
            a = x.split(',')

        for c in a:

            c = c.split(":")
            c[0] = c[0].replace(" ", "")

            stock[c[0]] = c[1]

        ClientSocket.send(str.encode(Input))
        msg_stock = pickle.dumps(stock)
        ClientSocket.send(msg_stock)

    elif(Input == 'exit'):
        print("Leave from server")
        break
    elif(Input == 'check stock'):
        print("check stock in client")
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024).decode()
        print(Response)



ClientSocket.close()


