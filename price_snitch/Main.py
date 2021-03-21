from PriceWarner import PriceWarner
import pandas as pd
from Item import Item

config_file = "resources/config.yaml"
items_file = "resources/products.csv"

price_warner = PriceWarner(config_file)
items = pd.read_csv(items_file)

for _, row in items.iterrows():
    item = Item(row['name'], row['url'], row['threshold'])
    price_warner.process_row(item)

price_warner.process_warning_list()
print(str(len(price_warner.warning_list)) + " items under its threshold.")
print(str(len(price_warner.error_list)) + " items with errors.")