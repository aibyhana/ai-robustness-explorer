"""
AI Regulatory Stress Test: Employment Screening System
Interactive assessment for regulatory decision-makers.

Stanford SAFE: Designing Interactive Modules to Introduce
High-Ranking Decision Makers to Technical AI Fundamentals.
"""

import streamlit as st
import numpy as np

st.set_page_config(
    page_title="AI Regulatory Stress Test",
    page_icon="",
    layout="centered",
)

# ── Styles ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

    .block-container { padding-top: 0rem; max-width: 740px; }

    * { font-family: 'DM Sans', system-ui, sans-serif !important; }

    /* Hero banner */
    .hero {
        position: relative;
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 2rem;
        height: 260px;
    }
    .hero img {
        width: 100%; height: 100%;
        object-fit: cover;
        filter: brightness(0.35);
    }
    .hero-overlay {
        position: absolute; top: 0; left: 0;
        width: 100%; height: 100%;
        display: flex; flex-direction: column;
        justify-content: flex-end;
        padding: 2rem 2.2rem;
    }
    .hero-title {
        font-size: 1.85rem; font-weight: 700;
        color: #fff; line-height: 1.15;
        letter-spacing: -0.02em;
    }
    .hero-sub {
        font-size: 0.92rem; color: rgba(255,255,255,0.75);
        margin-top: 0.4rem; line-height: 1.5;
        max-width: 520px;
    }

    /* Phase headers */
    .phase-strip {
        display: flex; align-items: center; gap: 12px;
        margin-bottom: 1.2rem;
        padding-bottom: 0.8rem;
        border-bottom: 2px solid #eee;
    }
    .phase-num {
        background: #111; color: #fff;
        font-size: 0.7rem; font-weight: 700;
        padding: 4px 10px; border-radius: 100px;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        white-space: nowrap;
    }
    .phase-title {
        font-size: 1.15rem; font-weight: 600;
        color: #111;
    }

    /* Cards */
    .stat-card {
        background: #fafafa; border-radius: 12px;
        padding: 1.1rem; text-align: center;
        border: 1px solid #eee;
    }
    .stat-val {
        font-size: 2rem; font-weight: 700;
        color: #111; line-height: 1.15;
    }
    .stat-label {
        font-size: 0.78rem; color: #999;
        margin-top: 0.15rem; font-weight: 500;
    }
    .candidate-card {
        background: #fff; border: 1px solid #eee;
        border-radius: 14px; padding: 1.3rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .candidate-card-photo {
        display: flex; align-items: center; gap: 14px;
        margin-bottom: 1rem;
    }
    .candidate-photo {
        width: 52px; height: 52px; border-radius: 50%;
        object-fit: cover; border: 2px solid #eee;
    }
    .candidate-name {
        font-size: 1.05rem; font-weight: 600; color: #111;
    }
    .candidate-sub {
        font-size: 0.82rem; color: #888; margin-top: 1px;
    }
    .detail-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
    }
    .detail-cell {
        background: #f7f7f5; border-radius: 8px;
        padding: 10px 14px;
    }
    .detail-label {
        font-size: 0.7rem; color: #999;
        text-transform: uppercase; letter-spacing: 0.04em;
        font-weight: 600;
    }
    .detail-val {
        font-size: 0.88rem; font-weight: 600;
        color: #222; margin-top: 2px;
    }

    /* Notes */
    .note {
        padding: 0.9rem 1.1rem; margin: 0.7rem 0;
        font-size: 0.87rem; line-height: 1.55;
        border-radius: 10px;
    }
    .note-blue {
        background: #eef3ff; color: #1e3a5f;
        border: 1px solid #d0ddf0;
    }
    .note-amber {
        background: #fef8ec; color: #5c4813;
        border: 1px solid #f0e0b0;
    }
    .note-red {
        background: #fef0f0; color: #6b1a1a;
        border: 1px solid #f0c8c8;
    }
    .note-green {
        background: #eef6ee; color: #1a4a1a;
        border: 1px solid #c8e0c8;
    }

    /* Criteria box */
    .criteria-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #f0f1ee 100%);
        border: 1px solid #e0e0dc;
        border-radius: 14px; padding: 1.4rem 1.6rem;
        margin-bottom: 1.5rem;
        font-size: 0.88rem; line-height: 1.65;
    }
    .criteria-title {
        font-size: 0.95rem; font-weight: 700;
        color: #111; margin-bottom: 0.6rem;
    }

    /* Assessment cards on intro */
    .assess-card {
        background: #fff; border: 1px solid #eee;
        border-radius: 12px; padding: 1.2rem;
        text-align: center; height: 100%;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        transition: transform 0.15s ease;
    }
    .assess-card:hover { transform: translateY(-2px); }
    .assess-num {
        font-size: 0.65rem; font-weight: 700;
        color: #999; letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.3rem;
    }
    .assess-title {
        font-size: 0.92rem; font-weight: 600; color: #111;
    }
    .assess-desc {
        font-size: 0.78rem; color: #888;
        margin-top: 0.2rem;
    }

    /* Weight bars */
    .bar-bg {
        height: 6px; background: #eee;
        border-radius: 3px; overflow: hidden;
        margin-top: 5px;
    }
    .bar-fill {
        height: 100%; border-radius: 3px;
        transition: width 0.3s ease;
    }

    /* Comparison cards */
    .compare-card {
        background: #fff; border: 1px solid #eee;
        border-radius: 12px; padding: 1rem 1.2rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .compare-header {
        display: flex; justify-content: space-between;
        align-items: center; margin-bottom: 0.7rem;
    }
    .compare-label {
        font-size: 0.85rem; font-weight: 600; color: #111;
    }
    .decision-badge {
        font-size: 0.72rem; font-weight: 600;
        padding: 3px 10px; border-radius: 100px;
    }
    .badge-yes {
        background: #e6f4e6; color: #1a6b1a;
    }
    .badge-no {
        background: #fce8e8; color: #8b1a1a;
    }

    .footer-text {
        text-align: center; color: #bbb;
        font-size: 0.72rem; margin-top: 2.5rem;
        padding-top: 1rem;
        border-top: 1px solid #eee;
    }

    /* Progress bar override */
    .stProgress > div > div > div > div {
        background: #111 !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Unsplash photos for candidates ───────────────────────────────────────
PHOTOS = {
    "Katrin Bauer": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=100&h=100&fit=crop&crop=face",
    "Heinrich Vogel": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&h=100&fit=crop&crop=face",
    "Sophie Laurent": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=100&h=100&fit=crop&crop=face",
    "Lukas Schmidt": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face",
    "Brigitte Engel": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=100&h=100&fit=crop&crop=face",
    "Felix Mayer": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=100&h=100&fit=crop&crop=face",
    "Amira Hassan": "https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=100&h=100&fit=crop&crop=face",
    "Wolfgang Krause": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop&crop=face",
}

HERO_IMG = "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&h=500&fit=crop"

# ── Data ─────────────────────────────────────────────────────────────────
EDU = ["No formal degree", "Vocational qualification", "Bachelor's degree",
       "Master's degree", "Doctorate"]
LANG_NAMES = {
    1: "German",
    2: "German, English",
    3: "German, English, French",
    4: "German, English, French, Spanish",
}

PEOPLE = [
    dict(name="Katrin Bauer", exp=8, edu=3, lang=3, age=34,
         bg="Municipal planning office, 8 years in project management"),
    dict(name="Heinrich Vogel", exp=6, edu=2, lang=2, age=54,
         bg="State government, policy implementation and coordination"),
    dict(name="Sophie Laurent", exp=4, edu=1, lang=4, age=28,
         bg="EU translation office, administrative support"),
    dict(name="Lukas Schmidt", exp=5, edu=4, lang=2, age=31,
         bg="University research institute, published policy papers"),
    dict(name="Brigitte Engel", exp=10, edu=2, lang=2, age=49,
         bg="Federal ministry, interdepartmental coordination"),
    dict(name="Felix Mayer", exp=1, edu=2, lang=2, age=24,
         bg="City council internship, recent graduate"),
    dict(name="Amira Hassan", exp=4, edu=3, lang=4, age=29,
         bg="International development agency, policy analysis"),
    dict(name="Wolfgang Krause", exp=9, edu=3, lang=2, age=51,
         bg="Parliamentary research service, legislative analysis"),
]

R2_PAIRS = [
    dict(
        a=dict(exp=7, edu=3, lang=2, age=33),
        b=dict(exp=7, edu=3, lang=2, age=48),
        diff="age", label="Age",
        desc="15 years older (33 versus 48)",
        insight=(
            "The position criteria explicitly state that age is not a "
            "relevant factor. The AI nonetheless treats it as one. This "
            "constitutes automated age discrimination, concealed within "
            "a system that reports high overall accuracy."
        ),
    ),
    dict(
        a=dict(exp=5, edu=3, lang=3, age=35),
        b=dict(exp=5, edu=3, lang=2, age=35),
        diff="lang", label="Languages",
        desc="one fewer language (3 versus 2)",
        insight=(
            "Both candidates meet the language requirement of two. A "
            "third language is listed as preferred, not required. "
            "The AI treats it as decisive, giving disproportionate "
            "weight to a non-essential qualification."
        ),
    ),
    dict(
        a=dict(exp=8, edu=2, lang=2, age=36),
        b=dict(exp=4, edu=3, lang=2, age=36),
        diff="exp", label="Experience versus Education",
        desc="4 fewer years but a master's instead of a bachelor's",
        insight=(
            "The AI heavily favours formal education over practical "
            "experience. An 8-year veteran with a bachelor's degree is "
            "rejected while a 4-year master's graduate is accepted. "
            "Whether this trade-off is appropriate is a policy decision "
            "that should not be delegated to an algorithm."
        ),
    ),
    dict(
        a=dict(exp=6, edu=3, lang=2, age=30),
        b=dict(exp=6, edu=3, lang=2, age=52),
        diff="age", label="Age",
        desc="22 years older (30 versus 52)",
        insight=(
            "Identical qualifications produce opposite outcomes, "
            "determined entirely by age. This is precisely the type of "
            "automated discrimination that the EU AI Act's high-risk "
            "classification for employment systems is designed to address."
        ),
    ),
]

FIELD_LABELS = {"exp": "Experience", "edu": "Education",
                "lang": "Languages", "age": "Age"}


def ground_truth(c):
    edu, exp, lang = c["edu"], c["exp"], c["lang"]
    if edu < 2:
        return 0
    if edu >= 3 and exp >= 2:
        return 1
    if edu >= 2 and exp >= 5:
        return 1
    if edu >= 2 and exp >= 3 and lang >= 3:
        return 1
    return 0


_W = dict(exp=0.14, edu=0.85, lang=0.55, age=-0.038, bias=-2.4)


def ai_prob(c):
    z = (_W["exp"] * c["exp"] + _W["edu"] * c["edu"]
         + _W["lang"] * c["lang"] + _W["age"] * c["age"] + _W["bias"])
    return 1 / (1 + np.exp(-z))


def ai_pred(c):
    return 1 if ai_prob(c) > 0.5 else 0


def fmt_field(key, val):
    if key == "exp":
        return f"{val} year{'s' if val != 1 else ''}"
    if key == "edu":
        return EDU[val]
    if key == "lang":
        return LANG_NAMES.get(val, str(val))
    return str(val)


# ── Session state ────────────────────────────────────────────────────────
_defaults = dict(
    phase="intro",
    r1_idx=0, r1_you=0, r1_ai=0, r1_errors=[],
    r1_feedback=None, r1_decided=False,
    r2_idx=0, r2_score=0, r2_feedback=None, r2_decided=False,
    r3_discoveries=[],
)
for _k, _v in _defaults.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v

phase = st.session_state.phase


# ══════════════════════════════════════════════════════════════════════════
# INTRO
# ══════════════════════════════════════════════════════════════════════════
if phase == "intro":
    st.markdown(
        f'<div class="hero">'
        f'<img src="{HERO_IMG}" alt="">'
        f'<div class="hero-overlay">'
        f'<div class="hero-title">AI Regulatory Stress Test</div>'
        f'<div class="hero-sub">'
        f'A government agency proposes using AI to screen civil service '
        f'applications. The vendor reports 92% accuracy. Evaluate that '
        f'claim through three structured assessments.'
        f'</div></div></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="criteria-box">'
        '<div class="criteria-title">Position: Policy Advisor, '
        'Civil Service</div>'
        '<b>Required:</b> Bachelor\'s degree or higher. Minimum 3 years '
        'of relevant professional experience.<br>'
        '<b>Preferred:</b> Master\'s degree or doctorate. 7 or more years '
        'of experience. Multilingual. Public sector background.<br>'
        '<b>Not relevant:</b> Age, gender, or number of languages beyond '
        'the two required for the role.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="assess-card">'
            '<div class="assess-num">Assessment 01</div>'
            '<div class="assess-title">Your judgment<br>against the AI</div>'
            '</div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="assess-card">'
            '<div class="assess-num">Assessment 02</div>'
            '<div class="assess-title">Identifying<br>decision flaws</div>'
            '</div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="assess-card">'
            '<div class="assess-num">Assessment 03</div>'
            '<div class="assess-title">Uncovering<br>hidden biases</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    st.markdown("")
    if st.button("Begin assessment", type="primary",
                 use_container_width=True):
        st.session_state.phase = "round1"
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════
# ROUND 1
# ══════════════════════════════════════════════════════════════════════════
elif phase == "round1":
    idx = st.session_state.r1_idx
    total = len(PEOPLE)
    p = PEOPLE[idx]
    photo = PHOTOS.get(p["name"], "")

    st.markdown(
        '<div class="phase-strip">'
        '<span class="phase-num">Assessment 1 of 3</span>'
        '<span class="phase-title">Your judgment against the AI</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    sc1, sc2 = st.columns(2)
    with sc1:
        st.metric("Your score", f"{st.session_state.r1_you}/{idx}")
    with sc2:
        st.metric("AI score", f"{st.session_state.r1_ai}/{idx}")

    st.markdown(
        "Review the candidate against the published criteria. "
        "Should this person be invited to interview?"
    )

    st.markdown(
        f'<div class="candidate-card">'
        f'<div class="candidate-card-photo">'
        f'<img class="candidate-photo" src="{photo}" alt="">'
        f'<div>'
        f'<div class="candidate-name">{p["name"]}</div>'
        f'<div class="candidate-sub">Candidate {idx+1} of {total}</div>'
        f'</div></div>'
        f'<div class="detail-grid">'
        f'<div class="detail-cell"><div class="detail-label">Experience</div>'
        f'<div class="detail-val">{p["exp"]} years</div></div>'
        f'<div class="detail-cell"><div class="detail-label">Education</div>'
        f'<div class="detail-val">{EDU[p["edu"]]}</div></div>'
        f'<div class="detail-cell"><div class="detail-label">Languages</div>'
        f'<div class="detail-val">{LANG_NAMES[p["lang"]]}</div></div>'
        f'<div class="detail-cell"><div class="detail-label">Age</div>'
        f'<div class="detail-val">{p["age"]}</div></div>'
        f'</div>'
        f'<div style="margin-top:8px;" class="detail-cell">'
        f'<div class="detail-label">Background</div>'
        f'<div class="detail-val">{p["bg"]}</div></div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    def _r1_handle(user_dec):
        person = PEOPLE[st.session_state.r1_idx]
        gt = ground_truth(person)
        ai = ai_pred(person)
        u_ok = user_dec == gt
        a_ok = ai == gt
        if u_ok:
            st.session_state.r1_you += 1
        if a_ok:
            st.session_state.r1_ai += 1
        if not a_ok:
            st.session_state.r1_errors.append(
                dict(person=person, ai_said=ai, correct=gt))

        ct = "interview" if gt else "pass"
        at = "interview" if ai else "pass"

        if u_ok and a_ok:
            msg = (f"Both correct. {person['name']} meets the criteria "
                   f"for an {ct}.")
            kind = "green"
        elif u_ok and not a_ok:
            extra = ""
            if person["age"] >= 45 and gt == 1 and ai == 0:
                extra = (f" This candidate is {person['age']}. "
                         "Consider whether the AI may be penalising age.")
            elif person["edu"] <= 1 and ai == 1:
                extra = (" The AI appears to have over-weighted language "
                         "skills while ignoring the missing degree "
                         "requirement.")
            msg = (f"Your assessment was correct. The AI recommended "
                   f"\"{at},\" which was wrong.{extra}")
            kind = "green"
        elif not u_ok and a_ok:
            msg = (f"The AI was correct here. The appropriate "
                   f"decision was \"{ct}.\"")
            kind = "red"
        else:
            msg = (f"A difficult case. Both assessments reached the "
                   f"wrong conclusion. The correct decision was \"{ct}.\"")
            kind = "amber"

        st.session_state.r1_feedback = (msg, kind)
        st.session_state.r1_decided = True

    if not st.session_state.r1_decided:
        cy, cn = st.columns(2)
        with cy:
            if st.button("Invite to interview",
                         use_container_width=True, key=f"r1y{idx}"):
                _r1_handle(1)
                st.rerun()
        with cn:
            if st.button("Pass",
                         use_container_width=True, key=f"r1n{idx}"):
                _r1_handle(0)
                st.rerun()

    if st.session_state.r1_feedback:
        msg, kind = st.session_state.r1_feedback
        css = {"green": "note-green", "red": "note-red",
               "amber": "note-amber"}.get(kind, "note-blue")
        st.markdown(f'<div class="note {css}">{msg}</div>',
                    unsafe_allow_html=True)

        if idx < total - 1:
            if st.button("Next candidate", use_container_width=True):
                st.session_state.r1_idx += 1
                st.session_state.r1_feedback = None
                st.session_state.r1_decided = False
                st.rerun()
        else:
            if st.button("View Assessment 1 results", type="primary",
                         use_container_width=True):
                st.session_state.phase = "r1_results"
                st.rerun()

    st.progress((idx + 1) / total)


# ══════════════════════════════════════════════════════════════════════════
# ROUND 1 RESULTS
# ══════════════════════════════════════════════════════════════════════════
elif phase == "r1_results":
    you = st.session_state.r1_you
    ai_sc = st.session_state.r1_ai
    total = len(PEOPLE)

    st.markdown(
        '<div class="phase-strip">'
        '<span class="phase-num">Assessment 1 Results</span>'
        '<span class="phase-title">'
        + ("Your score matched or exceeded the AI."
           if you >= ai_sc
           else "The AI scored higher.")
        + '</span></div>',
        unsafe_allow_html=True,
    )

    lc, rc = st.columns(2)
    with lc:
        st.markdown(
            f'<div class="stat-card"><div class="stat-val">'
            f'{you}/{total}</div>'
            f'<div class="stat-label">Your score</div></div>',
            unsafe_allow_html=True,
        )
    with rc:
        st.markdown(
            f'<div class="stat-card"><div class="stat-val">'
            f'{ai_sc}/{total}</div>'
            f'<div class="stat-label">AI score</div></div>',
            unsafe_allow_html=True,
        )

    if you >= ai_sc:
        st.markdown(
            '<div class="note note-amber"><b>Consider the following:</b> '
            'you reviewed each candidate carefully. This AI processes '
            'hundreds of applications per hour. Even if your judgment '
            'is more reliable, it cannot be applied at the same scale. '
            'The relevant question is not whether the AI is perfect, '
            'but whether its specific errors are acceptable.</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="note note-amber"><b>The AI was more accurate '
            'overall, but accuracy alone does not indicate fairness.</b> '
            'Examine the cases below where the AI made errors. Is there '
            'a pattern?</div>',
            unsafe_allow_html=True,
        )

    errors = st.session_state.r1_errors
    if errors:
        st.markdown("#### Cases where the AI was incorrect")
        for e in errors:
            pp = e["person"]
            photo = PHOTOS.get(pp["name"], "")
            ai_t = "Interview" if e["ai_said"] else "Pass"
            co_t = "Interview" if e["correct"] else "Pass"
            st.markdown(
                f'<div style="display:flex;align-items:center;gap:12px;'
                f'padding:10px 0;border-bottom:1px solid #eee;">'
                f'<img src="{photo}" style="width:36px;height:36px;'
                f'border-radius:50%;object-fit:cover;">'
                f'<div style="flex:1;font-size:0.88rem;">'
                f'<b>{pp["name"]}</b>, age {pp["age"]}, '
                f'{pp["exp"]} years experience, {EDU[pp["edu"]]}<br>'
                f'<span style="color:#888;">AI: {ai_t} (correct: '
                f'{co_t})</span></div></div>',
                unsafe_allow_html=True,
            )

        age_errs = [e for e in errors
                    if e["person"]["age"] >= 45
                    and e["correct"] == 1 and e["ai_said"] == 0]
        if age_errs:
            st.markdown(
                '<div class="note note-red"><b>A pattern emerges.</b> '
                'The AI rejected qualified candidates over the age of '
                '45. The job criteria state that age should not be a '
                'factor. Assessment 2 will examine this further.</div>',
                unsafe_allow_html=True,
            )

    if st.button("Continue to Assessment 2", type="primary",
                 use_container_width=True):
        st.session_state.phase = "round2"
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════
# ROUND 2
# ══════════════════════════════════════════════════════════════════════════
elif phase == "round2":
    idx = st.session_state.r2_idx
    total = len(R2_PAIRS)
    pair = R2_PAIRS[idx]

    st.markdown(
        '<div class="phase-strip">'
        '<span class="phase-num">Assessment 2 of 3</span>'
        '<span class="phase-title">Identifying decision flaws</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"**Correct so far:** {st.session_state.r2_score} of {idx}"
    )
    st.markdown(
        "Two nearly identical candidates received opposite decisions. "
        "Identify which detail caused the reversal."
    )

    ca, cb = st.columns(2)
    for col, lbl, pk in [(ca, "Candidate A", "a"),
                         (cb, "Candidate B", "b")]:
        prof = pair[pk]
        dec = ai_pred(prof)
        dec_txt = "Interview" if dec else "Pass"
        badge_cls = "badge-yes" if dec else "badge-no"

        rows = ""
        for k in ["exp", "edu", "lang", "age"]:
            other = "b" if pk == "a" else "a"
            diff = prof[k] != pair[other][k]
            weight = "font-weight:700;" if diff and st.session_state.r2_decided else ""
            bg = "background:#fff8e8;" if diff and st.session_state.r2_decided else ""
            rows += (
                f'<div style="display:flex;justify-content:space-between;'
                f'padding:5px 8px;border-radius:4px;{bg}">'
                f'<span style="color:#888;font-size:0.82rem;">'
                f'{FIELD_LABELS[k]}</span>'
                f'<span style="font-size:0.85rem;{weight}">'
                f'{fmt_field(k, prof[k])}</span></div>'
            )

        with col:
            st.markdown(
                f'<div class="compare-card">'
                f'<div class="compare-header">'
                f'<span class="compare-label">{lbl}</span>'
                f'<span class="decision-badge {badge_cls}">{dec_txt}'
                f'</span></div>{rows}</div>',
                unsafe_allow_html=True,
            )

    st.markdown("")
    st.markdown("**Which factor caused the AI to reverse its decision?**")

    if not st.session_state.r2_decided:
        fields = list(FIELD_LABELS.keys())
        rng = np.random.RandomState(idx + 42)
        rng.shuffle(fields)

        cols = st.columns(len(fields))
        for i, k in enumerate(fields):
            with cols[i]:
                if st.button(FIELD_LABELS[k], key=f"r2_{idx}_{k}",
                             use_container_width=True):
                    ok = k == pair["diff"]
                    if ok:
                        st.session_state.r2_score += 1
                    st.session_state.r2_feedback = (ok, pair)
                    st.session_state.r2_decided = True
                    st.rerun()

    if st.session_state.r2_feedback:
        ok, p2 = st.session_state.r2_feedback
        if ok:
            st.markdown(
                f'<div class="note note-green"><b>Correct.</b> '
                f'{p2["insight"]}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="note note-red"><b>The determining factor '
                f'was {p2["label"].lower()}.</b> {p2["insight"]}</div>',
                unsafe_allow_html=True,
            )

        if idx < total - 1:
            if st.button("Next comparison", use_container_width=True):
                st.session_state.r2_idx += 1
                st.session_state.r2_feedback = None
                st.session_state.r2_decided = False
                st.rerun()
        else:
            if st.button("View Assessment 2 results", type="primary",
                         use_container_width=True):
                st.session_state.phase = "r2_results"
                st.rerun()

    st.progress((idx + 1) / total)


# ══════════════════════════════════════════════════════════════════════════
# ROUND 2 RESULTS
# ══════════════════════════════════════════════════════════════════════════
elif phase == "r2_results":
    sc = st.session_state.r2_score
    total = len(R2_PAIRS)

    st.markdown(
        '<div class="phase-strip">'
        '<span class="phase-num">Assessment 2 Results</span>'
        f'<span class="phase-title">{sc} of {total} correctly '
        f'identified</span></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="note note-blue"><b>The pattern is consistent.</b> '
        'Two of the four reversals were caused by age alone, a factor '
        'the position criteria explicitly exclude. The AI also assigns '
        'disproportionate weight to languages and formal education '
        'beyond what the role requires. Assessment 3 allows you to '
        'explore these biases directly.</div>',
        unsafe_allow_html=True,
    )

    if st.button("Continue to Assessment 3", type="primary",
                 use_container_width=True):
        st.session_state.phase = "round3"
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════
# ROUND 3
# ══════════════════════════════════════════════════════════════════════════
elif phase == "round3":
    st.markdown(
        '<div class="phase-strip">'
        '<span class="phase-num">Assessment 3 of 3</span>'
        '<span class="phase-title">Uncovering hidden biases</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        "The candidate below was recommended for interview. Adjust the "
        "parameters of their application. Determine which factors the "
        "AI penalises inappropriately and which it over-weights."
    )

    BASE = dict(exp=12, edu=3, lang=4, age=41)
    photo = PHOTOS["Amira Hassan"]

    st.markdown(
        f'<div class="candidate-card">'
        f'<div class="candidate-card-photo">'
        f'<img class="candidate-photo" src="{photo}" alt="">'
        f'<div>'
        f'<div class="candidate-name">Amira Hassan</div>'
        f'<div class="candidate-sub">12 years in federal ministry. '
        f'Master\'s degree. Four languages. Age 41.</div>'
        f'</div></div></div>',
        unsafe_allow_html=True,
    )

    exp = st.slider("Years of experience (position requires 3 or more)",
                    0, 20, BASE["exp"])
    edu = st.slider("Education level (position requires bachelor's or higher)",
                    0, 4, BASE["edu"],
                    help="0 = No degree, 1 = Vocational, 2 = Bachelor's, "
                         "3 = Master's, 4 = Doctorate")
    st.caption(f"Selected: {EDU[edu]}")

    lang = st.slider("Languages spoken (position requires 2)",
                     1, 4, BASE["lang"])
    st.caption(f"Selected: {LANG_NAMES[lang]}")

    age = st.slider("Age (should not affect the decision)", 22, 62,
                    BASE["age"])

    cur = dict(exp=exp, edu=edu, lang=lang, age=age)
    prob = ai_prob(cur)
    dec = 1 if prob > 0.5 else 0

    if dec:
        st.success(
            f"AI decision: **Invite to interview** "
            f"(confidence: {prob:.0%})"
        )
    else:
        st.error(
            f"AI decision: **Pass** "
            f"(confidence: {1 - prob:.0%})"
        )

    disc = list(st.session_state.r3_discoveries)

    age_only = dict(**BASE)
    age_only["age"] = age
    if (ai_pred(age_only) == 0 and age > BASE["age"]
            and "age" not in disc):
        disc.append("age")

    lang_only = dict(**BASE)
    lang_only["lang"] = lang
    if (ai_pred(lang_only) == 0 and lang < BASE["lang"]
            and "lang" not in disc):
        disc.append("lang")

    st.session_state.r3_discoveries = disc

    if "age" in disc:
        st.markdown(
            '<div class="note note-red"><b>Bias identified: age '
            'discrimination.</b> Increasing this candidate\'s age '
            'while holding all other qualifications constant caused '
            'the AI to reject them. The position criteria state that '
            'age is not a relevant factor.</div>',
            unsafe_allow_html=True,
        )

    if "lang" in disc:
        st.markdown(
            '<div class="note note-amber"><b>Disproportionate weighting: '
            'languages.</b> Reducing languages to 2, the number the '
            'position actually requires, reversed the AI\'s decision. '
            'The system treats a non-essential qualification as '
            'decisive.</div>',
            unsafe_allow_html=True,
        )

    if len(disc) < 2:
        if "age" in disc:
            st.markdown(
                '<div class="note note-blue">You have identified the age '
                'bias. Now reduce the number of languages to 2, which '
                'meets the position requirement, and observe the '
                'result.</div>',
                unsafe_allow_html=True,
            )
        elif "lang" in disc:
            st.markdown(
                '<div class="note note-blue">You have identified the '
                'language weighting issue. Now increase the candidate\'s '
                'age and observe whether the AI penalises older '
                'applicants.</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="note note-blue">Adjust one parameter at a '
                'time. Begin with age: increase it while keeping all '
                'other factors unchanged.</div>',
                unsafe_allow_html=True,
            )
    else:
        if st.button("View complete findings", type="primary",
                     use_container_width=True):
            st.session_state.phase = "finale"
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════
# FINALE
# ══════════════════════════════════════════════════════════════════════════
elif phase == "finale":
    st.markdown(
        f'<div class="hero" style="height:180px;">'
        f'<img src="{HERO_IMG}" alt="">'
        f'<div class="hero-overlay" style="justify-content:center;'
        f'align-items:center;text-align:center;">'
        f'<div class="hero-title" style="font-size:1.5rem;">'
        f'Assessment Summary</div>'
        f'<div class="hero-sub" style="text-align:center;">'
        f'Findings from the regulatory stress test</div>'
        f'</div></div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f'<div class="stat-card"><div class="stat-val">'
            f'{st.session_state.r1_you}/{len(PEOPLE)}</div>'
            f'<div class="stat-label">Assessment 1</div></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<div class="stat-card"><div class="stat-val">'
            f'{st.session_state.r2_score}/{len(R2_PAIRS)}</div>'
            f'<div class="stat-label">Assessment 2</div></div>',
            unsafe_allow_html=True,
        )
    with c3:
        n = len(st.session_state.r3_discoveries)
        st.markdown(
            f'<div class="stat-card"><div class="stat-val">'
            f'{n} bias{"es" if n != 1 else ""}</div>'
            f'<div class="stat-label">Assessment 3</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("### How the AI weights its decisions")
    st.markdown(
        "The system was trained on historical hiring data. It learned "
        "decision patterns from previous outcomes, including biases "
        "embedded in past decisions."
    )

    weights = [
        ("Education level", 85, True,
         "Appropriate: aligns with requirements"),
        ("Languages spoken", 55, False,
         "Over-weighted: role requires 2, AI treats 3+ as essential"),
        ("Age", 38, False,
         "Should carry zero weight: age discrimination"),
        ("Years of experience", 14, True,
         "Under-weighted: AI favours credentials over practice"),
    ]

    for label, w, fair, note in weights:
        color = "#2a7a2a" if fair else "#b33"
        st.markdown(
            f'<div style="margin-bottom:0.8rem;">'
            f'<div style="display:flex;justify-content:space-between;'
            f'font-size:0.82rem;margin-bottom:3px;">'
            f'<span style="font-weight:600;">{label}</span>'
            f'<span style="font-size:0.78rem;color:{color};">'
            f'{note}</span></div>'
            f'<div class="bar-bg">'
            f'<div class="bar-fill" style="width:{w}%;'
            f'background:{color};"></div></div></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        "The position criteria state that age is not relevant. However, "
        "the AI learned from data in which older candidates were selected "
        "less frequently, and reproduced this pattern as though it were "
        "a legitimate criterion. **The AI did not create the bias. It "
        "inherited it from historical decisions and applied it at scale.**"
    )

    st.markdown("---")
    st.markdown("### Regulatory implications")

    st.markdown(
        '<div class="note note-blue"><b>Accuracy does not indicate '
        'fairness.</b> The AI achieved 92% accuracy while systematically '
        'discriminating by age. A system can produce mostly correct '
        'outcomes and still embed impermissible biases.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="note note-blue"><b>Historical data encodes '
        'historical biases.</b> AI trained on past decisions will '
        'reproduce past discrimination unless specific technical '
        'countermeasures are applied. Automated systems scale bias at '
        'speeds that manual processes never could.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="note note-blue"><b>Effective regulation requires '
        'more than accuracy benchmarks.</b> Three categories of testing '
        'are necessary: robustness testing (stable decisions under minor '
        'variation?), bias auditing (do protected characteristics '
        'influence outcomes?), and explainability (can the system '
        'account for each decision?).</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="note note-amber"><b>Regulatory consideration:</b> '
        'approving an AI system on the basis of accuracy alone is '
        'comparable to evaluating a hiring manager solely by the number '
        'of positions filled, without examining whether they '
        'discriminated in the process.</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")
    if st.button("Restart assessment", use_container_width=True):
        for k, v in _defaults.items():
            st.session_state[k] = v
        st.rerun()

# ── Footer ───────────────────────────────────────────────────────────────
st.markdown(
    '<div class="footer-text">'
    'AI Regulatory Stress Test. Stanford SAFE prototype. '
    'Developed to demonstrate how interactive tools can support '
    'technically informed policy decisions on AI systems.'
    '</div>',
    unsafe_allow_html=True,
)
