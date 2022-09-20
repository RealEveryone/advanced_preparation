from project.car.car import Car


class MuscleCar(Car):
    DEFAULT_MIN_SPEED_LIMIT = 250
    DEFAULT_MAX_SPEED_LIMIT = 450

    @property
    def type(self):
        return 'MuscleCar'

