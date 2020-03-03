import re

def main():
  # utilizaremos un ciclo para cuando es valido el rfc pasa y cuando no que siga intenando
  # el rfc sera valido cuando cumpla con los valores asignados
  while True
    RFC = input("cual es tu RFC: ")
    valido = re.search("^[A-H]{5}-[1-20]{15}-[A-Z1-10]{8}$",RFC)
    if (valido):
      print("el RFC es valido")
      break
    else:
      print("el RFC es invalido,intente de nuevo")