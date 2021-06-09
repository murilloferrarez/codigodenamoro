# -*- coding: utf-8 -*-
import datetime


def enum(**enums):
    return type('Enum', (), enums)


EstadoCivil = enum(solteiro='Solteiro', enrolado='Enrolado', casado='Casado',
                   namorando='Namorando', divorciado='Divorciado', viuvo='Viúvo')


class Pessoa:
    def __init__(self, nome, apelido, nascimento, status, emoji, arroba, bio):
        self.nome = nome
        self.apelido = apelido
        self.nascimento = nascimento
        self.status = status
        self.emoji = emoji
        self.arroba = arroba
        self.bio = bio
        self.planos = []
        self.viagens = []

    def to_string(self):
        str = '------------------------------------------------------\n' + \
            ' Nome: ' + self.nome + \
            '(' + self.apelido + ' ' + self.emoji + ')' + \
            '\n Status: ' + self.status + '\n Instagram: ' + self.arroba + ' - ' + self.bio + \
            '\n Planos: [' + ' '.join(self.planos) + ']' + \
            '\n Viagens: [' + ' '.join(self.viagens) + ']'
        print(str)


murillo = Pessoa(
    'Murillo Ferrarez',
    'Lillo',
    datetime.datetime(1989, 9, 11),
    EstadoCivil.solteiro,
    '📐👁️',
    '@eusouomurillo',
    '🚀Nômade Digital -- 🤷🏻‍♂️ Um sonhador liberto e livre'


)

joao = Pessoa(
    'João Fouyer',
    'Angrito',
    datetime.datetime(1998, 5, 22),
    EstadoCivil.solteiro,
    '🍺',
    '@joaofouyer',
    'Hello, Stranger'
)


def main():
    murillo.viagens = ['Israel 🇮🇱', 'Thailandia 🇹🇭', 'Islândia 🇮🇸']
    murillo.planos = ['Aprender Mandarim 🇨🇳',
                      'Jogar Tênis 🎾', 'Comprar Carro Gay 🏳️‍🌈']
    joao.viagens = ['México 🇲🇽', 'Itália 🇮🇹', 'Japão 🇯🇵']
    joao.planos = ['Fazer boneco de neve ⛄',
                   'Aprender a tocar piano 🎹', 'Jogar Tênis 🎾']
    murillo.to_string()
    joao.to_string()
    quer_namorar(obj)


def quer_namorar(objecoes):
    if not objecoes:
        aceitar()


def aceitar():
    aceita = False
    infinito = float('inf')
    muitas = 50
    if (muito_amor
        and nomades
        and respeito >= infinito
        and viagens >= muitas
        and 'sinceridade' in dialogos
            and 'paciencia' in dialogos):
        aceita = True
        fundir(murillo, joao)
        murillo.status = EstadoCivil.namorando
        joao.status = EstadoCivil.namorando
        murillo.bio += "💍 " + joao.arroba
        joao.bio += "💍 " + murillo.arroba
        definir("Cazalzinho", True)
    murillo.to_string()
    joao.to_string()


def fundir(a, b):
    a.planos += b.planos
    a.viagens += b.viagens

    b.planos = a.planos
    b.viagens = a.viagens


def definir(key, value):
    pass


def init_set(value):
    pass


muito_amor = True
respeito = float('inf')
viagens = 5000
nomades = True
dialogos = ['sinceridade', 'paciencia', 'compreensao']
obj = False
main()
