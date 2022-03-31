import grpc
import time
from concurrent import futures

import dica_pb2_grpc
import dica_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class DicaServer(dica_pb2_grpc.DicaServiceServicer):

    def __init__(self) :
        self.palavra = ''
        self.numJogadores = 4
        self.jogadores = []

    def CriarJogador(self, request, context):
        self.jogadores.append(request.nome)
        return dica_pb2.NomeJogadorResp(nome=request.nome, recebida=request.recebida)

    def EscolherPalavra(self, request, context):
        self.palavra = request.palavra
        return dica_pb2.PalavraResp(nome=self.palavra, recebida=request.recebida)

    def VerPalavra(self, request, context):
        return dica_pb2.PalavraResp(nome=self.palavra, recebida=request.recebida)
    
    def Palpitar(self, request, context):
        '''
        recebe o palpite enviado pelo jogador e retorna se é igual ao da palavra escolhida
        request: requisição do servidor
        '''
        palpite = request.palpite
        
        if self.palavra == palpite:
            return True
        
        return False


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dica_pb2_grpc.add_DicaServiceServicer_to_server(
        DicaServer(), server)

    for i in range(50050, 50053, 1):
        server.add_insecure_port('[::]:' + str(i))

    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
    print('Iniciando o jogo...')
