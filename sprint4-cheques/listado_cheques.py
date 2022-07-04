import sys,csv
import datetime


POSICION_ARGUMENTO_NOMBRE_ARCHIVO = 1
POSICION_ARGUMENTO_DNI = 2
POSICION_ARGUMENTO_TIPO = 3
POSICION_ARGUMENTO_ESTADO = 4
POSICION_ARGUMENTO_FECHA = 5


ETIQUETA_CABECERA_CSV_NUM_CHEQUE = 'NroCheque'
ETIQUETA_CABECERA_CSV_CODIGO_BANCO = 'CodigoBanco'
ETIQUETA_CABECERA_CSV_CODIGO_SUCURSAL = 'CodigoSucursal'
ETIQUETA_CABECERA_CSV_NUMERO_CUENTA_ORIGEN = 'NumeroCuentaOrigen'
ETIQUETA_CABECERA_CSV_NUMERO_CUENTA_DESTINO = 'NumeroCuentaDestino'
ETIQUETA_CABECERA_CSV_VALOR = 'Valor'
ETIQUETA_CABECERA_CSV_FECHA_ORIGEN = 'FechaOrigen'
ETIQUETA_CABECERA_CSV_FECHA_PAGO = 'FechaPago'
ETIQUETA_CABECERA_CSV_DNI = 'DNI'
ETIQUETA_CABECERA_CSV_TIPO = 'Tipo'
ETIQUETA_CABECERA_CSV_ESTADO = 'Estado'


if __name__ == '__main__':
    with open(sys.argv[POSICION_ARGUMENTO_NOMBRE_ARCHIVO]) as archivo:
        lector = csv.reader(archivo)
        datos = list(lector)

    cabecera = datos[0]

    (posicion_num_cheque,
    posicion_codigo_banco,
    posicion_codigo_sucursal,
    posicion_numero_cuenta_origen,
    posicion_numero_cuenta_destino,
    posicion_valor,
    posicion_fecha_origen,
    posicion_fecha_pago,
    posicion_dni,
    posicion_tipo,
    posicion_estado) = (cabecera.index(ETIQUETA_CABECERA_CSV_NUM_CHEQUE),
                        cabecera.index(ETIQUETA_CABECERA_CSV_CODIGO_BANCO),
                        cabecera.index(ETIQUETA_CABECERA_CSV_CODIGO_SUCURSAL),
                        cabecera.index(ETIQUETA_CABECERA_CSV_NUMERO_CUENTA_ORIGEN),
                        cabecera.index(ETIQUETA_CABECERA_CSV_NUMERO_CUENTA_DESTINO),
                        cabecera.index(ETIQUETA_CABECERA_CSV_VALOR),
                        cabecera.index(ETIQUETA_CABECERA_CSV_FECHA_ORIGEN),
                        cabecera.index(ETIQUETA_CABECERA_CSV_FECHA_PAGO),
                        cabecera.index(ETIQUETA_CABECERA_CSV_DNI),
                        cabecera.index(ETIQUETA_CABECERA_CSV_TIPO),
                        cabecera.index(ETIQUETA_CABECERA_CSV_ESTADO))

valor = input("Elige: Pantalla o CSV")
valor = valor.lower()

if(valor == "pantalla"):
    datos_cliente = list(filter(
        lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI], datos[1:]))
    print(','.join(cabecera))

    for dato in datos_cliente:
        print(','.join(dato))
elif(valor == "csv"):
        archivoNuevo = open(
            f"{posicion_dni}{str(datetime.datetime.now()).replace(':','_')}.csv", "x")

        #datos_cliente = list(filter(lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI], datos[1:]))
        #for item in datos:
        #    newitem = item(filter(lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI], datos[1:]))
        #    print(newitem)

        archivoNuevo.write(str(datos))
        archivoNuevo.close()
else:
    print("Error")
           

       