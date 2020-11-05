import unireedsolomon as rs 


for i in range(0,30):
    text_in=open("textos_in/texto_"+str(i)+'.txt',"r").read()
    tam=len(text_in)
    print('Texto a codificar: ' , text_in,'\n')

    coder= rs.RSCoder(70,tam)#tamaño del texto codif, tamaño texto plano
    c=coder.encode(text_in)
    print('Texto codificado: ',c,'\n')
    text_out=open("textos_out/texto_"+str(i)+'.txt',"w")
    text_out.write(c)
    text_out.close()

