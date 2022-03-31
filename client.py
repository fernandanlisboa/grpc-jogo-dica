import threading
from urllib import response
import grpc
import dica_pb2_grpc
import dica_pb2


class Client:
    def __init__(self, nome: str):
        self.nome = nome
        # channel = grpc.insecure_channel(f'{endereco}:{porta}')
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = dica_pb2_grpc.DicaServiceStub(channel)
        #threading.Thread(target=self.__entrar_jogo, daemon=True).start()
        self.__entrar_jogo()
        # threading.Thread(target=self.__l)

    def __escutar_dicas(self):
        return True

    def __entrar_jogo(self):
        response = self.stub.CriarJogador(
            dica_pb2.NomeJogador(nome=self.nome))
        print(f'resp: {response}')


# adicionar as portas que o cliente vai acessar
if __name__ == '__main__':
    nome_jogador = input('Digite seu nome: ')
    c = Client(nome_jogador)
