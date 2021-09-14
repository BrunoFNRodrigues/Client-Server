from enlace import *
import time
import numpy as np
import random
import binascii
from utils import Pack

def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com4 = enlace('COM4')
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com4.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print("ON")
        #aqui você deverá gerar os dados a serem transmitidos. 
        # imageR = "./imgs/image.png"
        # imageW = "./imgs/recebidaCopia.png"
        
        Bufferrx, nrx = com4.getData(1)

        com4.sendData(np.asarray(Bufferrx))
        txLen = int.from_bytes(Bufferrx, "big")
        print("Recebendo dados...")
        for i in range(0, txLen):
            package = com4.getData(114)
            print(package)

        

    
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com4.disable()        
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com4.disable()        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
