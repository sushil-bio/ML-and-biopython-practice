import random
import pandas as pd

random.seed(42)

# Amino acid groups with biological meaning
hydrophobic = "AILMFWVP"   # Found more in structural proteins
charged = "DEKRH"          # Found more in enzymes (active sites)
polar = "STNQYC"           # Found more in transport proteins
all_aa = "ACDEFGHIKLMNPQRSTVWY"

def generate_protein(protein_type, length=100):
    """Generate a synthetic protein sequence with biologically realistic bias."""
    seq = []
    for _ in range(length):
        r = random.random()
        if protein_type == "enzyme":
            # Enzymes have more charged residues (active sites)
            if r < 0.45:
                seq.append(random.choice(charged))
            elif r < 0.75:
                seq.append(random.choice(polar))
            else:
                seq.append(random.choice(hydrophobic))
        elif protein_type == "structural":
            # Structural proteins have more hydrophobic residues
            if r < 0.55:
                seq.append(random.choice(hydrophobic))
            elif r < 0.80:
                seq.append(random.choice(polar))
            else:
                seq.append(random.choice(charged))
        elif protein_type == "transport":
            # Transport proteins have balanced composition
            if r < 0.35:
                seq.append(random.choice(polar))
            elif r < 0.65:
                seq.append(random.choice(hydrophobic))
            else:
                seq.append(random.choice(charged))
    return "".join(seq)

# Generate 150 proteins: 50 of each type
data = []
for _ in range(50):
    data.append({"sequence": generate_protein("enzyme"), "type": "enzyme"})
    data.append({"sequence": generate_protein("structural"), "type": "structural"})
    data.append({"sequence": generate_protein("transport"), "type": "transport"})

df = pd.DataFrame(data)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv("protein_sequences.csv", index=False)

print("Protein dataset generated!")
print(f"Shape: {df.shape}")
print(f"Protein types: {df['type'].value_counts().to_dict()}")
print(f"\nExample sequence (first 50 characters):")
print(f"  {df['sequence'].iloc[0][:50]}...")
print(f"  Type: {df['type'].iloc[0]}")
