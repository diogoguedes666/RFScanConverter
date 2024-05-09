import streamlit as st
import pandas as pd
import base64
import io

def detect_csv_separator(sample_data):
    """Detect the most likely CSV separator used in the file."""
    if b';' in sample_data and b',' not in sample_data:
        return b';'
    elif b',' in sample_data and b';' not in sample_data:
        return b','
    else:
        return b';'

def convert_csv_content(csv_file):
    """Convert CSV content to the desired format."""
    # Read CSV file as bytes and decode to string
    csv_content = csv_file.read()
    csv_content_str = csv_content.decode('utf-8')
    
    # Determine CSV separator
    csv_separator = detect_csv_separator(csv_content)
    
    # Read CSV using pandas with detected separator
    df = pd.read_csv(io.StringIO(csv_content_str), sep=csv_separator.decode('utf-8'), header=None)
    
    converted_data = []
    
    for index, row in df.iterrows():
        frequency = str(row.iloc[0]).strip()  # Frequency from first column
        value = str(row.iloc[1]).strip() if len(row) > 1 else ''  # Value from second column (if exists)
        
        # Format the frequency and convert to float
        if '.' in frequency:
            # Split frequency into integer and decimal parts
            int_part, dec_part = frequency.split('.')
            # Format frequency with 6 decimal places and convert to float
            formatted_frequency = f"{int_part}.{dec_part[:6].ljust(6, '0')}"
        else:
            # Add .000000 if frequency doesn't have decimal part
            formatted_frequency = f"{frequency}.000000"
        
        # Convert formatted frequency to float and divide by 1000000
        frequency_float = float(formatted_frequency) / 1000000
        
        # Format the frequency to have 3 integer digits and 6 decimal places
        formatted_frequency_output = f"{frequency_float:.6f}"
        
        # Append the formatted line to converted_data
        converted_data.append(f"{formatted_frequency_output}, {value}")
    
    return '\n'.join(converted_data)

# Streamlit UI
st.set_page_config(page_title="TinySA/RF Explorer Converter to Wireless Workbench", page_icon=":level_slider:")

# Custom CSS for background image
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url('data:image/gif;base64,R0lGODlhAQABAIAAAAUEBAAAACwAAAAAAQABAAACAkQBADs=') center center no-repeat;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

image_url = "https://i.postimg.cc/9FTzQjqf/monsterlogo.png"
st.markdown(
    f'<img src="{image_url}" style="display: block; margin-left: auto; margin-right: auto; width: 25%;" />',
    unsafe_allow_html=True
)

st.title("TinySA/RF Explorer to Wireless Workbench Converter")
st.markdown("by [monsterDSP](https://instagram.com/monsterdsp)")
uploaded_files = st.file_uploader("Select Multiple .CSV Files", accept_multiple_files=True, type='csv')

if uploaded_files:
    for uploaded_file in uploaded_files:
        converted_data = convert_csv_content(uploaded_file)
        
        # Downloadable link for converted file
        b64 = base64.b64encode(converted_data.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{uploaded_file.name}_OK.txt">Download {uploaded_file.name}_OK.txt</a>'
        st.markdown(href, unsafe_allow_html=True)
