#Final Project
A = 0
B = 0
C = 0
D = 0
x = print("This will be a quiz to determine which Marvel character you are", "To choose your option type the associated letter")
y = print(input("Which color do you prefer?, A: Blue, B: Green, C: Red, D: Yellow: "))
if y == A:
    A + 1
elif y == B:
    B + 1
elif y == C:
    C + 1
elif y == D:
    D + 1
else:
    print("You did not pick one of the four options")
print(x, y)
