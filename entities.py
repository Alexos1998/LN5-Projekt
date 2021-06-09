class Boss:

    leben = 800
    baseAttack = 15
    

    def __init__(self, type):
        self.type = type

class Normal:

    leben = 400
    baseAttack = 10

    def __init__(self, type):
        self.type = type


class Fighter:

    leben = 1200
    baseAttack = 20

    def __init__(self, type):
        self.type = type