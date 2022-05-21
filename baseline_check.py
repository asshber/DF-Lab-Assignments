
dump1 = open('1.dd','rb')
dump2 = open('2.dd','rb')
bytes=b'x00'
bytes1=b'x00'
while bytes:
	bytes=dump1.read(512)
	bytes1=dump2.read(512)
	if(bytes!=bytes1):
		print("Not same")
		exit()

print("Same")

