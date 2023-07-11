archivo=open("devices.txt","a")

while True:
    newItem=input("Ingrese la nueva información (separado por un espacio): ")
    if newItem=="exit":
        break
    archivo.write(newItem+"\n")
    
#lista.write(archivo)
print (archivo)
    
archivo.close()
