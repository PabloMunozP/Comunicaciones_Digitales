import os
from time import process_time
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


def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    #dictionary = dict((chr(i), chr(i)) for i in xrange(dict_size))
    dictionary = {chr(i): chr(i) for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    """Decompress a list of output ks to a string."""

    # Build the dictionary.
    dict_size = 256
    #dictionary = dict((chr(i), chr(i)) for i in xrange(dict_size))
    dictionary = {chr(i): chr(i) for i in range(dict_size)}

    w = result = compressed.pop(0)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result += entry

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result

if __name__=='__main__':
    
    start=process_time()
    dif=[]
    salida3=open('Salida_Aleatorias.txt','w')
    salida3.write('\n Aleatorias\n')
    for i in range(1,31):
        
        entrada= open("/mnt/c/Users/frost/Desktop/Lab1/Aleatorias/Ale_"+str(i)+".txt",'r').read()
        tam_org=os.path.getsize("/mnt/c/Users/frost/Desktop/Lab1/Aleatorias/Ale_"+str(i)+".txt")
        encoding=compress(entrada)
        print(encoding,'\n')
        salida1=open("lzw_encode_"+str(i)+".txt",'w')
        encoding=str(encoding).replace('[','').replace(',', '').replace(']','').replace(' ','').replace("\'",'')
        print(encoding)
        salida1.write(str(encoding))
        salida1.close()
        tam_comp=os.path.getsize("/mnt/c/Users/frost/Desktop/Lab1/Sin perdida/lzw/lzw_encode_"+str(i)+".txt")
        dif.append(tam_org-tam_comp)
        salida3.write('Diferencia '+ str(tam_org-tam_comp) +' bytes    Entropia: '+ str(entropy(encoding))+'\n')
        #decoding=decompress(encoding)
        #salida2=open("lzw_decode_"+str(i)+".txt",'w')
        #salida2.write(str(decoding))
        #salida2.close()

    stop=process_time()
    tiempo=(stop-start)/30    
    salida3.write('Tiempo: '+str(tiempo )+ ' segundos\n')
    print('tiempo total: ', tiempo,' segundos\n')
