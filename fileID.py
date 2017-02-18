def checkFile(file_txt,var):
	try:
		file=open(file_txt,'r')
	except:
		file=open(file_txt,'w')
		file.write(var)

def readID(file_txt):
	file=open(file_txt,'r')
	content=file.readline()
	return content

def overwriteID(file_txt,ID):
	file = open(file_txt, "w")
	file.write(str(ID))
	file.close()

def readList(file_txt):
	content = []
	file=open(file_txt,'r')
	for read in range(0,3):
		word = file.readline().strip('\n')
		content.append(word)
	return content

def overwriteList(file_txt,in_list):
	file = open(file_txt, "w")
	for line_list in range(0,3):
		file.write(str(in_list[line_list])+"\n")
	file.close()

checkFile("state.txt","0")