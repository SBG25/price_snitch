import ScrapperInterface as I

class Game(I.ScrapperInterface):
    url = "www.game.es"

    def update_price(self, soup, item):
        price = soup.find('div', attrs={'class':'buy-xl buy-new'})

        base_price = price.find('small', attrs={'class':'buy--price-small u-line-through'})
        current_price_int = price.find('span', attrs={'class':'int'}).text.replace('\n','').replace('\t','').replace('\r','')
        current_price_decimal = float(price.find('span', attrs={'class':'decimal'}).text[1:]) / 100
        if(base_price == None):
            current_price_int = float(current_price_int) + current_price_decimal
            base_price = current_price_int
        else:
            base_price = base_price.text
            current_price_int = float(current_price_int.replace(base_price, ''))
            current_price_int = current_price_int + current_price_decimal
            base_price = float((base_price)[:-1].replace(',','.'))
        current_price = current_price_int

        item.set_base_price(base_price)
        item.set_current_price(current_price)
        item.set_discount()