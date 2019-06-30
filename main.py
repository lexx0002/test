documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def find_holder():
    find_holders = 0
    number = input('Введите номер документа, который вы ищете ')
    for document in documents:
        if document['number'] == number:
            print(document['name'])
            find_holders = 1
    if find_holders != 1:
        print('Этого номера нет в документах')

def show_all_documents():
    for document in documents:
        for a in document:
            if a == 'type':
                print(document[a], end=' ', sep='')
            else:
                print('"', document[a], '"', sep='', end=' ')
        print('\n')

def find_directory():
    find_holders = 0
    number = input('Введите номер документа, который вы ищете ')
    for directory in directories:
        for shelf in directories[directory]:
            if shelf == number:
                print('Данный документ находится на ', directory, ' полке.', sep='')
                find_holders = 1
    if find_holders != 1:
        print('Этого номер нет в документах')

def add_documents():
    type_of_document = input('Введите тип документа \n')
    number_of_document = input('Введите номер документа \n')
    name_of_holder = input('Введите имя и фамилию человека, кому принадлежит этот документ \n')
    shelf_of_document = input('Введите на какой полке будет храниться этот документ ')

    documents.append({'type': type_of_document, 'number': number_of_document, 'name': name_of_holder})
    directories[shelf_of_document].append(number_of_document)
    print('Ваш документ добавлен')

def delete_document():
    number_of_document = input('Введите номер документа, который необходимо удалить \n')
    for document in documents:
        if document['number'] == number_of_document:
            documents.remove(document)
    for directory in directories:
        for shelf in directories[directory]:
            if shelf == number_of_document:
                directories[directory].remove(shelf)

def move_document():
    number_of_document = input('Введите номер документа, который необходимо переместить \n')
    shelf_of_document = input('На какую полку переместить данный документ? ')
    for directory in directories:
        for shelf in directories[directory]:
            if shelf == number_of_document:
                directories[directory].remove(shelf)
    directories[shelf_of_document].append(number_of_document)
    print(directories)

def add_new_shelf():
    new_shelf = input('Введите номер новой полки ')
    directories[new_shelf] = []
    print('Полка добавлена.')
    '''
    мне кажется тут можно было задание построить на том, что есть n полок, добавить следующую, или есть 1, 2, 4 полки, добавить следующую, либо заполнить пропуски, было бы интереснее
    '''

command = input('Введите команду, которую необходимо выполнить:\n').upper()
if command == 'P':
    find_holder()
elif command == 'L':
    show_all_documents()
elif command == 'S':
    find_directory()
elif command == 'A':
    add_documents()
elif command == 'D':
    delete_document()
elif command == 'M':
    move_document()
elif command == 'AS':
    add_new_shelf()
else:
    print('Не найдена команда')
