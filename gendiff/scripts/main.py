from argparse import ArgumentParser

# uv run python ./gendiff/scripts/main.py -h
def main():
    # Создаем объект парсера аргументов и указываем описание скрипта
    parser = ArgumentParser(description="Compares two configuration files and shows a difference.")
    
    # Добавляем именованный аргумент
    parser.add_argument("-f", "--format", type=str, help="set format of output")
    
    # Добавляем 2 позиционных аргумента
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    
    #parser.print_help()
    
    # Получаем результат разбора аргументов командной строки, с которыми был вызван скрипт    
    args = parser.parse_args()
    # print(type(args)) # argparse.Namespace
    # print(args) # Namespace(first_file='f1', second_file='f2')
    

if __name__ == "__main__":
    main()
