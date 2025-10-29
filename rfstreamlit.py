import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="RF Scan Converter - monsterDSP",
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
    background: #1a1a1a;
    color: white;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.stApp {
    background: transparent;
}

.hero-section {
    text-align: center;
    padding: 4rem 2rem;
    background: rgba(168, 85, 247, 0.05);
    border-radius: 24px;
    border: 1px solid rgba(168, 85, 247, 0.1);
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.feature-description {
    font-size: 1.2rem;
    color: #e5e7eb;
    margin: 1.5rem 0;
    line-height: 1.6;
}

.cta-button {
    background: linear-gradient(135deg, #a855f7, #9333ea) !important;
    color: white !important;
    padding: 1.25rem 2.5rem !important;
    border-radius: 16px !important;
    font-weight: 700 !important;
    font-size: 1.25rem !important;
    border: none !important;
    box-shadow: 0 8px 32px rgba(168, 85, 247, 0.4) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    transition: all 0.3s ease !important;
    cursor: pointer !important;
    display: inline-block !important;
    text-decoration: none !important;
    animation: glow 2s ease-in-out infinite alternate !important;
}

.cta-button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 12px 40px rgba(168, 85, 247, 0.6) !important;
    animation: none !important;
}

@keyframes glow {
    from {
        box-shadow: 0 8px 32px rgba(168, 85, 247, 0.4);
    }
    to {
        box-shadow: 0 8px 32px rgba(168, 85, 247, 0.7);
    }
}

.badge {
    display: inline-block;
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.875rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 1rem;
}

.product-title {
    font-size: 2.5rem;
    font-weight: 800;
    margin: 1rem 0;
    background: linear-gradient(135deg, #a855f7, #c084fc, #e879f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
}

.description {
    font-size: 1.1rem;
    color: #9ca3af;
    margin-bottom: 2rem;
    line-height: 1.6;
}

.footer-text {
    text-align: center;
    margin-top: 3rem;
    font-size: 0.9rem;
    color: #6b7280;
}

.footer-text a {
    color: #a855f7;
    text-decoration: none;
}

.footer-text a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# Main content
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    # Logo
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0 3rem 0;">
        <img src="https://www.monsterdsp.com/images/rfconverter-logo.png"
             style="width: 300px; max-width: 100%; filter: drop-shadow(0 0 30px rgba(168, 85, 247, 0.4));">
    </div>
    """, unsafe_allow_html=True)

    # Hero section
    st.markdown("""
    <div class="hero-section">
        <div class="badge">FREE TOOL</div>
        <h1 class="product-title">RF Scan Converter</h1>
        <p class="feature-description">
            Convert TinySA/RF Explorer scans to Wireless Workbench format
        </p>

    </div>
    """, unsafe_allow_html=True)

    # CTA Button
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <a href="https://www.monsterdsp.com/shop/rfconverter" class="cta-button" target="_blank">
            🚀 OPEN FREE TOOL NOW
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Additional info
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem;">
        <p style="color: #9ca3af; font-size: 1rem; margin-bottom: 0.5rem;">
            ✨ No registration required • Instant access • Professional results
        </p>
        <p style="color: #6b7280; font-size: 0.9rem;">
            Join thousands of audio professionals using monsterDSP tools
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer-text">
        <p>
            Visit <a href="https://www.monsterdsp.com" target="_blank">monsterDSP.com</a> for more professional audio tools
        </p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem;">
            © 2025 monsterDSP. All rights reserved.
        </p>
    </div>
    """, unsafe_allow_html=True)
