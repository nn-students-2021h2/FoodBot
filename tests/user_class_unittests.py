import unittest
import sourse.user_class


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.correct_user = sourse.user_class.User(
            user_id=603485721,
            name="Daria",
            age=23,
            sex="женский",
            height=170,
            weight=60,
            activity="средняя",
            goal="похудение")

    def test_age_falls_in_range(self):
        self.assertTrue(self.correct_user.age >= 16 & self.correct_user.age <= 99)

    def test_height_falls_in_range(self):
        self.assertTrue(self.correct_user.height >= 100 & self.correct_user.height < 300)

    def test_weight_falls_in_range(self):
        self.assertTrue(self.correct_user.weight > 10 & self.correct_user.weight < 1000)

    def test_sex_types(self):
        self.assertTrue(self.correct_user.sex in ("женский", "мужской"))

    def test_activity_types(self):
        self.assertTrue(self.correct_user.activity in ("нулевая", "слабая", "средняя", "высокая", "экстремальная"))

    def test_goal_types(self):
        self.assertTrue(self.correct_user.goal in ("похудение", "поддержание формы", "набор массы"))

    def test_count_norm_returns_none(self):
        self.assertIsNone(self.correct_user.count_norm())

    def test_calorie_norm_not_none(self):
        self.assertIsNotNone(self.correct_user.calorie_norm)

    def test_protein_norm_not_none(self):
        self.assertIsNotNone(self.correct_user.protein_norm)

    def test_fat_norm_not_none(self):
        self.assertIsNotNone(self.correct_user.fat_norm)

    def test_carb_norm_not_none(self):
        self.assertIsNotNone(self.correct_user.carb_norm)


if __name__ == '__main__':
    unittest.main()
