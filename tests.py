import unittest
import subway

class SubwaySystemTests(unittest.TestCase):

    def test_add_train_line(self):
        subway_system = subway.SubwaySystem()
        subway_system.add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="1")
        self.assertDictEqual(subway_system.network, {'Canal': {'Houston': {'line': '1', 'time': 1}}, 'Houston': {'Canal': {'line': '1', 'time': 1}, 'Christopher': {'line': '1', 'time': 1} }, '14th': {'Christopher': {'line': '1', 'time': 1}}, 'Christopher': {'Houston': {'line': '1', 'time': 1}, '14th': {'line': '1', 'time': 1}}})
        subway_system.add_train_line(stops=["Spring", "West 4th", "14th", "23rd"], name="E")

        self.assertDictEqual(subway_system.network, {'West 4th': {'14th': {'line': 'E', 'time': 1}, 'Spring': {'line': 'E', 'time': 1}}, '14th': {'West 4th': {'line': 'E', 'time': 1}, 'Christopher': {'line': '1', 'time': 1}, '23rd': {'line': 'E', 'time': 1}}, 'Spring': {'West 4th': {'line': 'E', 'time': 1}}, '23rd': {'14th': {'line': 'E', 'time': 1}}, 'Houston': {'Canal': {'line': '1', 'time': 1}, 'Christopher': {'line': '1', 'time': 1}}, 'Canal': {'Houston': {'line': '1', 'time': 1}}, 'Christopher': {'14th': {'line': '1', 'time': 1}, 'Houston': {'line': '1', 'time': 1}}})

    def test_take_train(self):
        subway_system = subway.SubwaySystem()
        subway_system.add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="1")
        subway_system.add_train_line(stops=["Spring", "West 4th", "14th", "23rd"], name="E")
        subway_system.add_train_line(stops=["Wall", "Fulton", "Park Place", "Chambers", "14th", "34th"], name="2")
        path = subway_system.take_train(origin="Houston", destination="23rd")
        path2 = subway_system.take_train(origin="23rd", destination="Houston")
        path3 = subway_system.take_train(origin="Spring", destination="Canal")
        self.assertEqual(path, ['Houston', 'Christopher', '14th', '23rd'])
        self.assertEqual(path2, ['23rd', '14th', 'Christopher', 'Houston'])
        self.assertEqual(path3, ['Spring', 'West 4th', '14th', 'Christopher', 'Houston', 'Canal'])

    def test_take_train_with_time(self):
        subway_system = subway.SubwaySystem()
        subway_system.add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="1", time_between_stations=[("Canal", "Houston", 3), ("Houston", "Christopher", 7),("Christopher", "14th", 2)])
        subway_system.add_train_line(stops=["Spring", "West 4th", "14th", "23rd"], name="E",time_between_stations=[("Spring", "West 4th", 1),("West 4th", "14th", 5),("14th", "23rd", 2),])
        path = subway_system.take_train(origin="Houston", destination="23rd")
        self.assertEqual(path, (["Houston", "Christopher", "14th", "23rd"], 11))


if __name__ == "__main__":
    unittest.main()
