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
    df = pd.read_csv(io.StringIO(csv_content_str), sep=csv_separator.decode('utf-8'))
    
    converted_data = []
    
    for index, row in df.iterrows():
        frequency = str(row.iloc[0]).strip()  # Frequency from first column
        value = str(row.iloc[1]).strip() if len(row) > 1 else ''  # Value from second column (if exists)
        
        # Format the frequency
        if '.' in frequency:
            # Split frequency into integer and decimal parts
            int_part, dec_part = frequency.split('.')
            # Take the first 3 characters of the integer part and the first 6 characters of the decimal part
            formatted_frequency = f"{int_part[:3]}.{dec_part[:6].ljust(6, '0')}"
        else:
            formatted_frequency = frequency.ljust(10)  # If no decimal part, left justify
        
        # Append the formatted line to converted_data
        converted_data.append(f"{formatted_frequency}, {value}")
    
    return '\n'.join(converted_data)

# Streamlit UI
st.set_page_config(page_title="TinySA Converter", page_icon=":level_slider:")



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

image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtEoHXxXuvW679Es7DmIESHFnOI3WjkuEK5q6tCKwp-Q&s"
st.markdown(f"![Your Image]({image_url})")

st.title("TinySA to Wireless Workbench Converter")
st.caption("by monsterDSP")

uploaded_files = st.file_uploader("Select Multiple .CSV Files", accept_multiple_files=True, type='csv')

if uploaded_files:
    for uploaded_file in uploaded_files:
        converted_data = convert_csv_content(uploaded_file)
        
        # Downloadable link for converted file
        b64 = base64.b64encode(converted_data.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{uploaded_file.name}_OK.txt">Download {uploaded_file.name}_OK.txt</a>'
        st.markdown(href, unsafe_allow_html=True)
