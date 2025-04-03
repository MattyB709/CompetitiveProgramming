from tqdm import tqdm
prod = 1
for i in tqdm(range(13**14)):
    prod *= 2
    prod %= 13**14
    if prod == 170:
        print(i)
        break