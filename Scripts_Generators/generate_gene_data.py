import numpy as np
import pandas as pd

np.random.seed(42)

# 100 patients: 50 healthy, 50 cancer
n_patients = 100
n_genes = 20

# Gene names (using real-sounding gene symbols)
gene_names = [
    'TP53', 'BRCA1', 'EGFR', 'MYC', 'KRAS',
    'PTEN', 'RB1', 'APC', 'VEGFA', 'HER2',
    'CDK4', 'MDM2', 'BRAF', 'PIK3CA', 'ATM',
    'NOTCH1', 'FOXP3', 'IL6', 'TNF', 'GAPDH'
]

data = {}

for i, gene in enumerate(gene_names):
    if gene in ['BRCA1', 'TP53', 'EGFR', 'MYC', 'KRAS', 'VEGFA', 'HER2']:
        # These genes are DIFFERENTIALLY EXPRESSED in cancer
        healthy = np.random.normal(loc=5.0, scale=1.0, size=50)
        cancer = np.random.normal(loc=12.0, scale=1.5, size=50)
    else:
        # These genes are NOT different between groups
        healthy = np.random.normal(loc=7.0, scale=1.5, size=50)
        cancer = np.random.normal(loc=7.5, scale=1.5, size=50)
    
    data[gene] = np.concatenate([healthy, cancer])

# Add target: 0 = Healthy, 1 = Cancer
data['diagnosis'] = np.array([0]*50 + [1]*50)

df = pd.DataFrame(data)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # Shuffle
df.to_csv('gene_expression_data.csv', index=False)

print("Gene expression dataset generated!")
print(f"Shape: {df.shape}")
print(f"Patients: {n_patients} (50 Healthy, 50 Cancer)")
print(f"Genes measured: {n_genes}")
print(f"\nDifferentially expressed genes (the ones that CHANGE in cancer):")
print("BRCA1, TP53, EGFR, MYC, KRAS, VEGFA, HER2")
