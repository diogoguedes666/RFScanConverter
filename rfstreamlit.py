import streamlit as st


 


st.set_page_config(
    page_title="TinySA → Wireless Workbench Converter",
    page_icon=":satellite:",
    layout="wide",
)

 

st.markdown(
    """
    <style>
    :root {
        color-scheme: dark;
    }
    #MainMenu, header {visibility: hidden;}
    footer {visibility: hidden;}
    div[data-testid="stAppViewContainer"] {
        background:
            radial-gradient(circle at 22% 18%, rgba(99, 102, 241, 0.22), transparent 55%),
            radial-gradient(circle at 85% 15%, rgba(251, 191, 36, 0.18), transparent 50%),
            linear-gradient(145deg, #05060F 0%, #0F172A 40%, #020617 100%);
        background-attachment: fixed;
        font-family: "SF Pro Display", "SF Pro Text", "Helvetica Neue", "Segoe UI", sans-serif;
        color: #F8FAFC;
        padding-bottom: 4rem;
    }
    .footer-brand { display:flex; align-items:center; justify-content:center; padding: 2.5rem 0 2.75rem; }
    .footer-brand img { height: 18px; opacity: 0.9; filter: drop-shadow(0 6px 18px rgba(15,23,42,0.55)); }
    .app-logo { display:flex; justify-content:center; margin: -0.5rem 0 4rem; }
    .app-logo img { height: clamp(84px, 12vw, 150px); filter: drop-shadow(0 8px 24px rgba(2,6,23,0.55)); }
    .hero-wrapper {
        padding: 7.5rem 0 3rem;
        display: flex;
        align-items: flex-start;
        justify-content: center;
        gap: 2.6rem;
        flex-wrap: wrap;
        max-width: 1100px;
        margin: 0 auto;
    }
    .hero-copy {
        max-width: 520px;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        border-radius: 999px;
        padding: 0.4rem 1rem;
        background: rgba(148, 163, 255, 0.14);
        border: 1px solid rgba(148, 163, 255, 0.25);
        font-size: 0.95rem;
        letter-spacing: 0.02em;
        text-transform: uppercase;
    }
    .hero-headline {
        font-size: clamp(2.8rem, 3.6vw, 3.6rem);
        font-weight: 700;
        line-height: 1.05;
        margin: 1.75rem 0 1rem;
        color: #FFFFFF; /* máximo contraste */
        letter-spacing: -0.01em;
        text-shadow:
            0 2px 14px rgba(2, 6, 23, 0.55),
            0 0 1px rgba(2, 6, 23, 0.85);
    }
    .hero-copy { position: relative; z-index: 1; }
    .hero-copy::before {
        content: "";
        position: absolute;
        inset: -12px -18px;
        border-radius: 22px;
        background: linear-gradient(180deg, rgba(2,6,23,0.35), rgba(2,6,23,0.15) 60%, transparent 100%);
        filter: blur(8px);
        z-index: -1;
        pointer-events: none;
    }
    .hero-subtext {
        font-size: 1.18rem;
        line-height: 1.7;
        color: rgba(226, 232, 240, 0.88);
    }
    .hero-stats {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 2.5rem;
        margin-top: 3rem;
        margin-bottom: 2rem;
        flex-wrap: wrap;
        max-width: 1100px;
        margin-left: auto;
        margin-right: auto;
    }
    .hero-stats span {
        display: flex;
        flex-direction: column;
        font-size: 0.94rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: rgba(148, 163, 184, 0.92);
    }
    .hero-stats strong {
        font-size: 1.25rem;
        color: #F8FAFC;
        margin-bottom: 0.35rem;
    }
    .hero-card {
        flex: 0 1 420px;
        min-width: 320px;
        max-width: 460px;
        background: rgba(2, 6, 23, 0.55);
        border-radius: 26px;
        padding: 2.75rem;
        border: 1px solid rgba(148, 163, 184, 0.18);
        box-shadow:
            0 40px 120px rgba(15, 23, 42, 0.55),
            inset 0 1px 0 rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(28px);
    }
    .hero-card h3 {
        margin: 0;
        font-size: 1.4rem;
        font-weight: 600;
    }
    .hero-card p {
        margin-top: 1.05rem;
        margin-bottom: 1.7rem;
        color: rgba(203, 213, 225, 0.9);
        font-size: 1.02rem;
        line-height: 1.72;
    }
    .hero-card ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .hero-card li {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.85rem;
        font-size: 0.98rem;
        color: rgba(226, 232, 240, 0.92);
    }
    .hero-card li::before {
        content: "";
        width: 8px;
        height: 8px;
        border-radius: 999px;
        background: linear-gradient(120deg, #60A5FA, #A855F7);
        box-shadow: 0 0 12px rgba(96, 165, 250, 0.8);
    }
    .stButton > button {
        width: auto; /* reduced width */
        font-size: 1.22rem;
        font-weight: 650;
        letter-spacing: 0.08em;
        padding: 1.18rem 2.6rem;
        border-radius: 999px;
        border: none;
        color: #020617;
        background: linear-gradient(135deg, #F8FAFC 5%, #E2E8F0 38%, #C7D2FE 78%, #A855F7 100%);
        box-shadow:
            0 22px 38px rgba(99, 102, 241, 0.32),
            0 0 0 1px rgba(226, 232, 240, 0.32);
        transition: transform 220ms ease, box-shadow 220ms ease, filter 220ms ease;
        text-transform: uppercase;
        animation: glowPulse 3.4s ease-in-out infinite;
    }
    .cta-button {
        display: inline-block;
        font-size: 1.22rem;
        font-weight: 650;
        letter-spacing: 0.08em;
        padding: 1.18rem 2.6rem;
        min-width: 280px;
        border-radius: 999px;
        border: none;
        color: #020617;
        background: linear-gradient(135deg, #F8FAFC 5%, #E2E8F0 38%, #C7D2FE 78%, #A855F7 100%);
        box-shadow:
            0 22px 38px rgba(99, 102, 241, 0.32),
            0 0 0 1px rgba(226, 232, 240, 0.32);
        transition: transform 220ms ease, box-shadow 220ms ease, filter 220ms ease;
        text-transform: uppercase;
        animation: glowPulse 3.4s ease-in-out infinite;
        text-decoration: none;
        text-align: center;
    }
    .cta-button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow:
            0 30px 60px rgba(129, 140, 248, 0.38),
            0 0 0 1px rgba(148, 163, 255, 0.6);
        filter: brightness(1.05);
    }
    .cta-button:active {
        transform: scale(0.993);
        box-shadow:
            0 18px 35px rgba(67, 56, 202, 0.28),
            0 0 0 1px rgba(148, 163, 255, 0.55);
    }
    @keyframes glowPulse {
        0% {
            box-shadow:
                0 20px 36px rgba(99, 102, 241, 0.28),
                0 0 0 1px rgba(226, 232, 240, 0.32);
        }
        50% {
            box-shadow:
                0 32px 56px rgba(165, 180, 252, 0.42),
                0 0 0 1px rgba(196, 181, 253, 0.55);
        }
        100% {
            box-shadow:
                0 20px 36px rgba(99, 102, 241, 0.28),
                0 0 0 1px rgba(226, 232, 240, 0.32);
        }
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow:
            0 30px 60px rgba(129, 140, 248, 0.38),
            0 0 0 1px rgba(148, 163, 255, 0.6);
        filter: brightness(1.05);
    }
    .stButton > button:active {
        transform: scale(0.993);
        box-shadow:
            0 18px 35px rgba(67, 56, 202, 0.28),
            0 0 0 1px rgba(148, 163, 255, 0.55);
    }
    .cta-note {
        margin-top: 0.75rem;
        font-size: 0.96rem;
        letter-spacing: 0.02em;
        color: rgba(165, 180, 252, 0.92);
    }
    .tool-card {
        margin-top: 2rem;
        padding: 0;
        border-radius: 28px;
        background: rgba(15, 23, 42, 0.78);
        border: 1px solid rgba(148, 163, 184, 0.22);
        box-shadow: 0 30px 90px rgba(2, 6, 23, 0.6);
        backdrop-filter: blur(26px);
        overflow: hidden;
    }
    .tool-card-inner {
        padding: 2.8rem 3rem 2.2rem;
    }
    .tool-card-inner h2 {
        font-size: 1.9rem;
        margin-bottom: 0.5rem;
    }
    .tool-card-inner p {
        color: rgba(226, 232, 240, 0.82);
        margin-bottom: 1.8rem;
        font-size: 1.02rem;
    }
    [data-testid="stFileUploader"] > label div {
        font-size: 1.05rem;
        font-weight: 600;
        color: rgba(248, 250, 252, 0.95);
        margin-bottom: 0.8rem;
    }
    [data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"] {
        border-radius: 22px;
        border: 1px dashed rgba(148, 163, 184, 0.35);
        background: rgba(30, 41, 59, 0.7);
        padding: 1.85rem 1.5rem;
        color: rgba(203, 213, 225, 0.88);
    }
    [data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"]:hover {
        border-color: rgba(148, 163, 255, 0.75);
        box-shadow: inset 0 0 0 1px rgba(148, 163, 255, 0.28);
    }
    [data-testid="stFileUploader"] button {
        border-radius: 999px !important;
        font-weight: 600;
    }
    .conversion-lede {
        margin-top: 0.9rem;
        font-size: 0.95rem;
        color: rgba(148, 163, 184, 0.92);
    }
    .conversion-result {
        margin-top: 1.4rem;
        padding: 1.25rem 1.4rem 1.6rem;
        border-radius: 20px;
        background: rgba(30, 41, 59, 0.75);
        border: 1px solid rgba(148, 163, 184, 0.18);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }
    .conversion-result h4 {
        margin: 0 0 0.35rem 0;
        font-size: 1.05rem;
    }
    .conversion-result span {
        font-size: 0.9rem;
        color: rgba(148, 163, 184, 0.9);
    }
    .stDownloadButton > button {
        width: 100%;
        margin-top: 0.95rem;
        border-radius: 999px;
        background: linear-gradient(120deg, #6366F1, #8B5CF6);
        border: none;
        font-weight: 600;
        letter-spacing: 0.04em;
        box-shadow: 0 14px 30px rgba(99, 102, 241, 0.32);
    }
    .stDownloadButton > button:hover {
        filter: brightness(1.05);
    }
    @media (max-width: 900px) {
        .hero-wrapper {
            padding-top: 4rem;
            gap: 2.5rem;
        }
        .hero-card {
            padding: 2.1rem;
        }
        .tool-card-inner {
            padding: 2.2rem 1.8rem 1.8rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="app-logo">
        <img src="https://rfconverterwhitetext.tiiny.site/rfconverterwhitetext.png" alt="RF Converter" />
    </div>
    """,
    unsafe_allow_html=True,
)

cta_columns = st.columns([1, 6, 1], gap="large")
with cta_columns[1]:
    st.markdown(
        '<div style="text-align:center;"><a href="https://www.monsterdsp.com/shop/rfconverter" class="cta-button">OPEN FREE RF TOOL</a></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="cta-note" style="text-align: center;">Acesso 100% gratuito. Use em <b><u><a href="https://www.monsterdsp.com/shop/rfconverter" style="color:inherit;text-decoration:underline;">monsterdsp.com/shop/rfconverter</a></u></b>. Apoie a monsterDSP — compre nossos plugins.</div>',
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="hero-wrapper">
        <div class="hero-copy">
            <div class="hero-badge">
                <span>monsterDSP</span>
                <span style="opacity:0.75;">RF Converter • online e gratuito</span>
            </div>
            <h1 class="hero-headline">Coordenadores de RF ganhando tempo.</h1>
            <p class="hero-subtext">
                Desenvolvemos o RF Converter aqui no Brasil para quem precisa coordenar radiofrequências com
                orçamento apertado. Faça upload do seu scan do TinySA (ou RF Explorer), veja o espectro na hora
                e baixe o arquivo no formato do Wireless Workbench em segundos.
            </p>
        </div>
        <div class="hero-card">
            <h3 style="color: white;">RF Converter: por que você precisa?</h3>
            <p>
                Criado por especialistas do áudio ao vivo, acostumados a horários apertados e turnês longas.
            </p>
            <ul>
                <li>Detecta separadores automaticamente — qualquer formatação é aceita</li>
                <li>Formata os arquivos no padrão do Wireless Workbench</li>
                <li>Pré-visualiza o espectro antes de baixar o `.txt` final</li>
                <li>Faz em segundos o que humanos não fazem em minutos — sobra tempo para um café (ou um baseadinho)</li>
            </ul>
        </div>
    </div>
    <div class="hero-stats">
        <span><strong>CENTENAS</strong>de scans TinySA/RF Explorer processados</span>
        <span><strong>Poucos segundos</strong> para visualizar espectro + exportar</span>
        <span><strong>100%</strong> gratuito — sem login</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer brand logo at the bottom of the page
st.markdown(
    """
    <div class=\"footer-brand\">
        <a href=\"https://www.monsterdsp.com\" target=\"_blank\" rel=\"noopener noreferrer\">
            <img src=\"https://www.monsterdsp.com/monsterDSP_nav_logo.png\" alt=\"monsterDSP\" />
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)