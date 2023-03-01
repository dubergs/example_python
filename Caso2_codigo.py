accion1 = "Ya identifiqué el proyecto a trabajar" 
comparacion_proyecto = 1 and 2 and 3
proyectoA = 2
hora = 10000
horas_diarias = 8
dias = 30 
sueldo_max = 1500000  
print(accion1) 

sueldo_diario = hora * horas_diarias 
print("El salario diario es:", ) 
print(sueldo_diario) 
sueldo_mensual = sueldo_diario * dias 
print("El salario mensual es:") 
print(sueldo_mensual)
aumentar = 6.0
aumento = ((sueldo_mensual * (aumentar/100) * 3) + sueldo_mensual)

# if sueldo_mensual 
if sueldo_mensual > sueldo_max and proyectoA == 1:
    print("Su salario es mayor al tope máximo") 

if sueldo_mensual < sueldo_max and proyectoA == 2: 
    print("Se te incremento un 6% por hora:", aumento)

if sueldo_mensual < sueldo_max and proyectoA == 3: 
    print("Se te incremento un 6% por hora:", aumento)