import numpy as np
import matplotlib.pyplot as plt

# 1. Timeline
t = np.linspace(3590,3610,5000)

# 2. Delta wave
delta_wave = 3 * np.sin(2 * np.pi * 1.2 * t)

# 3. Peak position
spike_loc_low = 3595 #low-risk location
spike_loc_high = 3605 #high-risk location

# 4.generate Sword peak
spike_low = 2 * np.exp(-((t - spike_loc_low)**2) / (2 * 0.05**2))
spike_high = 12 * np.exp(-((t - spike_loc_high)**2) / (2 * 0.05**2))

# 5. Noise
noise = np.random.normal(0, 0.4, 5000)

# 6. Be composed of (only once)
eeg_combined = delta_wave + spike_low + spike_high + noise

# 7. Plotting
plt.figure(figsize=(12,5))
plt.plot(t, eeg_combined, color='darked', label='EEG Signal')
plt.axvline(3600, color='blue', linestyle='--', label='3600s Threshould')
plt.axvspan(3600, 3610, color='red', alpha=0.1, label='High Risk')
plt.legend()
plt.title('Sleepwalking Arousal Probability Shift at 3600s')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude (µV)')
plt.legend()
plt.grid(True, alpha=0.2)
plt.show()
