from argparse import ArgumentParser
from typing import get_args

from gendiff import generate_diff
from gendiff.formatters import DiffViewType
from gendiff.utils.file_reader import AVAILABLE_FILE_EXTX


def main():
    # Создаем объект парсера аргументов и указываем описание скрипта
    parser = ArgumentParser(
        description="Compares two configuration files " + 
            f"in {AVAILABLE_FILE_EXTX} format and displays the differences.",
    )
    
    # Добавляем именованный аргумент
    parser.add_argument(
        "-f", "--format", 
        type=str, 
        default="stylish", 
        help="output format",
        choices=list(get_args(DiffViewType))
    )
    
    # Добавляем 2 позиционных аргумента
    parser.add_argument("filepath1", type=str)
    parser.add_argument("filepath2", type=str)
    
    # Получаем результат разбора аргументов командной строки, 
    # с которыми был вызван скрипт    
    args = parser.parse_args()
    
    formatted_diffs = generate_diff(args.filepath1, args.filepath2, args.format)
    
    print(formatted_diffs)


if __name__ == "__main__":
    main()
