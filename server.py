from queue import Empty
import grpc
import time
from concurrent import futures

import dica_pb2_grpc
import dica_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

_EMPTY = dica_pb2.google_dot_protobuf_dot_empty__pb2.Empty()


class DicaServer(dica_pb2_grpc.DicaServiceServicer):

    def __init__(self):
        self.palavra = ''
        self.numJogadores = 4
        self.jogadores = []
        self.dicas = []
        self.palpites = []
        self.vez = 0
        self.fim = False
        self.ganhador = ''
        # Mostra se o jogo espera por alguém e quem faz o jogo esperar
        self.espera = False
        self.espera_jogador = ''
        self.rodadas = 1
        self.msg_recebidas = 0

    def PartidaStream(self, request, context):
        print('Esperando Jogadores')
        while len(self.jogadores) < 4:
            self.espera = True

        self.espera_jogador = self.jogadores[self.vez]

        print('Dupla 1: ' + self.jogadores[0] + ' e ' + self.jogadores[2])
        print('Dupla 2: ' + self.jogadores[1] + ' e ' + self.jogadores[3])

        # TODO trocar por sorteio
        primeiro_jogador = 0
        self.vez = primeiro_jogador

        print('response: ', dica_pb2.NomeJogadorResp(
            nome=self.jogadores[primeiro_jogador], recebida=True))

        return dica_pb2.NomeJogadorResp(nome=self.jogadores[primeiro_jogador], recebida=True)

    # def DicaStream(self, request, context):

        # while len(self.dicas) != self.rodadas:
        #     self.espera = True
        # indice = self.vez

        # return dica_pb2.NomeJogadorResp(nome=self.jogadores[indice], recebida=True)

    def ConfereVez(self, request, context):
        self.espera = True
        self.espera_jogador = self.jogadores[self.vez]
        print('Estamos esperando por ', self.espera_jogador)
        return dica_pb2.NomeJogadorResp(nome=self.jogadores[self.vez], recebida=True)

    def CriarJogador(self, request, context):
        self.jogadores.append(request.nome)
        return dica_pb2.NomeJogadorResp(nome=request.nome, recebida=True)

    def EscolherPalavra(self, request, context):
        self.vez += 1
        self.palavra = request.palavra
        self.espera = False

        return dica_pb2.PalavraResp(palavra=self.palavra, recebida=True)

    def VerPalavra(self, request, context):
        # print('vendo palavra')
        return dica_pb2.PalavraResp(palavra=self.palavra, recebida=True)

    def MensagemRecebida(self, request, context):
        # if request.recebida == True:
        print('MENSAGEM RECEBIDA!')
        self.msg_recebidas += 1
        return _EMPTY

    def DarDica(self, request, context):
        # TODO verificações de palavras repetidas
        dica = request.dica
        self.dicas.append(dica)
        # self.vez += 2
        indice = self.vez+2

        # self.espera = False
        # self.espera_jogador = self.jogadores[indice]
        print(f'Agora esperamos: {self.espera_jogador}')
        return dica_pb2.NomeJogadorResp(nome=self.jogadores[indice], recebida=True)

    def VerDica(self, request, context):
        # TODO verificação se a lista foi atualizada: out of range, caso seja a mesma palavra da rodada anterior
        print(self.vez)
        print(f'Dica: {self.dicas[-1]}')
        # altera a vez só após todos os usuários receberem a dica!
        print(f'recebido {self.msg_recebidas} vezes')
        if self.msg_recebidas == len(self.jogadores)-1:
            print('entrou no if')
            self.vez += 2
            self.espera_jogador = self.jogadores[self.vez]
            self.espera = True

        return dica_pb2.Dica(dica=self.dicas[-1])

    def DarPalpite(self, request, context):
        # TODO verificações de palavras repetidas
        '''
        recebe o palpite enviado pelo jogador e retorna se é igual ao da palavra escolhida
        request: requisição do servidor
        '''
        self.msg_recebidas = 0
        print(f'{request.palpite}')
        print(f'{request.jogador}')
        palpite = request.palpite
        self.palpites.append(palpite)
        print(f'palpites:\n {self.palpites}')
        if palpite == self.palavra:
            self.fim = True
            self.ganhador = request.jogador
            print('entrou no IF -> GANHOU')
        else:
            self.rodadas += 1
            print('entrou no ELSE -> PERDEU')

            # TODO modificar a lógica de passar a vez caso mude para sorteio
            # TODO array para armazenar indices dos jogadores que darão as dicas na partida
            if self.vez == 3:
                self.vez = 0
            elif self.vez == 2:
                self.vez = 1

            # 0 1 2 3
            # D
            #     P
            #   D
            #       P
            # D
            #   ...
        self.espera = False

        return _EMPTY

    def VerPalpite(self, request, context):
        print(f'Palpite: {self.palpites[-1]}')
        if self.msg_recebidas == 3:
            print(f'vez de {self.jogadores[self.vez]}')
        return dica_pb2.PalpiteResposta(palpite=self.palpites[-1], acertou=self.fim, recebeu=True)

    def ConfereEspera(self, request, context):
        print(f'espera por: {self.espera_jogador}')
        return dica_pb2.EsperaResp(espera=self.espera, jogador=self.espera_jogador, recebida=True)

    def AlteraEspera(self, request, context):
        self.espera = request.espera
        print(f'espera alterada para: {self.espera}')
        return dica_pb2.EsperaResp(espera=self.espera, jogador=self.espera_jogador, recebida=True)

    def ConfereFim(self, request, context):
        self.msg_recebidas = 0
        if self.fim == True:
            return dica_pb2.FimResp(fim=self.fim, ganhador=self.ganhador)
        else:
            return dica_pb2.FimResp(fim=self.fim)


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
