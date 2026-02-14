import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

print("=" * 50)
print("Intelligent Sleep Analysis System V2.0")
print("=" * 50)

name = input("Please enter your name: ")
rem_hours = 2.0
deep_hours = 2.0
age = int(input("Please enter age: "))
deep_score = 0
REM_score = 0
sleeping_time_score = 0
number_wake_up = 0
sleeping_eff = 0.0
scores = 0
print("\n" + name + ",starting analysing you sleep...")

hours= 8

if age < 18:
  deep_target=2.5
  rem_target=2.0
elif age < 40:
  deep_target=2.0
  rem_target=1.8
else:
  deep_target=1.2
  rem_target=1.5
  
light_hours = 8 - deep_hours - rem_hours - 0.5
wake_hours = 0.5
    
Deep_hours = deep_target + random.uniform(-0.1,1.0)
rem_hours = rem_target + random.uniform(-0.4,0.4)
light_hours = hours - deep_hours - rem_hours - 0.5
wake_hours = 0.5

print("age: " + str(age))
print("deep_target:" + str(deep_target))
print("deep_hours: " + str(deep_hours))
sleep_stages = []
for i in range(hours):
  if i == 0:
    sleep_stages.append('REM')
  elif i < 3:
    sleep_stages.append('N2 sleeping')
  elif i < 5:
    sleep_stages.append('N3 deep sleep')
  elif i < 6:
    sleep_stages.append('REM')
  else:
    sleep_stages.append('N2 sleeping')
    
deep_score = min(100, deep_hours * 40)
rem_score = min(100, rem_hours * 40)
sleep_score = 85
wake_score = 90
eff_score = 88

print("deep_score: " + str(int(deep_score)))
print("REM score: " + str(int(REM_score)))
print("sleeping_time_score: " + str(int(sleeping_time_score)))
print("number_wake_up: " + str(int(number_wake_up)))
print("sleeping efficiency: " + str(int(sleeping_eff)))

total_score = (deep_score + rem_score + sleep_score + wake_score + eff_score) / 5
print("/n total_score: " + str(int(total_score)) + "score")


if total_score >=85:
  print("Evaluation: Quality sleep! Continue to maintain")
  print("Suggestion: Maintain the current routine")
elif total_score >= 70:
  print("Evaluation: Average sleep, there is room for improvement")
  print("Suggestion: Stay away from your mobile phone 1 hour before going to bed")
elif total_score >= 50:
  print("Evaluation: Poor sleep quality")
  print("Suggestion: fixed routine time, relax before going to bed")
else:
  print("Evaluation: Severe sleep deprive")
  print("Suggestions: It is recommended to consult a doctor")
  
plt.figure(figsize=(14,10))
plt.subplot(2,2,1)
stage_counts = [
sleep_stages.count("sober"),
sleep_stages.count("N1 sleep"),
sleep_stages.count("N2 shallow sleep"),
sleep_stages.count("N3 deep sleep"),
sleep_stages.count("REM"),
]

plt.pie(stage_counts,
        labels = ['awake','N1','N2','N3','REM'],
        autopct='%1.1f%%')
plt.title('The proportion of sleep stage')

scores = {
  "deep score": int(deep_score),
  "rem score": int(rem_score),
  "sleep score": sleep_score,
  "wake score" : wake_score,
  "efficiency": eff_score
}

# plt.subplot(2,2,2, projection='polar')
#categories = ['deep mode','REM','in sleep','wake up','effieciency']
#values = [deep_score, rem_score, sleep_score, wake_score, eff_score]

#N = len(categories)
#angles = [n / float(N) * 2 * 3.14159 for n in range(N)]

#values.append(values[0])
#values.append(angles[0])

#plt.plot(angles, values, 'o-', linewidth = 2)
#plt.fill(angles, values, alpha = 0.25)
#plt.xticks(angles[:1], categories)
#plt.ylim(0,100)
#plt.title('sleeping quality radar map')
#categories = list(scores.keys())
#values = list(scores.values())
#N=len(categories)
#Angles = [n/float(N) * 2 * np.pi for n in range(N)]
#values += values [:1]
#Angles += angles [:1]

#plt.plot(angles, values, 'o-', linewidth = 2)
#plt.fill(angles, values, alpha = 0.25)
#plt.xticks(angles[:-1],categories, size = 8)
#plt.ylim(0,100)
#plt.title('Sleep Quality Radar Chart')

plt.subplot(2,2,3)
stage_map = {'Sober':0,'N1 sleep':1,'N2 shallow sleep':2,'N3 deep sleep':3,'REM':4}
y = []
for s in sleep_stages:
  if s == "awake":
    y.append(0)
  elif s == "N1 sleep" or s == 'N1':
    y.append(1)
  elif s == "N2 sleep" or s == 'N2':
    y.append(2)
  elif s == "N3 sleep" or s == 'N3':
    y.append(3)
  elif s == "REM":
    y.append(4)
  else:
    y.append(0)

print("y length: " + str(len(y)))
print("The value of y: " + str(y))

y = [1,2,3,4,3,2,4,2]

plt.figure(figsize=(10,6))
print("y length:" + str(len(y)))
print("hours:" + str(hours))

if len(y) != hours:
  print("length incorrect, repair now...")
  while len(y) < hours:
    y.append(2)
  y = y[:hours]
  
plt.plot(range(8), y, 'go-', linewidth = 2, markersize=8)
plt.yticks([1,2,3,4],['N1','N2','N3','REM'])
plt.xlabel('Time (hours)')
plt.ylabel('Sleep Stage')
plt.title(name + 'Sleep Structure')
plt.grid(True)
plt.show()
print("\n Analysis completed! The report has been saved")

print("\n" + "="*50)
print("Pandas data analysis")
print("=" * 50)

sleep_codes = []
for stage in sleep_stages:
  if 'N1' in stage:
    sleep_codes.append(1)
  elif 'N2' in stage:
    sleep_codes.append(2)
  elif 'N3' in stage:
    sleep_codes.append(3)
  elif 'REM' in stage:
    sleep_codes.append(4)
  else:
    sleep_codes.append(0)

print("sleep_codes length: " + str(len(sleep_codes)))
print("sleep_codes: " + str(sleep_codes))

print("\n" + "="*50)
print("pandas data analysis")
print("=" * 50)

sleep_codes = []
for stage in sleep_stages:
  if 'N1' in stage:
    sleep_codes.append(1)
  elif 'N2' in stage:
    sleep_codes.append(2)
  elif 'N3' in stage:
    sleep_codes.append(3)
  elif 'REM' in stage:
    sleep_codes.append(4)
  else:
    sleep_codes.append(0)

print("\n" + "="*50)
print("forced reconstruction of data")
print("=" * 50)

sleep_stages = []
for i in range(8):
  if i == 0:
    sleep_stages.append('REM')
  elif i < 3:
    sleep_stages.append('N2')
  elif i < 5:
    sleep_stages.append('N3')
  elif i < 6:
    sleep_stages.append('REM')
  else:
    sleep_stages.append('N2')
    
hours = 8
print("Rebuilt sleep_stages: ", sleep_stages)
print("length: ",len(sleep_stages))

print("\n" + "="*50)
print("Pandas data analysis")
print("=" * 50)

sleep_codes = []
for stage in sleep_stages:
  if 'N1' in stage or 'asleep' in stage:
    sleep_codes.append(1)
  elif 'N2' in stage or 'shallow sleep' in stage:
    sleep_codes.append(2)
  elif 'N3' in stage or 'deep sleep' in stage:
    sleep_codes.append(3)
  elif 'REM' in stage:
    sleep_codes.append(4)
  else:
    sleep_codes.append(0)
    
print("sleep_stages length:" , len(sleep_stages))
print("sleep_codes length:" , len(sleep_codes))
print("hours:" , hours)

if len(sleep_codes) != hours:
  print("length incorrect, must repair")
  sleep_codes = [2,2,2,2,2,2,2,2]
  
sleep_df = pd.DataFrame({
  'hour':list(range(1, hours+1)),
  'stage':sleep_stages[:hours],
  'code':sleep_codes[:hours]
})

print("\n success")
print(sleep_df)
print("\n each stage appear times: ")
print("\n" + "="*50)
print("pandas data analysis")
print("="*50)

new_stages = []
for s in sleep_stages:
  if 'REM' in s:
    new_stages.append('REM')
  elif ' N3' in s or 'deep sleep' in s or 'deep' in s:
    new_stages.append('N3')
  elif 'N2' in s or "shallow sleep" in 'sleeping' in s:
    new_stages.append('N2')
  elif 'N1' in s or "asleep" in s:
    new_stages.append('N1')
  else:
    new_stages.append('N2')
sleep_stages = new_stages

sleep_codes = []
for stage in sleep_stages:
  if stage == 'N1':
    sleep_codes.append(1)
  elif stage == 'N2':
    sleep_codes.append(2)
  elif stage == 'N3':
    sleep_codes.append(3)
  elif stage == "REM":
    sleep_codes.append(4)
  else:
    sleep_codes.append(0)
    
min_len = min(len(sleep_stages), 8)
df = pd.DataFrame({
  'hour' : list(range(1, min_len+1)),
  'stage': sleep_stages,
  'code': sleep_codes
})

df = pd.DataFrame({
  'hour' : list(range(1,len(sleep_stages)+1)),
  'stage' : sleep_stages,
  'code': sleep_codes
})
print(df)
print(df['stage'].value_counts())

print(df)
print(df['stage'].value_counts())
print("\n data table: ")
print(sleep_df)
print("\n each stage appear time: ")
print(sleep_df.iloc[:, 1].value_counts())

print("\n initial data: ")
print(sleep_df)
print("\n number of occurrences in each stage: ")
print(sleep_df['stage'].value_counts())
print("\n Average code value of each stage:")
print(sleep_df.groupby('stage')['code'].mean())

sleep_df.to_csv('my_sleep_data.csv', index = False)
print("\n The data has been saved to my_sleep_data.csv")

sleep_df.plot(x = 'hour', y = 'code', kind='line',marker = 'o')
plt.title('changes in the sleep stage')
plt.ylabel('stages')
plt.show()
