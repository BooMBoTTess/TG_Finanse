class Product_item:
    def __init__(self, name, price, quantity, sum):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sum = sum
        self.unique_name = ''

    def set_unique_name(self):
        '''
        Достать уникальное название для товара, чтобы называть разные товары одинаково
        '''
        pass

    def __repr__(self):
        return f'"Название: {self.name}, цена: {self.price}, количество: {self.quantity}, стоимость: {self.sum}"'

    def __iter__(self):
        for attr_name in self.__dict__:
            yield getattr(self, attr_name)