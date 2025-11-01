from argparse import ArgumentParser
from gendiff import generate_diff


# uv run python ./gendiff/scripts/main.py -h
# uv run python ./gendiff/scripts/main.py f1 f2
# uv run python ./gendiff/scripts/main.py ./tests/test_data/file1.json ./tests/test_data/file2.json
def main():
    # Создаем объект парсера аргументов и указываем описание скрипта
    parser = ArgumentParser(description="Compares two configuration files and shows a difference.")
    
    # Добавляем именованный аргумент
    parser.add_argument("-f", "--format", type=str, help="set format of output")
    
    # Добавляем 2 позиционных аргумента
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    
    # Получаем результат разбора аргументов командной строки, с которыми был вызван скрипт    
    args = parser.parse_args()
    
    diffs_str = generate_diff(args.first_file, args.second_file)
    print(diffs_str)

if __name__ == "__main__":
    main()
