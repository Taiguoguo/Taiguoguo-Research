import numpy as np
import matplotlib.pyplot as plt
import random

print("=" * 60)
print("Computational Neuroscience Sleep Simulator V3.0")
print("=" * 60)

name = input("Please enter baseline subject name: ")
age = int(input("Please enter subject age matrix (1-90): "))
total_hours = 8
total_minutes = total_hours * 60  # 480分钟高密度采样/480 minutes of high-density sampling
epoch_intervals = 10              # 每10分钟进行一次脑电状态标记/EEG status is marked every 10 minutes.
total_epochs = total_minutes // epoch_intervals

print(f"\nInitializing stochastic EEG state compilation for {name}...")

# 1. 神经科学动态年龄配平矩阵 (Biological Age Decay Scaling)
if age < 18:
    base_n3 = 2.5
    base_rem = 2.0
    wake_probability = 0.05       # 青少年极少夜间惊醒/Adolescents rarely wake up at night
elif age < 40:
    base_n3 = 1.8
    base_rem = 1.7
    wake_probability = 0.12       # 中青年压力阶段，惊醒概率上升/During periods of high stress in young and middle-aged adults, the probability of waking up in a fright increases.
else:
    # 40岁以上慢波睡眠（N3）发生生理性退化衰减/Slow-wave sleep (N3) physiologically declines in people over 40 years of age.
    base_n3 = max(0.5, 1.5 - (age - 40) * 0.02)
    base_rem = max(0.8, 1.4 - (age - 40) * 0.01)
    wake_probability = 0.28       # 老年群体睡眠片段化（Fragmentation）/Sleep fragmentation in the elderly

# 引入自变量微观噪声对冲/Introducing microscopic noise as an independent variable for hedging
actual_n3_target = max(0.3, base_n3 + random.uniform(-0.3, 0.3))
actual_rem_target = max(0.5, base_rem + random.uniform(-0.2, 0.2))

# 2. 核心马尔可夫动态状态转移引擎 (Stochastic Markov Transition Matrix)
# 状态代码定义/Status code definition：4=Awake, 3=N1, 2=N2, 1=N3(Deep), 0=REM
states = ['Awake', 'N1', 'N2', 'N3', 'REM']
state_codes = [4, 3, 2, 1, 0]

sleep_trajectory = []
current_state = 'Awake' # 初始状态为清醒/The initial state is conscious.

# 使用时间依赖权重，模拟真实的睡眠周期（前半夜深睡多，后半夜REM多)/Using time-dependent weights, it simulates the real sleep cycle (more deep sleep in the first half of the night, more REM sleep in the second half of the night).
for epoch in range(total_epochs):
    current_time_hours = (epoch * epoch_intervals) / 60.0
    
    # 动态调配转移概率空间/Dynamically allocate the transition probability space
    if current_time_hours < 4.0:
        # 前半夜：高概率下沉至 N3深睡/First half of the night: High probability of sinking into N3 deep sleep
        weights = {
            'Awake': [0.4, 0.4, 0.1, 0.0, 0.1],
            'N1':    [0.1, 0.3, 0.5, 0.1, 0.0],
            'N2':    [0.0, 0.1, 0.4, 0.4, 0.1],
            'N3':    [0.0, 0.0, 0.3, 0.7, 0.0],
            'REM':   [0.1, 0.2, 0.5, 0.0, 0.2]
        }
    else:
        # 后半夜：N3概率耗尽，REM和清醒（Awake）概率飙升/Late at night: N3 probability depletes, REM and awakening (Awake) probabilities surge.
        weights = {
            'Awake': [0.5, 0.3, 0.2, 0.0, 0.0],
            'N1':    [0.2, 0.3, 0.3, 0.0, 0.2],
            'N2':    [0.1, 0.2, 0.4, 0.0, 0.3],
            'N3':    [0.0, 0.0, 0.6, 0.4, 0.0],
            'REM':   [0.2, 0.1, 0.4, 0.0, 0.3]
        }
        
    # 年龄变量对状态转移的强制修正（年龄越大，随机跳回Awake的概率越高)/The age variable forces a correction to the state transition (the older the person, the higher the probability of randomly jumping back to Awake).
    p_vector = weights[current_state]
    if random.random() < wake_probability:
        current_state = 'Awake'
    else:
        current_state = np.random.choice(states, p=p_vector)
        
    sleep_trajectory.append(current_state)

# 3. 临床多维品质测算矩阵/Clinical multidimensional quality assessment matrix
n3_epochs = sleep_trajectory.count('N3')
rem_epochs = sleep_trajectory.count('REM')
awake_epochs = sleep_trajectory.count('Awake')

calculated_n3_hours = (n3_epochs * epoch_intervals) / 60.0
calculated_rem_hours = (rem_epochs * epoch_intervals) / 60.0

deep_score = min(100.0, (calculated_n3_hours / actual_n3_target) * 90)
rem_score = min(100.0, (calculated_rem_hours / actual_rem_target) * 90)
wake_count = len([i for i in range(1, len(sleep_trajectory)) if sleep_trajectory[i] == 'Awake' and sleep_trajectory[i-1] != 'Awake'])
efficiency_score = max(40, 100 - (awake_epochs * 2.5) - (wake_count * 3))

print("\n" + "="*30 + " CLINICAL DATA LEDGER " + "="*30)
print(f"Target N3 Duration for Age {age}: {actual_n3_target:.2f} Hours | Simulated: {calculated_n3_hours:.2f} Hours")
print(f"Target REM Duration for Age {age}: {actual_rem_target:.2f} Hours | Simulated: {calculated_rem_hours:.2f} Hours")
print(f"Spontaneous Nocturnal Awakenings: {wake_count} times")
print(f"Calculated Sleep Efficiency Matrix: {efficiency_score:.1f}%")
print("="*82)

# 4. 激活高阶 2x2 多维脑电图表渲染引擎/Activate the advanced 2x2 multidimensional EEG chart rendering engine
plt.figure(figsize=(15, 11))

# 图 1：高阶标准临床睡眠结构图 (Hypnogram Architecture)
plt.subplot(2, 2, 1)
y_numerical = []
for state in sleep_trajectory:
    if state == 'Awake': y_numerical.append(4)
    elif state == 'N1': y_numerical.append(3)
    elif state == 'N2': y_numerical.append(2)
    elif state == 'N3': y_numerical.append(1)
    elif state == 'REM': y_numerical.append(0)

time_axis = np.arange(total_epochs) * epoch_intervals / 60.0
plt.step(time_axis, y_numerical, where='mid', color='#007722', linewidth=2.5, label='EEG Trajectory')
plt.yticks([4, 3, 2, 1, 0], ['Awake', 'N1 Sleep', 'N2 Shallow', 'N3 Deep (Slow-Wave)', 'REM Stage'])
plt.xlabel('Clipped Timeline (Hours)')
plt.ylabel('Neurological State Layer')
plt.title(f"Clinical Hypnogram Architecture - Subject: {name} (Age: {age})")
plt.grid(True, linestyle='--', alpha=0.6)

# 图 2：雷达图 (Multi-Dimensional Quality Metrics)
plt.subplot(2, 2, 2, projection='polar')
categories = ['Deep Mode', 'REM Vector', 'Duration Index', 'Arousal Stability', 'Efficiency']
values = [deep_score, rem_score, 88.0, max(0, 100 - wake_count*10), efficiency_score]
N = len(categories)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
values += values[:1]
angles += angles[:1]

plt.plot(angles, values, 'o-', linewidth=2, color='#7700AA')
plt.fill(angles, values, alpha=0.3, color='#7700AA')
plt.xticks(angles[:-1], categories, size=11)
plt.ylim(0, 100)
plt.title('Dynamic Multi-Variable Quality Vector', y=1.1)

# 图 3：高精密度比例分布饼图/Figure 3: High-precision proportional distribution pie chart
plt.subplot(2, 2, 3)
counts = [sleep_trajectory.count(s) for s in states]
plt.pie(counts, labels=states, autopct='%1.1f%%', 
        colors=['#FF6666', '#66B2FF', '#99FF99', '#FFCC99', '#E0B0FF'],
        startangle=140, wedgeprops={'edgecolor': 'w', 'linewidth': 1})
plt.title('Biological Proportion of Extracted EEG Cycles')

plt.tight_layout()
plt.show()
print("\n[SUCCESS] Matrix compiled. Dynamic neural telemetry report generated safely.")
