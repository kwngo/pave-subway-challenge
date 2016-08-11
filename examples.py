import subway

subway_system = subway.SubwaySystem()
subway_system.add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="1")
subway_system.add_train_line(stops=["Spring", "West 4th", "14th", "23rd"], name="E")
subway_system.add_train_line(stops=["Wall", "Fulton", "Park Place", "Chambers", "14th", "34th"], name="2")
path = subway_system.take_train(origin="Houston", destination="23rd")
print("Answer to Challenge 1:", path)

subway_system_with_times = subway.SubwaySystem()
subway_system_with_times.add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="1", time_between_stations=[("Canal", "Houston", 3), ("Houston", "Christopher", 7),("Christopher", "14th", 2)])
subway_system_with_times.add_train_line(stops=["Spring", "West 4th", "14th", "23rd"], name="E",time_between_stations=[("Spring", "West 4th", 1),("West 4th", "14th", 5),("14th", "23rd", 2),])
path2 = subway_system_with_times.take_train(origin="Houston", destination="23rd")
print("Answer to Challenge 2:", path2)
