import sys,csv

POSICION_ARGUMENTO_NOMBRE_ARCHIVO = 1
POSICION_ARGUMENTO_DNI = 2
POSICION_ARGUMENTO_SALIDA = 3
POSICION_ARGUMENTO_TIPO = 4
POSICION_ARGUMENTO_ESTADO = 5
POSICION_ARGUMENTO_FECHA = 6


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

    datos_cliente = list(filter(lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI], datos[1:]))

    print(','.join(cabecera))
    for dato in datos_cliente:
        print(','.join(dato))
