import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Joro',10,100.0,1.0)


    def test_init(self):
        self.assertEqual(self.hero.username,'Joro')
        self.assertEqual(self.hero.level,10)
        self.assertEqual(self.hero.health,100.0)
        self.assertEqual(self.hero.damage,1.0)

    def test_fight_with_your_self_raises(self):
        with self.assertRaises(Exception) as ex:
            copy = Hero('Joro',10,100.0,1.0)
            self.hero.battle(copy)

        self.assertEqual(str(ex.exception),"You cannot fight yourself")

    def test_unsuccessful_battle_zero_or_negative_health(self):
        enemy = Hero('Scrapman',10,10,10)
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual(str(ex.exception),"Your health is lower than or equal to 0. You need to rest")

    def test_fight_with_enemy_hero_zero_or_negative_health(self):
        enemy = Hero('Scrapman',10,-1,1)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual(str(ex.exception),"You cannot fight Scrapman. He needs to rest")

    def test_the_draw_battle(self):
        enemy = Hero('Scrapman',1,10,10)
        self.hero.damage = 10
        self.hero.health = 10
        self.hero.level = 1
        result = self.hero.battle(enemy)
        self.assertEqual(result,"Draw")
        self.assertEqual(self.hero.health,0)
        self.assertEqual(enemy.health,0)

    def test_the_win_battle(self):
        enemy = Hero('Scrapman', 1, 10, 10)
        result = self.hero.battle(enemy)
        self.assertEqual(result,"You win")
        self.assertEqual(self.hero.health,95)
        self.assertEqual(enemy.health,0)

    def test_the_lose_battle(self):
        self.hero.health = 1
        self.hero.damage = 1
        self.hero.level = 1
        enemy = Hero('Scrapman', 1, 10, 10)
        result = self.hero.battle(enemy)
        self.assertEqual(result,"You lose")
        self.assertEqual(enemy.health,14)
        self.assertEqual(self.hero.health,-9)

    def test__str__(self):
        self.assertEqual("Hero Joro: 10 lvl\n"
                         "Health: 100.0\n"
                         "Damage: 1.0\n", str(self.hero))











if __name__ == '__main__':
    unittest.main()