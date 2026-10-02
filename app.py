"""
PCM Advanced Mock Test — Streamlit Application
================================================
A complete competitive-exam mock test with:
- 45 JEE-level questions (16 Phys + 16 Chem + 13 Math with 11 Trigonometry questions)
- Live JavaScript countdown timer with auto-submit
- Section-relative question palette (1 to 16 in Phys, 1 to 16 in Chem, 1 to 13 in Math)
- Direct 1-click jump navigation
- Comprehensive post-test analytics
"""

import streamlit as st
import streamlit.components.v1 as components
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
        font-size: 1.1rem;
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

    .q-text {
        font-size: 1.05rem;
        line-height: 1.7;
        color: var(--text-primary);
        margin-bottom: 20px;
        white-space: pre-wrap;
    }

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

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    div.stButton > button {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        border-radius: 8px;
        padding: 6px 14px;
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
        st.markdown("#### ⚡ Section 1: Physics (16 Qs)")
        st.markdown("""
        **Questions 1 to 16:**
        - Electrostatics & Gauss's Law
        - Capacitors & Dielectrics
        - Current Electricity & Wheatstone Bridge
        - Potentiometer & Drift Velocity
        - Moving Charges & Magnetism
        """)

    with col2:
        st.markdown("#### 🧪 Section 2: Chemistry (16 Qs)")
        st.markdown("""
        **Questions 1 to 16 (Q17–32 Overall):**
        - Chemical Kinetics & Rate Laws
        - Arrhenius Equation & Activation Energy
        - Solid State (fcc/bcc Density & Packing)
        - Solutions (Raoult's Law & Colligative Properties)
        """)

    with col3:
        st.markdown("#### 📐 Section 3: Mathematics (13 Qs)")
        st.markdown("""
        **Questions 1 to 13 (Q33–45 Overall):**
        - **Trigonometry (11 Questions)** — Identities, Equations, Max/Min Values, Inverse Trig, Cosine/Sine Products, Triangle Properties, Heights & Distances, General Solutions, Principal Values
        - Definite Integrals & Area Under Curves
        """)

    st.markdown("---")
    st.markdown("""
    > **Instructions:**
    > - The test is structured into **3 Sections**: Section 1 (Physics 16 Qs), Section 2 (Chemistry 16 Qs), and Section 3 (Mathematics 13 Qs).
    > - Buttons inside each section count cleanly from **1 to 16** (or 1 to 13 for Math).
    > - Click any question number directly in the palette to jump to it instantly.
    > - Use **Save & Next** to record your choice and move to the next question.
    > - The test will **auto-submit** when the 3-hour timer reaches zero.
    """)

    st.markdown("")
    c1, c2, c3 = st.columns([2, 1, 2])
    with c2:
        if st.button("🚀  START TEST", use_container_width=True, type="primary"):
            st.session_state.test_started = True
            st.session_state.start_time = datetime.now()
            st.rerun()


def render_timer_sidebar():
    """Sidebar with live JS timer, section palette, and navigation."""
    remaining = get_remaining_seconds()

    # Live JavaScript countdown timer embedded in sidebar
    timer_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;800&display=swap');
      body {{
        margin: 0;
        padding: 0;
        background: transparent;
        font-family: 'Inter', sans-serif;
      }}
      .timer-box {{
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
        border: 1px solid rgba(99,102,241,0.35);
        border-radius: 14px;
        padding: 12px 16px;
        text-align: center;
        box-shadow: 0 0 20px rgba(99,102,241,0.25);
      }}
      .timer-lbl {{
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1.5px;
        color: #a5b4fc;
        text-transform: uppercase;
        margin-bottom: 4px;
      }}
      .timer-val {{
        font-size: 32px;
        font-weight: 800;
        font-variant-numeric: tabular-nums;
        color: #e0e7ff;
        letter-spacing: 2px;
      }}
      .warn {{ color: #fbbf24 !important; }}
      .danger {{ color: #f87171 !important; animation: pulse 1s infinite; }}
      @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.5; }}
      }}
    </style>
    </head>
    <body>
      <div class="timer-box">
        <div class="timer-lbl">⏱️ Time Remaining</div>
        <div id="clock" class="timer-val">--:--:--</div>
      </div>
      <script>
        var remaining = {int(remaining)};
        var target = Date.now() + (remaining * 1000);

        function tick() {{
          var now = Date.now();
          var diff = Math.max(0, Math.floor((target - now) / 1000));
          var h = Math.floor(diff / 3600);
          var m = Math.floor((diff % 3600) / 60);
          var s = diff % 60;

          var hStr = (h < 10 ? '0' : '') + h;
          var mStr = (m < 10 ? '0' : '') + m;
          var sStr = (s < 10 ? '0' : '') + s;

          var el = document.getElementById('clock');
          if (el) {{
            el.innerText = hStr + ':' + mStr + ':' + sStr;
            if (diff <= 60) {{
              el.className = 'timer-val danger';
            }} else if (diff <= 900) {{
              el.className = 'timer-val warn';
            }}
          }}
        }}
        tick();
        setInterval(tick, 1000);
      </script>
    </body>
    </html>
    """

    with st.sidebar:
        components.html(timer_html, height=105)

    # Progress stats
    answered = len(st.session_state.answers)
    reviewed = len(st.session_state.marked_review)
    st.sidebar.markdown(f"**Answered:** {answered}/{TOTAL_QUESTIONS}  •  **Review:** {reviewed}")
    st.sidebar.progress(answered / TOTAL_QUESTIONS)

    # Calculate section stats
    section_stats = {}
    for subj in ["Physics", "Chemistry", "Mathematics"]:
        q_indices = [i for i, q in enumerate(QUESTIONS) if q["subject"] == subj]
        tot = len(q_indices)
        att = sum(1 for i in q_indices if i in st.session_state.answers)
        section_stats[subj] = {"total": tot, "attempted": att, "indices": q_indices}

    # Section-wise Question Palette counting 1..16 (or 1..13)
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### 🧩 Question Palette")
    st.sidebar.markdown("<small style='color:#94a3b8;'>Click any number to jump directly</small>", unsafe_allow_html=True)

    sections = [
        ("⚡ Section 1: Physics", "Physics"),
        ("🧪 Section 2: Chemistry", "Chemistry"),
        ("📐 Section 3: Mathematics", "Mathematics")
    ]

    for label, subj in sections:
        stats = section_stats[subj]
        st.sidebar.markdown(f"**{label}** ({stats['total']} Qs | {stats['attempted']}/{stats['total']} Answered)")
        
        indices = stats['indices']
        # Render clean grid row by row (4 items per row)
        for row_start in range(0, len(indices), 4):
            cols = st.sidebar.columns(4)
            row_indices = indices[row_start : row_start + 4]
            for col_idx, q_idx in enumerate(row_indices):
                sec_q_num = row_start + col_idx + 1  # 1 to 16 in Physics/Chem, 1 to 13 in Math
                is_current = (q_idx == st.session_state.current_q)

                btn_label = str(sec_q_num)
                btn_type = "primary" if is_current else "secondary"

                if cols[col_idx].button(btn_label, key=f"p_btn_{q_idx}", use_container_width=True, type=btn_type):
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

    # Section stats for navigation bar
    section_stats = {}
    for subj in ["Physics", "Chemistry", "Mathematics"]:
        q_indices = [i for i, item in enumerate(QUESTIONS) if item["subject"] == subj]
        tot = len(q_indices)
        att = sum(1 for i in q_indices if i in st.session_state.answers)
        section_stats[subj] = {"total": tot, "attempted": att, "indices": q_indices}

    # Section Quick Navigation Bar
    st.markdown("##### 📍 Jump to Section:")
    sec_cols = st.columns(3)
    sections_info = [
        ("⚡ Section 1: Physics (16 Qs)", "Physics"),
        ("🧪 Section 2: Chemistry (16 Qs)", "Chemistry"),
        ("📐 Section 3: Mathematics (13 Qs)", "Mathematics")
    ]
    curr_subj = q["subject"]

    for sc, (sec_title, sec_subj) in zip(sec_cols, sections_info):
        stats = section_stats[sec_subj]
        is_active_sec = (curr_subj == sec_subj)
        tab_label = f"{sec_title} — ({stats['attempted']}/{stats['total']} Done)"
        
        with sc:
            if st.button(
                tab_label, 
                key=f"sec_tab_{sec_subj}", 
                type="primary" if is_active_sec else "secondary",
                use_container_width=True
            ):
                first_q_in_sec = stats["indices"][0]
                st.session_state.current_q = first_q_in_sec
                st.rerun()

    # Subject badge class
    subj_cls = {
        "Physics": "badge-physics",
        "Chemistry": "badge-chemistry",
        "Mathematics": "badge-mathematics",
    }.get(q["subject"], "")

    # Calculate section-relative question number
    subj_indices = section_stats[curr_subj]["indices"]
    sec_q_num = subj_indices.index(idx) + 1
    sec_total = len(subj_indices)

    st.markdown(f"""
    <div class="question-card">
        <div class="q-header">
            <span class="q-number">Section {['Physics','Chemistry','Mathematics'].index(curr_subj)+1}: {q['subject']} — Question {sec_q_num} of {sec_total} <small style="color:#94a3b8;font-weight:400;">(Overall Q{idx+1}/45)</small></span>
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
    default_idx = option_keys.index(current_ans) if (current_ans and current_ans in option_keys) else None

    # Callback to immediately sync answer to session state on click
    def on_answer_select():
        radio_val = st.session_state.get(f"radio_{idx}")
        if radio_val:
            ans_key = radio_val.split(")")[0].strip()
            st.session_state.answers[idx] = ans_key

    selected = st.radio(
        "Select your answer:",
        options_list,
        index=default_idx,
        key=f"radio_{idx}",
        on_change=on_answer_select,
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

    with tabs[0]:
        render_subject_analysis(results)

    with tabs[1]:
        render_chapter_analysis(results)

    with tabs[2]:
        render_question_analysis(results)

    with tabs[3]:
        render_difficulty_analysis(results)

    with tabs[4]:
        render_mistake_analysis(results)

    with tabs[5]:
        render_negative_marking_analysis(results)

    with tabs[6]:
        render_performance_report(results)


def render_subject_analysis(results):
    st.markdown('<div class="section-title">📊 Subject-wise Performance</div>', unsafe_allow_html=True)

    for subj in ["Physics", "Chemistry", "Mathematics"]:
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

    for subj in ["Physics", "Chemistry", "Mathematics"]:
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

        if qr["status"] == "correct":
            status_icon = "✅"
            marks_str = f"+{CORRECT_MARKS}"
        elif qr["status"] == "wrong":
            status_icon = "❌"
            marks_str = str(WRONG_MARKS)
        else:
            status_icon = "⬜"
            marks_str = "0"

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
        category = mtype.split(" — ")[0] if " — " in mtype else mtype
        rows.append({
            "Mistake Type": category,
            "Count": count,
            "Percentage": f"{count/total_mistakes*100:.0f}%",
        })

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)


def render_negative_marking_analysis(results):
    st.markdown('<div class="section-title">📉 Negative Marking Analysis</div>', unsafe_allow_html=True)

    wrong = results["wrong"]
    wrong_marks = results["wrong_marks"]
    correct = results["correct"]
    score = results["score"]

    c1, c2, c3 = st.columns(3)
    c1.metric("Marks Lost (Negative)", f"−{wrong_marks}")
    c2.metric("Wrong Attempts", wrong)
    c3.metric("Score Without Negatives", f"{results['correct_marks']}/{MAX_MARKS}")


def render_performance_report(results):
    st.markdown('<div class="section-title">📋 Final Performance Report</div>', unsafe_allow_html=True)

    strong_topics = []
    weak_topics = []

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

    st.markdown("### 💪 Strong Areas")
    if strong_topics:
        for t in strong_topics:
            st.markdown(f"- ✅ {t}")
    else:
        st.info("No topics with ≥75% accuracy yet. Keep practicing!")

    st.markdown("")

    st.markdown("### ⚠️ Weak Areas")
    if weak_topics:
        for t in weak_topics:
            st.markdown(f"- ❌ {t}")
    else:
        st.success("No major weak areas detected. Great job!")

    score = results["score"]
    pct = results["percentage"]

    st.markdown("---")
    st.markdown("### 🏆 Overall Verdict")
    if pct >= 80:
        st.success(f"**Outstanding!** Score: {score}/{MAX_MARKS} ({pct:.1f}%). You are well-prepared for the exam.")
    elif pct >= 60:
        st.info(f"**Good performance.** Score: {score}/{MAX_MARKS} ({pct:.1f}%). Focus on weak areas to push into the top bracket.")
    elif pct >= 40:
        st.warning(f"**Average performance.** Score: {score}/{MAX_MARKS} ({pct:.1f}%). Significant improvement needed in multiple areas.")
    else:
        st.error(f"**Below average.** Score: {score}/{MAX_MARKS} ({pct:.1f}%). Review fundamentals and practice extensively.")


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
    else:
        render_start_screen()


if __name__ == "__main__":
    main()
