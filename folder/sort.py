f = open("outs.txt","r")
k = f.readline()
k = f.readline()
k = f.readline()
k = f.readline()
k = f.readline()
k = f.readline()
k = f.readline()
k = f.readline()
k = f.readline()
l = list()

while k != "":
	if(not(k.split(",")[1].split("_")[0] == "unknown" or k.split(",")[1].split("_")[0] == "no")):
		print(k)
		l.append(k.split(",")[0].split("\\")[2])
	k = f.readline()
lit = list(set(l))
print(lit)
print(len(lit))