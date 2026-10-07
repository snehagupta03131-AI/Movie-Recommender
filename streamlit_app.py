import streamlit as st
from src.recommender import recommend_movies_for_user, movies, ratings

st.set_page_config(
    page_title="CineMatch | Movie Recommendations",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background-color: #0B0E14;
        zoom: 100%;
    }

    .block-container {
        padding-top: 3rem;
        max-width: 1000px;
    }

    /* ===== TOP NAV ===== */
    .topnav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 40px;
        border-bottom: 1px solid #1F232D;
        margin-bottom: 50px;
    }
    .brand {
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        color: #F1F1F3 !important;
        letter-spacing: -0.5px;
    }
    .brand-accent {
        color: #4F7CFF;
    }
    .tag {
        color: #6B7280 !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
    }

    /* ===== HERO ===== */
    .hero-title {
        font-size: 2.6rem !important;
        font-weight: 700 !important;
        color: #F1F1F3 !important;
        margin: 0 0 14px 0 !important;
        line-height: 1.25 !important;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        color: #8B92A5 !important;
        font-size: 1.05rem !important;
        max-width: 620px;
        line-height: 1.65 !important;
        margin: 0 0 45px 0 !important;
    }

    /* ===== SECTION HEADERS ===== */
    .section-title {
        color: #F1F1F3 !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        margin: 0 0 22px 0 !important;
        letter-spacing: -0.3px;
    }

    /* ===== INPUT CARD ===== */
    .input-card {
        background: #131722;
        border: 1px solid #1F232D;
        border-radius: 12px;
        padding: 28px 28px 8px 28px;
        margin-bottom: 45px;
    }

    /* ===== MOVIE CARDS ===== */
    .movie-card {
        background: #131722;
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 20px;
        border: 1px solid #1F232D;
        display: flex;
        flex-direction: column;
        height: 340px;
    }
    .poster-box {
        width: 100%;
        height: 130px;
        background: #1A1F2B;
        border-bottom: 1px solid #1F232D;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 12px;
        box-sizing: border-box;
    }
    .poster-text {
        color: #4F7CFF !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        opacity: 0.9;
    }
    .card-body {
        padding: 18px 20px;
        flex: 1;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }
    .movie-rank {
        color: #4F7CFF !important;
        font-size: 0.7rem !important;
        font-weight: 700 !important;
        letter-spacing: 1.2px;
        text-transform: uppercase;
    }
    .movie-title {
        color: #F1F1F3 !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        margin: 8px 0 10px 0 !important;
        line-height: 1.4 !important;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
    .genre-tag {
        display: inline-block;
        background: #1A1F2B;
        color: #8B92A5 !important;
        padding: 4px 11px;
        border-radius: 6px;
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        margin: 2px 4px 2px 0;
        border: 1px solid #232838;
    }

    /* ===== WIDGET LABELS ===== */
    .stNumberInput label p, .stSlider label p {
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        color: #C1C6D3 !important;
    }
    .stButton button p {
        font-size: 1rem !important;
        font-weight: 600 !important;
    }
    div[data-testid="stButton"] button {
        background-color: #4F7CFF !important;
        border: none !important;
        border-radius: 8px !important;
    }
    div[data-testid="stButton"] button:hover {
        background-color: #3D68E8 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ===== TOP NAV =====
st.markdown("""
    <div class="topnav">
        <div class="brand">🎬 Cine<span class="brand-accent">Match</span></div>
        <div class="tag">Hybrid Recommendation Engine</div>
    </div>
""", unsafe_allow_html=True)

# ===== HERO =====
st.markdown('<p class="hero-title">Find your next favorite movie</p>', unsafe_allow_html=True)
st.markdown("""
    <p class="hero-subtitle">
        CineMatch blends collaborative filtering and content-based analysis
        to generate recommendations tailored specifically to your taste.
    </p>
""", unsafe_allow_html=True)

# ===== INPUT =====
st.markdown('<div class="section-title">Get Recommendations</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    user_id = st.selectbox(
    "Select User",
    options=sorted(ratings['userId'].unique().tolist())
)
with col2:
    n = st.slider("Number of recommendations", min_value=5, max_value=20, value=10)

get_recs = st.button("Get My Recommendations", use_container_width=True, type="primary")

st.write("")

# ===== RESULTS =====
if get_recs:
    with st.spinner("Analyzing your taste and finding perfect matches..."):
        recommendations = recommend_movies_for_user(user_id, n=n)

    st.markdown(f'<div class="section-title">Top {n} picks for User {user_id}</div>', unsafe_allow_html=True)

    cols = st.columns(3)
    for i, movie in enumerate(recommendations):
        genre_tags = "".join([f'<span class="genre-tag">{g}</span>' for g in movie['genres'].split('|')])
        card_html = f"""
        <div class="movie-card">
            <div class="poster-box">
                <div class="poster-text">{movie['title'][:35]}</div>
            </div>
            <div class="card-body">
                <div class="movie-rank">#{i+1} Match</div>
                <div class="movie-title">{movie['title']}</div>
                <div>{genre_tags}</div>
            </div>
        </div>
        """
        with cols[i % 3]:
            st.markdown(card_html, unsafe_allow_html=True)
else:
    st.info("Enter a User ID above and click the button to get personalized movie recommendations.")