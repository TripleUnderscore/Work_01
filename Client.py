

import argparse
import socket
import pickle
import time

HOST = 'localhost'
PORT = 6666


def send_indice(indice):

	try:
		client_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client_server_socket.connect((HOST, PORT))
		int_to_string = str(indice)
		client_server_socket.send(int_to_string.encode())

	except:
		print("\n[!] Error with the connexion to the computing server.")



def ask_for_list():

	try:
		client_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client_server_socket.connect((HOST, PORT))
		print("\n[+] Connexion initialisee.") 
		client_server_socket.send(b"list")

		print("\n[+] Reception de l'indice de suivi des taches et du registre des taches...")
		indice_encoded = client_server_socket.recv(1024)
		indice_decoded = indice_encoded.decode()
		indice = int(indice_decoded)

		i = 0
		while i != indice_suivi:
			data_received = client_server_socket.recv(1024)
			data_readable = pickle.loads(data_received)
			print("\n - {0}".format(data_readable)) 
			i += 1
			time.sleep(1)

	except:
		print("\n[!] Error with the connexion to the computing server.")



def stop_server():

	try:
		client_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client_server_socket.connect((HOST, PORT))
		client_server_socket.send(b"stop")

	except:
		print("\n[!] Error with the connexion to the computing server.")


### NOT IMPLEMENTED YET
#
# def start_server():
#
#	try:
#		os.system('SERVER.PY_PATH/server.py')
#
#
#	except:
#		print("\n[!] Error with the start to the computing server.")
#
###


def parsing_function():

	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--send", help="fibonacci indice you want to get ; exemple : send 7", type=int)
	parser.add_argument("-l", "--list", help="display list of tasks - scheduled and done -", action="store_true")
	parser.add_argument("-d", "--down", help="shutdown computing server ; you will need --go option to restart it, but all of saved tasks will be lost", action="store_true")
	# parser.add_argument("-g", "--go", help="restart computing server after using --stop option", action="store_true")
	args = parser.parse_args()

	if args.send:
		send_indice(args.send)
	elif args.list:
		ask_for_list()
	elif args.down:
		stop_server()
	# elif args.go:
	#	start_server()
	else:
		print("\nArgument error : use -h when launching the client to get more help\n")


def main():
	parsing_function()

if __name__ == '__main__':
	main()


