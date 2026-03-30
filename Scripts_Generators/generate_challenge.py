import pandas as pd
import numpy as np

np.random.seed(42)

# Create 200 synthetic patients
num_patients = 200

glucose = np.random.randint(70, 180, num_patients)
heart_rate = np.random.randint(60, 100, num_patients)
genetic_markers = np.random.randint(0, 20, num_patients)

# Diagnosis logic: If glucose is high AND genetic markers are high, they have the disease (1)
diagnosis = ((glucose > 130) & (genetic_markers > 10)).astype(int)

df = pd.DataFrame({
    'Glucose_Level': glucose,
    'Heart_Rate': heart_rate,
    'Genetic_Marker_Count': genetic_markers,
    'Diagnosed': diagnosis
})

df.to_csv("challenge_data.csv", index=False)
print("challenge_data.csv has been created!")
