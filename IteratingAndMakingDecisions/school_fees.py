""" If my School fees is less then 10k, 
I won't pay any trip_fee. 
If it is between 10k and 30k, 
I'll pay 20% trip_fee. 
If it is between 30k and 100k, 
I'll pay 35% trip_fee, and over 100k, 
I'll (gladly) pay 45% trip_fee"""

SchoolFees = 15000
if SchoolFees<10000: 
	trip_fee=0.2
elif SchoolFees<30000:
	trip_fee = 0.2
elif SchoolFees < 100000:
	trip_fee =0.35
else:
	trip_fee =0.45

print("I will pay:", SchoolFees ," and ",SchoolFees * trip_fee, "trip fee this Semester")