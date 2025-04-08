import random
import my_module
rand_num = random.randint(1,10)
print(rand_num
      )
rand_num_0_to_1 = random.random() * 6 #up to but not including
print(rand_num_0_to_1
      )
random_float = random.uniform(1,10) #up to and including
print(random_float
      )
# Pause 1 - head or tails printer, "coin flipper"
coin_state = random.randint(0,1)
if coin_state == 1:
    print("Heads")
else:
    print("Tails")
print(my_module.my_favorite_number) #import module.function
# second approach using floating point and comparing to halfway point
coin = random.uniform(0, 1)
if coin <= .5:
    print("Heads")
else:
    print("Tails")
