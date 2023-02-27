"""
accion1 = "Ya estoy en la entrada del evento"
accion2 = "Me estoy registrando" 

#estrutura de control (condicional o sentencia  if o si)
# permite continuar un flujo(realizar algo) si se cumple una condicion
# y en caso de no cumplirse, se puede o no continuar con otro flujo (hacer otra cosa) 
# esta sentencia (condicional if) va acompañado de los operadores de comparacion


if estrutura_datos_uno < estrutura_datos_dos
if estrutura_datos_uno > estrutura_datos_dos
if estrutura_datos_uno <= estrutura_datos_dos
if estrutura_datos_uno >= estrutura_datos_dos
if estrutura_datos_uno == estrutura_datos_dos
if estrutura_datos_uno != estrutura_datos_dos


# hay varias maneras de utilizar la sentencia if
#if simple, if compuesto, if anidado
 

#if simple
dato_comparacion = 18
edad =  19



if edad >= dato_comparacion:
    print("Ingresar, disfrutar del evento")

#if compuesto
if edad >= dato_comparacion:
    print("Ingresar, disfrutar del evento")
else:
    print("No ingresar")



fecha_evento = "28-02-2023"
fecha_comparacion = "28-02-2023"
boleta = True

#if anidado
if edad >= dato_comparacion and boleta and fecha_evento == fecha_comparacion:
    print("Ingresar, disfrutar del evento")
else:
    print("No ingresar")
"""
""
#localidad de voletas
dato_comparacion = 18
edad =  19
boleta = True
localidad = 2

if edad >= dato_comparacion and boleta:
    print("Ingrese, disfruta del evento")
else:
    print("No puedes ingresar, sigue intentando")

if localidad >= dato_comparacion and boleta:
    print("Selecciona el tipo de voleta que desea")

if localidad == 1 and edad >= dato_comparacion and boleta:
    print("La localidad de su voleta es vip")
if localidad == 2 and edad >= dato_comparacion and boleta:
    print("La localidad de su voleta es preferencial")
if localidad == 3 and edad >= dato_comparacion and boleta:
    print("La localidad de su voleta es general")
if localidad == 4 and edad >= dato_comparacion and boleta:
    print("La localidad de su voleta es baja")
if localidad < 1 or localidad > 4:
    print("La localidad de su boleta es erronea")
""

