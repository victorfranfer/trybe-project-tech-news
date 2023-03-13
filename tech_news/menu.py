import sys


# Requisitos 11 e 12
def analyzer_menu():
    print("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.""")
    user_input = input()
    if user_input == 0:
        print("Digite quantas notícias serão buscadas:")
    elif user_input == 1:
        print("Digite o título:")
    elif user_input == 2:
        print("Digite a data no formato aaaa-mm-dd:")
    elif user_input == 3:
        print("Digite a categoria:")
    else:
        sys.stderr.write("Opção inválida")
