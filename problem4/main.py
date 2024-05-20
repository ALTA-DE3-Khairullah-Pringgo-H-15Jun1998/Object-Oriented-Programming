# tulis solusi code disini
class ShippingGoods:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    def calculate_volume(self):
        return self.length * self.width * self.height

    def calculate_price(self):
        if self.calculate_volume() >= 50 and self.weight >= 1:
            return 5000
        else:
            return 0

    def print_details(self):
        print(f"Length: {self.length} cm")
        print(f"Width: {self.width} cm")
        print(f"Height: {self.height} cm")
        print(f"Weight: {self.weight} kg")
        print(f"Volume: {self.calculate_volume()} cm3")
        print(f"Price: Rp. {self.calculate_price()}")

# Example usage
goods1 = ShippingGoods(10, 5, 2, 0.5)
goods1.print_details()

goods2 = ShippingGoods(20, 10, 5, 2)
goods2.print_details()

goods3 = ShippingGoods(5, 3, 1, 0.1)
goods3.print_details()
