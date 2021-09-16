from enlace import *
import time
import numpy as np
from utils import *

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
        imageW = "D:/Faculdade/4_semestre/FisComp/Client-Server/imgs/recebidaCopia.png"
        SaveImage = open(imageW, 'wb')
        BufferRx, nrx = com4.getData(15)
        txLen = BufferRx[10:11]
        time.sleep(0.01)
        com4.sendData(np.asarray(txLen))
        PacksLen = int.from_bytes(txLen, "big")-1
        print("Recebendo dados...")
        num_pack = -1
        while num_pack != PacksLen:
            BufferRx, nRx = com4.getData(15)
            txLen = int.from_bytes(BufferRx[10:11], "big")
            print("txLen:",txLen)
            package, nRx = com4.getData(txLen)
            num_pack = int.from_bytes(package[4:5], "big")
            print("Pacote {}/{} Enviado:".format(num_pack, PacksLen),package[10:txLen])
            time.sleep(0.01)
            if 1 == 1:
                com4.sendData(np.asarray(Datagrama(tipo="data", payload=b'\x01')))
            else:
                com4.sendData(np.asarray(Datagrama(tipo="data", payload=b'\x00')))
            SaveImage.write(package[10:txLen-4])

        SaveImage.close()
    
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
