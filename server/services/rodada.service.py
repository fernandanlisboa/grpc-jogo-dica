
import grpc

import config_rodada_pb2
import config_rodada_pb2_grpc

class RodadaService ():
    '''
    Serviço de cada rodada do jogo
    '''
    def __init__(self, palavra) :
        self.palavra = palavra
    
    
    def Palpitar(self, request, context):
        '''
        recebe o palpite enviado pelo jogador e retorna se é igual ao da palavra escolhida
        request: requisição do servidor
        '''
        palpite = request.palpite
        
        if self.palavra == palpite:
            return True
        
        return False
    