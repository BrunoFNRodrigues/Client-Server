#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from enlace import *
import time
import numpy as np
import random
import binascii
from utils import *


# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
# serialName = "COM3"                  # Windows(variacao de)


def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com3 = enlace('COM4')
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com3.enable()
        start = time.time()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print("ON")
        #aqui você deverá gerar os dados a serem transmitidos. 
        imageR = "./imgs/image.png"
        imageW = "./imgs/recebidaCopia.png"
        #seus dados a serem transmitidos são uma lista de bytes a serem transmitidos. Gere esta lista com o 
        #nome de txBuffer. Esla sempre irá armazenar os dados a serem enviados.
        #===========THIS============

        txBuffer = open(imageR, "rb").read()
        packs = Pack(txBuffer)
        lenPayload = len(packs)
        lenPayload =  (lenPayload).to_bytes(1, byteorder='big')

        #Estados
        handshake = 0
        enviando = 1
        estado = handshake
        validacao = 0

        #Handshake
        while estado == handshake:
            print("Enviando aperto de mão")
            if time.time()-start >= 5 and validacao != lenPayload:
                pergunta=input("Você quer continuar: ")
                if pergunta == "s":
                    start = time.time()
                    com3.sendData(np.asarray(Datagrama(tipo="handshake", payload=lenPayload)))
                    time.sleep(0.01)
                    validacao, nrx = com3.getData(1)
                    print("Validação:", validacao == lenPayload)
                    estado = enviando
                elif pergunta == 'n':
                    handshake = False
                    estado = -1
                    com3.disable()
            elif time.time()-start < 5 and validacao == lenPayload:
                estado = enviando

        for pack in packs:
            com3.sendData(np.asarray(pack))
            print("dado enviado", pack)
            time.sleep(0.1)
        


            





        

        
         
    
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com3.disable()       
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com3.disable()      

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
