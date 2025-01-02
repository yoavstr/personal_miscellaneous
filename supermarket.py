from typing import List, Dict, Any

class Supermarket:

    def __init__(self) -> None:
        """Init method, defining products and cart"""
        self.products: Dict[int, Dict[str, Any]] = {
            1: {"name": "Apple", "price": 2.00},
            2: {"name": "Bannana", "price": 1.50},
            3: {"name": "Milk", "price": 3.00},
            4: {"name": "Bread", "price": 2.50},
            5: {"name": "Egg", "price": 3.50},
            6: {"name": "Beer", "price": 2.00},
            7: {"name": "Cheese", "price": 1.00},
            8: {"name": "Chicken", "price": 2.50},
            9: {"name": "Beef", "price": 3.00},
            10: {"name": "Pasta", "price": 2.00}
        }

        self.cart: List = []

    def show_menu(self) -> None:
        """Function to show the options which user can take in the supermarket"""
        print("\nHappy Shopping!")
        print("1: View products")
        print("2. Add procuct to cart")
        print("3. Remove product from cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

    def view_products(self) -> None:
        """Function to show available products in the supermarket"""
        print("\nAvailable Products:")

        for product_id, product_info in self.products.items():
            print(f"{product_id}. {product_info['name']} - ${product_info['price']:.2f}")

    def add_to_cart(self) -> None:
        """Function to add a product to cart. Only allows to add available products."""
        self.view_products()
        product_id: int = int(input("\nEnter product number to add to cart: "))

        if product_id in self.products:
            self.cart.append(self.products[product_id])
            print(f"{self.products[product_id]['name']} has been added to cart")

        else:
            print("Invalid product number.")

    def remove_from_cart(self) -> None:
        """Function to remove a product from cart. Only allows to remove product if cart is not empty and if
        product is available"""
        if not self.cart:
            print("\nYour cart is empty")
            return
        
        print("\nItems in your cart:")

        for idx, item in enumerate(self.cart, start=1):
            print(f"{idx}. {item['name']} - ${item['price']:.2f}")

        item_to_remove = int(input("\nEnter the item to remove from cart: "))

        if 1 <= item_to_remove <= len(self.cart):
            removed_item = self.cart.pop(item_to_remove - 1)
            print(f"{removed_item['name']} has been removed from the cart")
        
        else:
            print("Invalid item number.")

    def view_cart(self) -> None:
        """Function to show the current cart products and total price."""
        if not self.cart:
            print("\nYour cart is empty.")

        else:
            print("\nItems in your cart:")
            total = 0

            for item in self.cart:
                print(f"- {item['name']} - ${item['price']:.2f}")
                total = total + item['price']
            
            print(f"Total: ${total:.2f}")

    def checkout(self) -> None:
        """Function to checkout. Clears cart, only allows to checkout if cart is not empty."""
        if not self.cart:
            print("Your cart is empty. Nothing to checkout.")

        else:
            total = sum(item['price'] for item in self.cart)
            print(f"\nYour total is ${total:.2f}. Proceeding to checkout...")
            self.cart.clear()
            print("Thank you for shopping with us!")

    def run(self) -> None:
        """Function that runs the programme using a while true loop"""
        while True:
            self.show_menu()
            choice = int(input("Enter your choice: "))
            choices = {1: self.view_products,
                       2: self.add_to_cart,
                       3: self.remove_from_cart,
                       4: self.view_cart,
                       5: self.checkout}
            
            if choice == 6:
                print("\nExiting the Supermarket. Thank you for shopping with us :)")
                break
            
            if choice not in choices:
                print("Invalid choice. Please try again.")

            if not choice:
                print("Invalid choice. Please try again.")

            else:
                choices[choice]()

if __name__ == "__main__":
    supermarket = Supermarket()
    supermarket.run()