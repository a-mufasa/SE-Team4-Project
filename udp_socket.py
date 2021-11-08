import socket
import time
import array

arr=[]
def get_recent_hits():
	a = [None]*len(arr)
	for i in range(len(arr)):
		a[i]=arr.pop(0)
	return a
	
udp_IP = "localhost" #127.0.0.1 or 192.168.1.100
udp_broadcast = 7500
udp_receive = 7500#7501

def udp_socket_receive():
	receive_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	receive_sock.bind((udp_IP, udp_receive))
	while True:
		data, addr = receive_sock.recvfrom(1024)
		a=data.decode().split(',')# fix to github
		arr.append(a)
	return

def udp_socket_send(Message): #change receives to sends
	Message = str(Message)
	send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	send_sock.sendto(Message.encode(), (udp_IP, udp_receive))

	
if __name__ == '__main__':
	print('main')
	