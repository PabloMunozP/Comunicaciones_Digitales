from time import process_time
from PIL import Image
time_start = process_time()

for i in range (1,31):
    im = Image.open( "COD_WEBP/" + str(i) + "_webp.webp")
    im.convert("RGB").save("DEC_WEBP/" + str(i) + "_png.png", compress_level = 9)
    
time_stop = process_time()
tiempo=(time_stop-time_start)/30
salida=open("DEC_WEBP.txt","w")
salida.write('Tiempo de decompresion: '+str(tiempo)+' segundos')
print("Tiempo decompresión:", tiempo, " sec.")
salida.close()

