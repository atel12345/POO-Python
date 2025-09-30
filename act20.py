adresses_ip=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]

#1)	192.168.0.1
#2)	169.254.0.1
#3)	172.16.0.1

adresses_ip.append("172.31.0.1")		#4)
print("Aprés l'ajout :\t",adresses_ip,"\n")

adresses_ip.remove("200.100.50.1")		#5)
print("Aprés la suppression :\t",adresses_ip,"\n")

#6) Il reste 5 adresses

if "192.168.0.1" in adresses_ip:		#7)
	print("192.168.0.1 existe dans la liste\n")

#8) L'adresse 10.0.0.1 est dans la classe A

adresses_ip.sort()						#9)
print("Aprés le tri croissant :\t",adresses_ip,"\n")

not_found=10							#10)
j=0
for i in adresses_ip:
	if (int(adresses_ip[j].split('.')[0])!=192):
		not_found=1
	j+=1
if(not_found):
	print("Il ya des adresses qui sont pas de classe C\n")
else:
	print("Toutes les adresses sont de classe C\n")


n_ip_pub=0								#11)
j=0
for i in adresses_ip:
	if (int(adresses_ip[j].split('.')[0]) not in {192,10,172}):
		n_ip_pub+=1
	j+=1
print(f"Il ya {n_ip_pub} adresse(s) ip publique(s)\n")