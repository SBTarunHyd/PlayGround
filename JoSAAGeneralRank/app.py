import streamlit as st
import pandas as pd

st.set_page_config(page_title="JoSAA Lite Cutoff Hub", layout="wide")

st.title("🎯 Lightweight JoSAA Cutoff Explorer")
st.write("Upload any standard JoSAA seat allocation historical archive to search matrix details.")

# File Uploader
uploaded_file = st.file_uploader("1. Choose JoSAA Excel File (.xlsx)", type=["xlsx"])

if uploaded_file:
    # Read the dataset securely
    df = pd.read_excel(uploaded_file)
    
    # Standardize column headers for reliable query access
    df.columns = [c.strip().lower() for c in df.columns]
    
    col_mapping = {}
    for col in df.columns:
        if 'institute' in col: col_mapping[col] = 'Institute'
        elif 'program' in col or 'branch' in col: col_mapping[col] = 'Branch'
        elif 'quota' in col: col_mapping[col] = 'Quota'
        elif 'seat' in col or 'category' in col: col_mapping[col] = 'Seat Type'
        elif 'gender' in col: col_mapping[col] = 'Gender'
        elif 'opening' in col: col_mapping[col] = 'Opening Rank'
        elif 'closing' in col: col_mapping[col] = 'Closing Rank'
        
    df = df.rename(columns=col_mapping)
    
    # Sanitize Rank variables into structural Numbers
    df['Opening Rank'] = pd.to_numeric(df['Opening Rank'].astype(str).str.replace(r'[^0-9]', '', regex=True), errors='coerce')
    df['Closing Rank'] = pd.to_numeric(df['Closing Rank'].astype(str).str.replace(r'[^0-9]', '', regex=True), errors='coerce')

    # Interface Filter Controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        institutes = sorted(df['Institute'].dropna().unique())
        selected_institute = st.selectbox("2. Select Target Institute", institutes)
        
    with col2:
        user_rank = st.number_input("3. Enter JEE Advanced Rank", min_value=1, value=5000, step=1)
        
    with col3:
        categories = sorted(df['Seat Type'].dropna().unique()) if 'Seat Type' in df.columns else []
        selected_category = st.selectbox("Filter Category (Optional)", ["All Categories"] + categories)

    if st.button("Submit & View Branches", type="primary"):
        # Filter down entries to specified queries
        res_df = df[df['Institute'] == selected_institute]
        if selected_category != "All Categories":
            res_df = res_df[res_df['Seat Type'] == selected_category]
            
        st.subheader(f"📊 Displaying available cuts for {selected_institute}")
        
        # Color Formatting: Highlight row if User Rank <= Closing Rank
        def highlight_eligible(row):
            if pd.notna(row['Closing Rank']) and user_rank <= row['Closing Rank']:
                return ['background-color: #d1fae5; color: #065f46'] * len(row) # Light Green
            return [''] * len(row)
            
        display_cols = ['Branch', 'Quota', 'Seat Type', 'Gender', 'Opening Rank', 'Closing Rank']
        valid_cols = [c for c in display_cols if c in res_df.columns]
        
        styled_df = res_df[valid_cols].style.apply(highlight_eligible, axis=1)
        st.dataframe(styled_df, use_container_width=True, height=600)
