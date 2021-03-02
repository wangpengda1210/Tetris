vee_engine_cars = Car.objects.filter(engine__type='vee', engine__volume__lte=300)
