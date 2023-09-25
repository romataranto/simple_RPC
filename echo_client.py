import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
numbers = input("give two numbers, separated by a comma: ")
operation = input("would you like the server to find the LCM or the mean? ")
delimiter = ";"
MSG = operation + delimiter + numbers

print("client starting - connecting to server at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"connection established, sending message '{MSG}'")
    s.sendall(bytes(MSG, 'utf-8'))
    print("message sent, waiting for reply")
    data = s.recv(1024)

print(f"received response: {data.decode('utf-8')} [{len(data)} bytes]")
print("client is done!")