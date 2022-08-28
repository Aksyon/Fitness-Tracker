

class Training():
    """Basic class for different sport activities."""
    LEN_STEP = {'SWM': 1.38,
                'RUN': 0.65,
                'WLK': 0.65
    }
    M_IN_KM = 1000
    H_IN_MIN = 60 

    def __init__(self, action: int, duration: float, weight: float):
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self):
        return self.get_distance() / self.duration
    
    def get_spent_calories(self):
        pass
    
    def show_training_info():
        pass


class Running(Training):
    """Class describe methods and parameters for running activity."""
    COEF_CALORIE_1 = 18
    COEF_CALORIE_2 = 20
    
    def get_spent_calories(self):
        return ((self.COEF_CALORIE_1 * self.get_mean_speed() -
                self.COEF_CALORIE_2) * self.weight / self.M_IN_KM *
                self.duration * self.H_IN_MIN)


class SportsWalking(Training):
    """Class describe methods and parameters for walking activity."""
    COEF_CALORIES_1 = 0.035
    COEF_CALORIES_2 = 0.029
    

    def __init__(self, height):
        super().__init__(self)
        self.height = height
    
    def get_spent_calories(self):
        return ((self.COEF_CALORIES_1 * self.weight + (self.get_mean_speed()**2
               // self.height) * self.COEF_CALORIES_2 * self.weight) *
               self.duration * self.H_IN_MIN)


class Swimming(Training):
    """Class describe methods and parameters for swimming activity."""
    COEF_CALORIES_1 = 1.1
    COEF_CALORIES_2 = 2

    def __init__(self, length_pool, count_pool):
        super.__init__(self)
        self.length_pool = length_pool
        self.count_pool = count_pool
    
    def get_mean_speed(self):
        return ((self.length_pool * self.count_pool) /
               self.M_IN_KM / self.duration)
    
    def get_spent_calories(self):
        return ((self.get_mean_speed() + self.COEF_CALORIES_1) *
               self.COEF_CALORIES_2 * self.weight)
