# -*- coding: utf-8 -*-
import dajarating
import unittest


class TestDajarep(unittest.TestCase):
    def test_dajarep(self):
        self.assertEqual(dajarating.dajarep.dajarep(u"猫が寝転んだ"), u"ネコ")  # ダジャレ
        self.assertEqual(dajarating.dajarep.dajarep(u"布団が吹っ飛んだ"), u"フトン")  # ダジャレ
        self.assertEqual(dajarating.dajarep.dajarep(u"イカは如何なものか"), u"イカ")  # ダジャレ
        self.assertEqual(dajarating.dajarep.dajarep(u"今日は良い天気ですね"), u"")  # NOTダジャレ
        self.assertEqual(dajarating.dajarep.dajarep(u"犬が犬小屋にいる"), u"")  # NOTダジャレ
        self.assertEqual(dajarating.dajarep.dajarep(u"人民の人民による人民のための政治"), u"")  # NOTダジャレ


if __name__ == "__main__":
    unittest.main()
