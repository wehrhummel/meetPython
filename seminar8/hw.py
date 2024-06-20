
def work_with_phonebook():

    choice = show_menu()
    phone_book = read_txt("phonebook.txt")
    while (choice != 7):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            find_abonent(phone_book, input("Введите фамилию или номер телефона абонента: "))
        elif choice == 3:
            add_user(phone_book)
            write_txt('phonebook.txt', phone_book)
        elif choice == 4:
            last_name = input('Фамилия: ')
            new_number = input('Номер телефона: ')
            print(change_number(phone_book, last_name, new_number))
            write_txt('phonebook.txt', phone_book)
        elif choice == 5:
            lastname = input('Фамилия: ')
            copy_to_another_phonebook(phone_book, lastname)
        elif choice == 6:
            lastname = input('Фамилия: ')
            delete_by_lastname(phone_book, lastname)
            write_txt('phonebook.txt', phone_book)
        choice = show_menu()


def show_menu():

    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента\n"
          "3. Добавить абонента в справочник\n"
          "4. Изменить номер телефона абонента\n"
          "5. Перенести абонента в другой справочник\n"
          "6. Удалить абонента\n"
          "7. Закончить работу")
    choice = int(input())
    return choice


def read_txt(filename):

    phone_book = []
    fields = ['last_name', 'first_name', 'phone_number', 'description']
    with open(filename, 'r', encoding='utf-8') as phb:
        for s in phb:
            s = s.replace('\n', '')
            record = dict(zip(fields, s.split(',')))
            phone_book.append(record)
        return phone_book


def write_txt(filename, phone_book):

    with open('phonebook.txt','w' ,encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            if len(phone_book[i]) == 1:
                phone_book.pop(i)
            s = ''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')


def print_result(phone_book):

    for i in range(len(phone_book)):
        # for v in phone_book[i].values():
        #     if len(phone_book[i]) > 0:
        #         print(f'{v}', end=' ')
        print(*[v for v in phone_book[i].values()])
        # print(*filter(lambda v: 0 < (abs(int(x)) // 10) < 10, num_list.split()))
        # print()


def find_abonent(phone_book, abonent_option):
    for i in range(len(phone_book)):
        if phone_book[i]['last_name'] == abonent_option or phone_book[i]['phone_number'] == abonent_option:
            print(phone_book[i]['last_name'], phone_book[i]['first_name'], phone_book[i]['phone_number'], phone_book[i]['description'])



def add_user(phone_book):
    last_name = input('Фамилия нового абонента: ')
    first_name = input('Имя: ')
    phone_number = input('Номер телефона: ')
    description = input('Описание: ')
    phone_book.append({'last_name': last_name, 'first_name': first_name, 'phone_number': phone_number, 'description': description})



def delete_by_lastname(phone_book, lastname):
    for i in range(len(phone_book)):
        if phone_book[i]['last_name'] == lastname:
            phone_book[i].clear()
            print(f'Абонент {lastname} удален')




def copy_to_another_phonebook(phone_book, lastname):

    phonebook_out = open(input('Имя файла, куда копируем абонента: '), 'a', encoding='utf-8')
    for i in range(len(phone_book)):
        s = ''
        if phone_book[i]['last_name'] == lastname:
            for ph in phone_book[i].values():
                s = s + ph + ','
            phonebook_out.write(f'{s[:-1]}\n')
    phonebook_out.close()



def change_number(phone_book, last_name, new_number):
    for i in range(len(phone_book)):
        if phone_book[i]['last_name'] == last_name:
            phone_book[i]['phone_number'] = new_number



work_with_phonebook()

