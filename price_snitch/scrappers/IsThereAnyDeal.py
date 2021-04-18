import ScrapperInterface as I


class IsThereAnyDeal(I.ScrapperInterface):
    name = "IsThereAnyDeal"

    def update_price(self, soup, item):
        price = soup.findAll('td', attrs={'class': 'gh-po__price'})[1].text[:-1].replace(',', '.')
        price = float(price)

        item.set_base_price(None)
        item.set_current_price(price)
        item.set_discount(None)
