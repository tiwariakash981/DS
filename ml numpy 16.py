import numpy as np
import random
print("random.random hamesha 1 ke andar hi value dega",np.random.random(1))

print("3*3 matrix but value lies between 0.0 to 1.0",np.random.random((3,3)))
print("1 se 4 ke beech ek integer value:",np.random.randint(1,4))

print("making 2d array",np.random.randint(1,4,(4,4)))
print("making 2d array",np.random.randint(1,4,(3,4,4)))

print("for generating same value use seed functiom",np.random.seed(10))
print(np.random.randint(1,4,(3,3)))

print("for generating same value",np.random.seed(10))
print(np.random.randint(1,4,(3,3)))

print("using random.rand u will get value between 0.0 to 1.0 only +ve values",np.random.rand(3))
print("gives -ve and +ve value",np.random.randn(3,3))

x=[1,2,3,4]
print("selects from a list ",np.random.choice(x))
print("gives a pemutated list",np.random.permutation(x))
print("gives a shuffled list",np.random.shuffle(x))
