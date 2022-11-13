documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people_doc():
    for doc in documents:
        if doc['number'] == number_document:
            return doc['name']

    return "Документ не существует"


def shelf():
    for shel, docum in directories.items():
        if number_document in docum:
            return f"Документ под номером: {number_document} находится на {shel} полке"

        print(f"Документ {number_document} не обноружен")


def list_document():
    for doc in documents:
        print(doc['name'], doc['number'], doc['type'])


def add_document():
    if shel not in directories:
        print("такой полки не существует")
        return
    documents.append({'type': type_document, 'number': number_document, 'name': name_human})
    directories[shel].append(number_document)


def delete_document():
    for key, doc in directories.items():
        if number_document in doc:
            doc.remove(number_document)
            break

        else:
            return "Такой номера не существует"

    for document in documents:
        if number_document == document['number']:
            del (document['name'], document['type'], document['number'])
            return "Документ и номер удолен"


def add_shelf():
    if shel in directories:
        print("Такая полка уже существует!")
        return
    directories[shel] = []
    return f"полка: {shel} добавлена"


while True:
    command = input("Ввидите команду: ")
    if command == "p":
        number_document = input("Введите номер документа: ")
        print(people_doc())
    elif command == "s":
        number_document = input("Введите номер документа: ")
        print(shelf())
    elif command == "l":
        print(list_document())
    elif command == "a":

        type_document = input("Вид документа: ")
        number_document = input("Номер документа: ")
        name_human = input("Введите Имя и Фамилию: ")
        shel = input("Введите номер полки: ")
        print(add_document())
        print(list_document())
    elif command == "d":
        number_document = input("Номер документа: ")
        print(delete_document())
        print(list_document())
    elif command == "as":
        shel = input("Введите номер полки которую хотите добавить: ")
        print(add_shelf())
    elif command == "q":
        break
