import socket
import math

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

delimiter = ";"

print("server starting - listening for connections at IP", HOST, "and port", PORT)
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
            
            decoded_data = data.decode('utf-8') #decoding incoming data from bytes to a string

            print("received client message: " + decoded_data)

            operation = decoded_data.split(delimiter)[0]
            both_numbers = decoded_data.split(delimiter)[1]

            print("requested operation is " + operation)
            print("requested arguments: " + both_numbers)
            #print("computing " + operation + " of " + both_numbers)

            first_num = int(both_numbers.split(",")[0])
            second_num = int(both_numbers.split(",")[1])

            print(f"computing {operation} of {both_numbers}")

            if operation == "LCM":
                LCM = math.lcm(first_num,second_num)
                #print("The LCM of " + str(first_num) + " and " + str(second_num) + " is " + str(LCM))
                print(f"The LCM of {first_num} and {second_num} is {LCM}")
                print("sending result back to client")
                conn.sendall(bytes(str(LCM), 'utf-8'))
            elif operation == "mean":
                mean = (first_num + second_num) / 2
                #print("The mean of " + str(first_num) + " and " + str(second_num) + " is " + str(mean))
                print(f"The mean of {first_num} and {second_num} is {mean}")
                print("sending result back to client")
                conn.sendall(bytes(str(mean), 'utf-8'))
            else:
                print("ERROR: Invalid operation")
                print("sending result back to client")
                conn.sendall("ERROR: Invalid operation")

print("server is done!")