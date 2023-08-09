import serial
import requests
import webbrowser

# Defina o URL do site que você deseja abrir
site_url = "https://tmi.intermaritima.com.br/"
 
# Imagem ASCII
ascii_art = '''
                 :############################################!.      
               .################################################!     
               !#################################################:
               !#################################################:
               !#################################################:
               !###################!###!!########!!##############:
               !###############!   :##.   :#####: :##############:
               !###############:   ##: .    !##!. ###############:
               !###############   !#!. !#:   .#: !###############:
               !##############.  :##! !###!.    :################:
               !#############:   !#! .!#####:   !################:
               !#################################################:
               !#################################################:
               !############!:.. .::!!!!!!!!!:. ...!#############:
               !###!!: ..:!##########################!:. .:!#####:
                 .!###########################################!..      
                !###############################################:     
                 .!#########################################!.       
'''
# Exibe a imagem ASCII
print(ascii_art)

# Abra o site no navegador padrão do sistema
webbrowser.open(site_url)

def ler_porta_serial(porta, velocidade, databits, parity, stopbits, flowcontrol, url):
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
    print("Conexão estabelecida com a porta serial:", porta)

    while True:
        if ser.in_waiting > 0:
            dado = ser.readline()
            dado_str = dado.decode()
            # Extrair o valor "16080" da string
            peso = dado_str.split()[1]
            print("Dados recebidos da Balança:", peso)
            enviar_dados_para_php(peso, url)

def enviar_dados_para_php(peso, url):
    try:
        # Enviar a requisição POST com os dados do peso
        response = requests.post(url, data=peso)  # Envia o peso diretamente como um valor de string no corpo da requisição
        # Verificar a resposta da página PHP (opcional)
        if response.status_code == 200:
            print("Dados enviados com sucesso para o Sistema da Balança.")
        else:
            print("Erro ao enviar os dados para o Sistema da Balança.")
    except requests.exceptions.RequestException as e:
        print("Erro de conexão:", e)

if __name__ == '__main__':
    porta_serial = "COM4"
    velocidade = 4800
    databits = 7
    parity = serial.PARITY_EVEN
    stopbits = 2
    flowcontrol = False
    webhook_url = site_url  # Substitua pelo URL do arquivo que vai receber em seu sistema de Balança
    ler_porta_serial(porta_serial, velocidade, databits, parity, stopbits, flowcontrol, webhook_url)
