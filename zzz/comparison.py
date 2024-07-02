import pandas as pd

filepath = f"C:/Users/carol/Downloads/manhattan-cleaned - Sheet1.csv"
df = pd.read_csv(filepath)

manhattan = df['Manhattan']
cleaned = df['Cleaned']

schools = []

n = 0

# figure out enumerate for this 
m = 0
while n < 394 and m < 394:
  if manhattan[n] == cleaned[m]:
    schools.append(manhattan[n])
  else:
    m += 1
    continue
  n +=1

print(schools)