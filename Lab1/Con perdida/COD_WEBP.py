from time import process_time
from PIL import Image
import os
time_start = process_time()

salida=open("COD_WEBP/COD_WEBP.txt","w")
for i in range (1,31):
    im = Image.open( "Imagenes/" + str(i) + ".png")
    tam_org=os.path.getsize("Imagenes/" + str(i) + ".png")
    im.convert('RGB').save("COD_WEBP/" + str(i) + "_webp.webp", quality = 50)
    tam_comp=os.path.getsize("COD_WEBP/" + str(i) + "_webp.webp")
    salida.write('Diferencia de tamaño:' + str(tam_org-tam_comp)+' bytes\n')
time_stop = process_time()
tiempo=(time_stop-time_start)/30
salida.write('Tiempo de compresion: '+str(tiempo)+' segundos')
print("Tiempo compresión:", tiempo, " sec.")
salida.close()
