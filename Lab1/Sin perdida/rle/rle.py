from time import process_time
import os 
import collections
import math
import sys
 
def entropy(text):
    m = len(text)
    bases = collections.Counter([tmp_base for tmp_base in text])
 
    entropy_value = 0
    for base in bases:
        n_i = bases[base]
        p_i = n_i / float(m)
        entropy_i = p_i * (math.log(p_i, 2))
        entropy_value += entropy_i
 
    return entropy_value * -1

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''
                
    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
        # ...then add the count and character
        # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
        # Or increment our counter
        # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        # If the character is numerical...
        if char.isdigit():
        # ...append it to our count
            count += char
        else:
        # Otherwise we've seen a non-numerical
        # character and need to expand it for
        # the decoding
            decode += char * int(count)
            count = ''
    return decode


if __name__=='__main__':

    start = process_time()
    dif=[]
    salida3=open('Salida.txt','w')
    salida3.write('\n Aleatorias\n\n')
    for i in range(1,31):
        entrada = open("/mnt/c/Users/frost/Desktop/Lab1/Aleatorias/Ale_"+str(i)+".txt",'r').read()
        tam_org=os.path.getsize("/mnt/c/Users/frost/Desktop/Lab1/Aleatorias/Ale_"+str(i)+".txt")
        encoding=rle_encode(entrada)
        #print(encoding)
        salida1=open("rle_encode_"+str(i)+".txt",'w')
        salida1.write(encoding)
        salida1.close()
        tam_comp=os.path.getsize("/mnt/c/Users/frost/Desktop/Lab1/Sin perdida/rle/rle_encode_"+str(i)+".txt")
        dif.append(tam_org-tam_comp)
        salida3.write('Diferencia '+ str(tam_org-tam_comp) +' bytes    Entropia: '+ str(entropy(encoding))+'\n')
        #decoding=rle_decode(encoding)
        #salida2=open("rle_decode_"+str(i)+".txt",'w')
        #salida2.write(decoding)
        #salida2.close()

    stop=process_time()
    tiempo=(stop-start)/30
    salida3.write('Tiempo: '+str(tiempo )+ ' segundos\n')
    print('tiempo total: ', tiempo,' segundos\n')







    