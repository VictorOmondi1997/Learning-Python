custormers = [
    dict(id=1, total=200, coupon_code='F20'), #F20; fixed $20
    dict(id=2, total=150, coupon_code='P30'), # p30 persent 30%
    dict(id=3, total=100, coupon_code='P50'),
    dict(id=4, total=110, coupon_code='F15'),
]
for custormer in custormers:
	code=custormer['coupon_code']
	if code=='F20':
		custormer['discount']=20.0
	elif code=='F15':
		custormer['discount']=15.0
	elif code=='P30':
		custormer['discount']=custormer['total']*0.3
	elif code=='P50':
		custormer['discount']=custormer['total']*0.5
	else:
		custormer['discount']=0.0
for custormer in custormers:
    print(custormer['id'], custormer['total'], custormer['discount'])	