
class Checkout(object):
    def __init__(self):
        self.items = list()

    def add(self, product, price):
        self.items.append({"product": str(product), "price": int(price)})

market = Checkout()
market.add("orange", 2)
print(market.items)

