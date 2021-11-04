import socket
import time

arr=[]
def get_recent_hits():
	a = [None]*len(arr)
	for i in range(len(arr)):
		a[i]=arr.pop(0).decode()
	return a
	
udp_IP = "192.168.1.100" #127.0.0.1 or 
udp_broadcast = 7500
udp_receive = 7501

def udp_socket_receive():
	receive_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	receive_sock.bind((udp_IP, udp_receive))
	while True:
		data, addr = receive_sock.recvfrom(1024)
		arr.append(data)
	return

def udp_socket_send(Message): #change receives to sends
	Message = str(Message)
	send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	send_sock.sendto(Message.encode(), (udp_IP, udp_broadcast))	

	
if __name__ == '__main__':
	print('main')
	