import os

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


def convert_bytes_number(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return num
        num /= 1024.0

def file_size_number(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return file_info.st_size

#----------------------------------------------------------------
total_texts = 0
total_bin = 0
for i in range(1,31):
    file_name_texts = "Repetidas/Rep" + str(i) + ".txt"
    file_name_bin = "Aleatorias/Ale_" + str(i) + ".bin"
    print("Nombre del archivo: " + str(i) + ".txt" + " - Tamaño del archivo original: " +
          file_size(file_name_texts) + " - Tamaño del archivo comprimido: " + file_size(file_name_bin))
    total_texts = total_texts + int(file_size_number(file_name_texts))
    total_bin = total_bin + int(file_size_number(file_name_bin))
    porcentaje = total_bin/total_texts
print("Porcentaje promedio de compresión: " + str(porcentaje*100) + "%")
