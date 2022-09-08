import  json
import bcrypt
ar=[]
tupla=set()
def Alumnos():
    archivo = open("Estudiantes.prn", "r")
    for x in archivo:
        ar.append(x[0:8])
        ar.append(x[8:].replace("\n",""))
        tupla.add(tuple(ar))
        ar.clear()
    archivo.close()
    #print(tupla)
    return tupla
def Confirmar_nombre(NC):
    Nombre = Alumnos()
    for NO in Nombre:
        c,n=NO
        if(NC==c):
            return n
    return False
def contrasena(NC,Contra):
    Usuario=[]
    Contrasena=open("Usuarios.txt","r")
    for CO in Contrasena:
        CO.replace("\n","")
        CO=CO.split(" ")
        num_Control,Cont_no_Sifrada,Cont_si_Sifrada=CO
        if NC==num_Control:
            print(bcrypt.checkpw(Contra.encode("utf-8"), Cont_si_Sifrada.encode("utf-8"))) #Esta cosa segun tiene que regresar el valor de True y no jala aunque la contraseña si consida, sepa pq?
            return Contra==Cont_no_Sifrada
    Contrasena.close()
def autenticar_usuario(NC,Contr):
    directorio={}
    nom=Confirmar_nombre(NC)
    if nom!=False:
        if True==contrasena(NC,Contr):
            directorio["Bandera: "] = True
            directorio["Usuario: "] = nom
            directorio["Mensaje: "] = "Bienvenido al Sistema de Autenticación de usuarios"
        else:
            directorio["Bandera: "] = False
            directorio["Usuario: "] = nom
            directorio["Mensaje: "] = "Contraseña incorrecta"

    else:
        directorio["Bandera: "]=False
        directorio["Usuario: "]=" "
        directorio["Mensaje: "]="No existe el Usuario"
    return json.dumps(directorio)

Ur=input("Ingresa el Usuario: " )
Con=input("Ingresa la Contraseña")
print(autenticar_usuario(Ur,Con))
