import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category)
from tech_news.analyzer.ratings import top_5_categories
# from time import sleep


# Requisitos 11 e 12
def analyzer_menu():
    user_input = input("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair. """)
    if user_input == "0":
        print("Digite quantas notícias serão buscadas:")
        amount = input()
        get_tech_news(int(amount))
    elif user_input == "1":
        print("Digite o título:")
        title = input()
        search_by_title(title)
    elif user_input == "2":
        print("Digite a data no formato aaaa-mm-dd:")
        date = input()
        search_by_date(date)
    elif user_input == "3":
        print("Digite a categoria:")
        category = input()
        search_by_category(category)
    elif user_input == "4":
        top_5_categories()
    elif user_input == "5":
        print("Encerrando script\n")
    else:
        sys.stderr.write("Opção inválida\n")
