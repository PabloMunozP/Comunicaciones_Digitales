from time import process_time
from PIL import Image
import os
from skimage.measure.entropy import shannon_entropy
time_start = process_time()


salida=open("COD_JP2/COD_JP2.txt","w")
for i in range (1,31):
    im = Image.open( "Imagenes/" + str(i) + ".png")
    tam_org=os.path.getsize("Imagenes/" + str(i) + ".png")
    im.convert("RGB").save("COD_JP2/" + str(i) + "_jp2.jp2", 'JPEG2000', quality_mode='dB')
    tam_comp=os.path.getsize("COD_JP2/" + str(i) + "_jp2.jp2")
    salida.write('Diferencia de tamaño:' + str(tam_org-tam_comp)+' bytes\n')    
time_stop = process_time()
tiempo=(time_stop-time_start)/30
salida.write('Tiempo de compresion: '+str(tiempo)+' segundos')
print("Tiempo compresión:", tiempo, " sec.")
salida.close()

entropia=0
for i in range (1,31):
    img2 = Image.open ("COD_JP2/" + str(i) + '_jp2.jp2')
    entropia= shannon_entropy(img2) + entropia
print(entropia/30, " Entropia promedio")

