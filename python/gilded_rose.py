# -*- coding: utf-8 -*-
class ItemUpdater:
    def update(self, item):
        self._update_sell_in(item)
        self._update_quality(item)

    def _update_sell_in(self, item):
        item.sell_in -= 1

    def _update_quality(self, item):
        # comportamiento por defecto
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.AGED_BRIE = "Aged Brie"
        self.SULFURAS = "Sulfuras, Hand of Ragnaros"
        self.BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    

    def _update_aged_brie(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

    def _update_backstage_pass(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.name == self.BACKSTAGE_PASSES:
                if item.sell_in < 11:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 6:
                    if item.quality < 50:
                        item.quality = item.quality + 1


    def _update_normal_item(self, item):
        if item.name != self.AGED_BRIE and item.name != self.BACKSTAGE_PASSES:
            if item.quality > 0:
                if item.name != self.SULFURAS:
                    item.quality = item.quality - 1

    def _is_sulfuras(self, item):
        return item.name == self.SULFURAS


    def update_quality(self):
        for item in self.items:
            if self._is_sulfuras(item):
                return  # no hacer nada
            self._update_aged_brie(item)
            self._update_backstage_pass(item)
            self._update_normal_item(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
