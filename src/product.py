class product_item:
    def __init__(self, name, price, quantity, sum):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sum = sum
        self.unique_name = ''

    def get_unique_name(self):
        pass

    def __repr__(self):
        return f'"Название: {self.name}, цена: {self.price}, количество: {self.quantity}, стоимость: {self.sum}"'
