import random
import string

# Declarando classes

class Criptografia:

    def __init__(self):
        self.chaves = {}
        self.carregar_chaves()

    # Função para criptografar    

    def criptografar(self, texto, chave):
        criptografado = []
        for i in range(len(texto)):
            criptografado.append(texto[i] ^ chave[i % len(chave)])
        return bytes(criptografado)

    # Função para gerar uma chave aleatoria e salvar

    def criar_chave_aleatoria(self, nome_chave):
        random_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
        self.chaves[nome_chave] = random_key.encode('utf-8')
        self.salvar_chaves()

    # Função para buscar a chave e mostrar a 'string' associada a ela 

    def buscar_chave(self, nome_chave):
        if nome_chave in self.chaves:
            return self.chaves[nome_chave]
        try:
            return bytes.fromhex(nome_chave)
        except ValueError:
            return None

    # Função para salvar as chaves em um arquivo '.txt'

    def salvar_chaves(self):
        with open("chaves.txt", "w") as arquivo:
            for chave_nome, chave in self.chaves.items():
                arquivo.write(f"{chave_nome}:{chave.hex()}\n")

    # Função para carregar as chaves ja salvas

    def carregar_chaves(self):
        try:
            with open("chaves.txt", "r") as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    partes = linha.strip().split(":")
                    if len(partes) == 2:
                        chave_nome, chave = partes
                        self.chaves[chave_nome] = bytes.fromhex(chave)
        except FileNotFoundError:
            pass

    # Função para verificar se a mensagem criptografada foi inserida em Hexadecimal

    def input_mensagem_cifrada_hex(self):
        while True:
            mensagem_cifrada_hex = input("Insira a frase criptografada em hexadecimal: ")
            if self.is_hexadecimal(mensagem_cifrada_hex):
                return mensagem_cifrada_hex
            else:
                print("O texto inserido não é um valor hexadecimal válido. Tente novamente.")

    def is_hexadecimal(self, texto):
        try:
            bytes.fromhex(texto)
            return True
        except ValueError:
            return False
        
    # Função para descriptograr 

    def descriptografar(self, texto_criptografado, chave):
        descriptografado = []
        for i in range(len(texto_criptografado)):
            descriptografado.append(texto_criptografado[i] ^ chave[i % len(chave)])
        return bytes(descriptografado)
    

    # Aqui incicia o programa

if __name__ == "__main__":
    criptografia = Criptografia()

    # Menu do programa com as opçoes disponiveis
   