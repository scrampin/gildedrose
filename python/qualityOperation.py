class QualityOperation:
    def reset(self, item):
        item.quality = 0

    def inc(self, item, number):
        if item.quality >= 50:
            return
        else:
            item.quality += number

    def dec(self, item, number):
        if item.quality <= 0:
            return
        else:
            item.quality -= number
