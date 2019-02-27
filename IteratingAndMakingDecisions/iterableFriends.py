friends = ['James Prudence', 
           'Silvester Otieno', 
           'Shirley Muronji', 
           'Brian Musee',
           'Leucrecia Jeruto']
ages = [21, 20, 19, 19,'sijui age']
ethnicities = ['Luo', 'BornTown', 'Luhya', 'Kamba', 'Kalenjin']
for friend, age, ethnicity in zip(friends, ages, ethnicities):
	print(friend, age,ethnicity)