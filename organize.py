import os
import shutil
import glob

# Create new folders
folders = ['Data', 'Scripts_Generators', 'Streamlit_App']
for f in folders:
    os.makedirs(f, exist_ok=True)

# Define where everything should go
moves = {
    '*.csv': 'Data',
    '*.fasta': 'Data',
    'generate_*.py': 'Scripts_Generators',
    'build_portfolio.py': 'Scripts_Generators',
    'app.py': 'Streamlit_App',
    'requirements.txt': 'Streamlit_App',
    'virus_brain.pkl': 'Streamlit_App'
}

# Move the files safely
for pattern, folder in moves.items():
    for file in glob.glob(pattern):
        try:
            shutil.move(file, os.path.join(folder, file))
        except Exception:
            pass

# Delete stray broken files
trash = ['m', 'Maths_Under_The_Hood_ipynb', 'DNA_README_TEMPLATE.md', 'TP53_README_TEMPLATE.md']
for file in trash:
    try:
        if os.path.exists(file):
            os.remove(file)
    except Exception:
        pass

print("Folder restructuring complete! Your repository is now organized.")
