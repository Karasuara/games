
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 50000)) #50000 portを開く ip本番は0.0.0.0
    s.listen(2)
    while True:
        conn, addr = s.accept() #接続したらコネクションとアドレスが入る
        with conn:
            while True:
                data = conn.recv(20) #データを受け取る
                if not data:
                    break
                print(data + "を受け取りました") #win or lose
                
                conn.sendall("あなたは" + data)