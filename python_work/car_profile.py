def make_car(maker, model, **car_info):
	car = {}
	car['maker'] = maker
	car['model'] = model
	for key, value in car_info.items():
		car[key] = value
	return car

car = make_car('subaru', 'outback', color='blue', tow_back=True)
print(car)
