import streamlit as st
import joblib 
from Bio.SeqUtils import gc_fraction

# 1. Load the AI Brain from your hard drive
brain = joblib.load("virus_brain.pkl")

st.title("🧬 Viral DNA Sequence Analyzer")
sequence = st.text_input("Paste a raw DNA Sequence here:")

if sequence:
    # 2. Calculate the Math Clue
    gc = gc_fraction(sequence) * 100
    
    # 3. Force the Brain to take the Exam! (Double brackets required)
    answer = brain.predict([[gc]])
    
    # 4. Print out the Official Diagnosis
    if answer[0] == 0:
        st.error(f"⚠️ Diagnosis: VIRUS 0 DETECTED! (GC = {gc:.2f}%)")
    else:
        st.success(f"✅ Diagnosis: VIRUS 1 DETECTED! (GC = {gc:.2f}%)")
