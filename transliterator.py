from os import rename, listdir
from os.path import basename, splitext
from pytils import translit
path = input("Введите адресс папки:")

list_file = listdir(path)

for n in list_file:
    transl_file_name = translit.slugify(splitext(basename(n))[0])
    extension_file = splitext(n)[1]
    rename(path+'\\' + n,path+'\\' + transl_file_name + extension_file)

