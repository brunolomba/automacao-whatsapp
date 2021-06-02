# import funcoes
class dados:

    def __init__(self, numero_celular, nome, sobrenome):
        self.numero_celular = numero_celular
        self.nome = nome
        self.sobrenome = sobrenome

    # Alterando o número do celular.
    def redefinir_numero_celular(self, numero_celular):
        self.numero_celular = numero_celular

    # Definindo a resposta visual padrão do objeto
    def __str__(self):
        return self.numero_celular

    # Definindo o Len do objeto
    def __len__(self):
        return len(self.numero_celular)

    def __getitem__(self, item):
        return self.numero_celular[item]


# Excluindo pontuações como: + ( ) -
def mascara_apenas_numeros(self):
    self.numero_celular = self.numero_celular.replace('+', '')
    self.numero_celular = self.numero_celular.replace('(', '')
    self.numero_celular = self.numero_celular.replace(')', '')
    self.numero_celular = self.numero_celular.replace(' ', '')
    self.numero_celular = self.numero_celular.replace('-', '')
    return self.numero_celular

# Adicionando o códifo nacional.
def adicionando_digitos_brasil(self):
    if len(self.numero_celular) == 11:
        self.numero_celular = '55' + self.numero_celular
        return self.numero_celular
    else:
        return self.numero_celular

# Verificando a quantidade de números digitados e código nacional.
def verificar_numero_celular(self):
    if len(self.numero_celular) == 13:
        if self.numero_celular.find('55') == 0:
            if self.numero_celular[4] == 9:
                return True


####################################################################################################################################
# Programa rodando.
numero_1 = dados('+55 (11) 9 5219-3891', 'Bruno', 'Lomba')
mascara_apenas_numeros(numero_1)
adicionando_digitos_brasil(numero_1)

# Correção do número digitado
while len(numero_1) != 13:
    numero_1.redefinir_numero_celular(input('Digite o número de celular com DDD Ex. (xx) x xxxx-xxxx: '))
    mascara_apenas_numeros(numero_1)
    adicionando_digitos_brasil(numero_1)
    if verificar_numero_celular(numero_1) == True:
        break

# Banco de dados fictício
banco_dados = {'bruno': '5511952193890','fulano':'5511987654321'}

# Verificando se o número existe no banco de dados e adicionando ele.
if str(numero_1) not in banco_dados.values():
    nome = input('Digite um nome para o contato: ')
    banco_dados[nome] = (str(numero_1))

print(banco_dados)

# banco_dados.append(numero_1)
# print(banco_dados)