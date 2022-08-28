

class Training():
    """Basic class for different sport activities."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    MIN_IN_H = 60 

    def __init__(self, action_amount: int, duration: float, weight: float):
        self.action_amount = action_amount
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        return (self.action_amount * self.LEN_STEP / self.M_IN_KM)

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration
    
    def get_spent_calories(self):
        pass
    
    def __str__(self):
        return self.__class__
    
    @staticmethod
    def show_training_info(self):
        info = InfoMessage()
        info.training_type = self.__class__
        info.duration = self.duration
        info.distance = self.get_distance()
        info.speed = self.get_mean_speed()
        info.calories = self.get_spent_calories()
        return info


class Running(Training):
    """Class describe methods and parameters for running activity."""
    COEF_CALORIE_1 = 18
    COEF_CALORIE_2 = 20
    
    def get_spent_calories(self) -> float:
        return ((self.COEF_CALORIE_1 * self.get_mean_speed() -
                self.COEF_CALORIE_2) * self.weight / self.M_IN_KM *
                self.duration * self.MIN_IN_H)


class SportsWalking(Training):
    """Class describe methods and parameters for walking activity."""
    COEF_CALORIES_1 = 0.035
    COEF_CALORIES_2 = 0.029
    
    def __init__(self, action_amount: int, duration: float, weight: float, height: float):
        super().__init__(action_amount, duration, weight)
        self.height = height
    
    def get_spent_calories(self) -> float:
        return ((self.COEF_CALORIES_1 * self.weight + (self.get_mean_speed()**2
               // self.height) * self.COEF_CALORIES_2 * self.weight) *
               self.duration * self.MIN_IN_H)


class Swimming(Training):
    """Class describe methods and parameters for swimming activity."""
    COEF_CALORIES_1 = 1.1
    COEF_CALORIES_2 = 2
    LEN_STEP = 1.38

    def __init__(self, action_amount: int, duration: float, weight: float,
                length_pool: int, count_pool: int):
        super().__init__(action_amount, duration, weight)
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
    MESSAGE = ('Тип тренировки: {activity}; '
               'Длительность: {duration} ч.; '
               'Дистанция: {distance} км; '
               'Ср. скорость: {speed} км/ч; '
               'Потрачено ккал: {calories}.')

    training_type = None
    duration = None
    distance = None
    speed = None
    calories = None

    @staticmethod
    def printing(self):
        return self.MESSAGE.format(
            activity = self.training_type,
            duration = '%.3f' % self.duration,
            distance = '%.3f' % self.distance,
            speed = '%.3f' % self.speed,
            calories = '%.3f' % self.calories
            )

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

if __name__ == '__main__':
    
    packages = [        
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

