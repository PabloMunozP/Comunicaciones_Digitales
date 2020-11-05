import random,string


for i in range(0,30):
    ran=random.seed()
    p=100
    text_in=open("textos_out/texto_"+str(i)+".txt","r").read()
    print('Texto original:', text_in)
    for j in range(0,len(text_in)):
        if random.randint(1,p) == 1:
            cambio=random.choice(string.printable)
            print('reemplaza: ' , text_in[j], ' por : ' , cambio)
            text_in=text_in[:j-1] + cambio +text_in[j+1:]
    
    print('Texto con error:',text_in)
    texto_out=open("textos_error/texto_"+str(i)+".txt","w")
    texto_out.write(text_in)
    texto_out.close()