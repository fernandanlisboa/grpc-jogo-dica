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
        self.dicas = []
        self.vez = 0

    def PartidaStream(self, request, context):
        print('Esperando Jogadores')
        while len(self.jogadores) < 2:
            espera = True
            #fica aqui paradinho

        print('calma')
        print('Dupla 1: ' + self.jogadores[0] + ' e ' + self.jogadores[1])
        #print('Dupla 2: ' + self.jogadores[1] + ' e ' + self.jogadores[3])

        #trocar por sorteio
        primeiro_jogador = 0
        return dica_pb2.NomeJogadorResp(nome=self.jogadores[primeiro_jogador], recebida=True)


    def CriarJogador(self, request, context):
        self.jogadores.append(request.nome)
        return dica_pb2.NomeJogadorResp(nome=request.nome, recebida=True)

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
