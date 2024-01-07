from Contacts import contact




class crud:
    
    def __init__(self):
        self.contacts = []
        
    def add_contact(self,contact):
        self.contacts.append(contact)
        
    def display_contacts(self):
        for index, contact in enumerate(self.contacts, start=1):
           print(f"{index}, Name: {contact.get_name()}, Email : {contact.get_email()}, Phone: {contact.phone()}, Direction: {contact.get_direction()}, DNI: {contact.get_dni()}")
        

print("Contact List: ")
my_crud = crud()
