"""
This program works in tandem with a server. It is a client designed to prompt the user 
for two numbers and an operation to perform. The operation options include finding 
the LCM or the mean of the two provided numbers. Once sent to the server, the
client receives a response from the server and presents this to the user.

"""
# low-level networking interface library
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# prompting the user for two numbers and to choose an operation
numbers = input("give two numbers, separated by a comma: ")
operation = input("would you like the server to find the LCM or the mean? ")

# sets the deliminter to be a semi-colon, useful to separate the user inputs
#   so the server knows where to look for the numbers/operation
delimiter = ";"
MSG = operation + delimiter + numbers

# tracing to let the user know that the client is attempting connection to the server
print("client starting - connecting to server at IP", HOST, "and port", PORT)

# once connected, the client converts the message to bytes and sends it to the server
# tracing lets the user know once the message has been sent
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"connection established, sending message '{MSG}'")
    s.sendall(bytes(MSG, 'utf-8'))
    print("message sent, waiting for reply")
    data = s.recv(1024)

# after the server has sent the response, the client converts back from bytes to
#   a string and displays this to the user
print(f"received response: {data.decode('utf-8')} [{len(data)} bytes]")
print("client is done!")