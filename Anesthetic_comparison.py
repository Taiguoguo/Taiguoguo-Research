import matplotlib.pyplot as plt
import numpy as np

# Set the timeline(10-second window)
t = np.linspace(0,10,5000)

# Create sub-picture: 5 kinds of anaesthetics + normal sleep
fig, axes = plt.subplots(6, 1, figsize=(14, 12),
sharex = True)
fig.suptitle('EEG Patterns Under Different Anesthetics vs Normal Sleep', frontsize=16)

# 1. Normal Deep Sleep
delta_normal = 3 * np.sin(2 * np.pi * 1.5 * t)
axes[0].plot(t, delta_normal + np.random.normal(0,0.2,5000), color = 'black', linewidth = 0.8)
axes[0].set_ylabel('Normal/nN3 Sleep', frontsize = 10)
axes[0].set_ylim(-5, 5)
axes[0].axhline(0, color = 'gray', linestyle='--', alpha = 0.5)

# 2. Propofol
prop_spindles = 1.5 * np.sin(2 * np.pi * 12 * t) * (np.sin(2 * np.pi * 0.5 * t) > 0)
propofol = 4 * np.sin(2 * np.pi * 1.8 * t) + 
prop_spindles + np.random.normal(0, 0.3, 5000)
axes[1].plot(t, propofol, color='blue', linewidth=0.8)
axes[1].set_ylabel('Propofol\n(Ideal)', frontsize = 10, color='blue')
axes[1].set_ylim(-6,6)
axes[1].axhline(0, color='gray', linestyle='--',alpha = 0.5)

# 3. Ketamine
ketamine = (2 * np.sin(2 * np.pi * 6 * t) + 1.5 * np.sin(2 * np.pi * 35 * t) + np.random.normal(0,0.4,5000))
axes[2].plot(t, ketamine, color='purple', linewidth=0.8)
axes[2].set_ylabel('Ketamine\n(Dissociative)',
frontsize=10, color='purple')
axes[2].set_ylim(-5,5)
axes[2].axhline(0, color='gray', linestyle='--', alpha = 0.5)

# 4.Heptaflurane
sevo = (3 * np.sin(2 * np.pi * 2 * t) + 1.2 * np.sin(2 * np.pi * 10 *t) + np.random.normal(0, 0.25, 5000))
axes[3].plot(t, sevo, color='green', linewidth=0.8)
axes[3].set_ylabel('Sevoflurane\n(Surgical)', frontsize=10, color='green')
axes[3].set_ylim(-5,5)
axes[3].axhline(0, color='gray', linestyle='--', alpha=0.5)

# 5. Detromethomethodin
dex = (1.5 * np.sin(2 * np.pi * 2 * t) + 2.5 * np.sin(2 * np.pi * 14 * t) * (np.sin(2 * np.pi * 0.8 * t) > 0) + np.random.normal(0,0.2,5000))
axes[4].plot(t, dex, color='teal', linewidth=0.8)
axes[4].set_ylabel('Dexmedetomidine\n(Arousable)', frontsize=10, color = 'teal)
axes[4].set_ylim(-5,5)
axes[4].axhline(0, color='gray', linestyle-'--', alpha=0.5)


# 6. Too deep anaesthesia - outbreak suppression
burst_suppression = np.zeros(5000)
for i in range(0,5000,1000):
  if i // 1000 % 2 == 0:
    burst = 5 * np.sin(2 * np.pi * 3 * t[i:i+800]) + np.random.normal(0,0.5, 800)
    burst_suppression[i:i+800] = burst
axes[5].plot(t, burst_suppression, color='red', linewidth=0.8)
axes[5].set_ylabel('Overdose \n(Burst Suppression)', frontsize = 10, color='red')
axes[5].set_ylim(-7,7)
axes[5].axhline(0, color='gray', linestyle='--', alpha=0.5)
axes[5].set_xlabel('Time (second)')

plt.tight_layout()
plt.savefig('anesthetic_egg_comparison.png', dpi=300)
plt,show()
print(" EEG The comparison chart has been generated: anesthetic_egg_comparison.png")
