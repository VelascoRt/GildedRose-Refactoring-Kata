class TestGildedRose:
    def test_normal_item_quality_decreases_by_1_before_sell_date(self):
        items = [Item("Normal Item", sellIn=10, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 19
        assert items[0].sell_in == 9

    def test_normal_item_quality_decreases_by_2_after_sell_date(self):
        items = [Item("Normal Item", sellIn=0, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 18

    def test_quality_never_goes_below_zero(self):
        items = [Item("Normal Item", sellIn=5, quality=0)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 0
    
    def test_quality_never_goes_below_zero(self):
        items = [Item("Normal Item", sellIn=5, quality=0)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 0

    def test_quality_2(self):
        items = [Item("Normal Item", sellIn=5, quality=0)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 12

    def test_quality_3(self):
        items = [Item("Normal Item", sellIn=12, quality=12)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 10

    def test_aged_brie_increases_quality_over_time(self):
        items = [Item("Aged Brie", sellIn=5, quality=10)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 11

    def test_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", sellIn=5, quality=50)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 50

    def test_quality_aged_brie1(self):
        items = [Item("Aged Brie", sellIn=100, quality=50)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 50

    def test_quality_brie2(self):
        items = [Item("Aged Brie", sellIn=500, quality=5000)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 5000

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sellIn=0, quality=80)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 80
        assert items[0].sell_in == 0

    def test_backstage_pass_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sellIn=0, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 0