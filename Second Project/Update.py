import pickle


class ContactList:
    
    ## en este metodo inicio una lista vacia y le determino que la cargue con los argumentos del metodo load_contacts()
    def __init__(self):
        self.contacts =[]
        self.load_contacts()
        
    # metodo añadir contacto y use el metodo guardar contacto
    
    def add_contacts(self,contact):
        self.contacts.append(contact)
        self.save_contacts()
    
    ## Metodo mostrar contactos, en este metodo se hace un recorrido que enumere los valores de la lista para poder mostrar
    
    def display_contacts(self):
        for index , contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact}")
            
    ## Metodo para remover contactos 
    
    def remove_contacts(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
            self.save_contacts()
            print("Contact Removed ")
        else:
            print("Invalid index ")
            
    ## metodo guardar contactos 
    
    def save_contacts(self):
       with open('contacts.pk1', 'wb') as file:
            pickle.dump(self.contacts, file) 
            
        
    def load_contacts(self):
        try:
           with open('contacts.pk1', 'rb') as file:
            self.contacts = pickle.load(file)
        except (FileNotFoundError, EOFError):
         self.contacts = []  