customer = input("Enter your name: ")

product1 = input("Enter the name of the first product: ")
price1 = float(input(f"Enter the price of {product1}: "))

product2 = input("Enter the name of the second product: ")
price2 = float(input(f"Enter the price of {product2}: "))

product3 = input("Enter the name of the third product: ")
price3 = float(input(f"Enter the price of {product3}: "))

subtotal = price1 + price2 + price3

if subtotal >= 5000:
    discount = subtotal * 0.20
elif subtotal >= 3000:
    discount = subtotal * 0.10
elif subtotal >= 1000:
    discount = subtotal * 0.05
else:
    discount = 0

final_total = subtotal - discount

print(f"\nCustomer Name: {customer}")
print(f"Product 1: {product1} Price: {price1:.2f}")
print(f"Product 2: {product2} Price: {price2:.2f}")
print(f"Product 3: {product3} Price: {price3:.2f}")

print(f"\nSubtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")