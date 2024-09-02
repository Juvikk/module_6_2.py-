class Vehicle:
    def __init__(self, owner: str, model: str, color='purple', engine_power=3500):
        self.owner = owner
        self.model = model
        self.engine_power = engine_power
        self.color = color

        def get_model(self):
            return f"Модель: {self.__model}"

        def get_horsepower(self):
            return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(),
              f'Владелец: {self.owner}')

        def set_color(self, new_color: str):
            if new_color.lower() in self.__COLOR_VARIANTS:
                self.__color = new_color
            else:
                print('91mНельзя сменить цвет на {new_color}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle = Sedan('dadya fyodor', 'zhigyli', 'purple', 3500)


vehicle.print_info()

vehicle.set_color('white')
vehicle.engine_power('1500')
vehicle.owner = 'dadya petya'