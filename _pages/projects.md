# Research Project: Music and Sleep Quality

## Overview
This project investigates how acoustic features of music influence sleep architecture and subjective sleep quality.

## Research Questions
1. Which musical features (Tempo, Harmony, Spectral centroid) most strongly correlate with sleep onset latency?
2. Does personalized music selection improve sleep efficiency compared to generic "relaxing" music?
3. How do individual differences in musical preference moderate these effects?

### Methodology


### Phase 1: Music Analysis
- **Tool**: Librosa (Python library for music analysis)
- **Features extracted**
- Temporal: Tempo, rhythm patterns
- Spectral: Mel-frequency cepstral coefficients (MFCCs), spectral contrast
- Tonal: key, harmony complexity

### Phase 2: Experimental Design
- **Participants**: 30 adults with self0-reported mild sleep difficulties
- **Design**: Within-subjects, counterbalanced
- **Conditions**
    1. Personalized music (based on preference)
    2. Standard relaxing music
    3. No music control

### Phase 3: Data Collection
- **Polysomnography**: EEG, EOG, EMG
- **Subjective measures**: Sleep diaries, PSQI questionnaires
- **Physiological**: Heart rate (PPG), actigraphy 

### Phase 4: Analysis Plan
1. **Preprocessing**: Sleep stage scoring (AASM standards)
2. **Primary outcomes**:
  - Sleep efficiency (SE)
  - Wake after sleep onset (WASO)
  - Slow-wave sleep percentage
3. **Statistical models**:
  - Linear mixed effects models
  - Mediation analysis for physiological pathways

## Project Timeline

- **Current Phase**: Literature synthesis and experimental design refinement
- **Next Phase**: Pilot testing and data collection toolkit preparation
- **Mid-term Goal**: Complete data acquisition and peliminary analysis
- **Final Objective**: Formulate comprehensive findings and prepare scholarly dissemination

  ## Technical Stack

  ### Music Analysis
  - **Librosa** (Python): Feature extraction (MFCCs, tempo, spectral contrast)
  - **MIRtoolbox** (MATLAB): Advanced music information retrieval
 
  ### Sleep data processing
  - **YASA** (Python): Automated sleep staging from EEG
  - **MNE-Python**: EEG preprocessing and visualization
  - **ActiGraph software**: Movement analysis
 
  ### Statistical Analysis
  - **R** (lme4, ggplot2): Linear mixed-effects models, visualization
  - **Python** (pandas, scikit-learn): Data processing, machine learning
 
  ### Hardware & Recording
  - Research-grade EEG system (e.g., SOMMOtouch, Embla)
  - PPG sensors for heart rate variability
  - sound-iosolated sleep laboratroy setup
 
    
* This is a dynamic research roadmap, iteratively optimized based on emerging insights and resource availability.*
