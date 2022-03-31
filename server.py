import grpc
import time
from concurrent import futures

import config_partida_pb2_grpc
from partida_service import PartidaService

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class DicaServer(PartidaService):

    def __init__(self) -> None:
        super().__init__()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    config_partida_pb2_grpc.add_PartidaServiceServicer_to_server(
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
