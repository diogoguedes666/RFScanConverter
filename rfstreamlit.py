import streamlit as st
import time

# Set page configuration
st.set_page_config(
    page_title="Redirecting to monsterDSP...",
    page_icon="🚀",
    layout="centered"
)

# Hide Streamlit's default menu and footer
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

body {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0a0a0a 100%);
    color: white;
}

.stApp {
    background: transparent;
}
</style>
""", unsafe_allow_html=True)

# Create a centered, beautiful redirect page using Streamlit components
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Logo
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0 2rem 0;">
        <img src="https://i.postimg.cc/CK1NXb3j/monster-DSPlogo.png" 
             style="width: 280px; max-width: 100%; filter: drop-shadow(0 0 20px rgba(168, 85, 247, 0.3));">
    </div>
    """, unsafe_allow_html=True)
    
    # Title with gradient
    st.markdown("""
    <h1 style="
        text-align: center;
        font-size: 2rem;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #a855f7, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    ">RF Scan Converter</h1>
    """, unsafe_allow_html=True)
    
    # Subtitle
    st.markdown("""
    <p style="
        text-align: center;
        font-size: 1.1rem;
        color: #9ca3af;
        margin-bottom: 2.5rem;
        line-height: 1.6;
    ">We've moved to our official website with enhanced features</p>
    """, unsafe_allow_html=True)
    
    # Countdown box
    st.markdown("""
    <div style="
        text-align: center;
        background: rgba(168, 85, 247, 0.1);
        border: 2px solid rgba(168, 85, 247, 0.3);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 2rem;
    ">
        <div style="font-size: 1rem; color: #9ca3af; margin-bottom: 0.5rem;">
            Click the button below to continue
        </div>
        <div id="countdown" style="font-size: 4rem; font-weight: bold; color: #a855f7; margin: 1rem 0;">
            3
        </div>
        <div style="font-size: 0.85rem; color: #6b7280; margin-top: 0.5rem; font-style: italic;">
            Auto-redirect will attempt in <span id="countdown-inline">3</span> seconds
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Button using Streamlit's link_button (most reliable)
    st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #a855f7, #9333ea) !important;
        color: white !important;
        padding: 1rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1.1rem;
        border: none;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        animation: pulse 2s infinite;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.4);
        animation: none;
    }
    
    @keyframes pulse {
        0%, 100% {
            box-shadow: 0 4px 15px rgba(168, 85, 247, 0.3);
        }
        50% {
            box-shadow: 0 4px 25px rgba(168, 85, 247, 0.5);
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Use st.link_button for reliable external navigation
    st.link_button("🚀 VISIT ENHANCED RF CONVERTER", "https://www.monsterdsp.com/shop/rfconverter", use_container_width=True)
    
    # URL info
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem; font-size: 0.9rem; color: #6b7280;">
        Redirecting to: <strong style="color: #a855f7;">www.monsterdsp.com/shop/rfconverter</strong>
    </div>
    """, unsafe_allow_html=True)

# Countdown JavaScript
st.markdown("""
<script>
    let countdown = 3;
    const countdownElement = document.getElementById('countdown');
    const countdownInline = document.getElementById('countdown-inline');
    
    if (countdownElement) {
        const timer = setInterval(function() {
            countdown--;
            
            if (countdown > 0) {
                countdownElement.textContent = countdown;
                if (countdownInline) {
                    countdownInline.textContent = countdown;
                }
            } else {
                clearInterval(timer);
                countdownElement.textContent = '→';
                if (countdownInline) {
                    countdownInline.textContent = '0';
                }
                
                // Try to find and click the Streamlit button
                const button = document.querySelector('div.stButton > button');
                if (button) {
                    button.click();
                }
            }
        }, 1000);
    }
</script>
""", unsafe_allow_html=True)
