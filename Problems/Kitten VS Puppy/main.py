import numpy as np

lst_1 = []
for i in input().split():
    lst_1.append(int(i))
lst_2 = input().split()
lst_3 = input().split()
lst_1 = np.array(lst_1)
lst_2 = np.array(lst_2)
lst_3 = np.array(lst_3)

# finish the code here, help the Kitten and the Puppy!
for word in np.where(lst_1 >= 0, lst_2, lst_3):
    print(word)
