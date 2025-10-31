from argparse import ArgumentParser


def main():
    # Создаем объект парсера аргументов и указываем описание скрипта
    parser = ArgumentParser(description="Compares two configuration files and shows a difference.")
    
    # Добавляем 2 позиционных аргумента
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    
    # Получаем результат разбора аргументов командной строки, с которыми был вызван скрипт    
    # args = parser.parse_args()
    # print(type(args)) # argparse.Namespace
    # print(args) # Namespace(first_file='f1', second_file='f2')
    

if __name__ == "__main__":
    main()
