# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dica_pb2 as dica__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DicaServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CriarJogador = channel.unary_unary(
                '/configuration.DicaService/CriarJogador',
                request_serializer=dica__pb2.NomeJogador.SerializeToString,
                response_deserializer=dica__pb2.NomeJogadorResp.FromString,
                )
        self.EscolherPalavra = channel.unary_unary(
                '/configuration.DicaService/EscolherPalavra',
                request_serializer=dica__pb2.Palavra.SerializeToString,
                response_deserializer=dica__pb2.PalavraResp.FromString,
                )
        self.VerPalavra = channel.unary_unary(
                '/configuration.DicaService/VerPalavra',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dica__pb2.PalavraResp.FromString,
                )
        self.VerDica = channel.unary_unary(
                '/configuration.DicaService/VerDica',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dica__pb2.Dica.FromString,
                )
        self.DarDica = channel.unary_unary(
                '/configuration.DicaService/DarDica',
                request_serializer=dica__pb2.Dica.SerializeToString,
                response_deserializer=dica__pb2.NomeJogadorResp.FromString,
                )
        self.DarPalpite = channel.unary_unary(
                '/configuration.DicaService/DarPalpite',
                request_serializer=dica__pb2.Palpite.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.VerPalpite = channel.unary_unary(
                '/configuration.DicaService/VerPalpite',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dica__pb2.PalpiteResposta.FromString,
                )
        self.PartidaStream = channel.unary_unary(
                '/configuration.DicaService/PartidaStream',
                request_serializer=dica__pb2.Palpite.SerializeToString,
                response_deserializer=dica__pb2.NomeJogadorResp.FromString,
                )
        self.ConfereEspera = channel.unary_unary(
                '/configuration.DicaService/ConfereEspera',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dica__pb2.EsperaResp.FromString,
                )
        self.AlteraEspera = channel.unary_unary(
                '/configuration.DicaService/AlteraEspera',
                request_serializer=dica__pb2.Espera.SerializeToString,
                response_deserializer=dica__pb2.EsperaResp.FromString,
                )
        self.ConfereVez = channel.unary_unary(
                '/configuration.DicaService/ConfereVez',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dica__pb2.NomeJogadorResp.FromString,
                )
        self.ConfereFim = channel.unary_unary(
                '/configuration.DicaService/ConfereFim',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dica__pb2.FimResp.FromString,
                )
        self.MensagemRecebida = channel.unary_unary(
                '/configuration.DicaService/MensagemRecebida',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.MostrarJogadores = channel.unary_unary(
                '/configuration.DicaService/MostrarJogadores',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dica__pb2.Jogadores.FromString,
                )


class DicaServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CriarJogador(self, request, context):
        """Recebe o nome dos jogadores
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EscolherPalavra(self, request, context):
        """Define a palavra que ser?? adivinhada na partida
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerPalavra(self, request, context):
        """O jogador que fornece a dica deve receber a palavra
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerDica(self, request, context):
        """envia a dica do jogador 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DarDica(self, request, context):
        """o jogador define a dica e retorna o nome do jogador que realizar?? o palpite
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DarPalpite(self, request, context):
        """recebe o palpite do jogador
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerPalpite(self, request, context):
        """mostra o palpite do jogador
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PartidaStream(self, request, context):
        """loop da partida
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfereEspera(self, request, context):
        """Verifica se os jogadores est??o esperando um evento do sistema
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AlteraEspera(self, request, context):
        """Verifica se os jogadores est??o esperando um evento do sistema
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfereVez(self, request, context):
        """Verifica se os jogadores est??o esperando um evento do sistema
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfereFim(self, request, context):
        """Verifica se o jogo acabou e retorna o vencedor
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MensagemRecebida(self, request, context):
        """Retorna ao servidor que a mensagem desejada foi recebida
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MostrarJogadores(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DicaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CriarJogador': grpc.unary_unary_rpc_method_handler(
                    servicer.CriarJogador,
                    request_deserializer=dica__pb2.NomeJogador.FromString,
                    response_serializer=dica__pb2.NomeJogadorResp.SerializeToString,
            ),
            'EscolherPalavra': grpc.unary_unary_rpc_method_handler(
                    servicer.EscolherPalavra,
                    request_deserializer=dica__pb2.Palavra.FromString,
                    response_serializer=dica__pb2.PalavraResp.SerializeToString,
            ),
            'VerPalavra': grpc.unary_unary_rpc_method_handler(
                    servicer.VerPalavra,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dica__pb2.PalavraResp.SerializeToString,
            ),
            'VerDica': grpc.unary_unary_rpc_method_handler(
                    servicer.VerDica,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dica__pb2.Dica.SerializeToString,
            ),
            'DarDica': grpc.unary_unary_rpc_method_handler(
                    servicer.DarDica,
                    request_deserializer=dica__pb2.Dica.FromString,
                    response_serializer=dica__pb2.NomeJogadorResp.SerializeToString,
            ),
            'DarPalpite': grpc.unary_unary_rpc_method_handler(
                    servicer.DarPalpite,
                    request_deserializer=dica__pb2.Palpite.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'VerPalpite': grpc.unary_unary_rpc_method_handler(
                    servicer.VerPalpite,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dica__pb2.PalpiteResposta.SerializeToString,
            ),
            'PartidaStream': grpc.unary_unary_rpc_method_handler(
                    servicer.PartidaStream,
                    request_deserializer=dica__pb2.Palpite.FromString,
                    response_serializer=dica__pb2.NomeJogadorResp.SerializeToString,
            ),
            'ConfereEspera': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfereEspera,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dica__pb2.EsperaResp.SerializeToString,
            ),
            'AlteraEspera': grpc.unary_unary_rpc_method_handler(
                    servicer.AlteraEspera,
                    request_deserializer=dica__pb2.Espera.FromString,
                    response_serializer=dica__pb2.EsperaResp.SerializeToString,
            ),
            'ConfereVez': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfereVez,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dica__pb2.NomeJogadorResp.SerializeToString,
            ),
            'ConfereFim': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfereFim,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dica__pb2.FimResp.SerializeToString,
            ),
            'MensagemRecebida': grpc.unary_unary_rpc_method_handler(
                    servicer.MensagemRecebida,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'MostrarJogadores': grpc.unary_unary_rpc_method_handler(
                    servicer.MostrarJogadores,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dica__pb2.Jogadores.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'configuration.DicaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DicaService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CriarJogador(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/CriarJogador',
            dica__pb2.NomeJogador.SerializeToString,
            dica__pb2.NomeJogadorResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EscolherPalavra(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/EscolherPalavra',
            dica__pb2.Palavra.SerializeToString,
            dica__pb2.PalavraResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerPalavra(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/VerPalavra',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dica__pb2.PalavraResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerDica(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/VerDica',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dica__pb2.Dica.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DarDica(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/DarDica',
            dica__pb2.Dica.SerializeToString,
            dica__pb2.NomeJogadorResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DarPalpite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/DarPalpite',
            dica__pb2.Palpite.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerPalpite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/VerPalpite',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dica__pb2.PalpiteResposta.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PartidaStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/PartidaStream',
            dica__pb2.Palpite.SerializeToString,
            dica__pb2.NomeJogadorResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfereEspera(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/ConfereEspera',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dica__pb2.EsperaResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AlteraEspera(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/AlteraEspera',
            dica__pb2.Espera.SerializeToString,
            dica__pb2.EsperaResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfereVez(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/ConfereVez',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dica__pb2.NomeJogadorResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfereFim(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/ConfereFim',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dica__pb2.FimResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MensagemRecebida(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/MensagemRecebida',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MostrarJogadores(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/configuration.DicaService/MostrarJogadores',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dica__pb2.Jogadores.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
