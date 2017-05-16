from qualityOperation import QualityOperation

class QualityUpdate:
    def __init__(self):
        self.qualityoperation = QualityOperation()

    def vanilla(self, item):
        if item.sell_in > 0:
            self.qualityoperation.dec(item, 1)
        else:
            self.qualityoperation.dec(item, 2)

    def conjured(self, conjured):
        if conjured.sell_in > 0:
            self.qualityoperation.dec(conjured, 2)
        else:
            self.qualityoperation.dec(conjured, 4)

    def cheese(self, brie):
        if brie.sell_in > 0:
            self.qualityoperation.inc(brie, 1)
        else:
            self.qualityoperation.inc(brie, 2)

    def bstgpass(self, bspass):
        if bspass.sell_in > 10:
            self.qualityoperation.inc(bspass, 1)
        elif bspass.sell_in <= 0:
            self.qualityoperation.reset(bspass)
        elif bspass.sell_in <= 5:
            self.qualityoperation.inc(bspass, 3)
        elif bspass.sell_in <= 10:
            self.qualityoperation.inc(bspass, 2)
