class Product:
    def __init__(self, identification, price, quantity):
        self.identification = identification
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self, products):
        self.products = products

    @property
    def value(self):
        return sum(product.price for product in self.products)

    # @property
    def stock(self):
        for product in self.products:
            print(product.identification, " -> ", product.quantity)


def main():
    product_1 = Product(3, 23, 5)
    product_2 = Product(2, 65, 7)
    inventory = Inventory(2 * [product_1] + 3 * [product_2])
    print(inventory.value)
    inventory.stock()


if __name__ == '__main__':
    main()
