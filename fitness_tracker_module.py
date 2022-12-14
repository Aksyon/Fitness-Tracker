from dataclasses import dataclass


@dataclass
class Training():
    """Basic class for different sport activities."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    MIN_IN_H = 60 

    action_amount: int
    duration: float
    weight: float

    def get_distance(self) -> float:
        return (self.action_amount * self.LEN_STEP / self.M_IN_KM)

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration
    
    def get_spent_calories(self):
        raise NotImplementedError('Subclasses should implement this!')
    
    @staticmethod
    def show_training_info(self):
        return InfoMessage(
            training_type = self.__class__.__name__,
            duration = self.duration,
            distance = self.get_distance(),
            speed = self.get_mean_speed(),
            calories = self.get_spent_calories()
        )


class Running(Training):
    """Class describe methods and parameters for running activity."""
    COEF_CALORIE_1 = 18
    COEF_CALORIE_2 = 20
    
    def get_spent_calories(self) -> float:
        return ((self.COEF_CALORIE_1 * self.get_mean_speed() -
                self.COEF_CALORIE_2) * self.weight / self.M_IN_KM *
                self.duration * self.MIN_IN_H)


@dataclass
class SportsWalking(Training):
    """Class describe methods and parameters for walking activity."""
    COEF_CALORIES_1 = 0.035
    COEF_CALORIES_2 = 0.029
    
    height: float
    
    def get_spent_calories(self) -> float:
        return ((self.COEF_CALORIES_1 * self.weight + (self.get_mean_speed()**2
               // self.height) * self.COEF_CALORIES_2 * self.weight) *
               self.duration * self.MIN_IN_H)


@dataclass
class Swimming(Training):
    """Class describe methods and parameters for swimming activity."""
    COEF_CALORIES_1 = 1.1
    COEF_CALORIES_2 = 2
    LEN_STEP = 1.38

    length_pool: int
    count_pool: int
    
    def get_mean_speed(self) -> float:
        return ((self.length_pool * self.count_pool) /
               self.M_IN_KM / self.duration)
    
    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.COEF_CALORIES_1) *
               self.COEF_CALORIES_2 * self.weight)


@dataclass
class InfoMessage():
    """Class describe info object."""
    MESSAGE = ('?????? ????????????????????: {activity}; '
               '????????????????????????: {duration} ??.; '
               '??????????????????: {distance} ????; '
               '????. ????????????????: {speed} ????/??; '
               '?????????????????? ????????: {calories}.')

    training_type: str = None
    duration: float = None
    distance: float = None
    speed: float = None
    calories: float = None

    @staticmethod
    def printing(self):
        return self.MESSAGE.format(
            activity = self.training_type,
            duration = '%.3f' % self.duration,
            distance = '%.3f' % self.distance,
            speed = '%.3f' % self.speed,
            calories = '%.3f' % self.calories
            )

sports_category = {'SWM' : Swimming,
                   'RUN' : Running,
                   'WLK' : SportsWalking
}

def read_package(workout_type, data):
    """Function for unpackaging the datat from sensors and creating object of
    sports activity classes."""
    try:
        activity = sports_category[workout_type](*data)
    except KeyError:
        raise KeyError(f'???? ?????????? ???? ???????????????????????????? ????????????????????: {workout_type}')
    return activity

def main(training):
    """Function for creating user message with activity parameters. """
    info = Training.show_training_info(training)
    print(InfoMessage.printing(info))

if __name__ == '__main__':
    
    packages = [        
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180])
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

