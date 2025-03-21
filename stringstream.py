import io

#Mostrando como funcionam streams
a_string = "McCauley Culkin"

#Cria uma stream de bytes à partir de uma string
a_file = io.StringIO(a_string)

#McCauley Culkin
print(a_file.read())
#
print(a_file.read())
#0
print(a_file.seek(0))
#McCauley C
print(a_file.read(10))
#10
print(a_file.tell())
#12
print(a_file.seek(12))
#kin
print(a_file.read())
