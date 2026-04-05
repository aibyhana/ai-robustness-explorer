"""
AI Stress Test: Employment Screening System
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
    @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;600;700&family=Source+Sans+3:wght@400;500;600&display=swap');

    .block-container { padding-top: 2rem; max-width: 700px; }

    h1, h2, h3 {
        font-family: 'Source Serif 4', Georgia, serif !important;
        font-weight: 600 !important;
        letter-spacing: -0.01em;
    }

    .report-header {
        font-family: 'Source Serif 4', Georgia, serif;
        font-size: 1.7rem; font-weight: 700;
        color: #1a1a1a; text-align: center;
        letter-spacing: -0.02em;
        margin-bottom: 0.2rem;
    }
    .report-sub {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.95rem; color: #666;
        text-align: center; margin-bottom: 2rem;
        line-height: 1.5;
    }
    .phase-label {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.72rem; font-weight: 600;
        color: #888; letter-spacing: 0.08em;
        text-transform: uppercase; margin-bottom: 0.15rem;
    }
    .phase-title {
        font-family: 'Source Serif 4', Georgia, serif;
        font-size: 1.25rem; font-weight: 600;
        color: #1a1a1a; margin-bottom: 0.8rem;
    }
    .metric-card {
        background: #f7f7f5; border-radius: 8px;
        padding: 1.1rem; text-align: center;
        border: 1px solid #e5e5e0;
    }
    .metric-val {
        font-family: 'Source Serif 4', Georgia, serif;
        font-size: 2rem; font-weight: 700;
        line-height: 1.2; color: #1a1a1a;
    }
    .metric-label {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.8rem; color: #888;
        margin-top: 0.15rem;
    }
    .note-info {
        background: #f0f4f8; border-left: 3px solid #4a7c9b;
        padding: 0.85rem 1rem; margin: 0.7rem 0;
        font-size: 0.88rem; color: #2c4a5e;
        font-family: 'Source Sans 3', sans-serif;
        line-height: 1.55;
    }
    .note-warn {
        background: #fdf6ec; border-left: 3px solid #b8860b;
        padding: 0.85rem 1rem; margin: 0.7rem 0;
        font-size: 0.88rem; color: #6b4f1a;
        font-family: 'Source Sans 3', sans-serif;
        line-height: 1.55;
    }
    .note-danger {
        background: #fdf0f0; border-left: 3px solid #a33;
        padding: 0.85rem 1rem; margin: 0.7rem 0;
        font-size: 0.88rem; color: #6b1a1a;
        font-family: 'Source Sans 3', sans-serif;
        line-height: 1.55;
    }
    .note-success {
        background: #eef6ee; border-left: 3px solid #3a7a3a;
        padding: 0.85rem 1rem; margin: 0.7rem 0;
        font-size: 0.88rem; color: #1a4a1a;
        font-family: 'Source Sans 3', sans-serif;
        line-height: 1.55;
    }
    .criteria-box {
        background: #fafaf8; border: 1px solid #e5e5e0;
        border-radius: 8px; padding: 1.1rem 1.3rem;
        margin-bottom: 1.5rem;
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.9rem; line-height: 1.6;
    }
    .bar-bg {
        height: 8px; background: #e9e9e4;
        border-radius: 4px; overflow: hidden;
        margin-top: 4px;
    }
    .bar-fill { height: 100%; border-radius: 4px; }
    .footer-text {
        text-align: center; color: #aaa;
        font-size: 0.75rem; margin-top: 2rem;
        font-family: 'Source Sans 3', sans-serif;
    }
    .candidate-detail {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.88rem; color: #444;
        line-height: 1.5;
    }
    .candidate-name {
        font-family: 'Source Serif 4', Georgia, serif;
        font-size: 1rem; font-weight: 600;
        color: #1a1a1a;
    }
    .round-card {
        background: #fafaf8; border: 1px solid #e5e5e0;
        border-radius: 8px; padding: 1rem;
        text-align: center;
    }
    .round-num {
        font-family: 'Source Serif 4', Georgia, serif;
        font-size: 1.1rem; font-weight: 600;
        color: #1a1a1a;
    }
    .round-desc {
        font-family: 'Source Sans 3', sans-serif;
        font-size: 0.8rem; color: #888;
        margin-top: 0.1rem;
    }
</style>
""", unsafe_allow_html=True)

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
            "third language is listed as a bonus, not a requirement. "
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
        '<div class="report-header">'
        'AI Regulatory Stress Test</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="report-sub">'
        'A government agency proposes using AI to screen civil service '
        'applications. The vendor reports 92% accuracy. This exercise '
        'allows you to evaluate that claim through three structured '
        'assessments.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="criteria-box">'
        '<div style="font-weight:600;color:#1a1a1a;margin-bottom:0.5rem;">'
        'Position: Policy Advisor (Civil Service)</div>'
        'The role requires analytical capability and public sector '
        'experience. The published hiring criteria are as follows:<br><br>'
        '<b>Required:</b> Bachelor\'s degree or higher. Minimum 3 years '
        'of relevant professional experience.<br>'
        '<b>Preferred:</b> Master\'s degree or doctorate. 7 or more years '
        'of experience. Multilingual. Public sector background.<br>'
        '<b>Not relevant to the decision:</b> Age, gender, or the number '
        'of languages beyond the two required for the role.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="round-card">'
            '<div class="round-num">Assessment 1</div>'
            '<div class="round-desc">Your judgment against the AI</div>'
            '</div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="round-card">'
            '<div class="round-num">Assessment 2</div>'
            '<div class="round-desc">Identifying decision flaws</div>'
            '</div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="round-card">'
            '<div class="round-num">Assessment 3</div>'
            '<div class="round-desc">Uncovering hidden biases</div>'
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

    st.markdown('<div class="phase-label">Assessment 1 of 3</div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="phase-title">Your judgment against the AI</div>',
        unsafe_allow_html=True,
    )

    sc1, sc2 = st.columns(2)
    with sc1:
        st.metric("Your score", f"{st.session_state.r1_you}/{idx}")
    with sc2:
        st.metric("AI score", f"{st.session_state.r1_ai}/{idx}")

    st.markdown(
        "Review the candidate below against the published hiring "
        "criteria. Should this person be invited to interview?"
    )

    st.markdown(
        f'<div class="candidate-name">{p["name"]}</div>'
        f'<div class="candidate-detail" style="color:#888;margin-bottom:0.6rem;">'
        f'Candidate {idx + 1} of {total}</div>',
        unsafe_allow_html=True,
    )

    lc, rc = st.columns(2)
    with lc:
        st.markdown(f"**Experience:** {p['exp']} years")
        st.markdown(f"**Education:** {EDU[p['edu']]}")
    with rc:
        st.markdown(f"**Languages:** {LANG_NAMES[p['lang']]}")
        st.markdown(f"**Age:** {p['age']}")
    st.markdown(f"**Background:** {p['bg']}")
    st.markdown("---")

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
            kind = "success"
        elif u_ok and not a_ok:
            extra = ""
            if person["age"] >= 45 and gt == 1 and ai == 0:
                extra = (f" This candidate is {person['age']} years old. "
                         "Consider whether the AI may be penalising age.")
            elif person["edu"] <= 1 and ai == 1:
                extra = (" The AI appears to have over-weighted language "
                         "skills while ignoring the missing degree "
                         "requirement.")
            msg = (f"Your assessment was correct. The AI recommended "
                   f"\"{at},\" which was wrong.{extra}")
            kind = "success"
        elif not u_ok and a_ok:
            msg = (f"The AI was correct on this one. The appropriate "
                   f"decision was \"{ct}.\"")
            kind = "error"
        else:
            msg = (f"A difficult case. Both you and the AI reached the "
                   f"wrong conclusion. The correct decision was \"{ct}.\"")
            kind = "warn"

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
        css = {"success": "note-success", "error": "note-danger",
               "warn": "note-warn"}.get(kind, "note-info")
        st.markdown(f'<div class="{css}">{msg}</div>',
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

    st.markdown('<div class="phase-label">Assessment 1 Results</div>',
                unsafe_allow_html=True)

    headline = ("Your score matched or exceeded the AI."
                if you >= ai_sc
                else "The AI scored higher than you.")
    st.markdown(
        f'<div class="phase-title">{headline}</div>',
        unsafe_allow_html=True,
    )

    lc, rc = st.columns(2)
    with lc:
        st.markdown(
            f'<div class="metric-card"><div class="metric-val">'
            f'{you}/{total}</div>'
            f'<div class="metric-label">Your score</div></div>',
            unsafe_allow_html=True,
        )
    with rc:
        st.markdown(
            f'<div class="metric-card"><div class="metric-val">'
            f'{ai_sc}/{total}</div>'
            f'<div class="metric-label">AI score</div></div>',
            unsafe_allow_html=True,
        )

    if you >= ai_sc:
        st.markdown(
            '<div class="note-warn"><b>Consider the following:</b> you '
            'reviewed each candidate carefully. This AI processes '
            'hundreds of applications per hour. Even if your judgment '
            'is more reliable, it cannot be applied at the same scale. '
            'The relevant question is not whether the AI is perfect, '
            'but whether its specific errors are acceptable.</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="note-warn"><b>The AI was more accurate overall, '
            'but accuracy alone does not indicate fairness.</b> Examine '
            'the cases below where the AI made errors. Is there a '
            'pattern?</div>',
            unsafe_allow_html=True,
        )

    errors = st.session_state.r1_errors
    if errors:
        st.markdown("#### Cases where the AI was incorrect")
        for e in errors:
            pp = e["person"]
            ai_t = "Interview" if e["ai_said"] else "Pass"
            co_t = "Interview" if e["correct"] else "Pass"
            st.markdown(
                f"**{pp['name']}**, age {pp['age']}, {pp['exp']} years "
                f"experience, {EDU[pp['edu']]}  \n"
                f"AI decision: **{ai_t}** (correct decision: **{co_t}**)"
            )

        age_errs = [e for e in errors
                    if e["person"]["age"] >= 45
                    and e["correct"] == 1 and e["ai_said"] == 0]
        if age_errs:
            st.markdown(
                '<div class="note-danger"><b>A pattern emerges.</b> '
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

    st.markdown('<div class="phase-label">Assessment 2 of 3</div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="phase-title">Identifying decision flaws</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"**Correct so far:** {st.session_state.r2_score} of {idx}"
    )
    st.markdown(
        "Two nearly identical candidates received opposite decisions "
        "from the AI. Identify which detail caused the reversal."
    )

    ca, cb = st.columns(2)
    for col, lbl, pk in [(ca, "Candidate A", "a"),
                         (cb, "Candidate B", "b")]:
        prof = pair[pk]
        dec = ai_pred(prof)
        dec_txt = "Interview" if dec else "Pass"
        with col:
            st.markdown(f"**{lbl}:** {dec_txt}")
            for k in ["exp", "edu", "lang", "age"]:
                other = "b" if pk == "a" else "a"
                diff = prof[k] != pair[other][k]
                bold = "**" if diff and st.session_state.r2_decided else ""
                st.markdown(
                    f"{bold}{FIELD_LABELS[k]}: "
                    f"{fmt_field(k, prof[k])}{bold}"
                )

    st.markdown("---")
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
                f'<div class="note-success"><b>Correct.</b> '
                f'{p2["insight"]}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="note-danger"><b>The determining factor was '
                f'{p2["label"].lower()}.</b> {p2["insight"]}</div>',
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

    st.markdown('<div class="phase-label">Assessment 2 Results</div>',
                unsafe_allow_html=True)
    st.markdown(
        f'<div class="phase-title">'
        f'{sc} of {total} correctly identified</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="note-info"><b>The pattern is consistent.</b> Two '
        'of the four reversals were caused by age alone, a factor the '
        'position criteria explicitly exclude. The AI also assigns '
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
    st.markdown('<div class="phase-label">Assessment 3 of 3</div>',
                unsafe_allow_html=True)
    st.markdown(
        '<div class="phase-title">Uncovering hidden biases</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        "The candidate below was recommended for interview. Adjust the "
        "parameters of their application using the controls. Determine "
        "which factors the AI penalises inappropriately and which it "
        "over-weights relative to the stated criteria."
    )

    BASE = dict(exp=12, edu=3, lang=4, age=41)

    st.markdown(
        "**Amira Hassan**  \n"
        "12 years in federal ministry. Master's degree. "
        "Four languages. Age 41."
    )
    st.markdown("---")

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
            '<div class="note-danger"><b>Bias identified: age '
            'discrimination.</b> Increasing this candidate\'s age '
            'while holding all other qualifications constant caused '
            'the AI to reject them. The position criteria state that '
            'age is not a relevant factor.</div>',
            unsafe_allow_html=True,
        )

    if "lang" in disc:
        st.markdown(
            '<div class="note-warn"><b>Disproportionate weighting: '
            'languages.</b> Reducing languages to 2, the number the '
            'position actually requires, reversed the AI\'s decision. '
            'The system treats a non-essential qualification as '
            'decisive.</div>',
            unsafe_allow_html=True,
        )

    if len(disc) < 2:
        if "age" in disc:
            st.markdown(
                '<div class="note-info">You have identified the age '
                'bias. Now reduce the number of languages to 2, which '
                'meets the position requirement, and observe the '
                'result.</div>',
                unsafe_allow_html=True,
            )
        elif "lang" in disc:
            st.markdown(
                '<div class="note-info">You have identified the '
                'language weighting issue. Now increase the candidate\'s '
                'age and observe whether the AI penalises older '
                'applicants.</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="note-info">Adjust one parameter at a time. '
                'Begin with age: increase it while keeping all other '
                'factors unchanged.</div>',
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
        '<div class="report-header">Assessment Summary</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="report-sub">'
        'Findings from the regulatory stress test of the employment '
        'screening AI.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f'<div class="metric-card"><div class="metric-val">'
            f'{st.session_state.r1_you}/{len(PEOPLE)}</div>'
            f'<div class="metric-label">Assessment 1</div></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<div class="metric-card"><div class="metric-val">'
            f'{st.session_state.r2_score}/{len(R2_PAIRS)}</div>'
            f'<div class="metric-label">Assessment 2</div></div>',
            unsafe_allow_html=True,
        )
    with c3:
        n = len(st.session_state.r3_discoveries)
        st.markdown(
            f'<div class="metric-card"><div class="metric-val">'
            f'{n} bias{"es" if n != 1 else ""}</div>'
            f'<div class="metric-label">Assessment 3</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("### How the AI weights its decisions")
    st.markdown(
        "The AI was trained on historical hiring data. It learned "
        "decision patterns from previous outcomes, including the biases "
        "of past hiring managers."
    )

    weights = [
        ("Education level", 85, True,
         "Appropriate: aligns with position requirements"),
        ("Languages spoken", 55, False,
         "Over-weighted: role requires 2, AI treats 3+ as essential"),
        ("Age", 38, False,
         "Should carry zero weight: constitutes age discrimination"),
        ("Years of experience", 14, True,
         "Under-weighted: AI favours credentials over practice"),
    ]

    for label, w, fair, note in weights:
        color = "#3a7a3a" if fair else "#a33"
        st.markdown(
            f'<div style="margin-bottom:0.7rem;">'
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
        "the AI learned from historical data in which older candidates "
        "were selected less frequently, and reproduced this pattern as "
        "though it were a legitimate criterion. **The AI did not create "
        "the bias. It inherited it from historical decisions and "
        "applied it at scale.**"
    )

    st.markdown("---")
    st.markdown("### Regulatory implications")

    st.markdown(
        '<div class="note-info"><b>Accuracy does not indicate fairness.'
        '</b> The AI achieved 92% accuracy. It was also systematically '
        'discriminatory. These two facts are not contradictory. A system '
        'can produce mostly correct outcomes while embedding '
        'impermissible biases in its decision logic.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="note-info"><b>Historical data encodes historical '
        'biases.</b> AI systems trained on past decisions will '
        'reproduce past discrimination unless specific technical '
        'countermeasures are implemented. Without safeguards, automated '
        'systems scale bias at speeds and volumes that manual processes '
        'never could.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="note-info"><b>Effective regulation requires more '
        'than accuracy benchmarks.</b> Three categories of testing are '
        'necessary: robustness testing (are decisions stable under minor '
        'input variation?), bias auditing (do protected characteristics '
        'influence outcomes?), and explainability requirements (can the '
        'system account for each decision?).</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="note-warn"><b>Regulatory consideration:</b> '
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
st.markdown("---")
st.markdown(
    '<div class="footer-text">'
    'AI Regulatory Stress Test. Stanford SAFE prototype. '
    'Developed to demonstrate how interactive tools can support '
    'technically informed policy decisions on AI systems.'
    '</div>',
    unsafe_allow_html=True,
)
