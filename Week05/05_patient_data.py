import numpy as np

patient_data = np.array([
[101, 45, 38.5, 100, 92],
[102, 23, 36.8, 75, 98],
[103, 67, 39.1, 110, 89],
[104, 54, 37.0, 80, 96],
[105, 34, 38.0, 95, 93],
[106, 72, 36.5, 70, 97],
], dtype=float)

print("Full Patient Data:\n", patient_data)
ages = patient_data[:, 1]
temps = patient_data[:, 2]
bp = patient_data[:, 3]
oxygen = patient_data[:, 4]

print("\nAverage Age:", ages.mean())
print("Average Temp:", temps.mean())
print("Average Oxygen:", oxygen.mean())
fever = patient_data[patient_data[:, 2] > 38.0]
print("\nFever Patients (Temp > 38):\n", fever)
low_oxygen = patient_data[patient_data[:, 4] < 94]
print("\nLow Oxygen Patients (<94):\n", low_oxygen)
high_bp = patient_data[patient_data[:, 3] > 100]
print("\nHigh BP Patients:\n", high_bp)
normalized_age = (ages - ages.min()) / (ages.max() - ages.min())
print("\nNormalized Age:", normalized_age)