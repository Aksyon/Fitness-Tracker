

from turtle import distance, speed


class Training():
    """Basic class for different sport activities."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    H_IN_MIN = 60 

    def __init__(self, action: int, duration: float, weight: float):
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration
    
    def get_spent_calories(self):
        pass
    @staticmethod
    def show_training_info(self):
        return InfoMessage(self)


class Running(Training):
    """Class describe methods and parameters for running activity."""
    COEF_CALORIE_1 = 18
    COEF_CALORIE_2 = 20
    
    def get_spent_calories(self) -> float:
        return ((self.COEF_CALORIE_1 * self.get_mean_speed() -
                self.COEF_CALORIE_2) * self.weight / self.M_IN_KM *
                self.duration * self.H_IN_MIN)


class SportsWalking(Training):
    """Class describe methods and parameters for walking activity."""
    COEF_CALORIES_1 = 0.035
    COEF_CALORIES_2 = 0.029
    

    def __init__(self, height: float):
        super().__init__(self)
        self.height = height
    
    def get_spent_calories(self) -> float:
        return ((self.COEF_CALORIES_1 * self.weight + (self.get_mean_speed()**2
               // self.height) * self.COEF_CALORIES_2 * self.weight) *
               self.duration * self.H_IN_MIN)


class Swimming(Training):
    """Class describe methods and parameters for swimming activity."""
    COEF_CALORIES_1 = 1.1
    COEF_CALORIES_2 = 2
    LEN_STEP = 1.38

    def __init__(self, length_pool: int, count_pool: int):
        super.__init__(self)
        self.length_pool = length_pool
        self.count_pool = count_pool
    
    def get_mean_speed(self) -> float:
        return ((self.length_pool * self.count_pool) /
               self.M_IN_KM / self.duration)
    
    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.COEF_CALORIES_1) *
               self.COEF_CALORIES_2 * self.weight)


class InfoMessage():
    """Class describe info object."""
    def __innit__(self):
        training_type = self.class_name
        duration = self.duration
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories
    
    @staticmethod
    def printing(self):
        return (f'Тип тренировки: {self.training_type};'
                f'Длительность: {self.duration} ч.;'
                f'Дистанция: {self.distance} км;'
                f'Ср. скорость: {self.speed} км/ч;'
                f'Потрачено ккал: {self.calories}.')


def read_package(workout_type, data):
    if workout_type == 'SWM':
        activity = Swimming(data[0], data[1], data[2], data[3], data[4])
    if workout_type == 'RUN':
        activity = Running(data[0], data[1], data[2])
    if workout_type == 'WLK':
        activity = SportsWalking(data[0], data[1], data[2], data[3])
    return activity

def main(training):
    info = Training.show_training_info(training)
    print(InfoMessage.printing(info))