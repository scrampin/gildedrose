# -*- coding: utf-8 -*-
import unittest

from inventory import Inventory
from item import Item

class InventoryTest(unittest.TestCase):

    def test_quality_degrade(self):
        items = [Item("expired", 0, 10)]
        inventory = Inventory(items)
        inventory.update()
        self.assertEquals(items[0].quality, 8)

    def test_quality_positive(self):
        items = [Item("poor quality", 5, 0)]
        inventory = Inventory(items)
        inventory.update()
        self.assertEquals(items[0].quality, 0)

    def test_brie_quality(self):
        items = [Item("Aged Brie", 5, 3)]
        inventory = Inventory(items)
        inventory.update()
        self.assertEquals(items[0].quality, 4)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 3)]
        inventory = Inventory(items)
        inventory.update()
        self.assertEquals(items[0].quality, 3)
        self.assertEquals(items[0].sell_in, 5)

    def test_passes_low(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 3)]
        inventory = Inventory(items)
        inventory.update()
        self.assertEquals(items[0].quality, 4)

    def test_passes_medium(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 3)]
        inventory = Inventory(items)
        inventory.update()
        self.assertEquals(items[0].quality, 5)

    def test_passes_high(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 3)]
        inventory = Inventory(items)
        inventory.update()
        self.assertEquals(items[0].quality, 6)

    def test_expired_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 40)]
        inventory = Inventory(items)
        inventory.update()
        self.assertEquals(items[0].quality, 0)

    def test_max_value(self):
        items = [Item("Aged Brie", 5, 50), Item("Backstage passes to a TAFKAL80ETC concert", 3, 50)]
        inventory = Inventory(items)
        inventory.update()
        self.assertEquals(items[0].quality, 50)
        self.assertEquals(items[1].quality, 50)

    def test_conjured_items(self):
        items = [Item("Conjured Mana Cake", 4, 8)]
        inventory = Inventory(items)
        inventory.update()
        self.assertEquals(items[0].quality, 6)

    def test_conjured_items_after_expiry(self):
        items = [Item("Conjured Mana Cake", 0, 8)]
        inventory = Inventory(items)
        inventory.update()
        self.assertEquals(items[0].quality, 4)

if __name__ == '__main__':
    unittest.main()
