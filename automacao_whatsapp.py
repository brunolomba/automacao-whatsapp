# import funcoes
class dados:
    def __init__(self, numero_celular):
        self.numero_celular = numero_celular

# Excluindo pontuações como: + ( ) -
def mascara_apenas_numeros(self):
    self.numero_celular = self.numero_celular.replace('+', '')
    self.numero_celular = self.numero_celular.replace('(', '')
    self.numero_celular = self.numero_celular.replace(')', '')
    self.numero_celular = self.numero_celular.replace(' ', '')
    self.numero_celular = self.numero_celular.replace('-', '')
    return self.numero_celular

# Verificando a quantidade de números digitados e código nacional.
def verificar_numero_celular(self):
    if len(self.numero_celular) == 13:
        if self.numero_celular.find('55') == 0:
            if self.numero_celular[4] == 9:
                return True

def redefinir_numero_celular(self, numero_celular):
    self.numero_celular = numero_celular

# Banco de dados fictício.
banco_dados = [5511952193890, 5511987654321]

# Programa rodando.
numero_1 = dados('+55(11)9 5219-38900')

while verificar_numero_celular(numero_1) != True:
    numero_1.redefinir_numero_celular = input('Digite um numero de celular com 13 dígitos exemplo: +55 (xx) x xxxx-xxxx: ')
    verificar_numero_celular(numero_1)