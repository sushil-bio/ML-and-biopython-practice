import pandas as pd
import random
from Bio.Seq import Seq

random.seed(42)

data = []
for i in range(200):
    length = random.choice([60, 90, 120])
    
    is_pathogenic = random.randint(0, 1)
    if is_pathogenic:
        # Pathogenic samples artificially have more G/C and heavier amino acids
        dna = "".join(random.choices("ATGCCCC", k=length))
    else:
        # Healthy samples are normal
        dna = "".join(random.choices("ATGC", k=length))
    
    # Automatically translate the DNA into actual Protein Sequences
    protein = str(Seq(dna).translate())
    
    data.append({
        "Sample_ID": f"Patient_{i+1}",
        "DNA_Sequence": dna,
        "Protein_Sequence": protein,
        "Is_Pathogenic": is_pathogenic
    })

df = pd.DataFrame(data)
df.to_csv("bio_challenge_data.csv", index=False)
print("bio_challenge_data.csv has been generated!")
