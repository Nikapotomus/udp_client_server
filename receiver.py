import socket

UDP_IP = "127.0.0.1"
UDP_RECEIVING_PORT = 5005
UDP_SENDING_PORT = 5006

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_RECEIVING_PORT))

def identify_calculation(pd):

    # print("Parsed packet is: {}").format(pd)
    if pd[1].strip() == "+":
        return int(pd[0]) + int(pd[2])

    if pd[1].strip() == "-":
        return int(pd[0]) - int(pd[2])

    if pd[1].strip() == "*":

        return (int(pd[0]) * int(pd[2]))

    if pd[1].strip() == "/":
        return int(pd[0]) / int(pd[2])

    return "Non supported manipulation"


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    if data is not None:
        print "Received packet:", data
        parsed_data = data.split(",")

        print("the result is : {}").format(identify_calculation(parsed_data))

        result = identify_calculation(parsed_data)

        print(">>> Sending back the result of {}".format(str(result)))
        sock.sendto(str(result), (UDP_IP, UDP_SENDING_PORT))
