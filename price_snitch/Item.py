class Item:

    def __init__(self, name, url, threshold, scrapper):
        self.name = name
        self.url = url
        self.threshold = threshold
        self.base_price = ""
        self.current_price = ""
        self.discount = ""
        self.scrapper = scrapper

    def set_base_price(self, base_price):
        self.base_price = base_price

    def set_current_price(self, current_price):
        self.current_price = current_price

    def set_discount(self, discount=None):
        if discount is None:
            self.discount = round(1 - (self.current_price / self.base_price), 2)
        else:
            self.discount = discount

    def __str__(self):
        return "(Name: " + self.name + ", scrapper: " + self.scrapper + ", URL: " + self.url + " , threshold: " + str(
            self.threshold) + ", base price: " + str(self.base_price) + ", current price: " + str(
            self.current_price) + ", discount: " + str(self.discount) + ")"

    def is_below_threshold(self):
        if str(self.threshold)[-1] == '%':
            return self.discount * 100 > float(self.threshold[:-1])
        else:
            return self.current_price < self.threshold
