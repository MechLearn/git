
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class Favorite(Contact):
    def __init__(self, nombre, email, phone, birthday):
        super().__init__(nombre,email,phone)
        self.birthday = birthday
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Bithday: {self.birthday}"
    
        
