import socket

host = '127.0.0.1'
port = 8090

with socket.socket() as sock:
	sock.connect((host, port))
	print("client connected")
	while True:
		data = input("#")
		ldata = data.lower()
		if ldata.split(' ')[0] == 'upload':
			with open(data.split(' ')[1]) as filename:
				fdata = filename.read()
			data = ldata.split(' ')[0] + '&' +data.split(' ')[1] + '&' + fdata
			sock.send(data.encode('utf-8'))
			response = sock.recv(1024)
			print(response.decode('utf-8'))

		elif ldata.split(' ')[0] == 'download':
			data = ldata.split(' ')[0] + '&' +data.split(' ')[1]
			sock.send(data.encode('utf-8'))
			rdata = sock.recv(1024)
			urdata = rdata.decode('utf-8')
			with open(urdata.split('&')[0], 'w') as filename:
				filename.write(urdata.split('&')[1])
			print('downloaded')

		elif ldata.split(' ')[0] == 'delete':
			data = ldata.split(' ')[0] + '&' + data.split(' ')[1]
			sock.send(data.encode('utf-8'))
			rdata = sock.recv(1024)
			rdata = rdata.decode('utf-8')
			print(rdata)

		elif ldata.split(' ')[0] == 'rename':
			data = ldata.split(' ')[0] + '&' + data.split(' ')[1] + '&' + data.split(' ')[2]
			sock.send(data.encode('utf-8'))
			rdata = sock.recv(1024)
			urdata = rdata.decode('utf-8')
			print(urdata)

		else:
			sock.send(data.encode('utf-8'))
			rdata = sock.recv(1024)
			print(rdata.decode('utf-8'))

		if data == "exit": break
