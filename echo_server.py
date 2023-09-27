"""
This program works in tadem with a client. It is a server designed to accept two
numbers and an operation from the client. With this information, the server will
perform the operation using the provided numbers and return the result to the
client.

"""
# necessary libraries
import socket
import math

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# the chosen delimiter on the client side, needed to decode the data
delimiter = ";"

# tracing to let the  user know that the server is attempting connection with the client
print("server starting - listening for connections at IP", HOST, "and port", PORT)

# once connected, tracing lets the user know
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            # decoding incoming data from bytes to a string
            decoded_data = data.decode('utf-8') 

            # tracing to let the user know what the received data is
            print("received client message: " + decoded_data)

            # separating the operation and numbers based on the delimiter
            operation = decoded_data.split(delimiter)[0]
            both_numbers = decoded_data.split(delimiter)[1]

            # tracing to let the user know what the operation and numbers are
            print("requested operation is " + operation)
            print("requested arguments: " + both_numbers)

            # separating the numbers with a comma as the delimiter
            # converting to float instead of int in case user inputs large number
            first_num = float(both_numbers.split(",")[0])
            second_num = float(both_numbers.split(",")[1])

            # tracing to let the user know what the server is performing
            print(f"computing {operation} of {both_numbers}")

            # series of if statements that will excecute based on operation
            # note useage of f-strings for improved readability
            if operation == "LCM" or operation == "lcm":
                # uses math library's built in LCM function
                LCM = math.lcm(int(first_num),int(second_num))

                # tracing to let the user know the 
                print(f"The LCM of {first_num} and {second_num} is {LCM}")
                print("sending result back to client")

                # converts integer to bytes and sends back to client
                conn.sendall(bytes(str(LCM), 'utf-8'))
            elif operation == "mean" or operation == "Mean":
                # basic calculation for mean
                mean = (first_num + second_num) / 2

                # tracing to let the user know the result
                print(f"The mean of {first_num} and {second_num} is {mean}")
                print("sending result back to client")

                # converts integer to bytes and sends back to client
                conn.sendall(bytes(str(mean), 'utf-8'))
            else:
                # if the given operation is neither LCM nor mean, there is an error
                print("ERROR: Invalid operation")
                print("sending result back to client")

                # sends error message back to the client
                conn.sendall("ERROR: Invalid operation")

print("server is done!")