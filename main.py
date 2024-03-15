import pepper_parser as parser


def main():
    max_number = ''

    while not max_number.isdigit():
        max_number = input("Введите количество страниц для парсинга: ")

    offers = parser.get_offers(int(max_number))

    if offers:
        for i in range(len(offers)):
            print(f'{i+1}. Название акции: "{offers[i][0]}"')
            print(f'{len(str(i+1))*" "}  Ссылка: {offers[i][1]}')
            print(f'{len(str(i+1))*" "}  Градусы: {offers[i][2]}\n')
    else:
        print("Произошла ошибка...")


if __name__ == "__main__":
    main()
