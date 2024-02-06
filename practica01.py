cont = 0

def hex_a_decimal(hexadecimal):
    return int(hexadecimal, 16)

def procesarLinea(linea):
    global cont

    if(cont == 0):
        linea = linea.split('\ufeff')
        linea = linea[1]
        cont += 1

    partes = linea.strip().split(',')
    
    numerosHexadecimales = partes[0].split('/')
    numerosHexadecimales = numerosHexadecimales[0]

    numerosHexadecimales = numerosHexadecimales.split(':')
    deimales = [hex_a_decimal(x) for x in numerosHexadecimales]
    
    sgundaCadena = partes[2]
    
    ip = partes[6].split('.')
    hex_ip = '.'.join(f"{int(x):X}" for x in ip)
    
    resultado = f"{sgundaCadena} : {' : '.join(map(str, deimales))} : {hex_ip}"
    
    return resultado

def procesamientoPorLotes(entrada, salida):
    with open(entrada, 'rb') as archivo, open(salida, 'w') as archivoSalida:
        for linea in archivo:
            linea = linea.decode('utf-8').strip()
            print(linea)
            resultado = procesarLinea(linea)
            archivoSalida.write(resultado + '\n')

entrada = '/home/dev_luis/Documentos/Universidad/S_SO/prueba2.txt'
salida = '/home/dev_luis/Documentos/Universidad/S_SO/resultado.txt'
procesamientoPorLotes(entrada, salida)