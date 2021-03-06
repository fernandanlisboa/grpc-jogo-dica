# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dica.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dica.proto',
  package='configuration',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ndica.proto\x12\rconfiguration\x1a\x1bgoogle/protobuf/empty.proto\"\x1b\n\x0bNomeJogador\x12\x0c\n\x04nome\x18\x01 \x01(\t\"1\n\x0fNomeJogadorResp\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\x10\n\x08recebida\x18\x02 \x01(\x08\"\x1a\n\x07Palavra\x12\x0f\n\x07palavra\x18\x01 \x01(\t\"0\n\x0bPalavraResp\x12\x0f\n\x07palavra\x18\x01 \x01(\t\x12\x10\n\x08recebida\x18\x02 \x01(\x08\"\x14\n\x04\x44ica\x12\x0c\n\x04\x64ica\x18\x01 \x01(\t\"+\n\x07Palpite\x12\x0f\n\x07palpite\x18\x01 \x01(\t\x12\x0f\n\x07jogador\x18\x02 \x01(\t\" \n\x0eRodadaResposta\x12\x0e\n\x06inicia\x18\x01 \x01(\x08\"D\n\x0fPalpiteResposta\x12\x0f\n\x07palpite\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x63\x65rtou\x18\x02 \x01(\x08\x12\x0f\n\x07recebeu\x18\x03 \x01(\x08\"\x18\n\x06\x45spera\x12\x0e\n\x06\x65spera\x18\x01 \x01(\x08\"?\n\nEsperaResp\x12\x0e\n\x06\x65spera\x18\x01 \x01(\x08\x12\x0f\n\x07jogador\x18\x02 \x01(\t\x12\x10\n\x08recebida\x18\x03 \x01(\x08\"b\n\x07\x46imResp\x12\x0b\n\x03\x66im\x18\x01 \x01(\x08\x12\x16\n\tganhador1\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tganhador2\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x0c\n\n_ganhador1B\x0c\n\n_ganhador2\"S\n\tJogadores\x12\x10\n\x08jogador1\x18\x01 \x01(\t\x12\x10\n\x08jogador2\x18\x02 \x01(\t\x12\x10\n\x08jogador3\x18\x03 \x01(\t\x12\x10\n\x08jogador4\x18\x04 \x01(\t\"\x1f\n\x0bRecebimento\x12\x10\n\x08recebida\x18\x01 \x01(\x08\x32\xd7\x07\n\x0b\x44icaService\x12L\n\x0c\x43riarJogador\x12\x1a.configuration.NomeJogador\x1a\x1e.configuration.NomeJogadorResp\"\x00\x12G\n\x0f\x45scolherPalavra\x12\x16.configuration.Palavra\x1a\x1a.configuration.PalavraResp\"\x00\x12\x42\n\nVerPalavra\x12\x16.google.protobuf.Empty\x1a\x1a.configuration.PalavraResp\"\x00\x12\x38\n\x07VerDica\x12\x16.google.protobuf.Empty\x1a\x13.configuration.Dica\"\x00\x12@\n\x07\x44\x61rDica\x12\x13.configuration.Dica\x1a\x1e.configuration.NomeJogadorResp\"\x00\x12>\n\nDarPalpite\x12\x16.configuration.Palpite\x1a\x16.google.protobuf.Empty\"\x00\x12\x46\n\nVerPalpite\x12\x16.google.protobuf.Empty\x1a\x1e.configuration.PalpiteResposta\"\x00\x12I\n\rPartidaStream\x12\x16.configuration.Palpite\x1a\x1e.configuration.NomeJogadorResp\"\x00\x12\x44\n\rConfereEspera\x12\x16.google.protobuf.Empty\x1a\x19.configuration.EsperaResp\"\x00\x12\x42\n\x0c\x41lteraEspera\x12\x15.configuration.Espera\x1a\x19.configuration.EsperaResp\"\x00\x12\x46\n\nConfereVez\x12\x16.google.protobuf.Empty\x1a\x1e.configuration.NomeJogadorResp\"\x00\x12>\n\nConfereFim\x12\x16.google.protobuf.Empty\x1a\x16.configuration.FimResp\"\x00\x12\x44\n\x10MensagemRecebida\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x46\n\x10MostrarJogadores\x12\x16.google.protobuf.Empty\x1a\x18.configuration.Jogadores\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_NOMEJOGADOR = _descriptor.Descriptor(
  name='NomeJogador',
  full_name='configuration.NomeJogador',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='configuration.NomeJogador.nome', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=85,
)


_NOMEJOGADORRESP = _descriptor.Descriptor(
  name='NomeJogadorResp',
  full_name='configuration.NomeJogadorResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='configuration.NomeJogadorResp.nome', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recebida', full_name='configuration.NomeJogadorResp.recebida', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=136,
)


_PALAVRA = _descriptor.Descriptor(
  name='Palavra',
  full_name='configuration.Palavra',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='palavra', full_name='configuration.Palavra.palavra', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=164,
)


_PALAVRARESP = _descriptor.Descriptor(
  name='PalavraResp',
  full_name='configuration.PalavraResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='palavra', full_name='configuration.PalavraResp.palavra', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recebida', full_name='configuration.PalavraResp.recebida', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=214,
)


_DICA = _descriptor.Descriptor(
  name='Dica',
  full_name='configuration.Dica',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dica', full_name='configuration.Dica.dica', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=236,
)


_PALPITE = _descriptor.Descriptor(
  name='Palpite',
  full_name='configuration.Palpite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='palpite', full_name='configuration.Palpite.palpite', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jogador', full_name='configuration.Palpite.jogador', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=281,
)


_RODADARESPOSTA = _descriptor.Descriptor(
  name='RodadaResposta',
  full_name='configuration.RodadaResposta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inicia', full_name='configuration.RodadaResposta.inicia', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=315,
)


_PALPITERESPOSTA = _descriptor.Descriptor(
  name='PalpiteResposta',
  full_name='configuration.PalpiteResposta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='palpite', full_name='configuration.PalpiteResposta.palpite', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acertou', full_name='configuration.PalpiteResposta.acertou', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recebeu', full_name='configuration.PalpiteResposta.recebeu', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=385,
)


_ESPERA = _descriptor.Descriptor(
  name='Espera',
  full_name='configuration.Espera',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='espera', full_name='configuration.Espera.espera', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=411,
)


_ESPERARESP = _descriptor.Descriptor(
  name='EsperaResp',
  full_name='configuration.EsperaResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='espera', full_name='configuration.EsperaResp.espera', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jogador', full_name='configuration.EsperaResp.jogador', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recebida', full_name='configuration.EsperaResp.recebida', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=476,
)


_FIMRESP = _descriptor.Descriptor(
  name='FimResp',
  full_name='configuration.FimResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fim', full_name='configuration.FimResp.fim', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ganhador1', full_name='configuration.FimResp.ganhador1', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ganhador2', full_name='configuration.FimResp.ganhador2', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_ganhador1', full_name='configuration.FimResp._ganhador1',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_ganhador2', full_name='configuration.FimResp._ganhador2',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=478,
  serialized_end=576,
)


_JOGADORES = _descriptor.Descriptor(
  name='Jogadores',
  full_name='configuration.Jogadores',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jogador1', full_name='configuration.Jogadores.jogador1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jogador2', full_name='configuration.Jogadores.jogador2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jogador3', full_name='configuration.Jogadores.jogador3', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jogador4', full_name='configuration.Jogadores.jogador4', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=578,
  serialized_end=661,
)


_RECEBIMENTO = _descriptor.Descriptor(
  name='Recebimento',
  full_name='configuration.Recebimento',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='recebida', full_name='configuration.Recebimento.recebida', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=663,
  serialized_end=694,
)

_FIMRESP.oneofs_by_name['_ganhador1'].fields.append(
  _FIMRESP.fields_by_name['ganhador1'])
_FIMRESP.fields_by_name['ganhador1'].containing_oneof = _FIMRESP.oneofs_by_name['_ganhador1']
_FIMRESP.oneofs_by_name['_ganhador2'].fields.append(
  _FIMRESP.fields_by_name['ganhador2'])
_FIMRESP.fields_by_name['ganhador2'].containing_oneof = _FIMRESP.oneofs_by_name['_ganhador2']
DESCRIPTOR.message_types_by_name['NomeJogador'] = _NOMEJOGADOR
DESCRIPTOR.message_types_by_name['NomeJogadorResp'] = _NOMEJOGADORRESP
DESCRIPTOR.message_types_by_name['Palavra'] = _PALAVRA
DESCRIPTOR.message_types_by_name['PalavraResp'] = _PALAVRARESP
DESCRIPTOR.message_types_by_name['Dica'] = _DICA
DESCRIPTOR.message_types_by_name['Palpite'] = _PALPITE
DESCRIPTOR.message_types_by_name['RodadaResposta'] = _RODADARESPOSTA
DESCRIPTOR.message_types_by_name['PalpiteResposta'] = _PALPITERESPOSTA
DESCRIPTOR.message_types_by_name['Espera'] = _ESPERA
DESCRIPTOR.message_types_by_name['EsperaResp'] = _ESPERARESP
DESCRIPTOR.message_types_by_name['FimResp'] = _FIMRESP
DESCRIPTOR.message_types_by_name['Jogadores'] = _JOGADORES
DESCRIPTOR.message_types_by_name['Recebimento'] = _RECEBIMENTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NomeJogador = _reflection.GeneratedProtocolMessageType('NomeJogador', (_message.Message,), {
  'DESCRIPTOR' : _NOMEJOGADOR,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.NomeJogador)
  })
_sym_db.RegisterMessage(NomeJogador)

NomeJogadorResp = _reflection.GeneratedProtocolMessageType('NomeJogadorResp', (_message.Message,), {
  'DESCRIPTOR' : _NOMEJOGADORRESP,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.NomeJogadorResp)
  })
_sym_db.RegisterMessage(NomeJogadorResp)

Palavra = _reflection.GeneratedProtocolMessageType('Palavra', (_message.Message,), {
  'DESCRIPTOR' : _PALAVRA,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.Palavra)
  })
_sym_db.RegisterMessage(Palavra)

PalavraResp = _reflection.GeneratedProtocolMessageType('PalavraResp', (_message.Message,), {
  'DESCRIPTOR' : _PALAVRARESP,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.PalavraResp)
  })
_sym_db.RegisterMessage(PalavraResp)

Dica = _reflection.GeneratedProtocolMessageType('Dica', (_message.Message,), {
  'DESCRIPTOR' : _DICA,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.Dica)
  })
_sym_db.RegisterMessage(Dica)

Palpite = _reflection.GeneratedProtocolMessageType('Palpite', (_message.Message,), {
  'DESCRIPTOR' : _PALPITE,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.Palpite)
  })
_sym_db.RegisterMessage(Palpite)

RodadaResposta = _reflection.GeneratedProtocolMessageType('RodadaResposta', (_message.Message,), {
  'DESCRIPTOR' : _RODADARESPOSTA,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.RodadaResposta)
  })
_sym_db.RegisterMessage(RodadaResposta)

PalpiteResposta = _reflection.GeneratedProtocolMessageType('PalpiteResposta', (_message.Message,), {
  'DESCRIPTOR' : _PALPITERESPOSTA,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.PalpiteResposta)
  })
_sym_db.RegisterMessage(PalpiteResposta)

Espera = _reflection.GeneratedProtocolMessageType('Espera', (_message.Message,), {
  'DESCRIPTOR' : _ESPERA,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.Espera)
  })
_sym_db.RegisterMessage(Espera)

EsperaResp = _reflection.GeneratedProtocolMessageType('EsperaResp', (_message.Message,), {
  'DESCRIPTOR' : _ESPERARESP,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.EsperaResp)
  })
_sym_db.RegisterMessage(EsperaResp)

FimResp = _reflection.GeneratedProtocolMessageType('FimResp', (_message.Message,), {
  'DESCRIPTOR' : _FIMRESP,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.FimResp)
  })
_sym_db.RegisterMessage(FimResp)

Jogadores = _reflection.GeneratedProtocolMessageType('Jogadores', (_message.Message,), {
  'DESCRIPTOR' : _JOGADORES,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.Jogadores)
  })
_sym_db.RegisterMessage(Jogadores)

Recebimento = _reflection.GeneratedProtocolMessageType('Recebimento', (_message.Message,), {
  'DESCRIPTOR' : _RECEBIMENTO,
  '__module__' : 'dica_pb2'
  # @@protoc_insertion_point(class_scope:configuration.Recebimento)
  })
_sym_db.RegisterMessage(Recebimento)



_DICASERVICE = _descriptor.ServiceDescriptor(
  name='DicaService',
  full_name='configuration.DicaService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=697,
  serialized_end=1680,
  methods=[
  _descriptor.MethodDescriptor(
    name='CriarJogador',
    full_name='configuration.DicaService.CriarJogador',
    index=0,
    containing_service=None,
    input_type=_NOMEJOGADOR,
    output_type=_NOMEJOGADORRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EscolherPalavra',
    full_name='configuration.DicaService.EscolherPalavra',
    index=1,
    containing_service=None,
    input_type=_PALAVRA,
    output_type=_PALAVRARESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='VerPalavra',
    full_name='configuration.DicaService.VerPalavra',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_PALAVRARESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='VerDica',
    full_name='configuration.DicaService.VerDica',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_DICA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DarDica',
    full_name='configuration.DicaService.DarDica',
    index=4,
    containing_service=None,
    input_type=_DICA,
    output_type=_NOMEJOGADORRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DarPalpite',
    full_name='configuration.DicaService.DarPalpite',
    index=5,
    containing_service=None,
    input_type=_PALPITE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='VerPalpite',
    full_name='configuration.DicaService.VerPalpite',
    index=6,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_PALPITERESPOSTA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PartidaStream',
    full_name='configuration.DicaService.PartidaStream',
    index=7,
    containing_service=None,
    input_type=_PALPITE,
    output_type=_NOMEJOGADORRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ConfereEspera',
    full_name='configuration.DicaService.ConfereEspera',
    index=8,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_ESPERARESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AlteraEspera',
    full_name='configuration.DicaService.AlteraEspera',
    index=9,
    containing_service=None,
    input_type=_ESPERA,
    output_type=_ESPERARESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ConfereVez',
    full_name='configuration.DicaService.ConfereVez',
    index=10,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_NOMEJOGADORRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ConfereFim',
    full_name='configuration.DicaService.ConfereFim',
    index=11,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_FIMRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MensagemRecebida',
    full_name='configuration.DicaService.MensagemRecebida',
    index=12,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MostrarJogadores',
    full_name='configuration.DicaService.MostrarJogadores',
    index=13,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_JOGADORES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DICASERVICE)

DESCRIPTOR.services_by_name['DicaService'] = _DICASERVICE

# @@protoc_insertion_point(module_scope)
