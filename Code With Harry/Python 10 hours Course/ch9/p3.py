# for n in range(2, 21):
#     for i in range(1,11):
#         table =f'{n} X {i} = {n * i}\n'
#         with open(f'Table of {n}.txt', 'a') as f:
#             f.write(table)

for n in range(2, 21):
    with open(f'Tables/Table of {n}.txt', 'w') as f:
        for i in range(1, 11):
            table = f'{n} X {i} = {n * i}\n'
            f.write(table)


