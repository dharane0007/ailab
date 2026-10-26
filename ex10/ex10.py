
# SECOND-HAND PRODUCT EXCHANGE SYSTEM

products = []


def add_product():
    print("\n--- Add Second-Hand Product ---")
    product_id = len(products) + 1

    name = input("Enter product name: ")
    category = input("Enter category: ")
    price = float(input("Enter expected price (Rs.): "))
    condition = input("Enter condition (Good/Excellent/Fair): ")
    seller = input("Enter seller name: ")
    contact = input("Enter contact number: ")

    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "condition": condition,
        "seller": seller,
        "contact": contact,
        "status": "Available"
    }

    products.append(product)
    print("\nProduct added successfully!")


def view_products():
    print("\n--- Available Products ---")

    available = [p for p in products if p["status"] == "Available"]

    if not available:
        print("No products available.")
        return

    print("-" * 75)
    print(f"{'ID':<5}{'Product':<18}{'Category':<15}"
          f"{'Price (Rs.)':<15}{'Condition':<12}")
    print("-" * 75)

    for p in available:
        print(f"{p['id']:<5}{p['name']:<18}{p['category']:<15}"
              f"{p['price']:<15.2f}{p['condition']:<12}")

    print("-" * 75)


def search_product():
    keyword = input("Enter product name or category to search: ").lower()

    found = False

    for p in products:
        if (keyword in p["name"].lower()
                or keyword in p["category"].lower()):
            if p["status"] == "Available":
                print("\nProduct Found")
                print("Product ID :", p["id"])
                print("Name       :", p["name"])
                print("Category   :", p["category"])
                print("Price      : Rs.", p["price"])
                print("Condition  :", p["condition"])
                print("Seller     :", p["seller"])
                print("Contact    :", p["contact"])
                found = True

    if not found:
        print("No matching available product found.")


def exchange_product():
    view_products()

    if not products or not any(
            p["status"] == "Available" for p in products):
        return

    try:
        product_id = int(input("Enter product ID to exchange: "))
    except ValueError:
        print("Please enter a valid product ID.")
        return

    for p in products:
        if p["id"] == product_id and p["status"] == "Available":
            print("Selected product:", p["name"])
            buyer = input("Enter buyer name: ")
            p["status"] = "Exchanged"
            print("\nExchange completed successfully!")
            print("Product :", p["name"])
            print("Buyer   :", buyer)
            print("Seller  :", p["seller"])
            return

    print("Invalid product ID or product already exchanged.")


def main():
    while True:
        print("\n===== SECOND-HAND PRODUCT EXCHANGE =====")
        print("1. Add Product")
        print("2. View Available Products")
        print("3. Search Product")
        print("4. Exchange Product")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            exchange_product()
        elif choice == "5":
            print("\nThank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
