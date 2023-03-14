import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category)
from tech_news.analyzer.ratings import top_5_categories


# Requisitos 11 e 12
def analyzer_menu():
    INPUT_MAPPING = {
        "0": lambda: get_tech_news(int(input(
            "Digite quantas notícias serão buscadas:"))),
        "1": lambda: search_by_title(input("Digite o título:")),
        "2": lambda: search_by_date(input(
            "Digite a data no formato aaaa-mm-dd:")),
        "3": lambda: search_by_category(input("Digite a categoria:")),
        "4": top_5_categories,
        "5": lambda: (print("Encerrando script\n")),
    }

    user_input = input("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair. """)
    if user_input in INPUT_MAPPING:
        INPUT_MAPPING[user_input]()
    else:
        sys.stderr.write("Opção inválida\n")
