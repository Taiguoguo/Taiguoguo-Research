# Trinket  版睡眠监测器
import numpy as np
import matplotlib.pyplot as plt
import random

print("=" * 50)
print("Intelligent Sleep Analysis System V2.0")
print("=" * 50)

name = input("Please enter your name: ")
REM_hours = 2.0
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
  Rem_target=1.8
else:
  deep_target=1.2
  Rem_target=1.5
    
Deep_hours = deep_target + random.uniform(-0.5,0.5)
Rem_hours = rem_target + random.uniform(-0.4,0.4)

light_hours = hours - Deep_hours - Rem_hours - 0.5
wake_hours = 0.5

sleep_stages = []
for hour in range(hours):
  if hour < wake_hours:
    state = "sober"
  elif hour < wake_hours + light_hours/3:
    stage = "N1 fall asleep"
  elif hour < wake_hours + light_hours:
    stage = "N2 shallow sleep"
  elif hour < wake_hours + light_hours + Deep_hours:
    stage = "N3 deep sleep"
  else:
    stage = "REM"
    sleep_stages.append(stage)
    
deep_score = min(100, deep_hours * 40)
rem_score = min(100, REM_hours * 40)
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
plt.plot(range(8), y, 'go-', linewidth = 2, markersize=8)
plt.yticks([1,2,3,4],['N1','N2','N3','REM'])
plt.xlabel('Time (hours)')
plt.ylabel('Sleep Stage')
plt.title(name + 'Sleep Structure')
plt.grid(True)
plt.show()
print("\n Analysis completed! The report has been saved")
