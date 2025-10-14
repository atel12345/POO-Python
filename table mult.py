file=open(r'C:/Users/HH\Desktop/py/mult.txt','w+')
for i in range(10):
    file.write(f"La table de multiplication de {i+1}\n")
    print("\n")
    for j in range(10):
        file.write(f"{i+1} x {j+1} = {2*(j+1)}\n")

file.close()