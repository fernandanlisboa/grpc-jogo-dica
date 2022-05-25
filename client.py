from ast import While
import threading
from urllib import response
import time
import grpc
import dica_pb2_grpc
import dica_pb2

import redis

empty = dica_pb2.google_dot_protobuf_dot_empty__pb2.Empty()


class Client:
    def __init__(self, nome: str):
        self.nome = nome
        self.espera_jogador = ''
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = dica_pb2_grpc.DicaServiceStub(channel)
        self.__entrar_jogo()
        self.__escutar_jogo()
        time.sleep(5)
        while True:
            self.__escutar_rodada()

            response = self.stub.ConfereFim(empty)
            #  só finaliza ou continua depois de todos terem recebido o palpite
            if response.fim:
                print('Resposta correta!')
                break
            print('Não foi dessa vez...')
            time.sleep(2)
        self.__fim_jogo(response.ganhador1, response.ganhador2)

    def __escutar_jogo(self):
        palavra = ''
        print('Esperando Jogadores')
        response = self.stub.PartidaStream(empty)

        duplas = self.stub.MostrarJogadores(empty)
        print(f'As duplas são: ')
        print(f'Dupla 1: {duplas.jogador1} e {duplas.jogador3}')
        print(f'Dupla 2: {duplas.jogador2} e {duplas.jogador4}')

        if(response.nome == self.nome):
            palavra = str(
                input('É a sua vez de escolher a palavra!\nPalavra: '))
            response_palavra = self.stub.EscolherPalavra(
                dica_pb2.Palavra(palavra=palavra))
            print(
                f'A palavra que você escolheu foi: {response_palavra.palavra}')
        else:
            print(f'{response.nome} está digitando a palavra!')
            self.__espera()

    def __escutar_rodada(self):

        response = self.stub.ConfereVez(empty)
        self.espera_jogador = response.nome

        print(f'{response.nome} quem dará a dica!')

        response_dica = dica_pb2.Dica(dica='')
        response_palpite = dica_pb2.PalpiteResposta(
            palpite='', acertou=False, recebeu=False)
        response_enviar_dica = dica_pb2.NomeJogadorResp(
            nome='', recebida=False)

        # TODO um loop para esperar nos outros clientes enquanto quem dá a dica n fornece
        if response.nome == self.nome:
            response_palavra = self.stub.VerPalavra(empty)
            print(f"A palavra é: {response_palavra.palavra}")
            dica = str(input('Forneça sua dica: '))
            response_enviar_dica = self.stub.DarDica(dica_pb2.Dica(dica=dica))
            self.espera_jogador = response_enviar_dica

            response_espera = self.stub.AlteraEspera(
                dica_pb2.Espera(espera=False))
        else:
            # TODO colocar um try except no loop enquanto a dica não é fornecida
            time.sleep(1)
            print(f'{response.nome} está digitando a dica!')
            self.__espera()

        response_dica = self.stub.VerDica(empty)
        self.stub.MensagemRecebida(empty)
        print(f"{response.nome} deu a dica: {response_dica.dica}")

        time.sleep(5)
        print(f'Quem dará o palpite é: {self.espera_jogador}!')

        if self.espera_jogador == self.nome:
            palpite = input(f'{self.nome}, digite seu palpite: ')
            self.stub.DarPalpite(
                dica_pb2.Palpite(palpite=palpite, jogador=self.nome))
            response_espera = self.stub.AlteraEspera(
                dica_pb2.Espera(espera=False))
        else:
            print(f'{self.espera_jogador} está digitando o palpite!')
            time.sleep(10)

            self.__espera()

        time.sleep(10)
        response_palpite = self.stub.VerPalpite(empty)
        self.stub.MensagemRecebida(empty)

        print(f'O palpite enviado foi {response_palpite.palpite}')

    def __entrar_jogo(self):
        response = self.stub.CriarJogador(
            dica_pb2.NomeJogador(nome=self.nome))
        # print(f'resp: {response}')

    def __espera(self):
        while True:

            response = self.stub.ConfereEspera(empty)

            self.espera_jogador = response.jogador

            if response.espera == False:
                break
            time.sleep(3)

    def __fim_jogo(self, ganhadorA, ganhadorB):
        r = redis.Redis(host='localhost', port=6379)
        r.set('ganhadores', ganhadorA + ' ' + 'e' + ' ' + ganhadorB)
        ganhadores = r.get('ganhadores')
        print((f'Parabéns! {ganhadores} ganharam o jogo!!!'))


if __name__ == '__main__':
    nome_jogador = input('Digite seu nome: ')
    c = Client(nome_jogador)
