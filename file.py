from datetime import datetime
import random


usuario = []
senha = []
cpf = []
extrato = []
reais = 0
Bitcoin = 0
Ethereum = 0
Ripple = 0
data = datetime.now()
CotR = 2.75
CotB = 40.3
CotE = 5.98

txt = ""

def escrever_no_arquivo(texto):
    global txt
    txt += texto + "\n"
with open("teste.txt", "w") as file:
    pass
# /////////////////////////////////////////////////////////////
print("Olá, seja bem-vindo à exchange")
efetuar_login1 = input("Usuario: ")
usuario.append(efetuar_login1)
escrever_no_arquivo(f"Usuario: {efetuar_login1}")

while True:
    efetuar_senha1 = input("Senha (mínimo 6 dígitos): ")
    if len(efetuar_senha1) >= 6:
        senha.append(efetuar_senha1)
        escrever_no_arquivo(f"Senha: {efetuar_senha1}")
        break
    else:   
        print("Tente com pelo menos seis dígitos.")

while True:
    efetuar_cpf1 = input("Digite seu CPF (11 números): ")
    if len(efetuar_cpf1) == 11:
        cpf.append(efetuar_cpf1)
        escrever_no_arquivo(f"CPF: {efetuar_cpf1}")
        break
    else:
        print("O CPF deve ter exatamente 11 números. Tente novamente.")
    print()


    
#Funçoes




def lista():
    print("/" * 40)
    print("Consultar saldo = 1")
    print("Consultar extrato = 2")
    print("Depositar = 3")
    print("Sacar = 4")
    print("Comprar criptomoedas = 5")
    print("Vender criptomoedas = 6")
    print("Atualizar cotação = 7")
    print("Sair = 8")
    print("/" * 40)

def saldo():
    global reais
    print("/" * 40)
    print("Nome:", usuario[0])
    print("CPF:", cpf[0])
    print("")
    print(f"Reais: {reais:.2f}")
    print(f"Bitcoin: {Bitcoin:.2f}")
    print(f"Ethereum: {Ethereum:.2f}")
    print(f"Ripple: {Ripple:.2f}")

def consultar_extrato():
    efetuar_cpf1 = input("Digite seu CPF (11 números): ")
    escrever_no_arquivo(f"Consultar extrato CPF: {efetuar_cpf1}")
    if efetuar_cpf1 != cpf[0]:
        print("Seu CPF não foi encontrado no sistema")
    else:
        for i in extrato:
            print(i)

def depositar():
    global reais
    dep_reais = float(input("Qual o valor do depósito: "))
    escrever_no_arquivo(f"Valor do deposito: {dep_reais}")
    reais += dep_reais
    efetuar_senha1 = input("Senha: ")
    escrever_no_arquivo(f"Senha: {efetuar_senha1}")
    if efetuar_senha1 != senha[0]:
        print("Senha incorreta")
    else:
        saldo()
        extD = (f"{data} + {dep_reais:.2f} REAL CT: 0.0 -- TX: 0.00 -- REAL: {reais:.2f} -- BTC: {Bitcoin:.2f} -- ETH: {Ethereum:.2f} -- XRP: {Ripple:.2f}")
        extrato.append(extD)

def sacar():
    global reais
    sac_reais = float(input("Qual o valor que você deseja sacar: "))
    escrever_no_arquivo(f"Valor do saque: {sac_reais}")
    if (sac_reais > reais) or (sac_reais < 0):
        print("Não foi possível realizar seu saque")
    else:
        reais -= sac_reais
        efetuar_senha1 = input("Senha: ")
        escrever_no_arquivo(f"Senha: {efetuar_senha1}")
        if efetuar_senha1 != senha[0]:
            print("Senha incorreta")
        else:
            saldo()
            extS = (f"{data} - {sac_reais:.2f} REAL CT: 0.0 -- TX: 0.00 -- REAL: {reais:.2f} -- BTC: {Bitcoin:.2f} -- ETH: {Ethereum:.2f} -- XRP: {Ripple:.2f}")
            extrato.append(extS)

def comprar_crp():
    global reais, Bitcoin, Ethereum, Ripple, CotB, CotE, CotR
    efetuar_senha1 = input("Senha: ")
    escrever_no_arquivo(f"Senha: {efetuar_senha1}")
    if efetuar_senha1 != senha[0]:
        print("Senha incorreta")
    else:
        print("Ripple: 0.01 -- Bitcoin: 0.02 -- Ethereum: 0.01")
        comprar = input("Qual criptomoeda você deseja comprar (Ripple, Bitcoin ou Ethereum): ")
        escrever_no_arquivo(f"Criptomoeda para comprar: {comprar}")
        valor = float(input("Qual o valor da compra: "))
        escrever_no_arquivo(f"Valor da compra: {valor}")
        if valor > reais:
            print("Saldo insuficiente, tente um valor menor")
        else:
            if comprar == "Ripple":
                R3 = valor / CotR
                R1 = R3 - (R3 * 0.01)
                Ripple += R1
                reais -= valor
                extR = (f"{data} + {valor:.2f} XRP CT: {CotR:.2f} -- TX: 0.01 -- REAL: {reais:.2f} -- BTC: {Bitcoin:.2f} -- ETH: {Ethereum:.2f} -- XRP: {Ripple:.2f}")
                extrato.append(extR)
            elif comprar == "Bitcoin":
                B3 = valor / CotB
                B1 = B3 - (B3 * 0.02)
                Bitcoin += B1
                reais -= valor
                extB = (f"{data} + {valor:.2f} BTC CT: {CotB:.2f} -- TX: 0.02 -- REAL: {reais:.2f} -- BTC: {Bitcoin:.2f} -- ETH: {Ethereum:.2f} -- XRP: {Ripple:.2f}")
                extrato.append(extB)
            elif comprar == "Ethereum":
                E3 = valor / CotE
                E1 = E3 - (E3 * 0.01)
                Ethereum += E1
                reais -= valor
                extE = (f"{data} + {valor:.2f} ETH CT: {CotE:.2f} -- TX: 0.01 -- REAL: {reais:.2f} -- BTC: {Bitcoin:.2f} -- ETH: {Ethereum:.2f} -- XRP: {Ripple:.2f}")
                extrato.append(extE)
            else:
                print("Tente uma moeda existente")

def vender_crp():
    global reais, Bitcoin, Ethereum, Ripple, CotB, CotE, CotR
    efetuar_senha1 = input("Senha: ")
    escrever_no_arquivo(f"Senha: {efetuar_senha1}")
    if efetuar_senha1 != senha[0]:
        print("Senha incorreta")
    else:
        vender = input("Qual criptomoeda você deseja vender (Ripple, Bitcoin ou Ethereum): ")
        escrever_no_arquivo(f"Criptomoeda para vender: {vender}")
        preço = float(input("Qual o valor da venda: "))
        escrever_no_arquivo(f"Valor da venda: {preço}")
        if vender == "Ripple":
            R4 = preço / CotR
            R2 = R4 + (R4 * 0.01)
            Ripple -= R2
            reais += preço
            extR1 = (f"{data} - {preço:.2f} XRP CT: {CotR:.2f} -- TX: 0.01 -- REAL: {reais:.2f} -- BTC: {Bitcoin:.2f} -- ETH: {Ethereum:.2f} -- XRP: {Ripple:.2f}")
            extrato.append(extR1)
        elif vender == "Bitcoin":
            B4 = preço / CotB
            B2 = B4 + (B4 * 0.03)
            Bitcoin -= B2
            reais += preço
            extB1 = (f"{data} - {preço:.2f} BTC CT: {CotB:.2f} -- TX: 0.03 -- REAL: {reais:.2f} -- BTC: {Bitcoin:.2f} -- ETH: {Ethereum:.2f} -- XRP: {Ripple:.2f}")
            extrato.append(extB1)
        elif vender == "Ethereum":
            E4 = preço / CotE
            E2 = E4 + (E4 * 0.02)
            Ethereum -= E2
            reais += preço
            extE1 = (f"{data} - {preço:.2f} ETH CT: {CotE:.2f} -- TX: 0.02 -- REAL: {reais:.2f} -- BTC: {Bitcoin:.2f} -- ETH: {Ethereum:.2f} -- XRP: {Ripple:.2f}")
            extrato.append(extE1)
        else:
            print("Tente uma moeda existente")

def cotaçao():
    global Ripple, Bitcoin, Ethereum, CotB, CotR, CotE
    atualizar = str(input("Deseja atualizar as cotações? "))
    escrever_no_arquivo(f"Atualizar cotacoes: {atualizar}")
    if atualizar == "não":
        return
    elif atualizar == "sim":
        atualizar_ripple = random.randint(-5, 5) / 100
        CotR *= atualizar_ripple
        Ripple *= (1 + atualizar_ripple)

        atualizar_bitcoin = random.randint(-5, 5) / 100
        CotB *= atualizar_bitcoin
        Bitcoin *= (1 + atualizar_bitcoin)

        atualizar_ethereum = random.randint(-5, 5) / 100
        CotE *= atualizar_ethereum
        Ethereum *= (1 + atualizar_ethereum)

        print(f'Cotação Ripple atualizado: {CotR:.2f}')
        print(f'Cotação Bitcoin atualizado: {CotB:.2f}')
        print(f'Cotação Ethereum atualizado: {CotE:.2f}')
        print("Acesse o saldo(1) para saber sua nova quantidade de criptomoedas")

# /////////////////////////////////////////////////////////////
lista()
print()
# //////////////////////////////////////////////////////////////////////////////////////////
while True:
    menu = int(input("Digite o número da operação que você deseja realizar: "))
    escrever_no_arquivo(f"Escolha do menu: {menu}")
    if menu == 1:
        saldo()
    elif menu == 2:
        consultar_extrato()
    elif menu == 3:
        depositar()
    elif menu == 4:
        sacar()
    elif menu == 5:
        comprar_crp()
    elif menu == 6:
        vender_crp()
    elif menu == 7:
        cotaçao()
    elif menu == 8:
        break



with open("teste.txt", "w") as file:
    file.write(txt)
