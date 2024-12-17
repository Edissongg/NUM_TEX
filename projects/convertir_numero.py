# convertir/convertir_numero.py

# Función para generar y concatenar palabras aleatorias
def generar_concatenar_palabras(palabras, conectores):
    resultado = []
    palabras_1 = "un"

    for i in range(len(palabras)):
        if len(palabras) == 2 or len(palabras) == 4:
            if palabras[0] == "un" and palabras_1 == "un":
                palabras_1 = ""
                resultado.append(palabras_1)  # Añadimos la palabra actual
            else:
                resultado.append(palabras[i])  # Añadimos la palabra actual
        else:
            resultado.append(palabras[i])  # Añadimos la palabra actual

        # Añadir los conectores entre las palabras
        if i < len(palabras) - 1:
            if conectores[len(palabras)-2-i] == " mil " and palabras[i] == "":
                continue
            elif conectores[len(palabras)-2-i] == " millones " and palabras[i] == "" and len(palabras) > 4:
                continue
            elif conectores[len(palabras)-2-i] == " millones " and palabras[i] == "un":
                resultado.append(" millon ")
            elif conectores[len(palabras)-2-i] == " billones " and palabras[i] == "un":
                resultado.append(" billon ") 
            else:
                resultado.append(conectores[len(palabras)-2-i])  # Añadimos el conector de esa posición
    
    return "".join(resultado)

# Función para convertir números a texto
def numero_a_letras(num, n_g, n_g_1):
    unidades = ["", "un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", 
                "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", 
                "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", 
                "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
    
    unidades_caso_2 = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", 
                "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", 
                "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", 
                "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
    
    decenas = ["", "", "", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    
    centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", 
                "setecientos", "ochocientos", "novecientos"]
    
    if num < 30:
        return unidades_caso_2[num] if n_g == n_g_1 else unidades[num]
    
    if num == 100:
        return "cien"
    
    if num > 99 and num < 200:
        return "ciento" if num % 100 == 0 else "ciento " + numero_a_letras(num % 100, n_g, n_g_1)
    
    if num >= 30 and num < 100:
        decena = num // 10
        unidad = num % 10
        return (decenas[decena] + (" y " + unidades_caso_2[unidad] if unidad > 0 else "") 
                if n_g == n_g_1 else 
                decenas[decena] + (" y " + unidades[unidad] if unidad > 0 else ""))
    
    if num >= 100 and num < 1000:
        centena = num // 100
        resto = num % 100
        return (centenas[centena] if resto == 0 else 
                centenas[centena] + " " + numero_a_letras(resto, n_g, n_g_1))

# Función principal que combina los grupos
def convertir_numero_a_texto(numero):
    numero_invertido = str(numero)[::-1]
    
    # Dividimos el número en grupos de tres cifras
    grupos = [numero_invertido[i:i+3] for i in range(0, len(numero_invertido), 3)]
    
    # Invertimos el orden de los grupos y convertimos los valores a enteros
    grupos_invertidos = [grupo[::-1] for grupo in grupos]
    grupos_invertidos.reverse()
    
    # Convertir a enteros
    grupos_enteros = [int(grupo) for grupo in grupos_invertidos]
    
    # Preparar los conectores
    conectores = [" mil ", " millones ", " mil ", " billones "]
    
    # Lista para almacenar los textos de los grupos
    grupos_texto = []
    cantidad_grupos = len(grupos_enteros)
    
    for i, grupo in enumerate(grupos_enteros, 1):
        grupo_texto = numero_a_letras(grupo, i, cantidad_grupos)
        grupos_texto.append(grupo_texto)
    
    # Concatenamos los grupos
    resultado = generar_concatenar_palabras(grupos_texto, conectores)
    return resultado.capitalize()
