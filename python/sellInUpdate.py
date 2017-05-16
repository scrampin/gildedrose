class SellInUpdate:
    def day(self, item):
        if "Sulfuras" in item.name:
            return
        else:
            item.sell_in -= 1
