import threading
from urllib import response
import time
import grpc
import dica_pb2_grpc
import dica_pb2

empty = dica_pb2.google_dot_protobuf_dot_empty__pb2.Empty()


class Client:
    def __init__(self, nome: str):
        self.nome = nome
        # channel = grpc.insecure_channel(f'{endereco}:{porta}')
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = dica_pb2_grpc.DicaServiceStub(channel)
        self.__entrar_jogo()
        # threading.Thread(target=self.__escutar_jogo).start()
        # threading.Thread(target=self.__l)
        self.__escutar_jogo()
        time.sleep(5)
        self.__escutar_rodada()

    def __escutar_jogo(self):
        palavra = ''
        print('Esperando Jogadores')
        response = self.stub.PartidaStream(empty)
        print(f'response:{response}')
        if(response.nome == self.nome):
            palavra = str(
                input('É a sua vez de escolher a palavra!\nPalavra: '))
            response_palavra = self.stub.EscolherPalavra(
                dica_pb2.Palavra(palavra=palavra))
            print(
                f'A palavra que você escolheu foi: {response_palavra.palavra}')

    # tá dando problema quando entra nessa função, mesmo se comentar o RodadaStream
    def __escutar_rodada(self):
        # inicia = False
        # while inicia == False:
        response = self.stub.RodadaStream(empty)
        print(f'{response.nome} quem dará a dica!')
        # inicia = response.inicia

        # if inicia == True:

        response_dica = ''
        response_palpite = ''
        response_enviar_dica = ''
        if response.nome == self.nome:
            response_palavra = self.stub.VerPalavra(empty)
            print(f"A palavra é: {response_palavra.palavra}")
            dica = input('Forneça a dica: ')
            response_enviar_dica = self.stub.DarDica(dica_pb2.Dica(dica=dica))
        else:
            # TODO colocar um try except no loop enquanto a dica não é fornecida
            print(f'{response.nome} está digitando a dica!')
        # TODO um loop para esperar nos outros clientes enquanto quem dá a dica n fornece

        response_dica = self.stub.VerDica(empty)
        print(f"{response.nome} deu a dica: {response_dica.dica}")

        if response_enviar_dica.nome == self.nome:
            palpite = input(f'{self.nome}, digite seu palpite: ')
            self.stub.DarPalpite(
                dica_pb2.DarPalpite(palpite=palpite))
        else:
            print(f'{response_enviar_dica.nome} está digitando o palpite!')

        response_palpite = self.stub.VerPalpite(empty)
        print(f'O palpite enviado foi {response_palpite.palpite}')
        if response_palpite.acertou == True:
            # TODO uma função no server que retorna os nomes de todos os jogadores para poder mostrar a dupla que ganhou!
            print(f'A palavra é: {response_palpite.palpite}!')
            print((f'Parabéns! {response_enviar_dica.nome} ganhou o jogo!!!'))
            # response = self.stub.VerPalpite(dica_pb2.VerPalpite(empty))

    def __entrar_jogo(self):
        response = self.stub.CriarJogador(
            dica_pb2.NomeJogador(nome=self.nome))
        print(f'resp: {response}')


# adicionar as portas que o cliente vai acessar
if __name__ == '__main__':
    nome_jogador = input('Digite seu nome: ')
    c = Client(nome_jogador)
