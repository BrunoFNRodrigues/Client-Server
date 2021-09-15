from enlace import *
import time
import numpy as np
from utils import Pack

def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com4 = enlace('COM3')
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com4.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print("ON")
        #aqui você deverá gerar os dados a serem transmitidos. 
        # imageR = "./imgs/image.png"
        # imageW = "./imgs/recebidaCopia.png"
        
        BufferRx, nrx = com4.getData(15)
        txLen = BufferRx[10:11]
        time.sleep(0.01)
        com4.sendData(np.asarray(txLen))
        PacksLen = int.from_bytes(BufferRx, "big")
        print("Recebendo dados...")

        for i in range(0, PacksLen):
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
