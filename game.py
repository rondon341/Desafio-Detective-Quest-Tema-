import sys

def menu():
    print("\n=== Detective Quest – Tema 4 ===")
    print("1. Jogar")
    print("2. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        jogar()
    elif escolha == "2":
        print("Até logo, detetive!")
        sys.exit()
    else:
        print("Opção inválida!")
        menu()

def jogar():
    print("\nVocê é um detetive chamado para investigar um misterioso desaparecimento em uma mansão antiga.")
    print("Ao chegar, a polícia informa que há três locais suspeitos para investigar:")
    print("1. Biblioteca")
    print("2. Jardim")
    print("3. Porão")

    escolha = input("Onde deseja começar a investigação? ")

    if escolha == "1":
        biblioteca()
    elif escolha == "2":
        jardim()
    elif escolha == "3":
        porao()
    else:
        print("Escolha inválida. Tente novamente.")
        jogar()

def biblioteca():
    print("\nNa biblioteca, você encontra um diário com páginas rasgadas.")
    print("As pistas sugerem que o culpado pode ser alguém da família.")
    print("Você decide:")
    print("1. Interrogar o mordomo")
    print("2. Procurar mais pistas no diário")

    escolha = input("Escolha: ")

    if escolha == "1":
        print("\nO mordomo se contradiz durante o interrogatório... Ele é o culpado!")
        final(True)
    else:
        print("\nAs páginas estão ilegíveis e você perde tempo demais. O culpado foge...")
        final(False)

def jardim():
    print("\nNo jardim, você encontra pegadas que levam até o portão.")
    print("Você decide:")
    print("1. Seguir as pegadas")
    print("2. Ignorar e voltar para a mansão")

    escolha = input("Escolha: ")

    if escolha == "1":
        print("\nVocê segue as pegadas e descobre que o vizinho estava envolvido.")
        final(True)
    else:
        print("\nEnquanto você perde tempo, o culpado escapa pela floresta.")
        final(False)

def porao():
    print("\nNo porão, você encontra uma porta trancada.")
    print("Você decide:")
    print("1. Forçar a porta")
    print("2. Procurar a chave")

    escolha = input("Escolha: ")

    if escolha == "1":
        print("\nVocê força a porta e encontra a vítima escondida! Caso resolvido!")
        final(True)
    else:
        print("\nEnquanto procura a chave, o culpado retorna e consegue fugir.")
        final(False)

def final(vitoria):
    if vitoria:
        print("\n🎉 Parabéns, detetive! Você solucionou o caso com sucesso!")
    else:
        print("\n💀 Infelizmente, o culpado escapou. O caso continua sem solução...")
    menu()

if __name__ == "__main__":
    menu() 
