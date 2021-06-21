import socket
from _thread import *
import pickle


def threaded_client(conn):

    file_location = "/usr/local/"
    command = []
    conn.send(str.encode(' Welcome to the Server'))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        print(data)
        if not data:
            # if data is not received break
            break
        elif(data == 'update stock'):
            data = conn.recv(1024)
            recd = pickle.loads(data)
            print(recd)
            stock['mevcut Soda'] = recd['Soda']
            stock['mevcut IceTea'] = recd['IceTea']
            stock['mevcut Water'] = recd['Water']
            a = "Stock updated"
            #conn.send(a.encode())  # send data to the client
        elif(data == 'check stock'):
            s = ""
            if (stock['IceTea'] == 0):
                s = s + "There is no IceTea in stock\n"


            else:
                s = s + "Required IceTea: " + str(int(stock['capacity IceTea']) - int(stock['mevcut IceTea'])) + "\n"

            if (stock['Water'] == 0):
                s = s + "There is no Water in stock\n"
            else:
                s = s + "Required Water: " + str(int(stock['capacity Water']) - int(stock['mevcut Water'])) + "\n"

            if (stock['Soda'] == 0):
                s = s + "There is no Soda in stock\n"
            else:
                s = s + "Required Soda: " + str(int(stock['capacity Soda']) - int(stock['mevcut Soda']))  + "\n"
            conn.send(s.encode())  # send data to the client
        else:
            s = "Command not found"
            conn.send(s.encode())  # send data to the client






    conn.close()  # close the connection


if __name__ == '__main__':
    ServerSocket = socket.socket()
    host = "...."
    port = 4001
    ThreadCount = 0
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    print('Waitiing for a Connection..')
    ServerSocket.listen(2)
    stock = {'IceTea': 10, 'Water': 10, 'Soda': 10, 'capacity IceTea': 5, 'capacity Water': 8, 'capacity Soda': 7, 'mevcut IceTea': 0, 'mevcut Water': 0, 'mevcut Soda': 0}
    recd = {'IceTea': 0, 'Water': 0, 'Soda': 0}
    while True:
        stock = stock
        recd = recd
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))

