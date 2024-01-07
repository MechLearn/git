

class Contact:
    
    def __init__(self,name,email,phone,direction,dni):
        
        self.name = name
        self.email = email
        self.phone = phone
        self.direction = direction
        self.dni = dni 
        
    def func(self):
        print(self.name, self.email, self.phone, self.direction, self.dni)
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_phone(self):
        return self.phone
    def get_direction(self):
        return self.direction
    def get_dni(self):
        return self.dni

contacts=[]

contact1 = Contact('David', '1@gmail.com', 3227526909, 'Calle 40#', 1069756743 )
contact2 = Contact('Beto', '1@gmail.com', 3227526909, 'Calle 40#', 1069756743 )
contact3 = Contact('alfonso', '1@gmail.com', 3227526909, 'Calle 40#', 1069756743 )
contact4 = Contact('Sebastian', '1@gmail.com', 3227526909, 'Calle 40#', 1069756743 )
contact5 = Contact('Brad', '1@gmail.com', 3227526909, 'Calle 40#', 1069756743 )

contacts.extend([contact1,contact2,contact3,contact4,contact5])

for Contact in contacts:
    print(
         f"Name: {Contact.get_name()}, Email: {Contact.get_email()}, "
        f"Phone: {Contact.get_phone()}, Direction: {Contact.get_direction()}, "
        f"DNI: {Contact.get_dni()}"
    )

        
