import streamlit as st
import pandas as pd

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="OM Fan Hub",
    page_icon="⚽",
    layout="wide",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800;900&family=Barlow:wght@300;400;500;600&display=swap');

:root {
    --bg:        #0d1117;
    --card:      #1a1a2e;
    --card2:     #12122a;
    --blue:      #009BDE;
    --navy:      #1B3A5C;
    --white:     #ffffff;
    --grey:      #c0c0ee;
    --muted:     #7070a0;
    --border:    rgba(0, 155, 222, 0.25);
    --border-hi: rgba(0, 155, 222, 0.7);
    --green:     #00c853;
    --orange:    #ff9100;
    --red:       #f44336;
}

/* ── Reset ── */
html, body, [class*="css"] {
    font-family: 'Barlow', sans-serif;
    background-color: var(--bg) !important;
    color: var(--grey);
}
.stApp { background-color: var(--bg) !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 3rem; max-width: 1200px; }

/* ── Header ── */
.app-header {
    text-align: center;
    padding: 2rem 0 1rem;
}
.app-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 4.5rem;
    font-weight: 900;
    color: var(--white);
    letter-spacing: 0.06em;
    text-transform: uppercase;
    line-height: 1;
    margin: 0;
}
.app-title span { color: var(--blue); }
.app-subtitle {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    color: var(--blue);
    letter-spacing: 0.25em;
    text-transform: uppercase;
    margin-top: 0.4rem;
}
.header-line {
    border: none;
    border-top: 2px solid var(--blue);
    margin: 1.2rem auto 0;
    width: 100%;
    opacity: 0.6;
    box-shadow: 0 0 12px rgba(0,155,222,0.5);
}

/* ── Tabs ── */
[data-testid="stTabs"] [role="tablist"] {
    gap: 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.5rem;
}
[data-testid="stTabs"] [role="tab"] {
    font-family: 'Barlow Condensed', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
    background: transparent !important;
    border: none !important;
    border-bottom: 3px solid transparent !important;
    padding: 0.7rem 1.4rem !important;
    border-radius: 0 !important;
    transition: color 0.2s, border-color 0.2s;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    color: var(--blue) !important;
    border-bottom: 3px solid var(--blue) !important;
    background: transparent !important;
}
[data-testid="stTabs"] [role="tab"]:hover {
    color: var(--white) !important;
}

/* ── Cards ── */
.card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
}
.card.highlight {
    border-color: var(--border-hi);
    box-shadow: 0 0 20px rgba(0,155,222,0.12);
}

/* ── Section labels ── */
.section-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--blue);
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.2rem;
}

/* ── Forms ── */
[data-testid="stForm"] {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
}
[data-testid="stForm"] label {
    font-family: 'Barlow Condensed', sans-serif !important;
    font-size: 0.7rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
}
[data-testid="stSelectbox"] > div > div {
    background: var(--card2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--white) !important;
}
[data-testid="stFormSubmitButton"] button {
    background: var(--blue) !important;
    color: var(--white) !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Barlow Condensed', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    padding: 0.55rem 1.4rem !important;
    width: 100%;
    box-shadow: 0 4px 15px rgba(0,155,222,0.3);
}
[data-testid="stFormSubmitButton"] button:hover {
    box-shadow: 0 4px 25px rgba(0,155,222,0.5) !important;
}

/* ── Transport result card ── */
.transport-card {
    background: var(--card);
    border: 1px solid var(--border-hi);
    border-radius: 12px;
    padding: 1.6rem;
    box-shadow: 0 0 24px rgba(0,155,222,0.15);
}
.transport-mode {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 2.2rem;
    font-weight: 900;
    color: var(--blue);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    line-height: 1;
}
.transport-detail {
    font-size: 0.82rem;
    color: var(--grey);
    margin-top: 0.3rem;
    line-height: 1.6;
}
.transport-stat {
    background: var(--card2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.7rem 1rem;
    text-align: center;
}
.transport-stat-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--muted);
}
.transport-stat-val {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--blue);
    line-height: 1.1;
}

/* ── Crowd badges ── */
.badge {
    display: inline-block;
    padding: 0.2rem 0.7rem;
    border-radius: 99px;
    font-size: 0.68rem;
    font-weight: 700;
    font-family: 'Barlow Condensed', sans-serif;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
.badge-calm  { background: rgba(0,200,83,0.15);  color: #00c853; border: 1px solid rgba(0,200,83,0.4); }
.badge-busy  { background: rgba(255,145,0,0.15); color: #ff9100; border: 1px solid rgba(255,145,0,0.4); }
.badge-full  { background: rgba(244,67,54,0.15); color: #f44336; border: 1px solid rgba(244,67,54,0.4); }

/* ── Bar table ── */
.bar-row {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.7rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
}
.bar-name {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1rem;
    font-weight: 800;
    color: var(--white);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.bar-meta {
    font-size: 0.73rem;
    color: var(--muted);
    margin-top: 0.1rem;
}
.bar-stars { color: var(--blue); font-size: 0.8rem; }
.bar-right { text-align: right; flex-shrink: 0; }

/* ── Filter pills ── */
.stRadio [data-testid="stRadio"] label { color: var(--grey) !important; }
.stRadio > label {
    font-family: 'Barlow Condensed', sans-serif !important;
    font-size: 0.65rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
}

/* ── Scoreboard ── */
.scoreboard {
    background: linear-gradient(135deg, var(--navy) 0%, #0a0a1a 100%);
    border: 1px solid var(--border-hi);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 0 40px rgba(0,155,222,0.15);
    margin-bottom: 1.2rem;
}
.match-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--blue);
    margin-bottom: 1rem;
}
.score-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
}
.team-name {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.8rem;
    font-weight: 900;
    color: var(--white);
    letter-spacing: 0.05em;
    text-transform: uppercase;
    width: 180px;
}
.team-name.right { text-align: left; }
.team-name.left  { text-align: right; }
.score-box {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 4.5rem;
    font-weight: 900;
    color: var(--blue);
    letter-spacing: 0.05em;
    line-height: 1;
    text-shadow: 0 0 30px rgba(0,155,222,0.5);
}
.score-sep { color: var(--muted); font-size: 3rem; font-weight: 300; }
.match-minute {
    display: inline-block;
    background: rgba(0,155,222,0.15);
    border: 1px solid var(--blue);
    border-radius: 99px;
    padding: 0.25rem 0.9rem;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--blue);
    letter-spacing: 0.1em;
    margin-top: 0.8rem;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(0,155,222,0.4); }
    50%       { box-shadow: 0 0 0 6px rgba(0,155,222,0); }
}

/* ── Stat bars ── */
.stat-bar-wrap { margin-bottom: 1rem; }
.stat-bar-label {
    display: flex;
    justify-content: space-between;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.35rem;
}
.stat-bar-track {
    background: var(--card2);
    border-radius: 99px;
    height: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
}
.stat-bar-fill {
    height: 100%;
    border-radius: 99px;
}

/* ── Donut chart (CSS-only) ── */
.donut-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 0.8rem;
}
.donut {
    width: 130px;
    height: 130px;
    border-radius: 50%;
    background: conic-gradient(var(--blue) 0% 58%, #2a2a50 58% 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}
.donut::after {
    content: '';
    position: absolute;
    width: 80px;
    height: 80px;
    background: var(--card);
    border-radius: 50%;
}
.donut-label {
    position: absolute;
    z-index: 1;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.3rem;
    font-weight: 900;
    color: var(--blue);
}
.donut-legend {
    display: flex;
    gap: 1rem;
    font-size: 0.72rem;
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
.legend-dot {
    display: inline-block;
    width: 8px; height: 8px;
    border-radius: 50%;
    margin-right: 0.35rem;
    vertical-align: middle;
}

/* ── AI Card ── */
.ai-card {
    background: linear-gradient(135deg, rgba(0,155,222,0.08) 0%, var(--card2) 100%);
    border: 1px solid var(--border-hi);
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
    position: relative;
    overflow: hidden;
}
.ai-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: var(--blue);
    box-shadow: 0 0 15px rgba(0,155,222,0.6);
}
.ai-tag {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.6rem;
    font-weight: 800;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--blue);
    margin-bottom: 0.5rem;
}
.ai-text {
    font-size: 0.9rem;
    color: var(--grey);
    line-height: 1.65;
}
.ai-text strong { color: var(--white); }

/* ── Metrics ── */
.metric-grid { display: flex; gap: 0.8rem; flex-wrap: wrap; }
.metric-cell {
    background: var(--card2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.9rem 1.2rem;
    flex: 1;
    min-width: 110px;
    text-align: center;
}
.metric-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 0.58rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.3rem;
}
.metric-val {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.6rem;
    font-weight: 900;
    color: var(--blue);
    line-height: 1;
}
.metric-sub { font-size: 0.68rem; color: var(--muted); margin-top: 0.15rem; }

/* ── Selectbox / radio overrides ── */
div[data-testid="stSelectbox"] label,
div[data-testid="stRadio"] label {
    color: var(--grey) !important;
}
div[data-testid="stRadio"] > label {
    font-family: 'Barlow Condensed', sans-serif !important;
    font-size: 0.65rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
}

/* ── Divider ── */
.blue-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.2rem 0;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <div class="app-title">OM <span>Fan</span> Hub</div>
    <div class="app-subtitle">One City &nbsp;·&nbsp; One Club &nbsp;·&nbsp; One App</div>
    <hr class="header-line">
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────

# Transport logic
TRANSPORT_DATA = {
    # (neighborhood, sector): (mode, line, duration, crowd)
    ("Noailles",         "Virage Sud"):            ("🚇 Metro", "Ligne 2 → Rond-Point du Prado", "12 min", "High"),
    ("Noailles",         "Virage Nord"):            ("🚇 Metro", "Ligne 2 → Rond-Point du Prado", "13 min", "High"),
    ("Noailles",         "Tribune Jean Bouin"):     ("🚇 Metro", "Ligne 2 → Rond-Point du Prado", "14 min", "High"),
    ("Noailles",         "Tribune Ganay"):          ("🚇 Metro", "Ligne 2 → Rond-Point du Prado", "14 min", "High"),
    ("Castellane",       "Virage Sud"):             ("🚇 Metro", "Ligne 1 → Castellane → Prado", "8 min",  "Medium"),
    ("Castellane",       "Virage Nord"):            ("🚌 Bus",   "Bus 21 direction Bonneveine",   "11 min", "Medium"),
    ("Castellane",       "Tribune Jean Bouin"):     ("🚌 Bus",   "Bus 21 direction Bonneveine",   "10 min", "Low"),
    ("Castellane",       "Tribune Ganay"):          ("🚇 Metro", "Ligne 1 → Castellane → Prado", "9 min",  "Medium"),
    ("Vieux-Port",       "Virage Sud"):             ("🚇 Metro", "Ligne 1 → Vieux-Port → Prado", "18 min", "Medium"),
    ("Vieux-Port",       "Virage Nord"):            ("🚌 Bus",   "Bus 83 direction Bonneveine",   "22 min", "Low"),
    ("Vieux-Port",       "Tribune Jean Bouin"):     ("🚌 Bus",   "Bus 83 direction Bonneveine",   "20 min", "Low"),
    ("Vieux-Port",       "Tribune Ganay"):          ("🚇 Metro", "Ligne 1 → Vieux-Port → Prado", "19 min", "Medium"),
    ("Baille",           "Virage Sud"):             ("🚶 Walk",  "Rue Paradis → Av. du Prado",   "18 min", "Low"),
    ("Baille",           "Virage Nord"):            ("🚶 Walk",  "Rue Breteuil → Bd Michelet",   "22 min", "Low"),
    ("Baille",           "Tribune Jean Bouin"):     ("🚶 Walk",  "Rue Breteuil → Bd Michelet",   "20 min", "Low"),
    ("Baille",           "Tribune Ganay"):          ("🚶 Walk",  "Av. du Prado direct",          "16 min", "Low"),
    ("La Plaine",        "Virage Sud"):             ("🚌 Bus",   "Bus 74 → Rond-Point du Prado", "25 min", "Medium"),
    ("La Plaine",        "Virage Nord"):            ("🚌 Bus",   "Bus 74 → Rond-Point du Prado", "27 min", "Low"),
    ("La Plaine",        "Tribune Jean Bouin"):     ("🚌 Bus",   "Bus 74 → Rond-Point du Prado", "26 min", "Low"),
    ("La Plaine",        "Tribune Ganay"):          ("🚌 Bus",   "Bus 74 → Rond-Point du Prado", "25 min", "Medium"),
    ("Saint-Charles",    "Virage Sud"):             ("🚇 Metro", "Ligne 1 → Castellane → Prado", "22 min", "High"),
    ("Saint-Charles",    "Virage Nord"):            ("🚇 Metro", "Ligne 1 → Castellane → Prado", "23 min", "High"),
    ("Saint-Charles",    "Tribune Jean Bouin"):     ("🚇 Metro", "Ligne 1 → Castellane → Prado", "24 min", "High"),
    ("Saint-Charles",    "Tribune Ganay"):          ("🚇 Metro", "Ligne 1 → Castellane → Prado", "22 min", "High"),
    ("Cours Julien",     "Virage Sud"):             ("🚌 Bus",   "Bus 21 → Bd Michelet",         "15 min", "Medium"),
    ("Cours Julien",     "Virage Nord"):            ("🚌 Bus",   "Bus 21 → Bd Michelet",         "16 min", "Medium"),
    ("Cours Julien",     "Tribune Jean Bouin"):     ("🚶 Walk",  "Rue d'Aubagne → Av. du Prado", "19 min", "Low"),
    ("Cours Julien",     "Tribune Ganay"):          ("🚌 Bus",   "Bus 21 → Bd Michelet",         "15 min", "Medium"),
}

NEIGHBORHOODS = ["Noailles", "Castellane", "Vieux-Port", "Baille", "La Plaine", "Saint-Charles", "Cours Julien"]
SECTORS       = ["Virage Sud", "Virage Nord", "Tribune Jean Bouin", "Tribune Ganay"]

# Bar data
BARS = pd.DataFrame([
    {"Bar": "Le Droit au But",     "Quartier": "Castellane",   "Distance": "350m", "Ambiance": 5, "Crowd": "Full"},
    {"Bar": "Bar des Supporters",  "Quartier": "Vieux-Port",   "Distance": "1.2km","Ambiance": 4, "Crowd": "Busy"},
    {"Bar": "L'Avant-Match",       "Quartier": "Baille",       "Distance": "600m", "Ambiance": 4, "Crowd": "Calm"},
    {"Bar": "Le Virage Bleu",      "Quartier": "Noailles",     "Distance": "900m", "Ambiance": 3, "Crowd": "Busy"},
    {"Bar": "Le Treizième Homme",  "Quartier": "La Plaine",    "Distance": "1.5km","Ambiance": 5, "Crowd": "Calm"},
])

# ─────────────────────────────────────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "🚇  Smart Transport",
    "🍺  Bar Finder",
    "📊  Live Match Stats",
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — SMART TRANSPORT
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown('<div class="section-label">Itinerary Planner</div>', unsafe_allow_html=True)

    left, right = st.columns([1, 1.4], gap="large")

    with left:
        with st.form("transport_form"):
            neighborhood = st.selectbox("📍 Your Neighborhood", NEIGHBORHOODS)
            sector       = st.selectbox("🏟️ Stadium Sector",    SECTORS)
            submitted    = st.form_submit_button("Get My Route →", use_container_width=True)

    with right:
        if submitted or True:  # show default on load
            key = (neighborhood if submitted else "Noailles",
                   sector       if submitted else "Virage Sud")
            rec = TRANSPORT_DATA.get(key, ("🚇 Metro", "Ligne 2 → Prado", "15 min", "Medium"))
            mode, line, duration, crowd = rec

            crowd_badge = {
                "Low":    '<span class="badge badge-calm">🟢 Low Crowd</span>',
                "Medium": '<span class="badge badge-busy">🟠 Medium Crowd</span>',
                "High":   '<span class="badge badge-full">🔴 High Crowd</span>',
            }.get(crowd, "")

            crowd_tip = {
                "Low":    "Comfortable journey — you'll have room to breathe.",
                "Medium": "Expect some queuing. Give yourself extra time.",
                "High":   "Very busy! Leave at least 30 min early.",
            }.get(crowd, "")

            st.markdown(f"""
            <div class="transport-card">
                <div class="transport-mode">{mode}</div>
                <div class="transport-detail" style="margin:0.5rem 0 0.8rem">{line}</div>
                {crowd_badge}
                <hr class="blue-divider">
                <div style="display:flex; gap:0.8rem; margin-bottom:1rem">
                    <div class="transport-stat" style="flex:1">
                        <div class="transport-stat-label">Est. Arrival</div>
                        <div class="transport-stat-val">{duration}</div>
                    </div>
                    <div class="transport-stat" style="flex:1">
                        <div class="transport-stat-label">Crowd Level</div>
                        <div class="transport-stat-val">{crowd}</div>
                    </div>
                    <div class="transport-stat" style="flex:1">
                        <div class="transport-stat-label">Sector</div>
                        <div class="transport-stat-val" style="font-size:0.9rem">{sector.split()[0]}</div>
                    </div>
                </div>
                <div style="background:rgba(0,155,222,0.07);border-radius:8px;padding:0.7rem 1rem;font-size:0.78rem;color:var(--grey);">
                    💡 <strong style="color:var(--white)">{crowd_tip}</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Tips row
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Matchday Tips</div>', unsafe_allow_html=True)
    t1, t2, t3 = st.columns(3)
    tips = [
        ("🎫", "Ticket Check", "Have your QR code ready 15 min before kickoff to avoid gate queues."),
        ("⏰", "Best Timing", "Arrive 45 min early — crowds peak at T-20 min before kickoff."),
        ("🔒", "Security", "No large bags or glass bottles. Metal detectors at all entrances."),
    ]
    for col, (icon, title, desc) in zip([t1, t2, t3], tips):
        with col:
            st.markdown(f"""
            <div class="card">
                <div style="font-size:1.8rem;margin-bottom:0.5rem">{icon}</div>
                <div style="font-family:'Barlow Condensed',sans-serif;font-size:0.85rem;font-weight:800;
                            color:var(--white);text-transform:uppercase;letter-spacing:0.05em;
                            margin-bottom:0.3rem">{title}</div>
                <div style="font-size:0.78rem;color:var(--grey);line-height:1.5">{desc}</div>
            </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — BAR FINDER
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="section-label">Supporter Bars Near Vélodrome</div>', unsafe_allow_html=True)

    filter_col, _ = st.columns([1, 2])
    with filter_col:
        crowd_filter = st.radio(
            "Filter by crowd level",
            options=["All", "Calm", "Busy", "Full"],
            horizontal=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    filtered = BARS.copy()
    if crowd_filter != "All":
        filtered = filtered[filtered["Crowd"] == crowd_filter]

    if filtered.empty:
        st.info("No bars match this filter right now.")
    else:
        for _, row in filtered.iterrows():
            stars      = "★" * row["Ambiance"] + "☆" * (5 - row["Ambiance"])
            crowd_html = {
                "Calm": '<span class="badge badge-calm">🟢 Calm</span>',
                "Busy": '<span class="badge badge-busy">🟠 Busy</span>',
                "Full": '<span class="badge badge-full">🔴 Full</span>',
            }.get(row["Crowd"], "")

            st.markdown(f"""
            <div class="bar-row">
                <div style="flex:1">
                    <div class="bar-name">{row['Bar']}</div>
                    <div class="bar-meta">📍 {row['Quartier']} &nbsp;·&nbsp; 
                         🗺️ {row['Distance']} from Vélodrome</div>
                    <div class="bar-stars" style="margin-top:0.3rem">{stars}</div>
                </div>
                <div class="bar-right">
                    {crowd_html}
                    <div style="font-size:0.7rem;color:var(--muted);margin-top:0.4rem">Ambiance {row['Ambiance']}/5</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Bar Map — Vélodrome Area</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card" style="text-align:center;padding:2.5rem;color:var(--muted);font-size:0.8rem">
        🗺️ &nbsp; Interactive map integration available in the full version
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — LIVE MATCH STATS
# ══════════════════════════════════════════════════════════════════════════════
with tab3:

    # — Scoreboard —
    st.markdown("""
    <div class="scoreboard">
        <div class="match-label">⚽ Ligue 1 · Matchday 28 · Stade Vélodrome</div>
        <div class="score-row">
            <div class="team-name left">Olympique<br>de Marseille</div>
            <div style="display:flex;align-items:center;gap:0.5rem">
                <div class="score-box">2</div>
                <div class="score-sep">—</div>
                <div class="score-box">1</div>
            </div>
            <div class="team-name right">Paris<br>Saint-Germain</div>
        </div>
        <div><span class="match-minute">⏱ 67'</span></div>
    </div>
    """, unsafe_allow_html=True)

    # — Metrics row —
    st.markdown("""
    <div class="metric-grid" style="margin-bottom:1.2rem">
        <div class="metric-cell">
            <div class="metric-label">Shots</div>
            <div class="metric-val">12</div>
            <div class="metric-sub">OM &nbsp;vs&nbsp; 6 PSG</div>
        </div>
        <div class="metric-cell">
            <div class="metric-label">Shots on target</div>
            <div class="metric-val">7</div>
            <div class="metric-sub">OM &nbsp;vs&nbsp; 3 PSG</div>
        </div>
        <div class="metric-cell">
            <div class="metric-label">Corners</div>
            <div class="metric-val">8</div>
            <div class="metric-sub">OM &nbsp;vs&nbsp; 3 PSG</div>
        </div>
        <div class="metric-cell">
            <div class="metric-label">Fouls</div>
            <div class="metric-val">9</div>
            <div class="metric-sub">OM &nbsp;vs&nbsp; 14 PSG</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # — Two-column stats —
    s1, s2 = st.columns([1.2, 1], gap="large")

    with s1:
        st.markdown('<div class="section-label">xG — Expected Goals</div>', unsafe_allow_html=True)

        xg_rows = [
            ("OM xG",  2.1, "#009BDE", "2.1"),
            ("PSG xG", 0.8, "#8a0000", "0.8"),
        ]
        for label, val, color, display in xg_rows:
            pct = val / 3.0 * 100
            st.markdown(f"""
            <div class="stat-bar-wrap">
                <div class="stat-bar-label">
                    <span>{label}</span>
                    <span style="color:var(--white);font-size:0.85rem">{display}</span>
                </div>
                <div class="stat-bar-track">
                    <div class="stat-bar-fill" style="width:{pct:.0f}%;background:{color};
                    box-shadow:0 0 10px {color}55;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-label" style="margin-top:1rem">Possession</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="stat-bar-wrap">
            <div class="stat-bar-label">
                <span>OM &nbsp;58%</span>
                <span>42%&nbsp; PSG</span>
            </div>
            <div class="stat-bar-track" style="height:14px">
                <div class="stat-bar-fill" style="width:58%;background:linear-gradient(90deg,#009BDE,#0070aa);
                     box-shadow:0 0 12px rgba(0,155,222,0.5);"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with s2:
        st.markdown('<div class="section-label">Possession Split</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="display:flex;flex-direction:column;align-items:center;gap:0.8rem;padding:0.5rem 0">
            <div style="position:relative;width:140px;height:140px;
                        border-radius:50%;
                        background: conic-gradient(#009BDE 0% 58%, #2a2a50 58% 100%);
                        display:flex;align-items:center;justify-content:center;">
                <div style="position:absolute;width:88px;height:88px;background:#1a1a2e;border-radius:50%;
                             display:flex;align-items:center;justify-content:center;
                             font-family:'Barlow Condensed',sans-serif;font-size:1.5rem;font-weight:900;
                             color:#009BDE;">58%</div>
            </div>
            <div style="display:flex;gap:1.2rem;font-family:'Barlow Condensed',sans-serif;
                        font-size:0.72rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase">
                <span><span style="display:inline-block;width:8px;height:8px;border-radius:50%;
                             background:#009BDE;margin-right:0.3rem;vertical-align:middle"></span>
                       OM 58%</span>
                <span><span style="display:inline-block;width:8px;height:8px;border-radius:50%;
                             background:#2a2a50;border:1px solid #555;margin-right:0.3rem;vertical-align:middle"></span>
                       PSG 42%</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # — AI Analysis card —
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">AI Match Analysis</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="ai-card">
        <div class="ai-tag">🤖 &nbsp; AI Analyst · Live Insight</div>
        <div class="ai-text">
            <strong>OM is dominating possession</strong> but PSG remains dangerous on counter-attacks.
            <strong>Aubameyang's xG of 1.3</strong> suggests a goal was coming — his movement between 
            the lines has been exceptional tonight. PSG's defensive block has conceded 
            <strong>7 shots on target</strong>, their worst figure in Ligue 1 this season.
            Watch for <strong>high-press triggers</strong> in the final 20 minutes as fatigue sets in.
            OM's wide channels are where the next goal is most likely to come from.
        </div>
        <hr class="blue-divider">
        <div style="display:flex;gap:1rem;flex-wrap:wrap">
            <div style="background:rgba(0,155,222,0.08);border:1px solid var(--border);
                        border-radius:8px;padding:0.5rem 0.9rem;font-size:0.72rem;color:var(--grey)">
                📍 <strong style="color:var(--white)">Aubameyang xG: 1.3</strong>
            </div>
            <div style="background:rgba(0,155,222,0.08);border:1px solid var(--border);
                        border-radius:8px;padding:0.5rem 0.9rem;font-size:0.72rem;color:var(--grey)">
                🔥 <strong style="color:var(--white)">OM Win Probability: 74%</strong>
            </div>
            <div style="background:rgba(0,155,222,0.08);border:1px solid var(--border);
                        border-radius:8px;padding:0.5rem 0.9rem;font-size:0.72rem;color:var(--grey)">
                ⚠️ <strong style="color:var(--white)">PSG Counter Threat: High</strong>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
