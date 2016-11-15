import socket

UDP_IP = "127.0.0.1"
UDP_SENDING_PORT = 5005
UDP_RECEIVING_PORT = 5006

print ("UDP target IP: {}".format(UDP_IP))
print ("UDP target port: {}".format(UDP_SENDING_PORT))
print ("Listening on port: {}".format(UDP_RECEIVING_PORT))

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


sock.bind((UDP_IP, UDP_RECEIVING_PORT))


while True:
    MESSAGE = raw_input('Enter the calculation in the format of eg: 2, *, 2\n')

    sock.sendto(MESSAGE, (UDP_IP, UDP_SENDING_PORT))

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    if data is not None:
        print "Result is:", data
