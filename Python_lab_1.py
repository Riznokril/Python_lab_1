class Park:
    def __init__(
            self, price_entrance_ticket = 0,
            length_bicycle_paths = 1234,  
            address = 'George Washington, 17',
            name = "Pogulyanka",
            max_number_people = 500,
            number_statues = 1):
        self.price_entrance_ticket = price_entrance_ticket
        self.length_bicycle_paths = length_bicycle_paths
        self.address = address
        self.name = name
        self.max_number_people = max_number_people
        self.number_statues = number_statues

    square = 3542

    @staticmethod
    def print_square():
        print("Square is ", Park.square)

    def __str__(self):
        return f'Price for entance ticket = {self.price_entrance_ticket} \n' \
            f'Length of bicycle peths = {self.length_bicycle_paths} \n' \
            f'Adress = {self.address} \n' \
            f'Name = {self.name} \n' \
            f'Maximum numver of people = {self.max_number_people} \n' \
            f'Number of statues = {self.number_statues} \n' 
    

if __name__ == '__main__':
    park_1 = Park()
    park_2 = Park(112, 0, "Doroshnka", "Bogdan", 1200, 3)

    print("----First park----")
    park_1.print_square()
    print(park_1)

    print("----Second park----")
    park_2.print_square()   
    print(park_2)