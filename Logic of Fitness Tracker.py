

class Trainning():
    """Basic class for different sport activities."""
    LEN_STEP = {'SWM': 1.38,
                'RUN': 0.65
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

