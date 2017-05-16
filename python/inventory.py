# -*- coding: utf-8 -*-
from qualityUpdate import QualityUpdate
from sellInUpdate import SellInUpdate

class Inventory(object):

    def __init__(self, items):
        self.items = items
        self.qualityupdate = QualityUpdate()
        self.sellinupdate = SellInUpdate()

    def update(self):
        for item in self.items:

            if "Sulfuras" in item.name:
                return
            elif "Brie" in item.name:
                self.qualityupdate.cheese(item)
            elif "Backstage pass" in item.name:
                self.qualityupdate.bstgpass(item)
            elif "Conjured" in item.name:
                self.qualityupdate.conjured(item)
            else:
                self.qualityupdate.vanilla(item)

            self.sellinupdate.day(item)
