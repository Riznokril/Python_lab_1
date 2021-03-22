class Park:
    def __init__(self, price_entrance_ticket = 0, length_bicycle_paths = 1234,  address = 'George Washington, 17',
    name = "Pogulyanka", max_number_people = 500, number_statues = 1):
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
    


park_1 = Park()

park_1.print_square()

print(park_1)