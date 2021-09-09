import binascii

def Datagrama(tipo="", npacks=0, num_pack=0, file_id="", payload_len=0, error_pack=0, crc=0, payload=""):
    eop = 'DEEEEE55'
    if tipo == "data":
        mensagem = "01"+"0000"+str(npacks)+str(num_pack)+str(payload_len)+str(error_pack)+str(crc)+payload+eop
        return binascii.unhexlify(mensagem)
    else:
        mensagem = "00"+"0000"+str(npacks)+str(num_pack)+file_id+str(error_pack)+str(crc)+payload+eop
