# MENU ORDERING SYSTEM
# By: GROUP 3 

# Starting Menu (with prices)
meals = {"A": ("Burger", 30), "B": ("Spaghetti", 40), "C": ("Fried Chicken", 40)}
drinks = {"1": ("Coke", 25), "2": ("Iced Tea", 20), "3": ("Water", 10)}

ADMIN_PASSWORD = "1234"

while True:
    print("\n=== Welcome to our Mini Restaurant ===")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = input("Choose your role (1-3): ")

    # CUSTOMER SIDE
    if choice == "1":
        print("\n--- MENU ---")
        print("Meals:")
        for code, (meal, price) in meals.items():
            print(f"  {code}. {meal} - ₱{price}")

        print("\nDrinks:")
        for code, (drink, price) in drinks.items():
            print(f"  {code}. {drink} - ₱{price}")

        meal_choice = input(f"\nEnter meal letter : ").upper()
        drink_choice = input("Enter drink number : ")

        if meal_choice in meals and drink_choice in drinks:
            meal_name, meal_price = meals[meal_choice]
            drink_name, drink_price = drinks[drink_choice]
            total = meal_price + drink_price

            confirm = input("Confirm your order? (yes/no): ").lower()

            # kung e confirm ba niya ang order
            if confirm == "yes":
                print("\nOrder Confirmed! Thank you.")
                print(f"You ordered {meal_name} and {drink_name}.")
                print(f"Total Price: ₱{total}")
            else:
                print("Order Cancelled. Returning to Menu.")
        else:
            print("\nInvalid selection. Item not in menu.")

    # ADMIN SIDE
    elif choice == "2":
        password = input("Enter admin password: ")

        while True:
            if password == ADMIN_PASSWORD:  #pag dili mo equal sa ADMIN_PASSWORD mo balik sa main menu
                print("\n--- Admin Dashboard ---")
                print("1. Add Meal")
                print("2. Add Drink")
                print("3. Log Out")
                admin_choice = input("Choose an option: ")

                if admin_choice == "1":
                    new_code = input("Enter code letter for meal (Example: D): ").upper()
                    new_meal = input("Enter new meal name: ").title()
                    price = int(input("Enter meal price: "))
                    meals[new_code] = (new_meal, price)
                    print(f"{new_meal} added at ₱{price}.")
                
                elif admin_choice == "2":
                    new_code = input("Enter number code for drink (Example: 4): ")
                    new_drink = input("Enter new drink name: ").title()
                    price = int(input("Enter drink price: "))
                    drinks[new_code] = (new_drink, price)
                    print(f"{new_drink} added at ₱{price}.")
                
                elif admin_choice == "3":
                    print("Returning to Menu...")
                    break
                else:
                    print("Invalid option.")
            else:
                print("Access Denied! Wrong password.")
                break

    # EXIT PROGRAM
    elif choice == "3":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice. Please try again.") 
        