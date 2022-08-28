

class Training():
    """Basic class for different sport activities."""
    LEN_STEP = {'SWM': 1.38,
                'RUN': 0.65,
                'WLK': 0.65
    }
    M_IN_KM = 1000

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
    """Class describe methods for running activity."""
    COEF_CALORIE_1 = 18
    COEF_CALORIE_2 = 20
    H_IN_MIN = 60

    def get_spent_calories(self):
        super.get_spent_calories(self)
        return ((self.COEF_CALORIE_1 * self.get_mean_speed() -
                self.COEF_CALORIE_2) * self.weight / self.M_IN_KM *
                self.duration * self.H_IN_MIN)

