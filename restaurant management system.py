import datetime
import random

menu = (
    ("Pizza", 250),
    ("Burger", 150),
    ("Pasta", 200),
    ("Coffee", 100),
    ("Ice Cream", 120)
)
reserved_tables = set()

orders = []

def display_menu():
    print("\n--- MENU ---")
    for index, item in enumerate(menu, start=1):
        print(f"{index}. {item[0]} - ₹{item[1]}")
def take_order():
    display_menu()
    choice = int(input("Enter item number to order: "))
    quantity = int(input("Enter quantity: "))
    item_name, item_price = menu[choice - 1]
    orders.append((item_name, quantity, item_price))
    print(f"✅ Added {quantity} x {item_name} to your order.")

def generate_bill():
    print("\n--- BILL ---")
    total = 0
    for item_name, qty, price in orders:
        subtotal = qty * price
        print(f"{item_name} x {qty} = ₹{subtotal}")
        total += subtotal
    tax = total * 0.05
    grand_total = total + tax
    print(f"Subtotal: ₹{total}")
    print(f"GST (5%): ₹{round(tax, 2)}")
    print(f"Total Bill: ₹{round(grand_total, 2)}")
    print(f"Bill Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def book_table():
    table_no = random.randint(1, 10)
    if table_no in reserved_tables:
        print(f"⚠ Table {table_no} is already booked. Trying another...")
        book_table()  
    else:
        reserved_tables.add(table_no)
        print(f"✅ Table {table_no} booked successfully!")

def main():
    while True:
        print("\n==== RESTAURANT MANAGEMENT ====")
        print("1. Show Menu")
        print("2. Place Order")
        print("3. Generate Bill")
        print("4. Book Table")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_menu()
        elif choice == '2':
            take_order()
        elif choice == '3':
            generate_bill()
        elif choice == '4':
            book_table()
        elif choice == '5':
            print("Thank you! Visit again.")
            break
        else:
            print(" Invalid choice. Try again.")

main()