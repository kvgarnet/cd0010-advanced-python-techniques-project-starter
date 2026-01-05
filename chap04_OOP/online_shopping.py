class Product:
    def __init__(self, name, description, price, seller, available):
        self.name = name
        self.description = description
        self.seller = seller
        self.reviews = []
        self.price = price
        self.available = available

    def __repr__(self):
        return f"Product({self.name}, {self.description}) at ${self.price}"

class Review:
    def __init__(self, content, user, product):
        self.content = content
        self.user = user
        self.product = product

    def __str__(self):
        return f"Review of {self.product} by {self.user}: '{self.content}'"


# from product import Product
# from review import Review


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reviews = []
        # below are added by kevin
        self.selling_list = []
        self.buying_list = []

    def write_review(self, content, product):
        review = Review(content, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        print(f"{self.name}'s review of {product.name}: {review.content}")
        return review

    def sell_product(self, name, description, price):
        product = Product(name, description, price, self, available=True)
        print(f"{product} is on the market!")
        # below are added by kevin
        self.selling_list.append(product.name)
        return product

    def buy_product(self, product):
        if product.available:
            print(f"{self.name} is buying {product.name}.")
            product.available = False
            # below are added by kevin
            self.buying_list.append(product.name)
            product.seller.selling_list.remove(product.name) 
        else:
            print(f"{product} is no longer available.")

    def __str__(self):
        return f"User(id={self.id}, name={self.name})"



brianna = User(1, 'Brianna')
mary = User(2, 'Mary')

# return a product class's instance : keyboard
keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
guitar = brianna.sell_product('Guitar', 'A nice metal guitar', 200)
print(keyboard.available)  # => True
print('selling list before sold')
print(f"Brinana's selling list: {brianna.selling_list}")  # =>['Keyboard', 'Guitar'] 
print(f"Mary's buying list: {mary.buying_list}")  # => [] 
mary.buy_product(keyboard)

print('selling list after sold')
print(f"Brinana's selling list: {brianna.selling_list}")  # =>['Guitar']
print(f"Mary's buying list: {mary.buying_list}")  # => ['Keyboard']
print(keyboard.available)  # => False
# return a Review class instance: review
review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)  # => True
print(review in keyboard.reviews)  # => True
