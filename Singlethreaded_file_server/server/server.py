import socket,os


host = '127.0.0.1'              #loopback ip address
port = 8080                   #listening port number


with socket.socket() as sock:
	print("Server initiated")
	sock.bind((host, port))
	sock.listen()
	client_sock_obj, address = sock.accept()
	with client_sock_obj:
			while True:
				data = client_sock_obj.recv(1024).decode('utf-8')
				if data.split('&')[0] == 'upload':
					with open(data.split('&')[1], 'w') as filename:
						filename.write(data.split('&')[2])
					print(address,data.split('&')[0],data.split('&')[1])
					client_sock_obj.send('uploaded'.encode('utf-8'))

				elif data.split('&')[0] == 'download':
					with open(data.split('&')[1]) as filename:
						fdata = filename.read()
					print(address, data.split('&')[0],data.split('&')[1])
					data = data.split('&')[1] + '&' + fdata
					client_sock_obj.send(data.encode('utf-8'))

				elif data.split('&')[0] == 'delete':
					os.remove(data.split('&')[1])
					print(address, data.split('&')[0],data.split('&')[1])
					client_sock_obj.send('deleted'.encode('utf-8'))

				elif data.split('&')[0] == 'rename':
					os.rename(data.split('&')[1], data.split('&')[2])
					print(address, data.split('&')[0],data.split('&')[1],data.split('&')[2])
					client_sock_obj.send('renamed'.encode('utf-8'))

				else:
					print(address, data)
					if data == 'exit': break
					client_sock_obj.send('data transfer complete'.encode('utf-8'))




		
