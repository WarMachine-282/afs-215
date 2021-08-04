
# class Checkout(object):
    
#     def __init__(self):
#         self.items = list()
#         self.total = 0

#     def add(self, product, price):
#         self.items.append({"product": str(product), "price": int(price)})
    
#     def cal_total(self, product):
#         self.total = 0
#         for product in self.items:
#             self.total += self.items[product]['price']
#         return self.totaL
    
#     # def discount(self):
#     #     if type(discount) != int:


# market = Checkout()

# # adding items with pricing to the array
# market.add("peanut butter", 6)
# market.add("orange", 1)
# market.add("milk", 3)
# print(market.items)
# print(market.cal_total)

class Checkout:
    class Discount:
        def __init__(self, quantity, price):
            self.quantity = quantity
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}


    def addItemPrice(self, item, price):
        self.prices[item] = price 


    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad item")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1


    def addDiscount(self, item, quantity, price):
        discount = self.Discount(quantity, price)
        self.discounts[item] = discount


    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
                total += self.calculateItemTotal(item, count) 
        return total


    def calculateItemTotal(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.quantity:
                total += self.calculateItemDiscountedTotal(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count
        return total


    def calculateItemDiscountedTotal(self, item, count, discount):
        total = 0
        numOfDiscounts = count/discount.quantity
        total += numOfDiscounts * discount.price
        remaining = count % discount.quantity
        total += remaining * self.prices[item]
        return total