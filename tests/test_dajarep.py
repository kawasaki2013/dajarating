# -*- coding: utf-8 -*-
__author__ = 'gabill'
import dajarating
import unittest

class TestDajarep(unittest.TestCase):
    def test_dajarep(self):
        self.assertEqual(dajarating.dajarep.dajarep(u"猫が寝転んだ"),u"ネコ")
        self.assertEqual(dajarating.dajarep.dajarep(u"布団が吹っ飛んだ"),u"フトン")
        self.assertEqual(dajarating.dajarep.dajarep(u"イカは如何なものか"),u"イカ")
        self.assertEqual(dajarating.dajarep.dajarep(u"今日は良い天気ですね"),u"")
        self.assertEqual(dajarating.dajarep.dajarep(u"犬が犬小屋にいる"),u"")
        self.assertEqual(dajarating.dajarep.dajarep(u"人民の人民による人民のための政治"),u"")

if __name__ == "__main__":
    unittest.main()