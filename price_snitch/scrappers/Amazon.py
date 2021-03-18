import ScrapperInterface as I

class Amazon(I.ScrapperInterface):
    url = "www.amazon.es"

    def update_price(self, soup, item):
        price = soup.find('div', attrs={'id':'price'})

        current_price = float(price.find('span', attrs={'id':'priceblock_ourprice'}).text[:-2].replace(',','.'))
        base_price = price.find('span', attrs={'class':'priceBlockStrikePriceString a-text-strike'})

        if(base_price == None):
            base_price = current_price
        else:
            base_price = float(base_price.text[:-2].replace(',','.'))

        item.set_base_price(base_price)
        item.set_current_price(current_price)
        item.set_discount()