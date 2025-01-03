from tinydb import TinyDB
from time import sleep
from os import system, name

lista = []
db = TinyDB('historico.json')

def verificar_sistema():
	sleep(0.7)
	if name == "nt": system("cls")
	else: system("clear")


def registrar_banco(registro):
	db.insert({"conta_realizada:": registro})


def carregar(value=0.8):
    print("carregando", end="\r")
    sleep(value)  
    print("carregando.", end="\r")
    sleep(value + 0.1)
    print("carregando..", end="\r")
    sleep(value + 0.1)
    print("carregando...", end="\r")
    sleep(value + 0.2)


def calc_basica(valor1, valor2):
	operacao = input('''
escolha a operacao
+ para adicao
- para subtracao
* para multiplicacao
/ para divisao
% para modulo
// para divisao minima
** para exponencial:
''')
	
	if operacao not in ["+", "-", "/", "*", "%", "//", "**"]:
		print(f"{operacao} não é um operador matematico, amigao")
		verificar_sistema()
	else:	
		operações = {
			"+": valor1 + valor2,
			"-": valor1 - valor2,
			"*": valor1 * valor2,
			"/": valor1 / valor2,
			"**": valor1 * valor2,
			"//": valor1 // valor2,
			"%": valor1 % valor2
		}
		carregar()
		print(f"{valor1} {operacao} {valor2} = {operações.get(operacao)}")
		result = f"{valor1} {operacao} {valor2}"
		registrar_banco(result)


def calc_porcentagi(valor1, valor2):
	print("""
esta calculadora oferece opções
relacionadas a cálculo de porcentagem de
um valor:
1-calcular a porcentagem de um numero
2-descobrir quantos porcento um numero é
de outro\n
""")
	pergunta = int(input("escolha uma opção:"))
	if pergunta == 1:
		operacao = valor2 * valor1 / 100
		result = f"{valor2} % de {valor1} = {operacao}%"
		print(result)
		registrar_banco(result)
	
	elif pergunta == 2:		
		operacao = valor2 / valor1 * 100
		result = f"{valor2} equivale a {operacao}% de {valor1}"
		print(result)
		registrar_banco(result)
	else:
		print(f"a opção {pergunta} não existe")
		verificar_sistema()


def calc_desconto(valor1, valor2):
	print("Calcule o valor de um produto com desconto")
	valor_com_desconto = valor1 - (valor1 * valor2 / 100)
	result = f"{valor1} menos {valor2} % = {valor_com_desconto}"
	registrar_banco(result)
	print(f"Esse é o valor do produto com desconto: {valor_com_desconto}$ reais")


def calc_media():
	quanti_notas = int(input("digite quanto notas ira calcular: "))
	for x in range(quanti_notas):
		x += 1
		notas = float(input(f"digite a {x} nota: "))
		lista.append(notas)
	
	resultado = sum(lista) / len(lista)
	result = f"a media de {len(lista)} notas = {resultado}"
	registrar_banco(result)
	print(f"a media de {len(lista)} notas eh {resultado}")


def calc_medidas():
	number = int(input("digite um valor para ser convertido: "))
	metros_for_centimetros = float(input("""
deseja converter:
1- metros para centímetros
2- centímetros para metros
"""))
	if metros_for_centimetros == 1:
		metros = number / 100
		print(f"{number} centímetros convertidos dão {metros} metros")
    	
	if metros_for_centimetros == 2:
		metros = number * 100
		print(f"{number} metros convertidos dão {metros} centímetros")