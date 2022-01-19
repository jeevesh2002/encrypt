def encrypt(path,key):
	try:	
		print('The path of file : ', path)
		print('Key for encryption : ', key)
		with open(path, 'rb') as fin:
			image = fin.read()
		image = bytearray(image)
		for index, values in enumerate(image):
			image[index] = values ^ key
		with open(path, 'wb') as fin:
			fin.write(image)
		print('Encryption Done...')
	except Exception:
		print('Error caught : ', Exception.__name__)

