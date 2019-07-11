import serial

#remplacer les XXXX par le num de la cart arduino
ser = serial.Serial('/dev/ttyACM0')
print("CRTL + C pour arreter")

#rentre dans la boucle
while True :
	#test avec le demarage 
	demarage = int(input('est ce que je m allume BG ?(1=oui / 2=non)'))
	print(ser)
	#envoye de la data 
	ser.write(str(demarage).encode())
