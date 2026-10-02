"""
PCM Advanced Mock Test — Streamlit Application
================================================
A complete competitive-exam mock test with:
- 45 JEE-level questions (16 Chem + 16 Phys + 13 Math)
- 3-hour countdown timer with auto-submit
- Question palette, navigation, and review marking
- Comprehensive post-test analytics
"""

import streamlit as st
from datetime import datetime
from collections import Counter, defaultdict
from questions import get_question_bank

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="PCM Advanced Mock Test",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Constants ────────────────────────────────────────────────
TOTAL_QUESTIONS = 45
DURATION_MINUTES = 180
MAX_MARKS = 180
CORRECT_MARKS = 4
WRONG_MARKS = -1
UNATTEMPTED_MARKS = 0

# ── Load questions once ──────────────────────────────────────
@st.cache_data
def load_questions():
    return get_question_bank()

QUESTIONS = load_questions()

# ── CSS ──────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    :root {
        --bg-primary: #0a0e1a;
        --bg-card: #111827;
        --bg-card-hover: #1a2236;
        --accent: #6366f1;
        --accent-glow: rgba(99,102,241,0.35);
        --green: #10b981;
        --red: #ef4444;
        --yellow: #f59e0b;
        --blue: #3b82f6;
        --cyan: #06b6d4;
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
        --border: #1e293b;
    }

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* Timer styles */
    .timer-container {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
        border: 1px solid rgba(99,102,241,0.3);
        border-radius: 16px;
        padding: 16px 24px;
        text-align: center;
        box-shadow: 0 0 30px var(--accent-glow);
        margin-bottom: 16px;
    }
    .timer-label {
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 2px;
        color: #a5b4fc;
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    .timer-value {
        font-size: 2.2rem;
        font-weight: 800;
        font-variant-numeric: tabular-nums;
        color: #e0e7ff;
        letter-spacing: 2px;
    }
    .timer-warning { color: #fbbf24 !important; }
    .timer-danger  { color: #f87171 !important; animation: pulse-red 1s infinite; }

    @keyframes pulse-red {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }

    /* Start screen */
    .hero-title {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #818cf8, #6366f1, #4f46e5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        text-align: center;
        color: var(--text-secondary);
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .info-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 16px;
        margin: 24px 0;
    }
    .info-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .info-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }
    .info-card .label {
        font-size: 0.8rem;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 6px;
    }
    .info-card .value {
        font-size: 1.8rem;
        font-weight: 800;
        color: var(--accent);
    }
    .info-card .value.green { color: var(--green); }
    .info-card .value.red { color: var(--red); }
    .info-card .value.yellow { color: var(--yellow); }

    /* Question card */
    .question-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 28px 32px;
        margin: 16px 0;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    }
    .q-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
        flex-wrap: wrap;
        gap: 8px;
    }
    .q-number {
        font-size: 1rem;
        font-weight: 700;
        color: var(--accent);
    }
    .q-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    .badge-physics    { background: rgba(59,130,246,0.15); color: #60a5fa; border: 1px solid rgba(59,130,246,0.3); }
    .badge-chemistry  { background: rgba(16,185,129,0.15); color: #34d399; border: 1px solid rgba(16,185,129,0.3); }
    .badge-mathematics{ background: rgba(245,158,11,0.15); color: #fbbf24; border: 1px solid rgba(245,158,11,0.3); }
    .badge-medium     { background: rgba(59,130,246,0.15); color: #60a5fa; }
    .badge-hard       { background: rgba(245,158,11,0.15); color: #fbbf24; }
    .badge-veryhard   { background: rgba(239,68,68,0.15);  color: #f87171; }

    .q-text {
        font-size: 1.05rem;
        line-height: 1.7;
        color: var(--text-primary);
        margin-bottom: 20px;
        white-space: pre-wrap;
    }

    /* Palette */
    .palette-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 42px;
        height: 42px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 0.85rem;
        margin: 3px;
        cursor: pointer;
        border: 2px solid transparent;
        transition: all 0.15s;
    }
    .palette-btn:hover { transform: scale(1.1); }
    .pal-unanswered { background: rgba(239,68,68,0.18); color: #f87171; border-color: rgba(239,68,68,0.4); }
    .pal-answered   { background: rgba(16,185,129,0.18); color: #34d399; border-color: rgba(16,185,129,0.4); }
    .pal-review     { background: rgba(245,158,11,0.18); color: #fbbf24; border-color: rgba(245,158,11,0.4); }
    .pal-current    { background: rgba(99,102,241,0.25); color: #a5b4fc; border-color: #6366f1; box-shadow: 0 0 12px var(--accent-glow); }

    /* Result cards */
    .result-hero {
        text-align: center;
        padding: 32px;
        background: linear-gradient(135deg, #1e1b4b, #312e81);
        border-radius: 20px;
        border: 1px solid rgba(99,102,241,0.3);
        margin-bottom: 24px;
    }
    .result-score {
        font-size: 4rem;
        font-weight: 900;
        color: #e0e7ff;
    }
    .result-max {
        font-size: 1.5rem;
        color: #a5b4fc;
    }
    .stat-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
        gap: 12px;
        margin: 20px 0;
    }
    .stat-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
    }
    .stat-label {
        font-size: 0.75rem;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stat-value {
        font-size: 1.6rem;
        font-weight: 800;
        margin-top: 4px;
    }
    .sv-green  { color: var(--green); }
    .sv-red    { color: var(--red); }
    .sv-blue   { color: var(--blue); }
    .sv-yellow { color: var(--yellow); }
    .sv-cyan   { color: var(--cyan); }
    .sv-accent { color: var(--accent); }

    /* Explanation box */
    .explanation-box {
        background: rgba(99,102,241,0.08);
        border-left: 4px solid var(--accent);
        border-radius: 0 12px 12px 0;
        padding: 16px 20px;
        margin-top: 12px;
        font-size: 0.92rem;
        line-height: 1.7;
        color: var(--text-primary);
        white-space: pre-wrap;
    }

    .correct-tag { color: var(--green); font-weight: 700; }
    .wrong-tag   { color: var(--red);   font-weight: 700; }
    .skip-tag    { color: var(--text-secondary); font-weight: 600; }

    /* Warning banners */
    .warning-banner {
        padding: 12px 20px;
        border-radius: 10px;
        font-weight: 600;
        text-align: center;
        margin-bottom: 12px;
        animation: fadeInDown 0.3s;
    }
    .warn-60  { background: rgba(245,158,11,0.15); color: #fbbf24; border: 1px solid rgba(245,158,11,0.3); }
    .warn-30  { background: rgba(245,158,11,0.25); color: #fbbf24; border: 1px solid rgba(245,158,11,0.5); }
    .warn-15  { background: rgba(239,68,68,0.2);   color: #f87171; border: 1px solid rgba(239,68,68,0.4); }
    .warn-5   { background: rgba(239,68,68,0.35);  color: #fca5a5; border: 1px solid rgba(239,68,68,0.6); }
    .warn-1   { background: rgba(239,68,68,0.5);   color: #fee2e2; border: 1px solid rgba(239,68,68,0.8); animation: pulse-red 0.5s infinite; }

    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-10px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* Section divider */
    .section-title {
        font-size: 1.3rem;
        font-weight: 800;
        color: var(--text-primary);
        margin: 32px 0 16px 0;
        padding-bottom: 8px;
        border-bottom: 2px solid var(--accent);
        display: inline-block;
    }

    /* Legend */
    .legend {
        display: flex;
        gap: 16px;
        flex-wrap: wrap;
        margin: 12px 0;
        font-size: 0.82rem;
    }
    .legend-item {
        display: flex;
        align-items: center;
        gap: 6px;
        color: var(--text-secondary);
    }
    .legend-dot {
        width: 14px;
        height: 14px;
        border-radius: 4px;
    }
    .dot-green  { background: var(--green); }
    .dot-red    { background: var(--red); }
    .dot-yellow { background: var(--yellow); }
    .dot-blue   { background: var(--blue); }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    div.stButton > button {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        border-radius: 10px;
        padding: 8px 20px;
        transition: all 0.2s;
    }
    </style>
    """, unsafe_allow_html=True)


# ── Session state initialization ─────────────────────────────
def init_session():
    defaults = {
        "test_started": False,
        "test_submitted": False,
        "start_time": None,
        "current_q": 0,
        "answers": {},          # {q_index: "A"/"B"/...}
        "marked_review": set(),
        "show_submit_confirm": False,
        "auto_submitted": False,
        "confirmed_warnings": set(),
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ── Timer helpers ────────────────────────────────────────────
def get_remaining_seconds():
    if st.session_state.start_time is None:
        return DURATION_MINUTES * 60
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    remaining = DURATION_MINUTES * 60 - elapsed
    return max(0, remaining)


def format_time(secs):
    secs = int(secs)
    h = secs // 3600
    m = (secs % 3600) // 60
    s = secs % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


# ── Scoring helpers ──────────────────────────────────────────
def compute_results():
    answers = st.session_state.answers
    results = {
        "correct": 0, "wrong": 0, "unattempted": 0,
        "correct_marks": 0, "wrong_marks": 0,
        "subject": defaultdict(lambda: {"correct": 0, "wrong": 0, "unattempted": 0, "total": 0}),
        "topic": defaultdict(lambda: {"correct": 0, "wrong": 0, "unattempted": 0, "total": 0}),
        "difficulty": defaultdict(lambda: {"correct": 0, "wrong": 0, "unattempted": 0, "total": 0, "attempted": 0}),
        "question_results": [],
        "mistake_types": [],
    }

    for i, q in enumerate(QUESTIONS):
        subj = q["subject"]
        topic = q["topic"]
        diff = q["difficulty"]
        user_ans = answers.get(i)
        correct_ans = q["answer"]

        results["subject"][subj]["total"] += 1
        results["topic"][f"{subj} — {topic}"]["total"] += 1
        results["difficulty"][diff]["total"] += 1

        qr = {
            "index": i,
            "question": q,
            "user_answer": user_ans,
            "correct_answer": correct_ans,
            "status": None,
            "marks": 0,
            "mistake_type": None,
        }

        if user_ans is None:
            results["unattempted"] += 1
            results["subject"][subj]["unattempted"] += 1
            results["topic"][f"{subj} — {topic}"]["unattempted"] += 1
            results["difficulty"][diff]["unattempted"] += 1
            qr["status"] = "unattempted"
            qr["marks"] = 0
        elif user_ans == correct_ans:
            results["correct"] += 1
            results["correct_marks"] += CORRECT_MARKS
            results["subject"][subj]["correct"] += 1
            results["topic"][f"{subj} — {topic}"]["correct"] += 1
            results["difficulty"][diff]["correct"] += 1
            results["difficulty"][diff]["attempted"] += 1
            qr["status"] = "correct"
            qr["marks"] = CORRECT_MARKS
        else:
            results["wrong"] += 1
            results["wrong_marks"] += abs(WRONG_MARKS)
            results["subject"][subj]["wrong"] += 1
            results["topic"][f"{subj} — {topic}"]["wrong"] += 1
            results["difficulty"][diff]["wrong"] += 1
            results["difficulty"][diff]["attempted"] += 1
            qr["status"] = "wrong"
            qr["marks"] = WRONG_MARKS
            # Classify mistake
            dist_info = q.get("distractor_info", {})
            mistake = dist_info.get(user_ans, "Conceptual mistake")
            qr["mistake_type"] = mistake
            results["mistake_types"].append(mistake)

        results["question_results"].append(qr)

    results["score"] = results["correct_marks"] - results["wrong_marks"]
    attempted = results["correct"] + results["wrong"]
    results["attempted"] = attempted
    results["accuracy"] = (results["correct"] / attempted * 100) if attempted > 0 else 0
    results["attempt_rate"] = attempted / TOTAL_QUESTIONS * 100
    results["percentage"] = results["score"] / MAX_MARKS * 100

    return results


# ══════════════════════════════════════════════════════════════
# SCREENS
# ══════════════════════════════════════════════════════════════

def render_start_screen():
    """Landing page before the test starts."""
    st.markdown('<div class="hero-title">PCM ADVANCED MOCK TEST</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">IAT / MHT-CET / JEE — Level Practice Paper</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">
        <div class="info-card"><div class="label">Questions</div><div class="value">45</div></div>
        <div class="info-card"><div class="label">Duration</div><div class="value">180 <span style="font-size:0.9rem">min</span></div></div>
        <div class="info-card"><div class="label">Max Marks</div><div class="value">180</div></div>
        <div class="info-card"><div class="label">Correct</div><div class="value green">+4</div></div>
        <div class="info-card"><div class="label">Wrong</div><div class="value red">−1</div></div>
        <div class="info-card"><div class="label">Unattempted</div><div class="value yellow">0</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 🧪 Chemistry (16 Q)")
        st.markdown("""
        **Main:** Chemical Kinetics (8-10 Q)
        - Rate law, Order, Molecularity
        - Integrated rate equations
        - Half-life, Arrhenius equation
        - Graph-based & numerical

        **Also:** Thermodynamics, Equilibrium,
        Electrochemistry, Solutions, Atomic
        Structure, Chemical Bonding, Organic
        """)

    with col2:
        st.markdown("#### ⚡ Physics (16 Q)")
        st.markdown("""
        **Main:** Electrostatics (8-10 Q)
        - Coulomb's law, Electric field
        - Potential, Gauss's law
        - Capacitors, Dielectrics
        - Graph-based & numerical

        **Also:** Current Electricity, Magnetism,
        EMI, Ray Optics, Modern Physics,
        Kinematics, Work-Energy-Power
        """)

    with col3:
        st.markdown("#### 📐 Mathematics (13 Q)")
        st.markdown("""
        **Main Topics:**
        - Units & Dimensions (2-3 Q)
        - Trigonometry (3-4 Q)
        - Mathematical Reasoning (2-3 Q)
        - 3D Geometry (2-3 Q)

        **Also:** Algebra, Differentiation,
        Vectors, Probability
        """)

    st.markdown("---")
    st.markdown("""
    > **Instructions:**
    > - Each question has exactly **4 options** with **one correct answer**.
    > - Use **Save & Next** to record your answer and move ahead.
    > - Use **Mark for Review** to flag a question for later.
    > - You can change your answer at any time before submission.
    > - The test will **auto-submit** when the timer reaches zero.
    > - Answers and explanations are revealed **only after submission**.
    """)

    st.markdown("")
    c1, c2, c3 = st.columns([2, 1, 2])
    with c2:
        if st.button("🚀  START TEST", use_container_width=True, type="primary"):
            st.session_state.test_started = True
            st.session_state.start_time = datetime.now()
            st.rerun()


def render_timer_sidebar():
    """Sidebar with timer, palette, and legend."""
    remaining = get_remaining_seconds()
    remaining_min = remaining / 60

    # Timer display
    timer_class = ""
    if remaining_min <= 1:
        timer_class = "timer-danger"
    elif remaining_min <= 15:
        timer_class = "timer-warning"

    st.sidebar.markdown(f"""
    <div class="timer-container">
        <div class="timer-label">Time Remaining</div>
        <div class="timer-value {timer_class}">{format_time(remaining)}</div>
    </div>
    """, unsafe_allow_html=True)

    # Warnings
    if remaining_min <= 1 and remaining > 0:
        st.sidebar.markdown('<div class="warning-banner warn-1">⚠️ FINAL MINUTE — Submit now!</div>', unsafe_allow_html=True)
    elif remaining_min <= 5:
        st.sidebar.markdown('<div class="warning-banner warn-5">⏰ Less than 5 minutes remaining!</div>', unsafe_allow_html=True)
    elif remaining_min <= 15:
        st.sidebar.markdown('<div class="warning-banner warn-15">⏰ 15 minutes remaining</div>', unsafe_allow_html=True)
    elif remaining_min <= 30:
        st.sidebar.markdown('<div class="warning-banner warn-30">⏰ 30 minutes remaining</div>', unsafe_allow_html=True)
    elif remaining_min <= 60:
        st.sidebar.markdown('<div class="warning-banner warn-60">⏰ 60 minutes remaining</div>', unsafe_allow_html=True)

    # Progress
    answered = len(st.session_state.answers)
    reviewed = len(st.session_state.marked_review)
    st.sidebar.markdown(f"**Answered:** {answered}/{TOTAL_QUESTIONS}  •  **Review:** {reviewed}")
    st.sidebar.progress(answered / TOTAL_QUESTIONS)

    # Legend
    st.sidebar.markdown("""
    <div class="legend">
        <div class="legend-item"><div class="legend-dot dot-blue"></div> Current</div>
        <div class="legend-item"><div class="legend-dot dot-green"></div> Answered</div>
        <div class="legend-item"><div class="legend-dot dot-yellow"></div> Marked Review</div>
        <div class="legend-item"><div class="legend-dot dot-red"></div> Not Answered</div>
    </div>
    """, unsafe_allow_html=True)

    # Section-wise Question Palette with Direct Jump
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### 🧩 Question Palette")
    st.sidebar.markdown("<small style='color:#94a3b8;'>Click any question to jump directly</small>", unsafe_allow_html=True)

    sections = [
        ("⚡ Physics", "Physics"),
        ("🧪 Chemistry", "Chemistry"),
        ("📐 Mathematics", "Mathematics")
    ]

    for label, subj in sections:
        st.sidebar.markdown(f"**{label}**")
        subj_q_indices = [i for i, q in enumerate(QUESTIONS) if q["subject"] == subj]
        
        cols = st.sidebar.columns(4)
        for idx_in_subj, q_idx in enumerate(subj_q_indices):
            col = cols[idx_in_subj % 4]
            is_current = (q_idx == st.session_state.current_q)
            is_ans = (q_idx in st.session_state.answers)
            is_rev = (q_idx in st.session_state.marked_review)

            if is_current:
                btn_label = f"▶{q_idx+1}"
                btn_type = "primary"
            elif is_rev:
                btn_label = f"🟡{q_idx+1}"
                btn_type = "secondary"
            elif is_ans:
                btn_label = f"🟢{q_idx+1}"
                btn_type = "secondary"
            else:
                btn_label = f"⚪{q_idx+1}"
                btn_type = "secondary"

            if col.button(btn_label, key=f"p_btn_{q_idx}", use_container_width=True, type=btn_type):
                st.session_state.current_q = q_idx
                st.rerun()

    st.sidebar.markdown("---")

    # Submit button in sidebar
    if st.sidebar.button("📮  SUBMIT TEST", type="primary", use_container_width=True):
        st.session_state.show_submit_confirm = True
        st.rerun()


def render_question_screen():
    """Main test-taking screen."""
    remaining = get_remaining_seconds()

    # Auto-submit if time's up
    if remaining <= 0:
        st.session_state.test_submitted = True
        st.session_state.auto_submitted = True
        st.rerun()

    render_timer_sidebar()

    idx = st.session_state.current_q
    q = QUESTIONS[idx]

    # Section Quick Navigation Bar
    st.markdown("### 📚 Test Sections")
    sec_cols = st.columns(3)
    sections_info = [
        ("⚡ Physics (Q1–16)", "Physics"),
        ("🧪 Chemistry (Q17–32)", "Chemistry"),
        ("📐 Mathematics (Q33–45)", "Mathematics")
    ]
    curr_subj = q["subject"]

    for sc, (sec_title, sec_subj) in zip(sec_cols, sections_info):
        is_active_sec = (curr_subj == sec_subj)
        with sc:
            if st.button(
                sec_title, 
                key=f"sec_tab_{sec_subj}", 
                type="primary" if is_active_sec else "secondary",
                use_container_width=True
            ):
                first_q_in_sec = next(i for i, item in enumerate(QUESTIONS) if item["subject"] == sec_subj)
                st.session_state.current_q = first_q_in_sec
                st.rerun()

    # Subject badge class
    subj_cls = {
        "Physics": "badge-physics",
        "Chemistry": "badge-chemistry",
        "Mathematics": "badge-mathematics",
    }.get(q["subject"], "")

    st.markdown(f"""
    <div class="question-card">
        <div class="q-header">
            <span class="q-number">Question {idx+1} / {TOTAL_QUESTIONS}</span>
            <div>
                <span class="q-badge {subj_cls}">{q['subject']}</span>
            </div>
        </div>
        <div class="q-text">{q['question']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Options as radio buttons
    options_list = [f"{k}) {v}" for k, v in q["options"].items()]
    option_keys = list(q["options"].keys())

    # Current selected answer
    current_ans = st.session_state.answers.get(idx)
    if current_ans and current_ans in option_keys:
        default_idx = option_keys.index(current_ans)
    else:
        default_idx = None

    selected = st.radio(
        "Select your answer:",
        options_list,
        index=default_idx,
        key=f"radio_{idx}",
        label_visibility="collapsed",
    )

    # Navigation buttons
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

    with col1:
        if st.button("⬅️ Previous", disabled=(idx == 0), use_container_width=True):
            st.session_state.current_q = max(0, idx - 1)
            st.rerun()

    with col2:
        if st.button("💾 Save & Next", type="primary", use_container_width=True):
            if selected:
                ans_key = selected.split(")")[0].strip()
                st.session_state.answers[idx] = ans_key
            if idx < TOTAL_QUESTIONS - 1:
                st.session_state.current_q = idx + 1
            st.rerun()

    with col3:
        is_reviewed = idx in st.session_state.marked_review
        review_label = "🔖 Unmark Review" if is_reviewed else "🔖 Mark for Review"
        if st.button(review_label, use_container_width=True):
            if is_reviewed:
                st.session_state.marked_review.discard(idx)
            else:
                st.session_state.marked_review.add(idx)
            st.rerun()

    with col4:
        if st.button("🗑️ Clear Response", use_container_width=True):
            if idx in st.session_state.answers:
                del st.session_state.answers[idx]
            st.rerun()

    with col5:
        if st.button("Next ➡️", disabled=(idx >= TOTAL_QUESTIONS - 1), use_container_width=True):
            st.session_state.current_q = min(TOTAL_QUESTIONS - 1, idx + 1)
            st.rerun()

    # Submit confirmation modal
    if st.session_state.show_submit_confirm:
        st.markdown("---")
        answered = len(st.session_state.answers)
        reviewed = len(st.session_state.marked_review)
        unanswered = TOTAL_QUESTIONS - answered

        st.warning("### ⚠️ Submit Confirmation")
        scol1, scol2, scol3 = st.columns(3)
        scol1.metric("Attempted", f"{answered}/{TOTAL_QUESTIONS}")
        scol2.metric("Unattempted", f"{unanswered}/{TOTAL_QUESTIONS}")
        scol3.metric("Marked for Review", reviewed)

        st.markdown("**Are you sure you want to submit the test?** This action cannot be undone.")

        bc1, bc2, _ = st.columns([1, 1, 3])
        with bc1:
            if st.button("✅ Yes, Submit", type="primary", use_container_width=True):
                st.session_state.test_submitted = True
                st.session_state.show_submit_confirm = False
                st.rerun()
        with bc2:
            if st.button("❌ Cancel", use_container_width=True):
                st.session_state.show_submit_confirm = False
                st.rerun()


# ── Auto-refresh mechanism ───────────────────────────────────
def setup_auto_refresh():
    """Inject JS to auto-refresh every 30 seconds during the test for timer updates."""
    if st.session_state.test_started and not st.session_state.test_submitted:
        remaining = get_remaining_seconds()
        # Refresh more frequently when time is low
        if remaining <= 60:
            interval = 5000   # every 5s in last minute
        elif remaining <= 300:
            interval = 10000  # every 10s in last 5 min
        else:
            interval = 30000  # every 30s otherwise

        # JavaScript-based countdown display + auto-refresh
        st.markdown(f"""
        <script>
        (function() {{
            var remaining = {int(remaining)};
            var interval = {interval};

            // Auto-refresh the page
            setTimeout(function() {{
                window.parent.location.reload();
            }}, interval);

            // Live countdown (cosmetic, updates between Streamlit reruns)
            var timerEl = document.querySelector('.timer-value');
            if (timerEl) {{
                setInterval(function() {{
                    remaining--;
                    if (remaining < 0) remaining = 0;
                    var h = Math.floor(remaining / 3600);
                    var m = Math.floor((remaining % 3600) / 60);
                    var s = remaining % 60;
                    var timeStr = String(h).padStart(2,'0') + ':' + String(m).padStart(2,'0') + ':' + String(s).padStart(2,'0');
                    timerEl.textContent = timeStr;
                    if (remaining <= 60) {{
                        timerEl.className = 'timer-value timer-danger';
                    }} else if (remaining <= 900) {{
                        timerEl.className = 'timer-value timer-warning';
                    }}
                    if (remaining <= 0) {{
                        window.parent.location.reload();
                    }}
                }}, 1000);
            }}
        }})();
        </script>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# RESULT SCREEN
# ══════════════════════════════════════════════════════════════

def render_result_screen():
    """Complete post-test analytics dashboard."""
    results = compute_results()

    if st.session_state.auto_submitted:
        st.error("⏰ **Time expired!** Your test has been automatically submitted.")

    # ── Hero score ───────────────────────────────────────────
    st.markdown(f"""
    <div class="result-hero">
        <div style="font-size:1rem;color:#a5b4fc;font-weight:600;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;">Test Result</div>
        <div class="result-score">{results['score']}</div>
        <div class="result-max">out of {MAX_MARKS}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Key metrics ──────────────────────────────────────────
    st.markdown(f"""
    <div class="stat-grid">
        <div class="stat-card"><div class="stat-label">Correct</div><div class="stat-value sv-green">{results['correct']}</div></div>
        <div class="stat-card"><div class="stat-label">Wrong</div><div class="stat-value sv-red">{results['wrong']}</div></div>
        <div class="stat-card"><div class="stat-label">Unattempted</div><div class="stat-value sv-yellow">{results['unattempted']}</div></div>
        <div class="stat-card"><div class="stat-label">Accuracy</div><div class="stat-value sv-cyan">{results['accuracy']:.1f}%</div></div>
        <div class="stat-card"><div class="stat-label">Attempt Rate</div><div class="stat-value sv-blue">{results['attempt_rate']:.1f}%</div></div>
        <div class="stat-card"><div class="stat-label">Negative Marks</div><div class="stat-value sv-red">−{results['wrong_marks']}</div></div>
        <div class="stat-card"><div class="stat-label">Percentage</div><div class="stat-value sv-accent">{results['percentage']:.1f}%</div></div>
        <div class="stat-card"><div class="stat-label">Positive Marks</div><div class="stat-value sv-green">+{results['correct_marks']}</div></div>
    </div>
    """, unsafe_allow_html=True)

    # ── Tabs for different analyses ──────────────────────────
    tabs = st.tabs([
        "📊 Subject Analysis",
        "📚 Chapter Analysis",
        "📝 Question Review",
        "🎯 Difficulty Analysis",
        "⚠️ Mistake Analysis",
        "📉 Negative Marking",
        "📋 Performance Report",
    ])

    # ── Tab 1: Subject-wise ──────────────────────────────────
    with tabs[0]:
        render_subject_analysis(results)

    # ── Tab 2: Chapter-wise ──────────────────────────────────
    with tabs[1]:
        render_chapter_analysis(results)

    # ── Tab 3: Question-wise ─────────────────────────────────
    with tabs[2]:
        render_question_analysis(results)

    # ── Tab 4: Difficulty ────────────────────────────────────
    with tabs[3]:
        render_difficulty_analysis(results)

    # ── Tab 5: Mistake Analysis ──────────────────────────────
    with tabs[4]:
        render_mistake_analysis(results)

    # ── Tab 6: Negative Marking ──────────────────────────────
    with tabs[5]:
        render_negative_marking_analysis(results)

    # ── Tab 7: Performance Report ────────────────────────────
    with tabs[6]:
        render_performance_report(results)


def render_subject_analysis(results):
    st.markdown('<div class="section-title">📊 Subject-wise Performance</div>', unsafe_allow_html=True)

    for subj in ["Chemistry", "Physics", "Mathematics"]:
        data = results["subject"][subj]
        total = data["total"]
        correct = data["correct"]
        wrong = data["wrong"]
        unattempted = data["unattempted"]
        attempted = correct + wrong
        accuracy = (correct / attempted * 100) if attempted > 0 else 0
        marks = correct * CORRECT_MARKS + wrong * WRONG_MARKS

        icon = {"Chemistry": "🧪", "Physics": "⚡", "Mathematics": "📐"}[subj]
        st.markdown(f"### {icon} {subj}")

        c1, c2, c3, c4, c5, c6 = st.columns(6)
        c1.metric("Total", total)
        c2.metric("Attempted", attempted)
        c3.metric("Correct", correct)
        c4.metric("Wrong", wrong)
        c5.metric("Marks", f"{marks}/{total*4}")
        c6.metric("Accuracy", f"{accuracy:.0f}%")

        # Bar chart
        import pandas as pd
        df = pd.DataFrame({
            "Category": ["Correct", "Wrong", "Unattempted"],
            "Count": [correct, wrong, unattempted],
        })
        st.bar_chart(df.set_index("Category"), color=["#10b981"])
        st.markdown("---")


def render_chapter_analysis(results):
    st.markdown('<div class="section-title">📚 Chapter-wise Performance</div>', unsafe_allow_html=True)

    import pandas as pd

    for subj in ["Chemistry", "Physics", "Mathematics"]:
        icon = {"Chemistry": "🧪", "Physics": "⚡", "Mathematics": "📐"}[subj]
        st.markdown(f"### {icon} {subj}")

        rows = []
        for topic_key, data in results["topic"].items():
            if topic_key.startswith(subj):
                topic_name = topic_key.split(" — ")[1]
                attempted = data["correct"] + data["wrong"]
                accuracy = (data["correct"] / attempted * 100) if attempted > 0 else 0
                marks = data["correct"] * CORRECT_MARKS + data["wrong"] * WRONG_MARKS
                rows.append({
                    "Topic": topic_name,
                    "Total": data["total"],
                    "Attempted": attempted,
                    "Correct": data["correct"],
                    "Wrong": data["wrong"],
                    "Accuracy": f"{accuracy:.0f}%",
                    "Marks": marks,
                })

        if rows:
            df = pd.DataFrame(rows)
            st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown("")


def render_question_analysis(results):
    st.markdown('<div class="section-title">📝 Question-wise Review</div>', unsafe_allow_html=True)

    filter_opt = st.selectbox("Filter by:", ["All", "Correct ✅", "Wrong ❌", "Unattempted ⬜"], key="q_filter")

    for qr in results["question_results"]:
        if filter_opt == "Correct ✅" and qr["status"] != "correct":
            continue
        if filter_opt == "Wrong ❌" and qr["status"] != "wrong":
            continue
        if filter_opt == "Unattempted ⬜" and qr["status"] != "unattempted":
            continue

        q = qr["question"]
        idx = qr["index"]

        # Status indicator
        if qr["status"] == "correct":
            status_icon = "✅"
            marks_str = f"+{CORRECT_MARKS}"
            tag_class = "correct-tag"
        elif qr["status"] == "wrong":
            status_icon = "❌"
            marks_str = str(WRONG_MARKS)
            tag_class = "wrong-tag"
        else:
            status_icon = "⬜"
            marks_str = "0"
            tag_class = "skip-tag"

        with st.expander(f"Q{idx+1}. {q['subject']} — {q['topic']}  {status_icon}  ({marks_str} marks)"):
            st.markdown(f"**{q['question']}**")
            st.markdown("")

            for opt_key, opt_val in q["options"].items():
                prefix = ""
                if opt_key == qr["correct_answer"]:
                    prefix = "✅ "
                elif opt_key == qr["user_answer"] and qr["status"] == "wrong":
                    prefix = "❌ "
                st.markdown(f"{prefix}**{opt_key})** {opt_val}")

            st.markdown("")

            if qr["status"] == "correct":
                st.success(f"Your answer: **{qr['user_answer']}** — Correct! (+{CORRECT_MARKS} marks)")
            elif qr["status"] == "wrong":
                st.error(
                    f"Your answer: **{qr['user_answer']}** | "
                    f"Correct answer: **{qr['correct_answer']}** ({WRONG_MARKS} mark)"
                )
                if qr["mistake_type"]:
                    st.warning(f"🔍 Mistake type: **{qr['mistake_type']}**")
            else:
                st.info(f"Not attempted. Correct answer: **{qr['correct_answer']}** (0 marks)")

            st.markdown(f"""<div class="explanation-box"><strong>📖 Explanation:</strong>\n\n{q['explanation']}</div>""", unsafe_allow_html=True)


def render_difficulty_analysis(results):
    st.markdown('<div class="section-title">🎯 Difficulty-wise Performance</div>', unsafe_allow_html=True)

    import pandas as pd

    rows = []
    for diff in ["Medium", "Hard", "Very Hard"]:
        data = results["difficulty"].get(diff, {"total": 0, "correct": 0, "wrong": 0, "unattempted": 0, "attempted": 0})
        attempted = data["correct"] + data["wrong"]
        accuracy = (data["correct"] / attempted * 100) if attempted > 0 else 0
        rows.append({
            "Difficulty": diff,
            "Total": data["total"],
            "Attempted": attempted,
            "Correct": data["correct"],
            "Wrong": data["wrong"],
            "Unattempted": data["unattempted"],
            "Accuracy": f"{accuracy:.0f}%",
        })

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("")
    st.markdown("#### Performance Breakdown by Difficulty")

    for diff in ["Medium", "Hard", "Very Hard"]:
        data = results["difficulty"].get(diff, {"total": 0, "correct": 0, "wrong": 0})
        total = data.get("total", 0)
        if total == 0:
            continue
        correct = data["correct"]
        wrong = data["wrong"]

        col1, col2 = st.columns([1, 3])
        with col1:
            emoji = {"Medium": "🟦", "Hard": "🟧", "Very Hard": "🟥"}[diff]
            st.markdown(f"**{emoji} {diff}**")
        with col2:
            st.progress(correct / total if total > 0 else 0, text=f"{correct}/{total} correct")


def render_mistake_analysis(results):
    st.markdown('<div class="section-title">⚠️ Mistake Analysis</div>', unsafe_allow_html=True)

    mistake_types = results["mistake_types"]

    if not mistake_types:
        st.success("🎉 No mistakes to analyze! Perfect score or all unattempted.")
        return

    import pandas as pd

    counter = Counter(mistake_types)
    total_mistakes = len(mistake_types)

    st.markdown(f"**Total wrong answers:** {total_mistakes}")

    rows = []
    for mtype, count in counter.most_common():
        # Extract the category from the distractor info string
        category = mtype.split(" — ")[0] if " — " in mtype else mtype
        rows.append({
            "Mistake Type": category,
            "Count": count,
            "Percentage": f"{count/total_mistakes*100:.0f}%",
        })

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)

    # Most common mistake
    most_common = counter.most_common(1)[0]
    st.error(f"🔴 **Most common mistake type:** {most_common[0]} ({most_common[1]} occurrences)")

    # Categorize
    st.markdown("---")
    st.markdown("#### Mistake Categories")

    conceptual = sum(v for k, v in counter.items() if "Conceptual" in k)
    calculation = sum(v for k, v in counter.items() if "Calculation" in k)
    formula = sum(v for k, v in counter.items() if "Formula" in k)
    silly = sum(v for k, v in counter.items() if "Silly" in k)
    other = total_mistakes - conceptual - calculation - formula - silly

    cats = [
        ("🧠 Conceptual mistakes", conceptual),
        ("🔢 Calculation mistakes", calculation),
        ("📐 Formula mistakes", formula),
        ("😅 Silly mistakes", silly),
    ]
    if other > 0:
        cats.append(("❓ Other mistakes", other))

    for label, count in cats:
        if count > 0:
            st.markdown(f"- **{label}:** {count} ({count/total_mistakes*100:.0f}%)")


def render_negative_marking_analysis(results):
    st.markdown('<div class="section-title">📉 Negative Marking Analysis</div>', unsafe_allow_html=True)

    wrong = results["wrong"]
    wrong_marks = results["wrong_marks"]
    correct = results["correct"]
    score = results["score"]
    attempted = results["attempted"]

    c1, c2, c3 = st.columns(3)
    c1.metric("Marks Lost (Negative)", f"−{wrong_marks}")
    c2.metric("Wrong Attempts", wrong)
    c3.metric("Score Without Negatives", f"{results['correct_marks']}/{MAX_MARKS}")

    st.markdown("")

    # Attempt accuracy
    attempt_accuracy = (correct / attempted * 100) if attempted > 0 else 0
    st.markdown(f"**Attempt Accuracy:** {attempt_accuracy:.1f}%")

    if attempt_accuracy < 50:
        st.error(
            "🔴 Your attempt accuracy is below 50%. This means **excessive guessing** is significantly "
            "hurting your score. Only attempt questions you are reasonably confident about."
        )
    elif attempt_accuracy < 70:
        st.warning(
            "🟡 Your attempt accuracy is moderate. Some wrong answers may be from risky guesses. "
            "Consider being more selective when unsure."
        )
    else:
        st.success(
            "🟢 Your attempt accuracy is good. You are selecting questions wisely. "
            "You may consider attempting a few more questions if time permits."
        )

    st.markdown("---")

    # Impact analysis
    score_without_neg = results["correct_marks"]
    penalty_impact = wrong_marks
    st.markdown(f"""
    #### Impact of Negative Marking

    | Metric | Value |
    |--------|-------|
    | Gross positive marks | +{score_without_neg} |
    | Penalty from wrong answers | −{penalty_impact} |
    | Net score | **{score}** |
    | Penalty as % of positive marks | {(penalty_impact/score_without_neg*100) if score_without_neg > 0 else 0:.1f}% |
    | Estimated risky guesses (accuracy < 25%) | {max(0, wrong - correct // 3)} |
    """)

    if penalty_impact > score_without_neg * 0.3:
        st.error("⚠️ Negative marks account for over 30% of your positive marks. Focus on accuracy over speed.")


def render_performance_report(results):
    st.markdown('<div class="section-title">📋 Final Performance Report</div>', unsafe_allow_html=True)

    # Identify strong and weak topics
    strong_topics = []
    weak_topics = []
    revision_topics = []

    for topic_key, data in results["topic"].items():
        total = data["total"]
        correct = data["correct"]
        wrong = data["wrong"]
        attempted = correct + wrong
        accuracy = (correct / attempted * 100) if attempted > 0 else 0

        topic_name = topic_key.split(" — ")[1] if " — " in topic_key else topic_key
        subj = topic_key.split(" — ")[0] if " — " in topic_key else ""

        if attempted > 0 and accuracy >= 75:
            strong_topics.append(f"{topic_name} ({subj})")
        elif attempted > 0 and accuracy < 50:
            weak_topics.append(f"{topic_name} ({subj})")
        unattempted = data["unattempted"]
        if wrong > 0 or unattempted > 0:
            revision_topics.append((f"{topic_name} ({subj})", wrong + unattempted, accuracy))

    # Strong areas
    st.markdown("### 💪 Strong Areas")
    if strong_topics:
        for t in strong_topics:
            st.markdown(f"- ✅ {t}")
    else:
        st.info("No topics with ≥75% accuracy yet. Keep practicing!")

    st.markdown("")

    # Weak areas
    st.markdown("### ⚠️ Weak Areas")
    if weak_topics:
        for t in weak_topics:
            st.markdown(f"- ❌ {t}")
    else:
        st.success("No major weak areas detected. Great job!")

    st.markdown("")

    # Priority revision
    st.markdown("### 📌 Priority Revision Topics")
    revision_sorted = sorted(revision_topics, key=lambda x: (-x[1], x[2]))
    for topic, issues, acc in revision_sorted[:8]:
        st.markdown(f"- 🔄 **{topic}** — {issues} incorrect/unattempted, accuracy {acc:.0f}%")

    st.markdown("")

    # Specific recommendations
    st.markdown("### 📖 Recommended Practice")

    recommendations = []

    for topic_key, data in results["topic"].items():
        topic_name = topic_key.split(" — ")[1] if " — " in topic_key else topic_key
        correct = data["correct"]
        wrong = data["wrong"]
        unattempted = data["unattempted"]
        total = data["total"]

        if wrong > 0:
            if "Kinetics" in topic_name:
                recommendations.append(f"Practice {wrong*5}+ Chemical Kinetics problems focusing on rate law, integrated equations, and Arrhenius equation.")
            elif "Electrostatics" in topic_name:
                recommendations.append(f"Solve {wrong*5}+ Electrostatics problems covering Gauss's law, capacitor combinations, and potential energy of charge systems.")
            elif "Trigonometry" in topic_name:
                recommendations.append(f"Practice {wrong*3}+ trigonometric equation problems and inverse trig function evaluations.")
            elif "3D Geometry" in topic_name:
                recommendations.append(f"Revise section formula, direction cosines, and practice {wrong*3}+ 3D geometry coordinate problems.")
            elif "Reasoning" in topic_name:
                recommendations.append(f"Review contrapositive, negation, and quantifier rules. Practice {wrong*3}+ logical reasoning problems.")
            elif "Dimensions" in topic_name:
                recommendations.append(f"Practice {wrong*3}+ dimensional analysis problems including finding dimensions of unknown quantities.")
            else:
                recommendations.append(f"Revise {topic_name} concepts and solve {wrong*4}+ practice problems.")

        if unattempted > 0 and wrong == 0 and correct == 0:
            recommendations.append(f"Study {topic_name} from scratch — all questions were left unattempted.")

    if not recommendations:
        recommendations.append("Excellent performance! Focus on timed practice to improve speed.")

    for rec in recommendations[:10]:
        st.markdown(f"- 📝 {rec}")

    st.markdown("---")

    # Overall verdict
    score = results["score"]
    pct = results["percentage"]

    st.markdown("### 🏆 Overall Verdict")
    if pct >= 80:
        st.success(f"**Outstanding!** Score: {score}/{MAX_MARKS} ({pct:.1f}%). You are well-prepared for the exam.")
    elif pct >= 60:
        st.info(f"**Good performance.** Score: {score}/{MAX_MARKS} ({pct:.1f}%). Focus on weak areas to push into the top bracket.")
    elif pct >= 40:
        st.warning(f"**Average performance.** Score: {score}/{MAX_MARKS} ({pct:.1f}%). Significant improvement needed in multiple areas.")
    elif pct >= 20:
        st.error(f"**Below average.** Score: {score}/{MAX_MARKS} ({pct:.1f}%). Review fundamentals and practice extensively.")
    else:
        st.error(f"**Needs major improvement.** Score: {score}/{MAX_MARKS} ({pct:.1f}%). Start with NCERT basics before attempting mock tests.")


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

def main():
    inject_css()
    init_session()

    if st.session_state.test_submitted:
        render_result_screen()
    elif st.session_state.test_started:
        render_question_screen()
        setup_auto_refresh()
    else:
        render_start_screen()


if __name__ == "__main__":
    main()
