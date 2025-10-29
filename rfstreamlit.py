import streamlit as st

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="RF Scan Converter - monsterDSP", page_icon=":level_slider:")

# Inject custom CSS to match monsterdsp.com dark theme with purple accents
st.markdown(
    """
    <style>
    :root {
        color-scheme: dark;
        --background-color: #0a0a0a;
        --background-secondary: #1a1a1a;
        --background-tertiary: #2a2a2a;
        --background-card: #1e1e1e;
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
        background: linear-gradient(to bottom right, var(--background-color), var(--background-secondary), var(--background-color)) !important;
        color: var(--text-color) !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica", Arial, sans-serif;
        font-size: 14px;
    }

    /* Force dark theme and override Streamlit light mode */
    html, body, .stApp {
        background: var(--background-color) !important;
        color: var(--text-color) !important;
    }

    /* Override all Streamlit containers */
    .stApp, .main, [data-testid="stApp"], [data-testid="stMain"] {
        background: var(--background-color) !important;
        background-image: none !important;
    }

    /* Override sidebar */
    .sidebar, .sidebar .sidebar-content, [data-testid="stSidebar"] {
        background: var(--background-secondary) !important;
    }

    /* Override all form elements and inputs */
    .stTextInput input, .stSelectbox select, .stTextArea textarea, .stNumberInput input {
        background: var(--background-tertiary) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--gray-800) !important;
    }

    /* Override checkboxes and radio buttons */
    .stCheckbox, .stRadio {
        background: transparent !important;
    }

    .stCheckbox label, .stRadio label {
        color: var(--text-secondary) !important;
    }

    /* Override all buttons */
    .stButton button {
        background: var(--background-tertiary) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--gray-800) !important;
    }

    /* Override tooltips and popovers */
    .stTooltip, [data-testid="tooltip"] {
        background: var(--background-card) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--gray-800) !important;
    }

    /* Override progress bars */
    .stProgress > div > div {
        background: var(--primary-color) !important;
    }

    /* Override tabs */
    .stTabs [data-baseweb="tab"] {
        background: var(--background-tertiary) !important;
        color: var(--text-secondary) !important;
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: var(--background-card) !important;
        color: var(--text-color) !important;
        border-color: var(--primary-color) !important;
    }

    /* Override expanders */
    .streamlit-expander {
        background: var(--background-tertiary) !important;
        border: 1px solid var(--gray-800) !important;
    }

    /* Override alerts and messages */
    .stAlert, .stSuccess, .stInfo, .stWarning, .stError {
        background: var(--background-tertiary) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--gray-800) !important;
    }

    /* Override dataframes and tables */
    .stDataFrame, table {
        background: var(--background-card) !important;
    }

    th, td {
        background: var(--background-card) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--gray-800) !important;
    }

    /* Override metrics */
    .stMetric {
        background: var(--background-tertiary) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--gray-800) !important;
    }

    /* Ultimate dark theme enforcement - override any light backgrounds */
    [style*="background-color: rgb(255"] {
        background-color: var(--background-color) !important;
    }

    [style*="background-color: #fff"] {
        background-color: var(--background-color) !important;
    }

    [style*="background-color: white"] {
        background-color: var(--background-color) !important;
    }

    [style*="background: rgb(255"] {
        background: var(--background-color) !important;
    }

    [style*="background: #fff"] {
        background: var(--background-color) !important;
    }

    [style*="background: white"] {
        background: var(--background-color) !important;
    }

    /* Force dark theme on all elements */
    * {
        color-scheme: dark !important;
    }

    /* Main container styling */
    .main {
        background: var(--background-color) !important;
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
        background: linear-gradient(135deg, var(--background-tertiary) 0%, var(--background-secondary) 100%);
        border: 2px dashed rgba(168, 85, 247, 0.4);
        border-radius: 16px;
        padding: 2rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(168, 85, 247, 0.1);
    }

    .stFileUploader:hover {
        border-color: var(--purple-400);
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.05) 0%, var(--background-secondary) 100%);
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
        background: linear-gradient(135deg, var(--background-tertiary) 0%, var(--background-card) 100%);
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

# Main content - Redirect page
image_url = "https://i.postimg.cc/CK1NXb3j/monster-DSPlogo.png"
st.markdown(f'''
<div class="hero-section">
    <div class="hero-logo-container">
        <img src="{image_url}" class="hero-logo" />
    </div>
    <div class="hero-content">
        <h1 class="hero-title">RF Scan Converter</h1>
        <p class="hero-subtitle">Enhanced Version Now Available</p>
        <p class="hero-brand">by <a href="https://www.monsterdsp.com" class="brand-link">monsterDSP</a></p>
    </div>
</div>
''', unsafe_allow_html=True)

# Redirect message and button
st.markdown("""
<div style="text-align: center; margin: 2rem auto; max-width: 600px;">
    <h2 style="color: var(--text-color); margin-bottom: 1.5rem; font-size: 1.5rem;">
        🚀 We've Moved to Our Official Website
    </h2>
    <p style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.6; margin-bottom: 2rem;">
        We've discontinued our Streamlit version and implemented a more powerful RF Scan Converter
        directly on our official website with enhanced features and better performance.
    </p>

    <!-- Countdown Timer -->
    <div style="text-align: center; margin: 2rem 0; padding: 1.5rem; background: var(--background-tertiary); border-radius: 12px; border: 1px solid var(--gray-800);">
        <p style="color: var(--text-secondary); font-size: 1rem; margin-bottom: 0.5rem;">
            🚀 Opening enhanced RF converter in:
        </p>
        <div id="countdown" style="font-size: 2.5rem; font-weight: bold; color: var(--primary-color); margin: 0.5rem 0;">
            3
        </div>
        <p style="color: var(--text-muted); font-size: 0.85rem; margin-top: 0.5rem;">
            Or click below to go now
        </p>
    </div>

    <div style="margin: 2rem 0;">
        <a href="https://www.monsterdsp.com/shop/rfconverter" target="_blank" style="
            background: linear-gradient(to right, #a855f7, #9333ea);
            color: white;
            padding: 1rem 2rem;
            border-radius: 12px;
            text-decoration: none;
            font-weight: 600;
            display: inline-block;
            transition: all 0.3s ease;
            box-shadow: 0 3px 12px rgba(168, 85, 247, 0.2);
            font-size: 1.1rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        " onmouseover="this.style.background='linear-gradient(to right, #9333ea, #a855f7)'; this.style.transform='translateY(-1px)'; this.style.boxShadow='0 4px 16px rgba(168, 85, 247, 0.3)'" onmouseout="this.style.background='linear-gradient(to right, #a855f7, #9333ea)'; this.style.transform='translateY(0)'; this.style.boxShadow='0 3px 12px rgba(168, 85, 247, 0.2)'">
            🌐 Visit Enhanced RF Converter
        </a>
    </div>
    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 2rem;">
        Opening: <strong style="color: var(--primary-color);">www.monsterdsp.com/shop/rfconverter</strong>
    </p>
</div>
""", unsafe_allow_html=True)

# Auto-redirect with countdown
st.markdown("""
<div id="countdown-script" style="display: none;">
<script>
    let countdown = 3;
    const countdownElement = document.getElementById('countdown');

    const timer = setInterval(function() {
        countdown--;
        if (countdownElement) {
            countdownElement.textContent = countdown;
        }

        if (countdown <= 0) {
            clearInterval(timer);
            // Try to redirect the parent window (works around iframe restrictions)
            try {
                window.top.location.href = 'https://www.monsterdsp.com/shop/rfconverter';
            } catch (e) {
                // Fallback: open in new tab if iframe restrictions prevent redirect
                window.open('https://www.monsterdsp.com/shop/rfconverter', '_blank');
                // Show message that redirect happened in new tab
                if (countdownElement) {
                    countdownElement.textContent = '→';
                    countdownElement.style.fontSize = '3rem';
                }
            }
        }
    }, 1000);
</script>
</div>
""", unsafe_allow_html=True)


