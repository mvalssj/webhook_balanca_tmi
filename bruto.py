import serial

def ler_porta_serial(porta, velocidade, databits, parity, stopbits, flowcontrol):
    ser = serial.Serial(
        port=porta,
        baudrate=velocidade,
        bytesize=databits,
        parity=parity,
        stopbits=stopbits,
        xonxoff=flowcontrol,
        rtscts=True,  # Habilita o controle RTS
        timeout=0
    )
    print(f"Conexão estabelecida com a porta serial: {porta}")

    while True:
        if ser.in_waiting > 0:
            dado = ser.readline()
            dado_str = dado.decode('latin-1')
            peso = dado_str[2:-2]
            #print("Peso recebido da balança:", dado_str)
            print("Peso recebido da balança:", peso)
            #print("Peso recebido da balança:", dado)

if __name__ == '__main__':
    porta_serial = "COM5"
    velocidade = 4800
    databits = 7
    parity = serial.PARITY_EVEN
    stopbits = 2
    flowcontrol = False
    ler_porta_serial(porta_serial, velocidade, databits, parity, stopbits, flowcontrol)
