"""
This program works in tandem with a server. It is a client designed to prompt the user 
for two numbers and an operation to perform. The operation options include finding 
the LCM or the mean of the two provided numbers. Once sent to the server, the
client receives a response from the server and presents this to the user.

"""

import socket # low-level networking interface library
import time # needed to add a delay

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

################################# USER INPUT & ERROR CHECKING #################################

# prompting the user for two numbers
numbers = input("give two numbers, separated by a comma: ")

# checks to make sure the input for numbers is allowed (ie. is an integer)
# checks to make sure a comma was provided to separate input numbers
# only breaks once valid numbers have been provided
while True:
    flag = False
    try:
        if ',' in numbers and not flag:
            flag = True
        else:
            numbers = input("a comma was not included in your input for numbers. please submit two numbers separated by a comma: ")

        first_num = int(numbers.split(",")[0])
        second_num = int(numbers.split(",")[1])
        print("the provided numbers have been accepted")
        break
    except ValueError:
        numbers = input("invalid input for numbers. please input two numbers separated by a comma: ")

# prompting the user to choose an operation
operation = input("would you like the server to find the LCM or the mean? ")

# checks to make sure that a valid operation was chosen
while True:
    if operation in ("LCM", "lcm") and (first_num == 0 or second_num == 0):
        print("LCM of zero cannot be computed. sending a command to the server in 5 seconds to compute the mean instead of LCM.")
        operation = "mean"
        time.sleep(1)
        print ("5")
        time.sleep(1)
        print ("4")
        time.sleep(1)
        print ("3")
        time.sleep(1)
        print ("2")
        time.sleep(1)
        print ("1")
        time.sleep(1)
        print ("0")
        break
    elif operation in ("LCM", "lcm", "mean", "Mean"):
        print("the provided operation has been accepted")
        break
    else:
        operation = input("invalid operation selected. please input either LCM or mean: ")
############################################################################################

##################################### SENDING MESSAGE #####################################

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

###########################################################################################

#################################### RECEIVING RESPONSE ####################################

# after the server has sent the response, the client converts back from bytes to
#   a string and displays this to the user
print(f"received response: {data.decode('utf-8')} [{len(data)} bytes]")

# if response from server is an error message, let the user knoew
if data.decode('utf-8') == "ERROR: Invalid operation":
    print("server could not compute request. please try again.")

###########################################################################################

print("client is done!")