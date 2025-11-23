# main.py
from calculadora import OPERACOES, mensagem_secreta
import os
import platform

def limpar_tela():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def obter_numero(mensagem="Digite um número: "):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, digite um número válido!")

def exibir_menu():
    print("=" * 40)
    print("     CALCULADORA PYTHON TURBO 3000    ".center(40))
    print("=" * 40)
    for chave, (nome, _) in OPERACOES.items():
        print(f"{chave}. {nome}")
    print("0. Sair")
    print("9. Mensagem secreta")
    print("=" * 40)

def main():
    print(mensagem_secreta())  # Easter egg na inicialização
    input("Pressione Enter para continuar...")
    
    while True:
        limpar_tela()
        exibir_menu()
        escolha = input("\nEscolha uma operação: ").strip()

        if escolha == "0":
            print("Valeu por usar a Calculadora Turbo 3000! Até mais!")
            break
        elif escolha == "9":
            limpar_tela()
            print("\n" + mensagem_secreta() * 5)
            input("\nPressione Enter para voltar...")
            continue
        elif escolha not in OPERACOES:
            input("Opção inválida! Pressione Enter para tentar novamente...")
            continue

        operacao_nome, funcao = OPERACOES[escolha]

        limpar_tela()
        print(f"→ {operacao_nome.upper()}")
        print("-" * 30)

        if escolha == "6":  # Raiz quadrada
            num = obter_numero("Digite o número: ")
            resultado = funcao(num)
        else:
            a = obter_numero("Digite o primeiro número: ")
            if escolha != "5":  # Potência pede expoente opcional
                b = obter_numero("Digite o segundo número: ")
                resultado = funcao(a, b)
            else:
                expoente = obter_numero("Digite o expoente (padrão 2): ") if input("Usar expoente padrão [2]? (s/N): ").strip().lower() != "s" else 2
                resultado = funcao(a, expoente)

        print(f"\nResultado: {resultado}")
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()