import random ,string

for i in range(0,30):
    textFile=open("textos_in/texto_"+str(i)+'.txt',"w")
    ran=random.seed()
    textData= "".join([random.choice(string.printable) for i in range(random.randint(30,50))])
    print(textData)
    textFile.write(textData)
    textFile.close()
