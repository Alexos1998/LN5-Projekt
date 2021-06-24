import random
test = "sadsadsadsadsaasdadad"
test2 = "fgfgfgfgfgfgfgfgff"
test4 = ''.join(random.sample(test,19))
test3= test2[:7] + test4[7:]
print(test3)