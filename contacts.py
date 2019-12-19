import csv

class Contact:
    def __init__(self, name,phone,email):
        self._name = name
        self._phone = phone
        self._email = email

class ContactBook:
    def __init__(self):
        self._contacts = []
    
    def add(self,name,phone,email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()
    
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def search(self,name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self,name):
        for i, contact in enumerate(self._contacts):
            if contact._name.lower() == name.lower():
                phone = str(input("Escribe el telefono del contacto: "))
                email = str(input("Escribe el email del contacto: "))
                contact._phone = phone
                contact._email = email
                self._contacts[i] = contact
                self._print_contact(contact)
                self._save()
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))
            for contact in self._contacts:
                writer.writerow((contact._name, contact._phone, contact._email))

    def _not_found(self):
        print('-----------------------------')
        print('No se encontró el contacto!!!')
        print('-----------------------------')

    def delete(self,name):
        for i, contact in enumerate(self._contacts):
            if contact._name.lower() == name.lower():
                del self._contacts[i]
                self._save()
                break

    def _print_contact(self,contact):
        print('-----------------------------------------')        
        print('Nombre: {}'.format(contact._name))
        print('Teléfono: {}'.format(contact._phone))
        print('Email: {}'.format(contact._email))
    
    def subir_datos(self,contact_book):
        with open('contacts.csv','r') as f:
            reader = csv.reader(f)
            for i,row in enumerate(reader):
                if i == 0 or ''.join(row) == "":
                    continue
                contact_book.add(row[0],row[1],row[2])


def run():
    contact_book = ContactBook()
    contact_book.subir_datos(contact_book)

    while True:
        command = str(input('''
            ---------------------------------------
            A G E N D A    D E     C O N T A C T O
            ---------------------------------------
            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
            Seleccione una opción: 
        ''')).lower()
        if command == 'a':
            name = str(input("Escribe el nombre del contacto: "))
            phone = str(input("Escribe el telefono del contacto: "))
            email = str(input("Escribe el email del contacto: "))
            contact_book.add(name, phone, email)
        elif command == 'ac':
            name = str(input("Escribe el nombre del contacto: "))
            contact_book.update(name)
        elif command == 'b':
            name = str(input("Escribe el nombre del contacto: "))
            contact_book.search(name)
        elif command == 'e':
            name = str(input("Escribe el nombre del contacto: "))
            contact_book.delete(name)
        elif command == 'l':
            contact_book.show_all()
        elif command == 's':
            break
        else:
            print('Opción no encontrada')

if __name__ == '__main__':
    run()
