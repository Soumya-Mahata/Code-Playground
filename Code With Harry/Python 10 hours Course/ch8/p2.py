def C_to_F(x):
    return (x * 9/5) + 32

c = int(input('Enter the amount in degree Celcious: '))
f = C_to_F(c)
print(f'{c}degree Celcious = {round(f, 2)}degree Farenhite')