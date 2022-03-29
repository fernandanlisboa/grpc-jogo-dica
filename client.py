import threading
from urllib import response
import grpc
import config_partida_pb2_grpc
import config_partida_pb2


class Client:
    def __init__(self, u: str):
        self.nome = u
        # channel = grpc.insecure_channel(f'{endereco}:{porta}')
        channel = grpc.insecure_channel('localhost:50051')
        self.stub_partida = config_partida_pb2_grpc.PartidaServiceStub(channel)
        threading.Thread(target=self.__entrar_jogo, daemon=True).start()
        # self.__entrar_jogo()
        # threading.Thread(target=self.__l)

    def __escutar_dicas(self):
        return True

    def __entrar_jogo(self):
        print('entrouu')
        response = self.stub_partida.CriarJogador(
            config_partida_pb2.NomeJogador(nome=self.nome))
        print(f'resp: {response}')


# adicionar as portas que o cliente vai acessar
if __name__ == '__main__':
    nome_jogador = input('Digite seu nome: ')
    c = Client(nome_jogador)
