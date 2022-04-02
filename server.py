from queue import Empty
import grpc
import time
from concurrent import futures

import dica_pb2_grpc
import dica_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class DicaServer(dica_pb2_grpc.DicaServiceServicer):

    def __init__(self):
        self.palavra = ''
        self.numJogadores = 4
        self.jogadores = []
        self.dicas = []
        self.palpites = []
        self.vez = 0
        self.fim = False

    def PartidaStream(self, request, context):
        print('Esperando Jogadores')
        while len(self.jogadores) < 4:
            espera = True
            # fica aqui paradinho

        print('calma')
        # msg = ''
        # for k in range(self.numJogadores//2):
        #     # msg += f''
        #     # if k % 2 == 0:
        #     msg = f'Dupla {k +1}: {self.jogadores[k]} e {self.jogadores[k+2]}'
        # else:
        #     print(msg)
        #     msg = ''
        print('Dupla 1: ' + self.jogadores[0] + ' e ' + self.jogadores[2])
        print('Dupla 2: ' + self.jogadores[1] + ' e ' + self.jogadores[3])

        # TODO trocar por sorteio
        primeiro_jogador = 0
        self.vez = primeiro_jogador
        print('response: ', dica_pb2.NomeJogadorResp(
            nome=self.jogadores[primeiro_jogador], recebida=True))

        return dica_pb2.NomeJogadorResp(nome=self.jogadores[primeiro_jogador], recebida=True)

    def RodadaStream(self, request, context):
        comeca = False
        # espera por 10 segundos -> tempo que o jogador leva para digitar
        # time.sleep(10)
        while self.palavra == '':
            # espera enquanto a palavra não é escolhida
            # time.sleep(1)
            print('Esperando...')
            espera = True
        # comeca = True
        print(f'A rodada vai começar! {self.palavra}')
        return dica_pb2.NomeJogadorResp(nome=self.jogadores[self.vez], recebida=True)

        # return dica_pb2.RodadaResposta(inicia=comeca)

    #     # while self.fim != True:

    def CriarJogador(self, request, context):
        self.jogadores.append(request.nome)
        return dica_pb2.NomeJogadorResp(nome=request.nome, recebida=True)

    def EscolherPalavra(self, request, context):
        self.vez += 1
        self.palavra = request.palavra

        return dica_pb2.PalavraResp(palavra=self.palavra, recebida=True)

    def VerPalavra(self, request, context):
        # print('vendo palavra')
        return dica_pb2.PalavraResp(palavra=self.palavra, recebida=True)

    def DarDica(self, request, context):
        #TODO verificações de palavras repetidas
        dica = request.dica
        self.dicas.append(dica)

        indice = self.vez+2

        return dica_pb2.NomeJogadorResp(nome=self.jogadores[indice], recebida=True)

    def VerDica(self, request, context):
        #TODO verificação se a lista foi atualizada: out of range, caso seja a mesma palavra da rodada anterior
        
        print(self.vez)
        print(f'Dica: {self.dicas[-1]}')
        return dica_pb2.Dica(dica=self.dicas[-1])

    def DarPalpite(self, request, context):
        #TODO verificações de palavras repetidas
        '''
        recebe o palpite enviado pelo jogador e retorna se é igual ao da palavra escolhida
        request: requisição do servidor
        '''
        self.palpites.append(request.palpite)

        if self.palavra == request.palpite:
            self.fim = True
        else:
            if self.vez == 1:
                self.vez = 0
            else:
                self.vez = 1

        

    def VerPalpite(self, request, context):
        '''
        '''
        return dica_pb2.PalpiteResposta(palpite=self.palpites[-1], acertou=self.fim, recebeu=True)


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
