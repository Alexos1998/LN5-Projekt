import random 

class Boss:

    leben = 800
    baseAttack = 15
    

    def __init__(self, type):
        self.name = type
Boss1 = Boss("Feuer")
Boss2 = Boss("Erde")
Boss3 = Boss("Blitz")

class Normal:

    leben = 400
    baseAttack = 10

    def __init__(self, type):
        self.name = type
Normal1 = Normal("Feuer")
Normal2 = Normal("Erde")
Normal3 = Normal("Blitz")

class Fighter:

    leben = 1000

def dmgCalc():

    print(f"Der Boss hat {Boss1.leben} Leben, hat einen Base-Schaden von {Boss1.baseAttack} und ist vom Typ {Boss1.name}\n")

    print(f"Das normale Monster hat {Normal1.leben} Leben, hat einen Base-Schaden von {Normal1.baseAttack} und ist vom typ {Normal1.name}")
dmgCalc()





