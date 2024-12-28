import streamlit as st
import pandas as pd
import base64
import io
import zipfile
from io import BytesIO
import os

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="TinySA/RF Explorer Converter to Wireless Workbench", page_icon=":level_slider:")

# Inject custom CSS to force light mode
st.markdown(
    """
    <style>
    :root {
        color-scheme: light;
        --background-color: #ffffff;
        --text-color: #000000;
        --primary-color: #ff4b4b;
    }
    body {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    .stButton button {
        background-color: var(--primary-color);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for tracking if files have been processed
if 'processed_files' not in st.session_state:
    st.session_state.processed_files = False

# Counter file handling
COUNTER_FILE = "file_counter.txt"
INIT_FLAG_FILE = "counter_initialized.flag"

def is_counter_initialized():
    return os.path.exists(INIT_FLAG_FILE)

def mark_counter_initialized():
    with open(INIT_FLAG_FILE, "w") as f:
        f.write("initialized")

def read_counter():
    try:
        with open(COUNTER_FILE, "r") as f:
            return int(f.read().strip() or 0)
    except FileNotFoundError:
        if not is_counter_initialized():
            # Only start from 141 if counter has never been initialized
            initial_count = 141
            mark_counter_initialized()
            save_counter(initial_count)
            return initial_count
        else:
            # If counter was initialized before but file is missing, 
            # continue from last known value in session state
            return getattr(st.session_state, 'total_count', 141)

def save_counter(count):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(count))

# Initialize counter from file
if 'total_count' not in st.session_state:
    st.session_state.total_count = read_counter()

# Function to increment the counter
def increment_file_count():
    st.session_state.total_count += 1
    save_counter(st.session_state.total_count)

# CSV processing
def detect_csv_separator(sample_data):
    if b';' in sample_data and b',' not in sample_data:
        return b';'
    elif b',' in sample_data and b';' not in sample_data:
        return b','
    else:
        return b';'

def convert_csv_content(csv_file):
    csv_content = csv_file.read()
    csv_content_str = csv_content.decode('utf-8')
    csv_separator = detect_csv_separator(csv_content)
    
    # Try to read with headers first
    df = pd.read_csv(io.StringIO(csv_content_str), sep=csv_separator.decode('utf-8'))
    
    # If the first row contains 'Frequency' in it, it's a header row
    if 'Frequency' in str(df.columns[0]):
        # Read again with proper header handling
        df = pd.read_csv(io.StringIO(csv_content_str), sep=csv_separator.decode('utf-8'))
    else:
        # No headers, read without them
        df = pd.read_csv(io.StringIO(csv_content_str), sep=csv_separator.decode('utf-8'), header=None)

    converted_data = []
    for index, row in df.iterrows():
        frequency = row.iloc[0]
        if isinstance(frequency, str):
            # Skip header row if it somehow got through
            if 'frequency' in frequency.lower():
                continue
            frequency = float(frequency.replace(',', '.'))  # Convert to float if it's a string
        value = row.iloc[1]
        if isinstance(value, str):
            value = float(value.replace(',', '.'))  # Convert to float if it's a string
        
        formatted_frequency = format_frequency(frequency)
        converted_data.append(f"{formatted_frequency}, {value:.3f}")
    
    return '\n'.join(converted_data)



def format_frequency(frequency):
    # Adjust the frequency to have 3 digits before the decimal point
    while frequency < 100:
        frequency *= 10
    while frequency >= 1000:
        frequency /= 10
    
    # Format to XXX.XXXXXX with exactly 6 digits after the decimal point
    formatted_frequency = f"{frequency:.6f}"
    return formatted_frequency


def create_zip(files_dict):
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zip_file:
        for file_name, content in files_dict.items():
            zip_file.writestr(file_name, content)
    buffer.seek(0)
    return buffer

# Streamlit UI setup

image_url = "https://i.postimg.cc/9FTzQjqf/monsterlogo.png"
st.markdown(f'<img src="{image_url}" style="display: block; margin-left: auto; margin-right: auto; width: 50%;" />', unsafe_allow_html=True)
st.title("TinySA/RF Explorer to Wireless Workbench Converter")
st.markdown("by [monsterDSP](https://instagram.com/monsterdsp)")
uploaded_files = st.file_uploader("Select Multiple .CSV Files", accept_multiple_files=True, type='csv')

if uploaded_files:
    files_dict = {}
    if not st.session_state.processed_files:
        for uploaded_file in uploaded_files:
            converted_data = convert_csv_content(uploaded_file)
            files_dict[uploaded_file.name + '_OK.txt'] = converted_data
            b64 = base64.b64encode(converted_data.encode()).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="{uploaded_file.name}_OK.txt">Download {uploaded_file.name}_OK.txt</a>'
            st.markdown(href, unsafe_allow_html=True)
            increment_file_count()
        st.session_state.processed_files = True

        # Create a ZIP file and provide a download link
        zip_buffer = create_zip(files_dict)
        b64_zip = base64.b64encode(zip_buffer.read()).decode()
        href_zip = f'''
        <a href="data:application/zip;base64,{b64_zip}" download="RFScanConverter_Files.zip" style="text-decoration: none;">
            <button style="
                background-color: #ff4b4b;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: block;
                font-size: 16px;
                margin: 20px auto;  /* Center the button */
                cursor: pointer;
                border-radius: 12px;
            ">Download All Converted Files as .ZIP</button>
        </a>
        '''
        st.markdown(href_zip, unsafe_allow_html=True)

# Display total count using session state
st.write(f"Total files processed by users: {st.session_state.total_count}")


