items = [
    {
        "category": "Fruits",
        "items": [
            {"type": "Apple", "price": 0.99, "quantity_in_stock": 200},
            {"type": "Banana", "price": 1.20, "quantity_in_stock": 12},
            {"type": "Grapes", "price": 2.00, "quantity_in_stock": 343},
            {"type": "Oranges", "price": 1.00, "quantity_in_stock": 211},
            {"type": "Peaches", "price": 1.50, "quantity_in_stock": 4},
            {"type": "Avocado", "price": 1.00, "quantity_in_stock": 5},
            {"type": "Strawberry", "price": 3.00, "quantity_in_stock": 34},
        ]
    },
    {
        "category": "Vegetables",
        "items": [
            {"type": "Carrot", "price": 0.50, "quantity_in_stock": 100},
            {"type": "Broccoli", "price": 1.25, "quantity_in_stock": 50},
            {"type": "Spinach", "price": 1.00, "quantity_in_stock": 80},
            {"type": "Tomato", "price": 0.75, "quantity_in_stock": 150},
        ]
    },
    {
        "category": "Dairy",
        "items": [
            {"type": "Milk", "price": 2.50, "quantity_in_stock": 100},
            {"type": "Cheese", "price": 3.00, "quantity_in_stock": 45},
            {"type": "Yogurt", "price": 1.50, "quantity_in_stock": 75},
            {"type": "Butter", "price": 2.75, "quantity_in_stock": 60},
        ]
    }
]


def shop():
    global price
    cart = []

    first_run = True
    total = 0

    try:
        while True:
            try:
                if first_run:
                    print("Welcome to our Grocery store!, please select the category you want to buy")
                    user = input("Enter 'start' to open our category list: ")

                    if user != "start":
                        print("invalid command, enter 'start'")
                        continue

                first_run = False

                for item in items:
                    print(item["category"])
                print("--" * 10)

                user_type = input("Pick a category: ")

                for item in items:
                    if user_type.lower() in item["category"].lower():
                        for products in item["items"]:
                            print(products["type"])
                        print("--" * 10)
                        break


                else:
                    print("invalid category selected")
                    user_type = input("Pick a category: ")
                    continue

                user_product = input("select a product: ")
                user_quantity = int(input("enter quantity: "))

                is_found = False

                for item in items:
                    for products in item["items"]:
                        if user_product.lower() in products["type"].lower():
                            # remaining_item_in_stock = user_quantity - products["quantity_in_stock"]
                            # if user_quantity <= products["quantity_in_stock"]:
                            #     products["quantity-in-stock"] -= user_quantity
                            #     print(f"remaining stock is {products['product_in_stock']}")
                            #     return True

                            total_price = products["price"] * user_quantity
                            selected_item = f"{user_product}: ${total_price}"
                            cart.append(selected_item)
                            is_found = True
                            break

                    if is_found:
                        break

                if not is_found:
                    print("Product not found")

                else:
                    print(f"Added to cart {cart}")
                    print("--" * 10)

                user_cont = input("Do you want to continue shopping: Y/N: ")

                if user_cont == "N":

                    if cart:
                        print(f"Your purchase is: {','.join(cart)}")
                        for price_tot in cart:
                            name, price = price_tot.split(': $')
                            total += float(price)

                        print("--" * 10)
                        print(f" The total amount to be paid is ${total}")
                        print("How would you like to pay")
                        print("--" * 10)

                    else:
                        print("your cart is empty")

                    break

                elif user_cont != "Y":
                    print("Invalid input please enter Y to continue or N to exit")
                    print("--" * 10)



            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting the shopping process.")




shop()
