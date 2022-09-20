from project.car.car import Car


class SportsCar(Car):
    DEFAULT_MIN_SPEED_LIMIT = 400
    DEFAULT_MAX_SPEED_LIMIT = 600

    @property
    def type(self):
        return 'SportsCar'
