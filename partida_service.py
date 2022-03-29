#  Coloca os jogadore no array
#  Um loop para os pares e outro para os ímpares
#  Criar partida() {}
import grpc

import config_partida_pb2
import config_partida_pb2_grpc


class PartidaService(config_partida_pb2_grpc.PartidaServiceServicer):
    numJogadores = 4
    jogadores = []
    palavra = ''

    def CriarJogador(self, request, context):
        self.jogadores.append(request.name)
        return config_partida_pb2.NomeJogadorResp(nome=request.nome, recebida=request.recebida)

    def EscolherPalavra(self, request, context):
        self.palavra = request.palavra
        return config_partida_pb2.PalavraResp(nome=self.palavra, recebida=request.recebida)

    def VerPalavra(self, request, context):
        return config_partida_pb2.PalavraResp(nome=self.palavra, recebida=request.recebida)
