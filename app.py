import streamlit as st
import joblib
from Bio.SeqUtils import gc_fraction

# Load the AI Brain
brain = joblib.load("virus_brain.pkl")

# Page Config
st.set_page_config(page_title="DNA Analyzer", page_icon="🧬")

# Header
st.title("🧬 Viral DNA Sequence Analyzer")
st.markdown("A Bioinformatics tool that analyzes raw DNA sequences and classifies viral strains using Machine Learning.")
st.divider()

# Input
sequence = st.text_area("Paste a raw DNA Sequence below:", height=150, placeholder="Example: ATGCGCTAGCTAGCT")

if st.button("🔬 Analyze Sequence"):
    if not sequence:
        st.warning("Please paste a DNA sequence first!")
    else:
        # Clean the input
        clean = sequence.upper().strip().replace(" ", "").replace("\n", "")
        
        # Validate: Only allow A, T, G, C
        invalid = set(clean) - {'A', 'T', 'G', 'C'}
        if invalid:
            st.error(f"❌ Invalid characters detected: {invalid}. DNA can only contain A, T, G, C!")
        else:
            gc = gc_fraction(clean) * 100
            answer = brain.predict([[gc]])

            st.divider()
            st.subheader("📊 Results")
            st.metric("GC-Content", f"{gc:.2f}%")

            if answer[0] == 0:
                st.error(f"⚠️ Diagnosis: VIRUS 0 DETECTED (High GC Strain)")
            else:
                st.success(f"✅ Diagnosis: VIRUS 1 DETECTED (Low GC Strain)")

