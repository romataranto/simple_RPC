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

# checks to make sure the input for numbers is allowed (ie. is a float)
# checks to make sure a comma was provided to separate input numbers
# only breaks infinite loop once valid numbers have been provided
while True:
    flag = False # using flag to break out of the if statement, but not infinite loop
    try:
        if ',' in numbers and not flag:
            flag = True
        elif not flag:
            numbers = input("a comma was not included in your input for numbers. please submit two numbers separated by a comma: ")

        first_num = float(numbers.split(",")[0])
        second_num = float(numbers.split(",")[1])
        print("the provided numbers have been accepted")
        break
    except ValueError:
        numbers = input("invalid input for numbers. please input two numbers separated by a comma: ")

# prompting the user to choose an operation
operation = input("would you like the server to find the LCM or the mean? ")

# checks to make sure that a valid operation was chosen
while True:
    # LCM of zero cannot be calculated, so the following if statement will change the operation to mean if
    #   zero is one of the provided numbers
    if operation in ("LCM", "lcm") and (first_num == 0 or second_num == 0):
        print("LCM of zero cannot be computed. sending a command to the server in 5 seconds to compute the mean instead of LCM.")
        operation = "mean"
        for i in range(5, -1, -1):
            print(i)
            time.sleep(1)
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
#   a string to a rounded float and displays this to the user
rounded_response = round(float(data.decode('utf-8')), 2) # round to 2 decimals
print(f"received response: {rounded_response} [{len(data)} bytes]")

# if response from server is an error message, let the user knoew
if data.decode('utf-8') == "ERROR: Invalid operation":
    print("server could not compute request. please try again.")

###########################################################################################

print("client is done!")