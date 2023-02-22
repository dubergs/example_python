datos_tienda = {
    "Zapatos": 350000,
    "Tenis": 280000,
    "Jeans": 200000,
    "Camisas": 175000,
}
print("Articulos de tienda:", datos_tienda)


#valor del total de los productos
price = datos_tienda["Camisas"] + datos_tienda["Jeans"] + datos_tienda["Tenis"] + datos_tienda["Zapatos"]
print("El total de todos los productos es:", price)

#promedio
promedio = price / 4
print("El precio promedio es de:", promedio)

#aumentar
aumentar = 6.2
aumento = datos_tienda["Jeans"]* (aumentar / 100)
valor_con_aumento = datos_tienda["Jeans"] + aumento 
print("El precio de los jeans incremento en un 6.2%")
print(valor_con_aumento)


#disminucion
disminucion = 0.8
disminuir = datos_tienda["Zapatos"] * (disminucion / 100)
precio_con_disminucion = datos_tienda["Zapatos"] - disminuir
print("El precio de los zapatos disminuyo un 0.8%")
print(precio_con_disminucion)


