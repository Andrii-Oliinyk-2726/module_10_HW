from collections import UserDict
replies = ["hello", ["good bye", "close", "exit"]]
answers = ['How can I help you?', 'Good bye!']
phonebook = {}


class AddressBook(UserDict): # логика поиска по записям
           
    def add_record(self): # добавляет Record в self.data
        pass

class Record: # отвечает за логику добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name
    def __init__(self, comand, name):
        self.comand = comand
        self.name = name


class Field: # будет родительским для всех полей, в нем потом реализуем логику общую для всех полей
    pass

class Name:
    def __init__(self, name):
        self.name = name # обязательное поле с именем

class Phone:
    # list_phone_numbers = []
    def __init__(self, phone_number = '') -> None: # необязательное поле с телефоном и таких одна запись (Record) может содержать несколько
        self.phone_number = phone_number
        # print('Phone_number= ', self.phone_number)

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except:
            return "Give me name and phone please"
    return inner

# hello-good_bye-others
@input_error
def reply(answer):
    if answer == replies[0]:
        return answers[0]
    elif answer in replies[1]:
        return answers[1]
    else:
        adressbook = AddressBook(phonebook)
        comand = answer.split()
        input_comand = Record(comand[0], comand[1])
        input_name = Name(comand[1])
        if len(comand) >= 3:
            input_phone_number = Phone(comand[2])

        if input_comand.comand == 'add' or input_comand.comand == 'change':
            phonebook[input_comand.name] = input_phone_number.phone_number
            print(phonebook)
        elif input_comand.comand == 'phone':
            print(phonebook[input_comand.name])
        elif input_comand.comand == 'show' and input_comand.name == 'all':
            print(phonebook)
        return 'Ok'
    
# phone_add-change-shows 
@input_error     
def add_change_shows(comand):
    if comand[0] == 'add' or comand[0] == 'change':
        phonebook[comand[1]] = comand[2]
        print(phonebook)
        return "Ok"
    elif comand[0] == 'phone':
        return phonebook[comand[1]]
    elif comand[0] == 'show' and comand[1] == 'all':
        return phonebook
    else:
        return "I don't understand you"

def main():
    botloop = True
    while botloop:
        print('user:', end=' ')
        rep = input().lower()
        print(reply(rep))
        if rep in replies[1]:
            botloop = False
       

if __name__ == '__main__':
    main()
    