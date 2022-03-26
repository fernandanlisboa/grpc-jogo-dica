    #  Coloca os jogadore no array
    #  Um loop para os pares e outro para os ímpares
    #  Criar partida() {}
    
import re
import grpc

import config_partida_pb2
import config_partida_pb2_grpc

    
class PatidaService(config_partida_pb2_grpc.PartidaServiceServicer):
    numJogadores = 4
    jogadores = []
    palavra = ''
    
    def CriarJogador(self, request, context):
        self.jogadores[request.index] = request.nome
        return config_partida_pb2.NomeJogadorResp(nome=request.nome, recebida=True)
    
    def EscolherPalavra(self, request, context):
        self.palavra = request.palavra
        return config_partida_pb2.PalavraResp(nome=self.palavra, recebida=True)
    
    def VerPalavra(self, request, context):
        return config_partida_pb2.PalavraResp(nome=self.palavra, recebida=True)