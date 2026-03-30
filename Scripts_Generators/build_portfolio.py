import os
import shutil

# Define the base paths
practice_dir = r"C:\Users\mules\Documents\ML and biopython practice"
base_dir = r"C:\Users\mules\Documents"

# The 3 new professional folders
folders = {
    "DNA-Sequence-Analyzer": [
        "DNA_Classifier.ipynb",
        "virus_brain.pkl",
        "virus_dataset.fasta",
        "generate_fasta.py",
        "requirements.txt",
        "app.py"
    ],
    "TP53-Gene-Expression": [
        "Gene_Expression.ipynb",
        "gene_expression_data.csv",
        "generate_gene_data.py"
    ],
    "Blood-Cell-CNN-Diagnosis": [
        ("nn.ipynb", "Blood_Cell_Diagnosis_CNN.ipynb")  # Rename as we copy
    ]
}

print("Starting portfolio cleanup...\n")

for folder, files in folders.items():
    folder_path = os.path.join(base_dir, folder)
    
    # Create the folder
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created: {folder}")
    
    # Copy files
    for file_info in files:
        if isinstance(file_info, tuple):
            src_name, dst_name = file_info
        else:
            src_name = dst_name = file_info
            
        src_path = os.path.join(practice_dir, src_name)
        dst_path = os.path.join(folder_path, dst_name)
        
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"  └─ Copied: {dst_name}")
        else:
            print(f"  └─ [!] File missing: {src_name}")
            
print("\nDone! Your new pristine portfolio folders have been created in your Documents folder.")
