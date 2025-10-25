import streamlit as st
import pandas as pd
import base64
import io
import zipfile
from io import BytesIO
import os
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from supabase import create_client

# Supabase setup
supabase_url = st.secrets["SUPABASE_URL"]
supabase_key = st.secrets["SUPABASE_KEY"]
supabase = create_client(supabase_url, supabase_key)

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="TinySA/RF Explorer Converter to Wireless Workbench", page_icon=":level_slider:")

# Inject custom CSS to match monsterdsp.com dark theme with purple accents
st.markdown(
    """
    <style>
    :root {
        color-scheme: dark;
        --background-color: #000000;
        --background-secondary: #111111;
        --background-tertiary: #1a1a1a;
        --text-color: #ffffff;
        --text-secondary: #9ca3af;
        --text-muted: #6b7280;
        --primary-color: #a855f7;
        --primary-hover: #9333ea;
        --purple-400: #c084fc;
        --purple-500: #a855f7;
        --purple-600: #9333ea;
        --gray-800: #1f2937;
        --gray-900: #111827;
        --border-neutral: #1f2937;
    }
    body {
        background: linear-gradient(to bottom right, var(--background-color), var(--background-secondary), var(--background-color));
        color: var(--text-color);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica", Arial, sans-serif;
        font-size: 14px;
    }

    /* Main container styling */
    .main {
        background: var(--background-color);
        padding-top: 2rem; /* add breathing room so hero isn't cut off */
    }
    .block-container {
        max-width: 900px;
        padding-left: 2rem;
        padding-right: 2rem;
        padding-top: 1rem;
        margin-left: auto;
        margin-right: auto;
    }

    /* Ensure proper spacing after hero section */
    .hero-section + .block-container {
        margin-top: 2rem;
    }

    /* Title and header styling */
    h1, h2, h3 {
        color: var(--text-color);
        background: linear-gradient(to right, var(--primary-color), var(--purple-400), var(--primary-color));
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Button styling */
    .stButton button {
        background: linear-gradient(to right, var(--primary-color), var(--purple-600));
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.3px;
        transition: all 0.3s ease;
        box-shadow: 0 3px 12px rgba(168, 85, 247, 0.2);
    }

    .stButton button:hover {
        background: linear-gradient(to right, var(--primary-hover), var(--purple-500));
        transform: translateY(-1px);
        box-shadow: 0 4px 16px rgba(168, 85, 247, 0.3);
    }

    /* File uploader styling */
    .stFileUploader {
        background: linear-gradient(135deg, var(--background-tertiary) 0%, rgba(26, 26, 26, 0.9) 100%);
        border: 2px dashed rgba(168, 85, 247, 0.4);
        border-radius: 16px;
        padding: 2rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(168, 85, 247, 0.1);
    }

    .stFileUploader:hover {
        border-color: var(--purple-400);
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.05) 0%, rgba(26, 26, 26, 0.95) 100%);
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(168, 85, 247, 0.15);
    }

    .stFileUploader:focus-within {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.2);
    }

    /* Download link styling */
    a[href*="download"] {
        background: linear-gradient(to right, var(--primary-color), var(--purple-600));
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        transition: all 0.3s ease;
        box-shadow: 0 3px 12px rgba(168, 85, 247, 0.2);
        text-transform: uppercase;
        letter-spacing: 0.3px;
        font-size: 0.875rem;
        margin: 0.75rem 0;
    }

    a[href*="download"]:hover {
        background: linear-gradient(to right, var(--primary-hover), var(--purple-500));
        transform: translateY(-1px);
        box-shadow: 0 4px 16px rgba(168, 85, 247, 0.3);
    }

    /* Text styling */
    .stMarkdown {
        color: var(--text-muted);
    }

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: var(--background-secondary);
    }

    /* Input field styling */
    .stTextInput input, .stSelectbox select, .stTextArea textarea {
        background: var(--background-tertiary);
        color: var(--text-color);
        border: 1px solid var(--gray-800);
        border-radius: 8px;
    }

    .stTextInput input:focus, .stSelectbox select:focus, .stTextArea textarea:focus {
        border-color: var(--purple-500);
        box-shadow: 0 0 0 2px rgba(168, 85, 247, 0.2);
    }

    /* Counter text styling */
    .stWrite {
        color: var(--text-secondary);
        font-size: 1.1em;
    }

    /* Hero Section styling */
    .hero-section {
        text-align: center;
        margin: 3rem auto 3rem auto; /* more headroom above */
        padding: 4rem 2rem 4rem 2rem; /* balanced internal spacing with extra top */
        max-width: 1000px;
        position: relative;
        background:
            radial-gradient(circle at 30% 20%, rgba(168, 85, 247, 0.10) 0%, transparent 40%),
            radial-gradient(circle at 70% 80%, rgba(147, 51, 234, 0.07) 0%, transparent 40%),
            linear-gradient(135deg, transparent 0%, rgba(168, 85, 247, 0.03) 25%, transparent 50%, rgba(168, 85, 247, 0.03) 75%, transparent 100%);
        border-radius: 24px; /* rounded on all corners */
        backdrop-filter: blur(10px);
        border: 1px solid rgba(168, 85, 247, 0.15); /* include top border */
        overflow: visible; /* avoid cutting off logo glow at the top */
    }

    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background:
            linear-gradient(45deg, transparent 0%, rgba(168, 85, 247, 0.02) 25%, transparent 50%, rgba(168, 85, 247, 0.02) 75%, transparent 100%),
            radial-gradient(circle at center top, rgba(168, 85, 247, 0.05) 0%, transparent 60%);
        pointer-events: none;
        z-index: 1;
    }

    .hero-logo-container {
        margin: 0 auto 3.25rem auto; /* slightly more breathing room below logo */
        position: relative;
        z-index: 2;
    }

    .hero-logo {
        width: 55%;
        max-width: 550px;
        height: auto;
        filter:
            drop-shadow(0 0 26px rgba(168, 85, 247, 0.45))
            drop-shadow(0 0 52px rgba(168, 85, 247, 0.25))
            brightness(1.03)
            saturate(1.05);
        transition: filter 0.25s ease;
    }

    .hero-logo:hover {
        filter:
            drop-shadow(0 0 32px rgba(168, 85, 247, 0.55))
            drop-shadow(0 0 64px rgba(168, 85, 247, 0.3))
            brightness(1.08)
            saturate(1.1);
    }

    .hero-content {
        position: relative;
        z-index: 2;
        margin-top: 2rem;
    }

    .hero-title {
        background: linear-gradient(135deg, #a855f7 0%, #c084fc 25%, #a855f7 50%, #9333ea 75%, #a855f7 100%);
        background-size: 200% 200%;
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 700;
        line-height: 1.1;
        margin-bottom: 1.5rem;
        letter-spacing: -0.02em;
        animation: titleGradient 8s ease-in-out infinite;
        text-shadow: 0 0 40px rgba(168, 85, 247, 0.3);
    }

    .hero-subtitle {
        color: #d1d5db;
        font-size: 1.25rem;
        font-weight: 400;
        margin-bottom: 2rem;
        letter-spacing: 0.02em;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
        opacity: 0.9;
    }

    .hero-brand {
        color: #9ca3af;
        font-size: 1.1rem;
        font-weight: 500;
        margin: 0;
    }

    .brand-link {
        color: #a855f7;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        text-shadow: 0 0 15px rgba(168, 85, 247, 0.4);
        position: relative;
    }

    .brand-link:hover {
        color: #c084fc;
        text-shadow: 0 0 20px rgba(168, 85, 247, 0.6);
        transform: translateY(-1px);
    }

    .brand-link::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(90deg, #a855f7, #c084fc);
        transition: width 0.3s ease;
    }

    .brand-link:hover::after {
        width: 100%;
    }

    /* Responsive design for hero section */
    @media (max-width: 768px) {
        .hero-section {
            margin: 0;
            padding: 3rem 1rem 4rem 1rem;
            border-radius: 0;
            border-left: none;
            border-right: none;
        }

        .hero-logo {
            width: 70%;
            max-width: 400px;
        }

        .hero-title {
            font-size: 2rem;
            line-height: 1.2;
        }

        .hero-subtitle {
            font-size: 1.1rem;
        }
    }

    /* Keyframes for animations */
    /* logoFloat removed to prevent bouncing */

    @keyframes titleGradient {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    /* Animated background effects */
    body::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background:
            radial-gradient(circle at 20% 50%, rgba(168, 85, 247, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(147, 51, 234, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 40% 80%, rgba(168, 85, 247, 0.15) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
    }

    /* Custom scrollbar for webkit browsers */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: var(--background-secondary);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--purple-500);
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--purple-400);
    }

    /* Selection styling */
    ::selection {
        background: rgba(168, 85, 247, 0.3);
        color: var(--text-color);
    }

    /* Focus styling for accessibility */
    *:focus {
        outline: 2px solid var(--purple-500);
        outline-offset: 2px;
    }

    /* Full width plotly charts */
    .js-plotly-plot {
        width: 100% !important;
        max-width: none !important;
    }

    /* Ensure the chart container takes full width */
    [data-testid="stPlotlyChart"] {
        width: 100% !important;
        max-width: none !important;
    }

    /* Spectrum preview styling */
    .spectrum-container {
        background: linear-gradient(135deg, rgba(26, 26, 26, 0.9) 0%, rgba(31, 41, 55, 0.8) 100%);
        border: 1px solid rgba(168, 85, 247, 0.25);
        border-radius: 20px;
        padding: 2rem;
        margin: 3rem auto 2rem auto;
        width: 100%;
        max-width: 1200px;
        backdrop-filter: blur(15px);
        box-shadow:
            0 20px 40px rgba(0, 0, 0, 0.3),
            0 0 30px rgba(168, 85, 247, 0.1);
        transition: all 0.3s ease;
    }

    .spectrum-container:hover {
        border-color: rgba(168, 85, 247, 0.4);
        box-shadow:
            0 25px 50px rgba(0, 0, 0, 0.4),
            0 0 40px rgba(168, 85, 247, 0.15);
        transform: translateY(-2px);
    }

    .spectrum-header {
        background: linear-gradient(135deg, #a855f7 0%, #c084fc 50%, #a855f7 100%);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
        text-align: center;
        font-size: 1.4rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        text-shadow: 0 0 20px rgba(168, 85, 247, 0.3);
    }

    /* Plotly chart styling */
    .js-plotly-plot .plotly-notifier {
        display: none !important;
    }

    /* Checkbox styling */
    .stCheckbox {
        margin: 0.5rem 0;
    }

    .stCheckbox label {
        color: var(--text-secondary);
        font-size: 0.875rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for tracking if files have been processed
if 'processed_files' not in st.session_state:
    st.session_state.processed_files = False

# Initialize spectrum data storage
if 'spectrum_data' not in st.session_state:
    st.session_state.spectrum_data = {}

if 'active_spectra' not in st.session_state:
    st.session_state.active_spectra = set()

if 'combined_view' not in st.session_state:
    st.session_state.combined_view = True

# Counter handling with Supabase
def get_counter():
    try:
        response = supabase.table('scan_counter').select('counter_value').single().execute()
        if response.data:
            return response.data['counter_value']
        else:
            # Initialize counter in Supabase if it doesn't exist
            supabase.table('scan_counter').insert({'counter_value': 141}).execute()
            return 141
    except Exception as e:
        st.error(f"Error accessing counter: {str(e)}")
        return 141

def increment_counter():
    try:
        current_count = get_counter()
        new_count = current_count + 1
        supabase.table('scan_counter').update({'counter_value': new_count}).eq('id', 1).execute()
        return new_count
    except Exception as e:
        st.error(f"Error incrementing counter: {str(e)}")
        return current_count + 1

# Initialize counter from Supabase
if 'total_count' not in st.session_state:
    st.session_state.total_count = get_counter()

# Function to increment the counter
def increment_file_count():
    st.session_state.total_count = increment_counter()

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
    spectrum_data = {'frequencies': [], 'amplitudes': [], 'filename': csv_file.name}

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

        # Store spectrum data - use original frequency value
        spectrum_data['frequencies'].append(frequency)
        spectrum_data['amplitudes'].append(value)

    return '\n'.join(converted_data), spectrum_data



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

def create_spectrum_plot(spectrum_data_dict, active_files, title="Spectrum Analysis"):
    """Create interactive spectrum plot using Plotly - Combined view only"""

    # Determine the appropriate unit for all spectra
    all_frequencies = []
    for filename in active_files:
        if filename in spectrum_data_dict:
            all_frequencies.extend(spectrum_data_dict[filename]['frequencies'])

    # Set default values
    display_unit = "MHz"
    tickformat = ".2f"

    if len(all_frequencies) > 0:
        max_freq = max(all_frequencies)
        if max_freq >= 1e9:  # GHz range
            display_unit = "GHz"
            tickformat = ".3f"
        elif max_freq >= 1e6:  # MHz range
            display_unit = "MHz"
            tickformat = ".2f"
        else:  # Hz range
            display_unit = "Hz"
            tickformat = ".0f"

    # Combined view - overlay all active spectra
    fig = go.Figure()

    colors = px.colors.qualitative.Set3  # Use a nice color palette

    for i, filename in enumerate(active_files):
        if filename in spectrum_data_dict:
            data = spectrum_data_dict[filename]
            color = colors[i % len(colors)]

            # Convert frequencies based on detected unit
            freq_values = data['frequencies']
            if display_unit == "GHz":
                frequencies_display = [f / 1e9 for f in freq_values]
            elif display_unit == "MHz":
                frequencies_display = [f / 1e6 for f in freq_values]
            else:  # Hz
                frequencies_display = freq_values

            fig.add_trace(go.Scatter(
                x=frequencies_display,
                y=data['amplitudes'],
                mode='lines',
                name=filename,
                line=dict(color=color, width=2),
                hovertemplate=f'<b>{filename}</b><br>Frequency: %{{x:.3f}} {display_unit}<br>Amplitude: %{{y:.3f}}<extra></extra>'
            ))

    fig.update_layout(
        title=title,
        xaxis_title=f"Frequency ({display_unit})",
        yaxis_title="Amplitude",
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        hovermode='closest',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=500,  # Taller for better visibility
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Configure axes for better spectrum display
    fig.update_xaxes(
        tickformat=tickformat,
        tickmode="auto",
        nticks=10,
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)',
        tickfont=dict(size=10)
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)',
        tickfont=dict(size=10)
    )

    return fig


# Streamlit UI setup

image_url = "https://i.postimg.cc/CK1NXb3j/monster-DSPlogo.png"
st.markdown(f'''
<div class="hero-section">
    <div class="hero-logo-container">
        <img src="{image_url}" class="hero-logo" />
    </div>
    <div class="hero-content">
        <h1 class="hero-title">TinySA/RF Explorer to Wireless Workbench Converter</h1>
        <p class="hero-subtitle">Now With Spectrum Preview</p>
        <p class="hero-brand">by <a href="https://www.monsterdsp.com" class="brand-link">monsterDSP</a></p>
    </div>
</div>
''', unsafe_allow_html=True)
uploaded_files = st.file_uploader("Select Multiple .CSV Files", accept_multiple_files=True, type='csv')

if uploaded_files:
    files_dict = {}

    # Process all uploaded files (not just the first time)
    for uploaded_file in uploaded_files:
        # Check if this file has already been processed
        if uploaded_file.name not in st.session_state.spectrum_data:
            # New file - process it
            converted_data, spectrum_data = convert_csv_content(uploaded_file)
            files_dict[uploaded_file.name + '_OK.txt'] = converted_data

            # Store spectrum data
            st.session_state.spectrum_data[uploaded_file.name] = spectrum_data
            st.session_state.active_spectra.add(uploaded_file.name)

            # Mark that files have been processed
            st.session_state.processed_files = True

    # If no files were processed in this iteration, ensure processed_files is still True
    if uploaded_files and not st.session_state.processed_files:
        st.session_state.processed_files = True

    # Always show downloads after files are uploaded

    # Individual file downloads
    for uploaded_file in uploaded_files:
        if uploaded_file.name in st.session_state.spectrum_data:
            converted_data = files_dict.get(uploaded_file.name + '_OK.txt', '')
            if converted_data:
                b64 = base64.b64encode(converted_data.encode()).decode()
                href = f'''
                <div style="margin: 8px 0; text-align: center;">
                    <a href="data:file/txt;base64,{b64}" download="{uploaded_file.name}_OK.txt" style="
                        background: linear-gradient(to right, #a855f7, #9333ea);
                        color: white;
                        padding: 0.75rem 1.5rem;
                        border-radius: 8px;
                        text-decoration: none;
                        font-weight: 600;
                        display: inline-block;
                        transition: all 0.3s ease;
                        box-shadow: 0 3px 12px rgba(168, 85, 247, 0.2);
                        text-transform: uppercase;
                        letter-spacing: 0.3px;
                        font-size: 0.875rem;
                    " onmouseover="this.style.background='linear-gradient(to right, #9333ea, #a855f7)'; this.style.transform='translateY(-1px)'; this.style.boxShadow='0 4px 16px rgba(168, 85, 247, 0.3)'" onmouseout="this.style.background='linear-gradient(to right, #a855f7, #9333ea)'; this.style.transform='translateY(0)'; this.style.boxShadow='0 3px 12px rgba(168, 85, 247, 0.2)'">
                        📁 Download {uploaded_file.name}_OK.txt
                    </a>
                </div>
                '''
                st.markdown(href, unsafe_allow_html=True)

    # ZIP download
    if len(files_dict) > 1:
        zip_buffer = create_zip(files_dict)
        b64_zip = base64.b64encode(zip_buffer.read()).decode()
        href_zip = f'''
        <div style="margin: 1rem 0; text-align: center;">
            <a href="data:application/zip;base64,{b64_zip}" download="RFScanConverter_Files.zip" style="text-decoration: none;">
                <button style="
                    background: linear-gradient(to right, #a855f7, #9333ea);
                    color: white;
                    border: none;
                    padding: 1rem 2rem;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 1rem;
                    font-weight: 600;
                    text-transform: uppercase;
                    letter-spacing: 0.3px;
                    cursor: pointer;
                    border-radius: 12px;
                    transition: all 0.3s ease;
                    box-shadow: 0 3px 12px rgba(168, 85, 247, 0.2);
                " onmouseover="this.style.background='linear-gradient(to right, #9333ea, #a855f7)'; this.style.transform='translateY(-1px)'; this.style.boxShadow='0 4px 16px rgba(168, 85, 247, 0.3)'" onmouseout="this.style.background='linear-gradient(to right, #a855f7, #9333ea)'; this.style.transform='translateY(0)'; this.style.boxShadow='0 3px 12px rgba(168, 85, 247, 0.2)'">📦 Download All Files as ZIP</button>
            </a>
        </div>
        '''
        st.markdown(href_zip, unsafe_allow_html=True)

    # Spectrum Preview Section - Centered
    if len(st.session_state.spectrum_data) > 0:
        # Use a unique key for the entire spectrum section to force refresh when new files are added
        spectrum_section_key = f"spectrum_section_{len(st.session_state.spectrum_data)}"
        st.markdown(f'<div class="spectrum-container" key="{spectrum_section_key}"><h3 class="spectrum-header">📊 Spectrum Preview</h3>', unsafe_allow_html=True)

        # Spectrum selection controls
        if len(st.session_state.spectrum_data) > 1:
            st.markdown('<div style="padding: 0.5rem 0 1rem 0; color: #9ca3af; font-size: 0.875rem;">Select spectra to display (uncheck to hide specific spectra):</div>', unsafe_allow_html=True)

            # Create checkboxes for each spectrum - all start checked
            for filename in st.session_state.spectrum_data.keys():
                # Ensure all spectra start as active by default
                if filename not in st.session_state.active_spectra:
                    st.session_state.active_spectra.add(filename)

                is_active = filename in st.session_state.active_spectra
                if st.checkbox(filename, value=is_active, key=f"active_{filename}"):
                    st.session_state.active_spectra.add(filename)
                else:
                    st.session_state.active_spectra.discard(filename)

        # Force spectrum plot to refresh when data changes
        spectrum_key = f"spectrum_{len(st.session_state.spectrum_data)}_{len(st.session_state.active_spectra)}_{list(st.session_state.spectrum_data.keys())}"

        # Create and display the plot
        if len(st.session_state.active_spectra) > 0:
            fig = create_spectrum_plot(
                st.session_state.spectrum_data,
                list(st.session_state.active_spectra),
                title="Spectrum Analysis"
            )

            if fig is not None:
                st.plotly_chart(fig, use_container_width=True, config={
                    'displayModeBar': True,
                    'displaylogo': False,
                    'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
                    'responsive': True
                }, key=spectrum_key)

        st.markdown(f'</div>', unsafe_allow_html=True)

# Display total count using session state
st.markdown(f'<div style="text-align: center; margin-top: 2rem; padding: 0.75rem; background: rgba(17, 24, 39, 0.5); border-radius: 12px; border: 1px solid #1f2937; border-left: 4px solid #a855f7;"><p style="color: #9ca3af; font-size: 0.875rem; margin: 0;"><span style="color: #a855f7; font-weight: 600;">Total files processed by users:</span> <span style="color: #ffffff; font-weight: bold; font-size: 1.125rem;">{st.session_state.total_count}</span></p></div>', unsafe_allow_html=True)


