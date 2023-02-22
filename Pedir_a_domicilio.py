lista_pedido = {
    "pizza x1": 20000,
    "Gaseosa x1": 10000,
    "hamburguesas x3": 21000,
    "helados x2": 16000
}
print(lista_pedido)
#costo pedido (sin propina)
valor_pedido = lista_pedido ["Gaseosa x1"] + lista_pedido ["pizza x1"] + lista_pedido ["hamburguesas x3"] + lista_pedido ["helados x2"]
print(valor_pedido)

#Propina
Propina = valor_pedido * (5/100)
print("La propina es de:", Propina)
#Costo total
suma = valor_pedido + Propina
print("El costo total del pedido es de:",suma)