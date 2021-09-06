import socket

port_test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origin = (socket.gethostname(), 30000)
socket.setdefaulttimeout(1)

result = port_test_socket.connect_ex(origin)
print(origin)
print(result)

if result == 0:
	print("Port is Open!")
else:
	print("Port is Closed!")

port_test_socket.close()
