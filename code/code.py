import pandas as pd

data = [['Cloud', 18], ['Python', 22], ['Fondamenti informatica', 27]]
df = pd.DataFrame(data=data, columns=['Esame', 'voto'])
print(df.describe())