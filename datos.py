
# utilizamos una variable de tiempo
import datetime
# Los datos que se tiene se calculan y son de caracteristicas diferentes.

def main():
 # Los string los usamos para preguntar.
 strDato = input("Dame un dato string: ")
 # Los valores numericos se ponen con string.
 _iDato = input("Dame un dato entero: ")
 iDato = int(_iDato)
 _fDato = input("Dame un dato float: ")
 fDato =float(_fDato)
 # Los valores de fecha se pregunta hasta la terminacion.
 _dtDato = input("Dame una fecha yyyy/mm/dd: ")
 # se extrae las posiciones de m a la n.
 #se extrae posiciones hasta el final.

 años=_dtDato[1:6]
 mes=_dtDato[2:5]
 dia=_dtDato[1-10:]
 print(años)
 print(mes)
 print(dia)
 dtDato = datetime.datetime(int(años), int(mes), int(dia))
 print(strDato)
 print(type(strDato))
 print(iDato)
 print(type(iDato))
 print(fDato)
 print(type(fDato))
 print(dtDato)
 print(type(dtDato))