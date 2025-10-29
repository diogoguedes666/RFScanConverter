import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(
    page_title="RF Scan Converter - monsterDSP",
    page_icon=":level_slider:",
    layout="centered"
)

# Hide Streamlit's default menu and footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Create the redirect page with countdown
redirect_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0a0a0a 100%);
            color: #ffffff;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }
        
        .container {
            text-align: center;
            max-width: 600px;
            width: 100%;
        }
        
        .logo {
            width: 280px;
            max-width: 80%;
            height: auto;
            margin-bottom: 3rem;
            filter: drop-shadow(0 0 20px rgba(168, 85, 247, 0.3));
        }
        
        h1 {
            font-size: 2rem;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #a855f7, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .subtitle {
            font-size: 1.1rem;
            color: #9ca3af;
            margin-bottom: 2.5rem;
            line-height: 1.6;
        }
        
        .countdown-box {
            background: rgba(168, 85, 247, 0.1);
            border: 2px solid rgba(168, 85, 247, 0.3);
        border-radius: 16px;
        padding: 2rem;
            margin-bottom: 2rem;
        }
        
        .countdown-label {
            font-size: 1rem;
            color: #9ca3af;
            margin-bottom: 0.5rem;
        }
        
        .countdown-note {
            font-size: 0.85rem;
            color: #6b7280;
            margin-top: 0.5rem;
            font-style: italic;
        }
        
        #countdown {
            font-size: 4rem;
            font-weight: bold;
            color: #a855f7;
            margin: 1rem 0;
        }
        
        .button {
            display: inline-block;
            background: linear-gradient(135deg, #a855f7, #9333ea);
        color: white;
            padding: 1rem 2.5rem;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
            font-size: 1rem;
        transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(168, 85, 247, 0.3);
        text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(168, 85, 247, 0.4);
        }
        
        .url {
            margin-top: 2rem;
            font-size: 0.9rem;
            color: #6b7280;
        }
        
        .url strong {
            color: #a855f7;
    }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://i.postimg.cc/CK1NXb3j/monster-DSPlogo.png" alt="monsterDSP" class="logo">
        
        <h1>RF Scan Converter</h1>
        <p class="subtitle">We've moved to our official website with enhanced features</p>
        
        <div class="countdown-box">
            <div class="countdown-label">Opening in new tab in</div>
            <div id="countdown">3</div>
            <div class="countdown-note">Will open in a new tab due to browser security</div>
        </div>
        
        <a href="https://www.monsterdsp.com/shop/rfexplorer" class="button" id="visitButton">
            Visit Now
        </a>
        
        <div class="url">
            Opening: <strong>www.monsterdsp.com/shop/rfexplorer</strong>
        </div>
    </div>

    <script>
        let countdown = 3;
        const countdownElement = document.getElementById('countdown');
        const targetUrl = 'https://www.monsterdsp.com/shop/rfexplorer';
        
        const timer = setInterval(function() {
            countdown--;
            
            if (countdown > 0) {
                countdownElement.textContent = countdown;
            } else {
                clearInterval(timer);
                countdownElement.textContent = '→';
                // Open in new tab/window - this works reliably in sandboxed iframes
                window.open(targetUrl, '_blank');
            }
        }, 1000);
        
        // Also open on button click
        document.getElementById('visitButton').addEventListener('click', function(e) {
            e.preventDefault();
            clearInterval(timer);
            window.open(targetUrl, '_blank');
        });
    </script>
</body>
</html>
"""

# Render the HTML component
components.html(redirect_html, height=600, scrolling=False)
