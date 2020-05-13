

import socket
import sys
import ctypes
import pickle
import time


def init_global():

	global suivi_des_taches
	suivi_des_taches = [0]
	global indice_suivi
	indice_suivi = 0



def init_listening_mode():

	HOST = 'localhost'
	PORT = 6666

	fibonacci_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	fibonacci_server_socket.bind((HOST, PORT))
	fibonacci_server_socket.listen(5)

	# print("[+] Serveur en ecoute sur le port {0}\n".format(PORT))

	get_connexion, infos_connexion = fibonacci_server_socket.accept()

	# print("[+] Connexion etablie.\n")
	# print("[+] Serveur en attente de tache a traiter...\n")

	receive_packet(get_connexion)

	get_connexion.send(b"[+] Fermeture du service reseau...")
	get_connexion.close()
	fibonacci_server_socket.close()

	sys.exit(0)



def receive_packet(get_connexion):

	packet_received = b''
	indicateur = 0

	while indicateur == 0:

		packet_received = get_connexion.recv(1024)

		if packet_received == b'list':
			send_list(get_connexion)

		elif packet_received == b'stop':
			indicateur += 1

		else:
			fibonacci_number_result = fibonacci_calculate(packet_received, get_connexion)

			if fibonacci_number_result == "Error":
				continue	

			else:
				send_response(fibonacci_number_result, get_connexion)



def fibonacci_calculate(packet_received, get_connexion):

	global suivi_des_taches
	global indice_suivi

	try:
		fibonacci_number_string = packet_received.decode()
		fibonacci_number = int(fibonacci_number_string)
		get_connexion.send(b"[+] Indice correct, initialisation du suivi de tache...")

		if indice_suivi != 0:
			suivi_des_taches.append('[scheduled] fibo {0}'.format(fibonacci_number))
		else:
			suivi_des_taches = ['[scheduled] fibo {0}'.format(fibonacci_number)]
		
		get_connexion.send(b"[+] Initialisation terminee.")
		get_connexion.send(b"[+] Traitement de la tache...")

		# Indiquer le chemin absolu du binaire
		fibonacci_calcul = ctypes.CDLL("/home/dodo/Bricolage/Scille/fibonacci_module.so")
		fibonacci_result = fibonacci_calcul.fibonacci_module(fibonacci_number)
		# fibonacci_calculate : nom de la fonction dans le .so

		temp = suivi_des_taches[indice_suivi][0:]+' (Result : {0})'.format(fibonacci_result)
		temp = temp.replace('scheduled', 'done')
		suivi_des_taches[indice_suivi] = temp

		indice_suivi += 1
		
		return fibonacci_number, fibonacci_result

	except:
		get_connexion.send(b"[+] Il semble qu'il y ait une erreur dans la nature de l'indice.")
		return "Error"



def send_response(fibonacci_number_result, get_connexion):

	get_connexion.send(b"[+] Calcul termine, transfert du resultat...")
	result_string = "Valeur du nombre de Fibonacci d'indice {0} : {1}.".format(fibonacci_number_result[0], fibonacci_number_result[1])
	get_connexion.send(result_string.encode())

	return



def send_list(get_connexion):

	global suivi_des_taches
	global indice_suivi

	if indice_suivi == 0:
		get_connexion.send(b"[!] Aucune tache enregistree")
	else:
		indice_suivi_string = str(indice_suivi)
		get_connexion.send(indice_suivi_string.encode())
		i = 0
		while i != indice_suivi: 
			data_to_send = pickle.dumps(suivi_des_taches[i])
			get_connexion.send(data_to_send)
			i += 1
			time.sleep(1)
	return



if __name__ == '__main__':
	init_global()
	init_listening_mode()


