import ScrapperInterface as I

class Pccomponentes(I.ScrapperInterface):
    url = "www.pccomponentes.com"

    def update_price(self, soup, item):
        price = soup.find('div', attrs={'class':'precioMain'})

        item.set_base_price(float(price['data-baseprice']))
        item.set_current_price(float(price['data-price']))
        item.set_discount()