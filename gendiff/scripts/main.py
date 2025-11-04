from argparse import ArgumentParser

from gendiff import generate_diff


# uv run python ./gendiff/scripts/main.py -h
# uv run python ./gendiff/scripts/main.py f1 f2
# uv run python ./gendiff/scripts/main.py --format plain f1 f2
# ruff: noqa: E501
def main():
    # Создаем объект парсера аргументов и указываем описание скрипта
    parser = ArgumentParser(
        description="Compares two configuration files and shows a difference.",
    )
    
    # Добавляем именованный аргумент
    parser.add_argument("-f", "--format", type=str, default="stylish", help="output format")
    
    # Добавляем 2 позиционных аргумента
    parser.add_argument("filepath1", type=str)
    parser.add_argument("filepath2", type=str)
    
    # Получаем результат разбора аргументов командной строки, 
    # с которыми был вызван скрипт    
    args = parser.parse_args()
    
    diffs_str = generate_diff(args.filepath1, args.filepath2, args.format)
    
    print(diffs_str)


if __name__ == "__main__":
    main()
