import socket

target_host = "127.0.0.1"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data
client.sendto("AAABBBCCC", (target_host, target_port))

# Send some data
request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
client.send(request.encode())

# Receive some data
response = client.recv(4096)

print(response)
