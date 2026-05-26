lista_sensores=[
   {"nombre_integrante1_1_lista": "nombre_integrante1_1", "integrante1_1_valor": 100}, 
   {"nombre_integrante1_1_lista": "nombre_integrante2_1", "integrante1_1_valor": 200}, 
   {"nombre_integrante1_1_lista": "nombre_integrante3_1", "integrante1_1_valor": 300}, 
]

print("listita")

for sensorsito in lista_sensores:

    nombresito1=sensorsito["nombre_integrante1_1_lista"]
    valorsito1=sensorsito["integrante1_1_valor"]

    if valorsito1 >=100:
        estadito="altito"

    elif valorsito1>50:
        estadito= "normal"
    else:
         estadito= "anormal"

    print ("estadito")


