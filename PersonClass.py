
class Person:
    def __init__(self,name, address,phone):
        self.name = name
        self.address = address
        self.phone = phone


    def get_name (self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_phone_number(self):
        return self.phone

    def print_person(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")


class Customer(Person):
    def __init__(self,name, address,phone, cust_number, on_list):
        Person.__init__(self,name, address,phone)

        self.__cust_number = cust_number
        self.__on_list = on_list

    def print_person(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")
        print('Customer Number:', self.__cust_number)
        if self.__on_list:
            print("On Mailing List: Yes")
        else:
            print("On Mailing List: No")