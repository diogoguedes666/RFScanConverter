import streamlit as st
import pandas as pd
import base64
import io
import sqlite3

# Initialize session state for tracking if files have been processed and total count
if 'processed_files' not in st.session_state:
    st.session_state.processed_files = False
if 'total_count' not in st.session_state:
    st.session_state.total_count = 0

# Database setup
def create_connection():
    conn = sqlite3.connect('file_count.db')
    return conn

def create_table(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS file_count (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                count INTEGER NOT NULL DEFAULT 1
            )
        ''')

def increment_file_count(conn):
    with conn:
        conn.execute('INSERT INTO file_count (count) VALUES (1)')

def total_files_processed(conn):
    with conn:
        result = conn.execute('SELECT SUM(count) FROM file_count').fetchone()
        return result[0] if result[0] else 0

# Load count on start and save to session state
def load_total_count():
    conn = create_connection()
    create_table(conn)
    total_count = total_files_processed(conn)
    conn.close()
    return total_count

if 'total_count' not in st.session_state:
    st.session_state.total_count = load_total_count()

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
    df = pd.read_csv(io.StringIO(csv_content_str), sep=csv_separator.decode('utf-8'), header=None)
    converted_data = []
    for index, row in df.iterrows():
        frequency = float(row.iloc[0])
        formatted_frequency = format_frequency(frequency)
        value = row.iloc[1] if len(row) > 1 else ''
        converted_data.append(f"{formatted_frequency}, {value}")
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

# Streamlit UI setup
st.set_page_config(page_title="TinySA/RF Explorer Converter to Wireless Workbench", page_icon=":level_slider:")

image_url = "https://i.postimg.cc/9FTzQjqf/monsterlogo.png"
st.markdown(f'<img src="{image_url}" style="display: block; margin-left: auto; margin-right: auto; width: 50%;" />', unsafe_allow_html=True)
st.title("TinySA/RF Explorer to Wireless Workbench Converter")
st.markdown("by [monsterDSP](https://instagram.com/monsterdsp)")
uploaded_files = st.file_uploader("Select Multiple .CSV Files", accept_multiple_files=True, type='csv')

conn = create_connection()

if uploaded_files:
    if not st.session_state.processed_files:
        for uploaded_file in uploaded_files:
            converted_data = convert_csv_content(uploaded_file)
            b64 = base64.b64encode(converted_data.encode()).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="{uploaded_file.name}_OK.txt">Download {uploaded_file.name}_OK.txt</a>'
            st.markdown(href, unsafe_allow_html=True)
            increment_file_count(conn)
        st.session_state.processed_files = True

st.session_state.total_count = total_files_processed(conn)
st.write(f"Total files processed by users: {st.session_state.total_count}")
conn.close()
