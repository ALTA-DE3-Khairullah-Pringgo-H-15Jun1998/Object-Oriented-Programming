import math

def calculate_volume(length, width, height):
    return length * width * height

def calculate_price(length, width, height, weight):
    volume = calculate_volume(length, width, height)
    if volume < 50:
        volume = 50

    rounded_weight = math.ceil(weight)

    price_per_kg = 5000
    total_price = rounded_weight * price_per_kg
    return total_price

if __name__ == "__main__":
    length = float(input("Masukkan panjang barang (cm): "))
    width = float(input("Masukkan lebar barang (cm): "))
    height = float(input("Masukkan tinggi barang (cm): "))
    weight = float(input("Masukkan berat barang (kg): "))

    price = calculate_price(length, width, height, weight)
    print(f"Total pengiriman barang : Rp. {price}")
