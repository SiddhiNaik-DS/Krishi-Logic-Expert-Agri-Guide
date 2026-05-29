import streamlit as st
import requests

# --- 1. CONFIGURATION, THEME BACKGROUND & STRICT EDGE ANIMATIONS ---
st.set_page_config(page_title="Krishi-Logic: Expert Agri-Guide", page_icon="🌱", layout="wide")

# Custom CSS for Background Color and Edge-Confined Animations
st.markdown("""
    <style>
    /* Premium Mint-Cream Background color */
    .stApp { 
        background-color: #f7fbf7; 
    }
    
    .main-header {
        font-size: 36px; color: #1b5e20; text-align: center;
        font-weight: 800; padding: 10px; border-bottom: 2px solid #81c784;
    }
    
    .agri-card {
        background-color: #ffffff; padding: 20px;
        border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px; border-left: 5px solid #2e7d32;
    }

    /* Left and Right Edge Containers */
    .left-animation, .right-animation {
        position: fixed;
        top: 0;
        height: 100%;
        width: 60px; /* Constrained gutter width */
        margin: 0;
        padding: 0;
        z-index: 9999; /* Ensure elements float on top of margins */
        pointer-events: none;
        overflow: hidden;
    }
    
    .left-animation { left: 5px; }
    .right-animation { right: 5px; }

    /* Individual Animated Elements */
    .edge-element {
        position: absolute;
        display: block;
        list-style: none;
        font-size: 24px;
        animation: fall-down linear infinite;
        bottom: 120%;
        width: 100%;
        text-align: center;
    }

    /* Keyframes for natural falling & swaying motion */
    @keyframes fall-down {
        0% {
            transform: translateY(0) rotate(0deg) translateX(0);
            opacity: 0;
        }
        10% {
            opacity: 0.7;
        }
        50% {
            transform: translateY(50vh) rotate(180deg) translateX(5px);
        }
        90% {
            opacity: 0.7;
        }
        100% {
            transform: translateY(110vh) rotate(360deg) translateX(-5px);
            opacity: 0;
        }
    }

    /* Staggered offsets for the Left Margin */
    .left-animation .edge-element:nth-child(1) { animation-duration: 12s; animation-delay: 0s; }
    .left-animation .edge-element:nth-child(2) { animation-duration: 16s; animation-delay: 3s; font-size: 18px; }
    .left-animation .edge-element:nth-child(3) { animation-duration: 14s; animation-delay: 7s; font-size: 28px; }

    /* Staggered offsets for the Right Margin */
    .right-animation .edge-element:nth-child(1) { animation-duration: 13s; animation-delay: 1s; }
    .right-animation .edge-element:nth-child(2) { animation-duration: 18s; animation-delay: 5s; font-size: 20px; }
    .right-animation .edge-element:nth-child(3) { animation-duration: 15s; animation-delay: 9s; font-size: 30px; }
    </style>

    <div class="left-animation">
        <div class="edge-element">🍃</div>
        <div class="edge-element">🌱</div>
        <div class="edge-element">💧</div>
    </div>

    <div class="right-animation">
        <div class="edge-element">🌾</div>
        <div class="edge-element">🍃</div>
        <div class="edge-element">🌱</div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. IMAGE VALIDATION HELPER ---
def get_valid_image(url):
    """Verifies image URL availability or drops a premium agricultural fallback."""
    fallback = "https://images.unsplash.com/photo-1464226184884-fa280b87c3a9?w=500&q=80"
    if not url or not url.startswith("http"):
        return fallback
    try:
        response = requests.head(url, timeout=1.5, allow_redirects=True)
        if response.status_code == 200:
            return url
    except:
        pass
    return fallback

# --- 3. SESSION STATE ---
if 'stage' not in st.session_state: st.session_state.stage = 1
if 'crop_choice' not in st.session_state: st.session_state.crop_choice = ""
if 'category_choice' not in st.session_state: st.session_state.category_choice = ""
if 'total_budget' not in st.session_state: st.session_state.total_budget = 15000.0

def change_stage(step):
    st.session_state.stage += step

def reset_app():
    # Safely delete all custom operational session state elements
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    # Reinitialize back to the clean stage 1 layout state
    st.session_state.stage = 1

# --- 4. 100-CROP VERIFIED VISUAL DATABASE ---
CROP_DB = {
    "Vegetables": {
        "Tomato": (18, 27, "Moderate", "https://images.unsplash.com/photo-1595855759920-86582396756a?w=500&q=80"),
        "Potato": (15, 20, "High", "https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=500&q=80"),
        "Onion": (13, 24, "Moderate", "https://images.unsplash.com/photo-1508747703725-7197771375a0?w=500&q=80"),
        "Brinjal": (21, 30, "Moderate", "https://images.unsplash.com/photo-1615484477778-ca3b77940c25?w=500&q=80"),
        "Cauliflower": (15, 20, "High", "https://images.unsplash.com/photo-1568584711075-3d021a7c3ec3?w=500&q=80"),
        "Okra (Bhindi)": (24, 35, "Moderate", "https://images.unsplash.com/photo-1449339043519-7d3a95baf5f1?w=500&q=80"),
        "Spinach": (10, 22, "High", "https://images.unsplash.com/photo-1576045057995-568f588f82fb?w=500&q=80"),
        "Cabbage": (15, 20, "High", "https://images.unsplash.com/photo-1550147760-44c9966d6bc7?w=500&q=80"),
        "Carrot": (15, 21, "Moderate", "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?w=500&q=80"),
        "Chilli": (20, 30, "Moderate", "https://images.unsplash.com/photo-1588253518679-1296144a84e5?w=500&q=80")
    },
    "Fruits": {
        "Mango": (24, 30, "Low", "https://images.unsplash.com/photo-1553279768-865429fa0078?w=500&q=80"),
        "Banana": (26, 30, "Very High", "https://images.unsplash.com/photo-1571771894821-ad9b5886479b?w=500&q=80"),
        "Guava": (20, 28, "Moderate", "https://images.unsplash.com/photo-1536592248579-9941a5a01a3d?w=500&q=80"),
        "Papaya": (21, 32, "Moderate", "https://images.unsplash.com/photo-1517282009859-f000ec3b26fe?w=500&q=80"),
        "Pomegranate": (25, 35, "Low", "https://images.unsplash.com/photo-1614062590749-34b7a151b635?w=500&q=80"),
        "Grapes": (15, 35, "Moderate", "https://images.unsplash.com/photo-1533616688419-b7a585564566?w=500&q=80"),
        "Apple": (21, 24, "Moderate", "https://images.unsplash.com/photo-1560806887-1e4cd0b6bcd6?w=500&q=80"),
        "Orange": (13, 37, "High", "https://images.unsplash.com/photo-1582979512210-99b6a53386f9?w=500&q=80"),
        "Watermelon": (24, 35, "Moderate", "https://images.unsplash.com/photo-1589984662646-e7b2e4962f18?w=500&q=80"),
        "Pineapple": (22, 32, "High", "https://images.unsplash.com/photo-1550258114-b83400c3c6ad?w=500&q=80")
    },
    "Flowers": {
        "Marigold": (18, 20, "Low", "https://images.unsplash.com/photo-1589883661923-6476cb0ae9f2?w=500&q=80"),
        "Rose": (15, 28, "Moderate", "https://images.unsplash.com/photo-1496062031456-07b8f162e322?w=500&q=80"),
        "Jasmine": (20, 35, "Moderate", "https://images.unsplash.com/photo-1527187162622-b35652f1459a?w=500&q=80"),
        "Hibiscus": (16, 32, "Moderate", "https://images.unsplash.com/photo-1551462147-ff29053bfc14?w=500&q=80"),
        "Tulip": (5, 17, "High", "https://images.unsplash.com/photo-1520763185298-1b434c919102?w=500&q=80"),
        "Sunflower": (20, 25, "Moderate", "https://images.unsplash.com/photo-1597848212624-a19eb35e2651?w=500&q=80"),
        "Orchid": (18, 29, "High", "https://images.unsplash.com/photo-1525310072745-f49212b5ac6d?w=500&q=80"),
        "Chrysanthemum": (15, 25, "Moderate", "https://images.unsplash.com/photo-1508784411316-02b8cd4d3a3a?w=500&q=80"),
        "Lotus": (20, 35, "Very High", "https://images.unsplash.com/photo-1502082553048-f009c37129b9?w=500&q=80"),
        "Lavender": (20, 30, "Low", "https://images.unsplash.com/photo-1528183429752-a97d0bf99b5a?w=500&q=80")
    },
    "Grains/Cereals": {
        "Wheat": (10, 25, "Moderate", "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=500&q=80"),
        "Rice (Paddy)": (20, 35, "Very High", "https://images.unsplash.com/photo-1536657235019-0307126618a4?w=500&q=80"),
        "Maize (Corn)": (18, 27, "Moderate", "https://images.unsplash.com/photo-1530053931934-972f778714df?w=500&q=80"),
        "Barley": (15, 25, "Low", "https://images.unsplash.com/photo-1534067783941-51c9c23eccfd?w=500&q=80"),
        "Millet (Bajra)": (25, 35, "Low", "https://images.unsplash.com/photo-1595123550441-d377e017de6a?w=500&q=80"),
        "Sorghum (Jowar)": (25, 32, "Low", "https://images.unsplash.com/photo-1563514227147-6d2ff665a6a0?w=500&q=80"),
        "Oats": (15, 25, "Moderate", "https://images.unsplash.com/photo-1586439702132-55ce0da671ef?w=500&q=80"),
        "Rye": (12, 18, "Moderate", "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=500&q=80"),
        "Quinoa": (18, 20, "Low", "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=500&q=80"),
        "Ragi": (25, 30, "Moderate", "https://images.unsplash.com/photo-1599307734111-9a70057ad93a?w=500&q=80")
    },
    "Pulses/Legumes": {
        "Chickpeas": (20, 30, "Low", "https://images.unsplash.com/photo-1547050079-6a1135b1400d?w=500&q=80"),
        "Moong Dal": (25, 35, "Low", "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=500&q=80"),
        "Toor Dal": (20, 30, "Low", "https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=500&q=80"),
        "Lentils": (18, 30, "Low", "https://images.unsplash.com/photo-1515543904379-3d757afe72e2?w=500&q=80"),
        "Kidney Beans": (15, 25, "Moderate", "https://images.unsplash.com/photo-1585914924626-15adac1e6402?w=500&q=80"),
        "Soybean": (20, 30, "Moderate", "https://images.unsplash.com/photo-1594756202469-9ff9799a2e4e?w=500&q=80"),
        "Peas": (10, 18, "Moderate", "https://images.unsplash.com/photo-1587570222018-09cb9f8260a9?w=500&q=80"),
        "Urad Dal": (25, 35, "Low", "https://images.unsplash.com/photo-1626132647523-66f5bf380027?w=500&q=80"),
        "Cowpea": (20, 30, "Moderate", "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=500&q=80"),
        "Green Gram": (25, 35, "Low", "https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=500&q=80")
    },
    "Oilseeds": {
        "Mustard": (10, 25, "Low", "https://images.unsplash.com/photo-1530595467537-0b5996c41f2d?w=500&q=80"),
        "Groundnut": (20, 30, "Moderate", "https://images.unsplash.com/photo-1568241695507-6cbe1900d8be?w=500&q=80"),
        "Sesame": (25, 35, "Low", "https://images.unsplash.com/photo-1536628218412-801f626d690e?w=500&q=80"),
        "Linseed": (10, 20, "Moderate", "https://images.unsplash.com/photo-1501430654243-c934cec2e1c0?w=500&q=80"),
        "Castor": (20, 26, "Low", "https://images.unsplash.com/photo-1444491741275-3747c53c99b4?w=500&q=80"),
        "Safflower": (20, 30, "Low", "https://images.unsplash.com/photo-1508962914676-134849a727f0?w=500&q=80"),
        "Coconut": (20, 32, "Very High", "https://images.unsplash.com/photo-1543157145-f78c636d023d?w=500&q=80"),
        "Palm Oil": (22, 32, "High", "https://images.unsplash.com/photo-1601597111158-2fceff292cdc?w=500&q=80"),
        "Rapeseed": (10, 25, "Low", "https://images.unsplash.com/photo-1530595467537-0b5996c41f2d?w=500&q=80"),
        "Sunflower Oil": (20, 25, "Moderate", "https://images.unsplash.com/photo-1597848212624-a19eb35e2651?w=500&q=80")
    },
    "Spices": {
        "Turmeric": (20, 30, "High", "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=500&q=80"),
        "Black Pepper": (25, 35, "High", "https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=500&q=80"),
        "Cardamom": (10, 35, "High", "https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=500&q=80"),
        "Clove": (25, 35, "High", "https://images.unsplash.com/photo-1589656966895-2f33e7653819?w=500&q=80"),
        "Cinnamon": (20, 30, "Moderate", "https://images.unsplash.com/photo-1509358271058-acd22cc93898?w=500&q=80"),
        "Ginger": (20, 30, "High", "https://images.unsplash.com/photo-1599422315622-c8de9e013bfd?w=500&q=80"),
        "Cumin": (20, 30, "Low", "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=500&q=80"),
        "Coriander": (20, 25, "Moderate", "https://images.unsplash.com/photo-1608797178974-15b35a61d121?w=500&q=80"),
        "Fennel": (15, 25, "Moderate", "https://images.unsplash.com/photo-1608797178974-15b35a61d121?w=500&q=80"),
        "Fenugreek": (15, 25, "Low", "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=500&q=80")
    },
    "Cash Crops": {
        "Cotton": (21, 30, "Moderate", "https://images.unsplash.com/photo-1594904351111-a072f80b1a71?w=500&q=80"),
        "Sugarcane": (20, 35, "Very High", "https://images.unsplash.com/photo-1528642473523-0dfb572236fa?w=500&q=80"),
        "Tobacco": (20, 30, "Moderate", "https://images.unsplash.com/photo-1536628218412-801f626d690e?w=500&q=80"),
        "Jute": (24, 38, "Very High", "https://images.unsplash.com/photo-1545167622-3a6ac756afa4?w=500&q=80"),
        "Rubber": (25, 34, "High", "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?w=500&q=80"),
        "Indigo": (20, 30, "Moderate", "https://images.unsplash.com/photo-1508962914676-134849a727f0?w=500&q=80"),
        "Tea": (13, 30, "High", "https://images.unsplash.com/photo-1554256273-6ff4f08eb11e?w=500&q=80"),
        "Coffee": (15, 28, "High", "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500&q=80"),
        "Cocoa": (21, 32, "High", "https://images.unsplash.com/photo-1587132137056-bfbf0166836e?w=500&q=80"),
        "Vanilla": (20, 30, "High", "https://images.unsplash.com/photo-1509358271058-acd22cc93898?w=500&q=80")
    },
    "Medicinal Plants": {
        "Aloe Vera": (20, 35, "Very Low", "https://images.unsplash.com/photo-1596199050105-6d5d32222916?w=500&q=80"),
        "Ashwagandha": (20, 32, "Low", "https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?w=500&q=80"),
        "Tulsi": (20, 35, "Moderate", "https://images.unsplash.com/photo-1603909223429-69bb7101f420?w=500&q=80"),
        "Neem": (20, 40, "Low", "https://images.unsplash.com/photo-1596199050105-6d5d32222916?w=500&q=80"),
        "Brahmi": (20, 30, "Very High", "https://images.unsplash.com/photo-1560493676-04071c5f467b?w=500&q=80"),
        "Amla": (20, 35, "Moderate", "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=500&q=80"),
        "Giloy": (20, 35, "Moderate", "https://images.unsplash.com/photo-1508962914676-134849a727f0?w=500&q=80"),
        "Stevia": (15, 30, "Moderate", "https://images.unsplash.com/photo-1596199050105-6d5d32222916?w=500&q=80"),
        "Lemongrass": (20, 35, "Moderate", "https://images.unsplash.com/photo-1515150144380-bca9f1650ed9?w=500&q=80"),
        "Mentha": (15, 25, "High", "https://images.unsplash.com/photo-1532911554325-4f9979f73156?w=500&q=80")
    },
    "Dry Fruits/Nuts": {
        "Almond": (15, 30, "Low", "https://images.unsplash.com/photo-1508888620463-90748d1143a7?w=500&q=80"),
        "Cashew": (20, 30, "Low", "https://images.unsplash.com/photo-1536628218412-801f626d690e?w=500&q=80"),
        "Walnut": (10, 25, "Moderate", "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=500&q=80"),
        "Pistachio": (20, 35, "Very Low", "https://images.unsplash.com/photo-1543157145-f78c636d023d?w=500&q=80"),
        "Dates": (25, 45, "Very Low", "https://images.unsplash.com/photo-1530912165037-77cf68c858fb?w=500&q=80"),
        "Hazelnuts": (15, 20, "Moderate", "https://images.unsplash.com/photo-1508888620463-90748d1143a7?w=500&q=80"),
        "Peanuts": (20, 30, "Moderate", "https://images.unsplash.com/photo-1568241695507-6cbe1900d8be?w=500&q=80"),
        "Apricot": (15, 30, "Moderate", "https://images.unsplash.com/photo-1594756202469-9ff9799a2e4e?w=500&q=80"),
        "Raisins": (15, 35, "Low", "https://images.unsplash.com/photo-1530912165037-77cf68c858fb?w=500&q=80"),
        "Betel Nut": (20, 30, "High", "https://images.unsplash.com/photo-1543157145-f78c636d023d?w=500&q=80")
    }
}

UNIT_MAP = {
    "Vegetables": "kg", "Fruits": "kg", "Flowers": "bundle", "Grains/Cereals": "quintal",
    "Pulses/Legumes": "kg", "Oilseeds": "kg", "Spices": "kg", "Cash Crops": "ton",
    "Medicinal Plants": "kg", "Dry Fruits/Nuts": "kg"
}

# --- 5. NAVIGATION HEADER ---
st.markdown('<div class="main-header">🌱 KRISHI-LOGIC</div>', unsafe_allow_html=True)
st.progress(st.session_state.stage / 6)

# --- 6. UI STAGES ---

# STAGE 1: SETUP
if st.session_state.stage == 1:
    st.title("🚜 Krishi-Logic: Project Setup")
    
    # Pre-select defaults safely if current data state is completely cleared
    if not st.session_state.category_choice:
        st.session_state.category_choice = list(CROP_DB.keys())[0]
    if not st.session_state.crop_choice:
        st.session_state.crop_choice = list(CROP_DB[st.session_state.category_choice].keys())[0]
        
    crop_info = CROP_DB[st.session_state.category_choice][st.session_state.crop_choice]
    
    col_img, col1, col2 = st.columns([1, 2, 2])
    
    with col_img:
        verified_img = get_valid_image(crop_info[3])
        st.image(verified_img, width=180, caption=f"Focus Variety: {st.session_state.crop_choice}")
        
    with col1:
        st.markdown('<div class="agri-card">', unsafe_allow_html=True)
        st.session_state.category_choice = st.selectbox("1. Select Crop Category", list(CROP_DB.keys()))
        st.session_state.crop_choice = st.selectbox(f"2. Select {st.session_state.category_choice} Variety", list(CROP_DB[st.session_state.category_choice].keys()))
        st.session_state.total_budget = st.number_input("3. Total Seasonal Budget (₹):", min_value=1000.0, value=15000.0)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.success(f"### Target Variant Setup\n* **Optimal Temperature:** {crop_info[0]}-{crop_info[1]}°C\n* **Water Requirement:** {crop_info[2]} Profile")
        st.button("Start Land Preparation Guide ➡️", on_click=change_stage, args=(1,), key="btn_stage_1_next")

# STAGE 2: LAND PREPARATION
elif st.session_state.stage == 2:
    st.title("🚜 Stage 1: Detailed Land Preparation")
    crop_info = CROP_DB[st.session_state.category_choice][st.session_state.crop_choice]
    
    col_img, col1, col2 = st.columns([1, 2, 2])
    with col_img:
        st.image(get_valid_image(crop_info[3]), width=180, caption=st.session_state.crop_choice)
        
    with col1:
        st.markdown("### 📋 Essential Inputs")
        temp = st.slider("Field Temp (°C):", 0, 50, 25)
        soil = st.selectbox("Soil Profile:", ["Loamy", "Clay", "Sandy", "Black Cotton", "Red Soil"])
        prep_cost = st.number_input("Tractor & Labor Cost (₹):", value=2000.0)
    with col2:
        st.markdown("### 💡 Expert Suggestions")
        st.info(f"**Necessary Tools:** For {st.session_state.crop_choice}, use a **Disc Plow** followed by a **Leveler**.")
        st.write("**Organic Load:** Apply 10 tons of Farm Yard Manure (FYM) per acre.")
        if temp > 30:
            st.warning("⚠️ High Heat: Incorporate green manure to improve water retention.")

    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Back", on_click=change_stage, args=(-1,), key="btn_stage_2_back")
    with c2: st.button("Next: Sowing ➡️", on_click=change_stage, args=(1,), key="btn_stage_2_next")

# STAGE 3: SOWING
elif st.session_state.stage == 3:
    st.title("🌱 Stage 2: Sowing & Seed Treatment")
    crop_info = CROP_DB[st.session_state.category_choice][st.session_state.crop_choice]
    
    col_img, col1, col2 = st.columns([1, 2, 2])
    with col_img:
        st.image(get_valid_image(crop_info[3]), width=180, caption=st.session_state.crop_choice)
        
    with col1:
        st.markdown("### 📋 Sowing Strategy")
        method = st.selectbox("Method:", ["Direct Sowing", "Transplanting", "Drilling"])
        seed_source = st.radio("Seed Source:", ["Certified Govt Seeds", "Private Hybrid", "Saved Seed"])
        sowing_cost = st.number_input("Seed & Labor Cost (₹):", value=2500.0)
    with col2:
        st.markdown("### 💡 AI Requirement Checklist")
        st.error("**Treatment:** Seed treatment with *Trichoderma* (10g/kg) is critical to prevent fungal rot.")
        st.info(f"**Depth/Spacing:** Maintain 45cm x 15cm geometry for optimal {st.session_state.crop_choice} growth.")
        if seed_source == "Saved Seed":
            st.warning("⚠️ Germination Alert: Perform a salt-water float test to remove hollow seeds.")

    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Back", on_click=change_stage, args=(-1,), key="btn_stage_3_back")
    with c2: st.button("Next: Growth/Irrigation ➡️", on_click=change_stage, args=(1,), key="btn_stage_3_next")

# STAGE 4: GROWTH & MAINTENANCE
elif st.session_state.stage == 4:
    st.title("💧 Stage 3: Nutrition & Irrigation")
    crop_info = CROP_DB[st.session_state.category_choice][st.session_state.crop_choice]
    
    col_img, col1, col2 = st.columns([1, 2, 2])
    with col_img:
        st.image(get_valid_image(crop_info[3]), width=180, caption=st.session_state.crop_choice)
        
    with col1:
        st.markdown("### 📋 Resource Inputs")
        irr_system = st.selectbox("System:", ["Drip (Recommended)", "Sprinkler", "Flood"])
        fert_plan = st.multiselect("Fertilizers to Apply:", ["Urea", "DAP", "Potash", "Zinc Sulfate", "Boron"])
        maint_cost = st.number_input("Irrigation & Fertilizer Cost (₹):", value=3500.0)
    with col2:
        st.markdown("### 💡 AI Growth Guide")
        crop_water = crop_info[2]
        st.write(f"**Water Profile:** {crop_water} Demand.")
        if "Urea" in fert_plan:
            st.info("💡 Split Application: Apply Urea in 3 doses (Sowing, 30 days, and Flowering).")
        st.write("**Pest Watch:** Monitor for Aphids and Jassids during early leaf stage.")

    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Back", on_click=change_stage, args=(-1,), key="btn_stage_4_back")
    with c2: st.button("Next: Harvesting ➡️", on_click=change_stage, args=(1,), key="btn_stage_4_next")

# STAGE 5: HARVESTING
elif st.session_state.stage == 5:
    st.title("🌾 Stage 4: Harvest & Post-Harvest")
    crop_info = CROP_DB[st.session_state.category_choice][st.session_state.crop_choice]
    
    col_img, col1, col2 = st.columns([1, 2, 2])
    with col_img:
        st.image(get_valid_image(crop_info[3]), width=180, caption=st.session_state.crop_choice)
        
    with col1:
        st.markdown("### 📋 Maturity Check")
        moisture = st.slider("Target Grain/Fruit Moisture (%):", 5, 30, 15)
        harv_cost = st.number_input("Harvest & Transport Cost (₹):", value=2000.0)
    with col2:
        st.markdown("### 💡 AI Storage Strategy")
        st.info("**Curing:** For root crops/onions, leave in field for 3 days for skin hardening.")
        if moisture > 14:
            st.error("⚠️ Storage Risk: High moisture will cause mold. Dry the crop before bagging.")
        st.write("**Packaging:** Use perforated crates for fruits or jute bags for grains.")

    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Back", on_click=change_stage, args=(-1,), key="btn_stage_5_back")
    with c2: st.button("Next: Selling Guide ➡️", on_click=change_stage, args=(1,), key="btn_stage_5_next")

# STAGE 6: SELLING GUIDE
elif st.session_state.stage == 6:
    st.title("💰 Stage 5: Market & Sales Optimizer")
    unit = UNIT_MAP.get(st.session_state.category_choice, "kg")
    crop_info = CROP_DB[st.session_state.category_choice][st.session_state.crop_choice]
    
    col_img, col1, col2 = st.columns([1, 2, 2])
    with col_img:
        st.image(get_valid_image(crop_info[3]), width=180, caption=st.session_state.crop_choice)
        
    with col1:
        mandi_price = st.number_input(f"Mandi Price (₹/{unit}):", value=100.0)
        making_charges = st.number_input(f"Total Overhead per {unit} (₹):", value=15.0)
    with col2:
        desired_profit = st.number_input(f"Profit Margin per {unit} (₹):", value=25.0)
        quantity = st.number_input(f"Harvested Quantity ({unit}s):", value=100.0)
    
    target_price = mandi_price + making_charges + desired_profit
    total_revenue = target_price * quantity
    
    st.divider()
    st.subheader("Seasonal Summary")
    st.metric("Suggested Sale Price", f"₹{target_price}/{unit}")
    st.metric("Total Projected Revenue", f"₹{total_revenue:,.2f}")
    
    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Back", on_click=change_stage, args=(-1,), key="btn_stage_6_back")
    with c2: st.button("🔄 Complete & Reset Project", on_click=reset_app, key="btn_stage_6_reset")