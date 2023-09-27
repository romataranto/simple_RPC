# simple_RPC

## Overview of Application

This is a Remote Procedure Call (RPC) server. It accepts incoming network requests to perform two distinct types of computation: Lowest Common Multiple (LCM) or the average (mean). The user inputs two arguments (two numbers), as well as the selected operation. The arguments are sent to a server to be computed, and then returned to the client to be displayed to the user.

## Client -> Server Message Format

The client creates the message (MSG) by concatonating the selected operation, a delimiter (in this case, a semi-colon), and the two inputed numbers. The numbers are separated by a comma. 

Appropriate error handling is implemented, ensuring that the correct information, in the correct format, has been provided. An infinite while loops lets the user know what is wrong with their input and keeps prompting them to provide correct arguments until they are accepted.

Finally, the client take the MSG and converts it to bytes, encoding using utf-8.

## Server -> Client Message Format

The server recieves the MSG from the client in bytes. First, it decodes it using utf-8. Then, it splits the string using the delimiter, separating the operation from the numbers. It further splits the numbers into first_num and second_num by using the comma. It then enters an if statement based on the operation type, where it will compute the result. Then, it re-encodes the result using utf-8 and sends it back to the client. The client then de-codes the result and displays it to the user.

Error handling is also implemented on the server side, however, to a lesser extent. If (somehow) the calculation fails, the server will send an error message back to the client so that the client can notify the user.

## Example Output

### LCM

If the user wanted to know what the LCM of 40 and 56 is, they would see the following output.

CLIENT:
```bash
C:\Users\romap\OneDrive\Documents\computer networks>python echo_client.py
give two numbers, separated by a comma: 40, 56
the provided numbers have been accepted
would you like the server to find the LCM or the mean? LCM
the provided operation has been accepted
client starting - connecting to server at IP 127.0.0.1 and port 65432
connection established, sending message 'LCM;40, 56'
message sent, waiting for reply
received response: 280.0 [3 bytes]
client is done!
```

SERVER:
```bash
C:\Users\romap\OneDrive\Documents\computer networks>python echo_server.py
server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 50931)
received client message: LCM;40, 56
requested operation is LCM
requested arguments: 40, 56
computing LCM of 40, 56
The LCM of 40.0 and 56.0 is 280
sending result back to client
server is done!
```

### Mean

If the user wanted to know what the mean of 4829 and 5298340 is, they would see the following output.

CLIENT:
``` bash
C:\Users\romap\OneDrive\Documents\computer networks>python echo_client.py
give two numbers, separated by a comma: 4829,5298340
the provided numbers have been accepted
would you like the server to find the LCM or the mean? mean
the provided operation has been accepted
client starting - connecting to server at IP 127.0.0.1 and port 65432
connection established, sending message 'mean;4829,5298340'
message sent, waiting for reply
received response: 2651584.5 [9 bytes]
client is done!
```

SERVER:
``` bash
C:\Users\romap\OneDrive\Documents\computer networks>python echo_server.py
server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 51087)
received client message: mean;4829,5298340
requested operation is mean
requested arguments: 4829,5298340
computing mean of 4829,5298340
The mean of 4829.0 and 5298340.0 is 2651584.5
sending result back to client
server is done!
```

## Acknowledgments

I would like to acknowledge Nathan Jennings for his Socket Programming in Python (Guide). This gave me a solid understanding of socket programming and a skelton code to begin with.

I would like to acknowledge my Dad. I gave him my code and asked him to break it. He broke it 6 different ways, which I fixed in error handling. It is a much more robust system now!
