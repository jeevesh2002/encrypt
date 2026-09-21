
def decrypt(path,key):
	try:
		print('The path of file : ', path)
		print('Note : Encryption key and Decryption key must be same.')
		print('Key for Decryption : ', key)
		with open(path, 'rb') as fin:
			image = fin.read()
		image = bytearray(image)
		for index, values in enumerate(image):
			image[index] = values ^ key
		with open(path, 'wb') as fin:
			fin.write(image)
		print('Decryption Done...')
	except Exception:
		print('Error caught : ', Exception.__name__)

