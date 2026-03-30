import random
import os

# Generate 200 DNA sequences of two different "Mystery Viruses"
# Virus 0 has a high GC content (more Gs and Cs)
# Virus 1 has a low GC content (more As and Ts)

file_path = os.path.join("c:\\Users\\mules\\Documents\\ML and biopython practice", "virus_dataset.fasta")

with open(file_path, 'w') as f:
    # Virus 0 (High GC)
    for i in range(1, 101):
        seq = "".join(random.choices(['A', 'T', 'G', 'G', 'C', 'C'], k=250))
        f.write(f">Virus_0_strain_{i}\n{seq}\n")
        
    # Virus 1 (Low GC)
    for i in range(1, 101):
        seq = "".join(random.choices(['A', 'A', 'T', 'T', 'G', 'C'], k=250))
        f.write(f">Virus_1_strain_{i}\n{seq}\n")

print(f"Successfully generated {file_path}")
