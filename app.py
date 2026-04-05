"""
AI Regulatory Stress Test: Employment Screening System
Stanford SAFE project prototype.
"""

import streamlit as st
import numpy as np

st.set_page_config(page_title="AI Regulatory Stress Test", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Karla:wght@400;500;600;700&display=swap');

    .block-container {
        padding-top: 0 !important;
        max-width: 780px;
    }

    .stApp {
        background: #0f0f0e;
    }

    * { font-family: 'Karla', sans-serif !important; }

    /* Override Streamlit defaults for dark bg */
    .stMarkdown, .stMarkdown p, .stMarkdown li,
    .stMarkdown span, label, .stSlider label {
        color: #d4d0c8 !important;
    }
    h1, h2, h3, h4 {
        color: #f0ece4 !important;
        font-family: 'Instrument Serif', Georgia, serif !important;
    }
    .stMetricValue { color: #f0ece4 !important; }
    .stMetricLabel { color: #8a8578 !important; }

    /* Hero */
    .hero-wrap {
        position: relative;
        margin: -1rem -1rem 2.5rem -1rem;
        height: 340px;
        overflow: hidden;
    }
    .hero-wrap img {
        width: 100%; height: 100%;
        object-fit: cover;
        filter: brightness(0.3) saturate(0.7);
    }
    .hero-content {
        position: absolute;
        bottom: 0; left: 0; right: 0;
        padding: 3rem 2.5rem 2.5rem;
        background: linear-gradient(transparent, rgba(15,15,14,0.95));
    }
    .hero-eyebrow {
        font-family: 'Karla', sans-serif;
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #c8a96e;
        margin-bottom: 0.6rem;
    }
    .hero-h1 {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 2.4rem;
        font-weight: 400;
        color: #f0ece4;
        line-height: 1.1;
        letter-spacing: -0.02em;
    }
    .hero-desc {
        font-size: 0.92rem;
        color: #9a9588;
        margin-top: 0.7rem;
        line-height: 1.6;
        max-width: 540px;
    }

    /* Phase header */
    .ph-strip {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #2a2926;
    }
    .ph-badge {
        background: #c8a96e;
        color: #0f0f0e;
        font-size: 0.62rem;
        font-weight: 700;
        padding: 5px 12px;
        border-radius: 3px;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        white-space: nowrap;
    }
    .ph-title {
        font-family: 'Instrument Serif', Georgia, serif !important;
        font-size: 1.3rem;
        color: #f0ece4;
    }

    /* Stat cards */
    .s-card {
        background: #1a1918;
        border: 1px solid #2a2926;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
    }
    .s-val {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 2.2rem;
        color: #f0ece4;
        line-height: 1.1;
    }
    .s-label {
        font-size: 0.72rem;
        color: #6a6560;
        margin-top: 0.2rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }

    /* Candidate card */
    .cand-card {
        background: #1a1918;
        border: 1px solid #2a2926;
        border-radius: 14px;
        padding: 0;
        margin-bottom: 1.2rem;
        overflow: hidden;
    }
    .cand-top {
        display: flex;
        align-items: center;
        gap: 18px;
        padding: 1.4rem 1.6rem 1rem;
    }
    .cand-photo {
        width: 72px;
        height: 72px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #2a2926;
        flex-shrink: 0;
    }
    .cand-name {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1.2rem;
        color: #f0ece4;
    }
    .cand-sub {
        font-size: 0.78rem;
        color: #6a6560;
        margin-top: 2px;
    }
    .cand-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1px;
        background: #2a2926;
        margin: 0 1px;
    }
    .cand-cell {
        background: #1a1918;
        padding: 12px 18px;
    }
    .cand-cell-label {
        font-size: 0.65rem;
        color: #6a6560;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .cand-cell-val {
        font-size: 0.9rem;
        color: #d4d0c8;
        margin-top: 3px;
        font-weight: 500;
    }
    .cand-bg-row {
        background: #161514;
        padding: 12px 18px;
        border-top: 1px solid #2a2926;
    }

    /* Notes */
    .nt {
        padding: 1rem 1.2rem;
        margin: 0.8rem 0;
        font-size: 0.86rem;
        line-height: 1.6;
        border-radius: 8px;
        border: 1px solid;
    }
    .nt-blue {
        background: rgba(74,124,155,0.08);
        border-color: rgba(74,124,155,0.25);
        color: #8bb8d4;
    }
    .nt-amber {
        background: rgba(200,169,110,0.08);
        border-color: rgba(200,169,110,0.25);
        color: #c8a96e;
    }
    .nt-red {
        background: rgba(180,80,70,0.08);
        border-color: rgba(180,80,70,0.25);
        color: #d4827a;
    }
    .nt-green {
        background: rgba(80,150,80,0.08);
        border-color: rgba(80,150,80,0.25);
        color: #7ab87a;
    }

    /* Criteria box */
    .crit-box {
        background: #161514;
        border: 1px solid #2a2926;
        border-radius: 12px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 2rem;
        font-size: 0.88rem;
        line-height: 1.7;
        color: #9a9588;
    }
    .crit-title {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1rem;
        color: #f0ece4;
        margin-bottom: 0.8rem;
    }
    .crit-box b { color: #d4d0c8; }

    /* Assessment cards */
    .ax-card {
        background: #161514;
        border: 1px solid #2a2926;
        border-radius: 10px;
        padding: 1.3rem;
        text-align: center;
        transition: border-color 0.2s;
    }
    .ax-card:hover { border-color: #c8a96e; }
    .ax-num {
        font-size: 0.6rem;
        font-weight: 700;
        color: #c8a96e;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }
    .ax-title {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1rem;
        color: #f0ece4;
        line-height: 1.3;
    }

    /* Comparison cards */
    .cmp-card {
        background: #1a1918;
        border: 1px solid #2a2926;
        border-radius: 10px;
        padding: 1rem 1.2rem;
    }
    .cmp-hdr {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.8rem;
    }
    .cmp-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: #d4d0c8;
    }
    .dec-pill {
        font-size: 0.68rem;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 3px;
        letter-spacing: 0.04em;
    }
    .dec-yes {
        background: rgba(80,150,80,0.15);
        color: #7ab87a;
    }
    .dec-no {
        background: rgba(180,80,70,0.15);
        color: #d4827a;
    }

    /* Weight bars */
    .wb-bg {
        height: 5px;
        background: #2a2926;
        border-radius: 3px;
        overflow: hidden;
        margin-top: 6px;
    }
    .wb-fill {
        height: 100%;
        border-radius: 3px;
    }

    /* Error list */
    .err-row {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 12px 0;
        border-bottom: 1px solid #1f1e1c;
    }
    .err-photo {
        width: 40px; height: 40px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #2a2926;
        flex-shrink: 0;
    }

    .footer-text {
        text-align: center;
        color: #3a3835;
        font-size: 0.7rem;
        margin-top: 3rem;
        padding-top: 1.2rem;
        border-top: 1px solid #1f1e1c;
    }

    /* Streamlit overrides */
    .stProgress > div > div > div > div {
        background: #c8a96e !important;
    }
    .stButton > button {
        background: #c8a96e !important;
        color: #0f0f0e !important;
        border: none !important;
        font-weight: 600 !important;
        font-family: 'Karla', sans-serif !important;
    }
    .stButton > button:hover {
        background: #d4b878 !important;
    }
    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="baseButton-secondary"] {
        background: #1a1918 !important;
        color: #d4d0c8 !important;
        border: 1px solid #2a2926 !important;
    }
    .stButton > button[kind="secondary"]:hover,
    .stButton > button[data-testid="baseButton-secondary"]:hover {
        border-color: #c8a96e !important;
        color: #c8a96e !important;
    }
    div[data-testid="stSlider"] label {
        color: #9a9588 !important;
    }
    .stCaption { color: #6a6560 !important; }
    .stAlert { border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)

PHOTOS = {
    "Katrin Bauer": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=200&h=200&fit=crop&crop=face",
    "Heinrich Vogel": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=200&h=200&fit=crop&crop=face",
    "Sophie Laurent": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=200&h=200&fit=crop&crop=face",
    "Lukas Schmidt": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&h=200&fit=crop&crop=face",
    "Brigitte Engel": "https://images.unsplash.com/photo-1594744803329-e58b31de8bf5?w=200&h=200&fit=crop&crop=face",
    "Felix Mayer": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&h=200&fit=crop&crop=face",
    "Elena Richter": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?w=200&h=200&fit=crop&crop=face",
    "Wolfgang Krause": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200&h=200&fit=crop&crop=face",
}

HERO_IMG = "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1400&h=600&fit=crop"

EDU = ["No formal degree", "Vocational qualification", "Bachelor's degree",
       "Master's degree", "Doctorate"]
LANG_NAMES = {1: "German", 2: "German, English",
              3: "German, English, French",
              4: "German, English, French, Spanish"}

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
    dict(name="Elena Richter", exp=4, edu=3, lang=4, age=29,
         bg="European Commission liaison, policy analysis"),
    dict(name="Wolfgang Krause", exp=9, edu=3, lang=2, age=51,
         bg="Parliamentary research service, legislative analysis"),
]

R2_PAIRS = [
    dict(a=dict(exp=7,edu=3,lang=2,age=33),
         b=dict(exp=7,edu=3,lang=2,age=48),
         diff="age",label="Age",
         desc="15 years older (33 versus 48)",
         insight="The position criteria explicitly state that age is not a relevant factor. The AI nonetheless treats it as one. This constitutes automated age discrimination, concealed within a system that reports high overall accuracy."),
    dict(a=dict(exp=5,edu=3,lang=3,age=35),
         b=dict(exp=5,edu=3,lang=2,age=35),
         diff="lang",label="Languages",
         desc="one fewer language (3 versus 2)",
         insight="Both candidates meet the language requirement of two. A third language is listed as preferred, not required. The AI treats it as decisive, giving disproportionate weight to a non-essential qualification."),
    dict(a=dict(exp=8,edu=2,lang=2,age=36),
         b=dict(exp=4,edu=3,lang=2,age=36),
         diff="exp",label="Experience versus Education",
         desc="4 fewer years but a master's instead of a bachelor's",
         insight="The AI heavily favours formal education over practical experience. An 8-year veteran with a bachelor's is rejected while a 4-year master's graduate is accepted. Whether this trade-off is appropriate is a policy decision that should not be delegated to an algorithm."),
    dict(a=dict(exp=6,edu=3,lang=2,age=30),
         b=dict(exp=6,edu=3,lang=2,age=52),
         diff="age",label="Age",
         desc="22 years older (30 versus 52)",
         insight="Identical qualifications produce opposite outcomes, determined entirely by age. This is precisely the type of automated discrimination that the EU AI Act's high-risk classification for employment systems is designed to address."),
]

FIELD_LABELS = {"exp":"Experience","edu":"Education","lang":"Languages","age":"Age"}

def ground_truth(c):
    edu,exp,lang = c["edu"],c["exp"],c["lang"]
    if edu<2: return 0
    if edu>=3 and exp>=2: return 1
    if edu>=2 and exp>=5: return 1
    if edu>=2 and exp>=3 and lang>=3: return 1
    return 0

_W = dict(exp=0.14,edu=0.85,lang=0.55,age=-0.038,bias=-2.4)

def ai_prob(c):
    z=_W["exp"]*c["exp"]+_W["edu"]*c["edu"]+_W["lang"]*c["lang"]+_W["age"]*c["age"]+_W["bias"]
    return 1/(1+np.exp(-z))

def ai_pred(c): return 1 if ai_prob(c)>0.5 else 0

def fmt_field(k,v):
    if k=="exp": return f"{v} year{'s' if v!=1 else ''}"
    if k=="edu": return EDU[v]
    if k=="lang": return LANG_NAMES.get(v,str(v))
    return str(v)

_defaults = dict(phase="intro",r1_idx=0,r1_you=0,r1_ai=0,r1_errors=[],
    r1_feedback=None,r1_decided=False,r2_idx=0,r2_score=0,
    r2_feedback=None,r2_decided=False,r3_discoveries=[])
for _k,_v in _defaults.items():
    if _k not in st.session_state: st.session_state[_k]=_v

phase = st.session_state.phase

# ═══════════════════ INTRO ═══════════════════
if phase=="intro":
    st.markdown(
        f'<div class="hero-wrap">'
        f'<img src="{HERO_IMG}" alt="">'
        f'<div class="hero-content">'
        f'<div class="hero-eyebrow">Stanford SAFE Project</div>'
        f'<div class="hero-h1">AI Regulatory<br>Stress Test</div>'
        f'<div class="hero-desc">'
        f'A government agency proposes using AI to screen civil service '
        f'applications. The vendor reports 92% accuracy. Evaluate that '
        f'claim through three structured assessments.</div>'
        f'</div></div>',unsafe_allow_html=True)

    st.markdown(
        '<div class="crit-box">'
        '<div class="crit-title">Position: Policy Advisor, Civil Service</div>'
        '<b>Required:</b> Bachelor\'s degree or higher. Minimum 3 years '
        'of relevant professional experience.<br>'
        '<b>Preferred:</b> Master\'s degree or doctorate. 7 or more years '
        'of experience. Multilingual. Public sector background.<br>'
        '<b>Not relevant:</b> Age, gender, or number of languages beyond '
        'the two required for the role.</div>',unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown('<div class="ax-card"><div class="ax-num">Assessment 01</div>'
            '<div class="ax-title">Your judgment<br>against the AI</div></div>',
            unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="ax-card"><div class="ax-num">Assessment 02</div>'
            '<div class="ax-title">Identifying<br>decision flaws</div></div>',
            unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="ax-card"><div class="ax-num">Assessment 03</div>'
            '<div class="ax-title">Uncovering<br>hidden biases</div></div>',
            unsafe_allow_html=True)

    st.markdown("")
    if st.button("Begin assessment",type="primary",use_container_width=True):
        st.session_state.phase="round1"; st.rerun()

# ═══════════════════ ROUND 1 ═══════════════════
elif phase=="round1":
    idx=st.session_state.r1_idx; total=len(PEOPLE); p=PEOPLE[idx]
    photo=PHOTOS.get(p["name"],"")

    st.markdown('<div class="ph-strip"><span class="ph-badge">Assessment 1 of 3</span>'
        '<span class="ph-title">Your judgment against the AI</span></div>',
        unsafe_allow_html=True)

    sc1,sc2=st.columns(2)
    with sc1: st.metric("Your score",f"{st.session_state.r1_you}/{idx}")
    with sc2: st.metric("AI score",f"{st.session_state.r1_ai}/{idx}")

    st.markdown("Review the candidate against the published criteria. Should this person be invited to interview?")

    st.markdown(
        f'<div class="cand-card">'
        f'<div class="cand-top">'
        f'<img class="cand-photo" src="{photo}" alt="">'
        f'<div><div class="cand-name">{p["name"]}</div>'
        f'<div class="cand-sub">Candidate {idx+1} of {total}</div></div></div>'
        f'<div class="cand-grid">'
        f'<div class="cand-cell"><div class="cand-cell-label">Experience</div>'
        f'<div class="cand-cell-val">{p["exp"]} years</div></div>'
        f'<div class="cand-cell"><div class="cand-cell-label">Education</div>'
        f'<div class="cand-cell-val">{EDU[p["edu"]]}</div></div>'
        f'<div class="cand-cell"><div class="cand-cell-label">Languages</div>'
        f'<div class="cand-cell-val">{LANG_NAMES[p["lang"]]}</div></div>'
        f'<div class="cand-cell"><div class="cand-cell-label">Age</div>'
        f'<div class="cand-cell-val">{p["age"]}</div></div></div>'
        f'<div class="cand-bg-row"><div class="cand-cell-label">Background</div>'
        f'<div class="cand-cell-val">{p["bg"]}</div></div></div>',
        unsafe_allow_html=True)

    def _r1(ud):
        person=PEOPLE[st.session_state.r1_idx]; gt=ground_truth(person); ai=ai_pred(person)
        u_ok=ud==gt; a_ok=ai==gt
        if u_ok: st.session_state.r1_you+=1
        if a_ok: st.session_state.r1_ai+=1
        if not a_ok: st.session_state.r1_errors.append(dict(person=person,ai_said=ai,correct=gt))
        ct="interview" if gt else "pass"; at="interview" if ai else "pass"
        if u_ok and a_ok: msg=f"Both correct. {person['name']} meets the criteria for an {ct}."; kind="green"
        elif u_ok and not a_ok:
            extra=""
            if person["age"]>=45 and gt==1 and ai==0: extra=f" This candidate is {person['age']}. Consider whether the AI may be penalising age."
            elif person["edu"]<=1 and ai==1: extra=" The AI appears to have over-weighted language skills while ignoring the missing degree requirement."
            msg=f"Your assessment was correct. The AI recommended \"{at},\" which was wrong.{extra}"; kind="green"
        elif not u_ok and a_ok: msg=f"The AI was correct here. The appropriate decision was \"{ct}.\""; kind="red"
        else: msg=f"A difficult case. Both assessments reached the wrong conclusion. The correct decision was \"{ct}.\""; kind="amber"
        st.session_state.r1_feedback=(msg,kind); st.session_state.r1_decided=True

    if not st.session_state.r1_decided:
        cy,cn=st.columns(2)
        with cy:
            if st.button("Invite to interview",use_container_width=True,key=f"r1y{idx}"): _r1(1); st.rerun()
        with cn:
            if st.button("Pass",use_container_width=True,key=f"r1n{idx}"): _r1(0); st.rerun()

    if st.session_state.r1_feedback:
        msg,kind=st.session_state.r1_feedback
        css={"green":"nt-green","red":"nt-red","amber":"nt-amber"}.get(kind,"nt-blue")
        st.markdown(f'<div class="nt {css}">{msg}</div>',unsafe_allow_html=True)
        if idx<total-1:
            if st.button("Next candidate",use_container_width=True):
                st.session_state.r1_idx+=1; st.session_state.r1_feedback=None; st.session_state.r1_decided=False; st.rerun()
        else:
            if st.button("View Assessment 1 results",type="primary",use_container_width=True):
                st.session_state.phase="r1_results"; st.rerun()
    st.progress((idx+1)/total)

# ═══════════════════ R1 RESULTS ═══════════════════
elif phase=="r1_results":
    you=st.session_state.r1_you; ai_sc=st.session_state.r1_ai; total=len(PEOPLE)
    headline="Your score matched or exceeded the AI." if you>=ai_sc else "The AI scored higher."
    st.markdown(f'<div class="ph-strip"><span class="ph-badge">Assessment 1 Results</span>'
        f'<span class="ph-title">{headline}</span></div>',unsafe_allow_html=True)

    lc,rc=st.columns(2)
    with lc: st.markdown(f'<div class="s-card"><div class="s-val">{you}/{total}</div><div class="s-label">Your score</div></div>',unsafe_allow_html=True)
    with rc: st.markdown(f'<div class="s-card"><div class="s-val">{ai_sc}/{total}</div><div class="s-label">AI score</div></div>',unsafe_allow_html=True)

    if you>=ai_sc:
        st.markdown('<div class="nt nt-amber"><b>Consider the following:</b> you reviewed each candidate carefully. This AI processes hundreds of applications per hour. Even if your judgment is more reliable, it cannot be applied at the same scale. The relevant question is not whether the AI is perfect, but whether its specific errors are acceptable.</div>',unsafe_allow_html=True)
    else:
        st.markdown('<div class="nt nt-amber"><b>The AI was more accurate overall, but accuracy alone does not indicate fairness.</b> Examine the cases below where the AI made errors. Is there a pattern?</div>',unsafe_allow_html=True)

    errors=st.session_state.r1_errors
    if errors:
        st.markdown("#### Cases where the AI was incorrect")
        for e in errors:
            pp=e["person"]; photo=PHOTOS.get(pp["name"],"")
            ai_t="Interview" if e["ai_said"] else "Pass"
            co_t="Interview" if e["correct"] else "Pass"
            st.markdown(f'<div class="err-row"><img class="err-photo" src="{photo}" alt="">'
                f'<div style="flex:1;font-size:0.86rem;"><b style="color:#d4d0c8;">{pp["name"]}</b>, age {pp["age"]}, '
                f'{pp["exp"]} years experience, {EDU[pp["edu"]]}<br>'
                f'<span style="color:#6a6560;">AI: {ai_t} (correct: {co_t})</span></div></div>',unsafe_allow_html=True)

        age_errs=[e for e in errors if e["person"]["age"]>=45 and e["correct"]==1 and e["ai_said"]==0]
        if age_errs:
            st.markdown('<div class="nt nt-red"><b>A pattern emerges.</b> The AI rejected qualified candidates over the age of 45. The job criteria state that age should not be a factor. Assessment 2 will examine this further.</div>',unsafe_allow_html=True)

    if st.button("Continue to Assessment 2",type="primary",use_container_width=True):
        st.session_state.phase="round2"; st.rerun()

# ═══════════════════ ROUND 2 ═══════════════════
elif phase=="round2":
    idx=st.session_state.r2_idx; total=len(R2_PAIRS); pair=R2_PAIRS[idx]

    st.markdown('<div class="ph-strip"><span class="ph-badge">Assessment 2 of 3</span>'
        '<span class="ph-title">Identifying decision flaws</span></div>',unsafe_allow_html=True)

    st.markdown(f"**Correct so far:** {st.session_state.r2_score} of {idx}")
    st.markdown("Two nearly identical candidates received opposite decisions. Identify which detail caused the reversal.")

    ca,cb=st.columns(2)
    for col,lbl,pk in [(ca,"Candidate A","a"),(cb,"Candidate B","b")]:
        prof=pair[pk]; dec=ai_pred(prof)
        dec_txt="Interview" if dec else "Pass"
        pill_cls="dec-yes" if dec else "dec-no"
        rows=""
        for k in ["exp","edu","lang","age"]:
            other="b" if pk=="a" else "a"
            diff=prof[k]!=pair[other][k]
            hl=' style="background:rgba(200,169,110,0.12);border-radius:4px;"' if diff and st.session_state.r2_decided else ""
            wt="font-weight:700;" if diff and st.session_state.r2_decided else ""
            rows+=f'<div{hl} style="display:flex;justify-content:space-between;padding:5px 8px;{wt}">'
            rows+=f'<span style="color:#6a6560;font-size:0.8rem;">{FIELD_LABELS[k]}</span>'
            rows+=f'<span style="color:#d4d0c8;font-size:0.84rem;">{fmt_field(k,prof[k])}</span></div>'
        with col:
            st.markdown(f'<div class="cmp-card"><div class="cmp-hdr">'
                f'<span class="cmp-label">{lbl}</span>'
                f'<span class="dec-pill {pill_cls}">{dec_txt}</span></div>'
                f'{rows}</div>',unsafe_allow_html=True)

    st.markdown(""); st.markdown("**Which factor caused the AI to reverse its decision?**")

    if not st.session_state.r2_decided:
        fields=list(FIELD_LABELS.keys()); rng=np.random.RandomState(idx+42); rng.shuffle(fields)
        cols=st.columns(len(fields))
        for i,k in enumerate(fields):
            with cols[i]:
                if st.button(FIELD_LABELS[k],key=f"r2_{idx}_{k}",use_container_width=True):
                    ok=k==pair["diff"]
                    if ok: st.session_state.r2_score+=1
                    st.session_state.r2_feedback=(ok,pair); st.session_state.r2_decided=True; st.rerun()

    if st.session_state.r2_feedback:
        ok,p2=st.session_state.r2_feedback
        if ok: st.markdown(f'<div class="nt nt-green"><b>Correct.</b> {p2["insight"]}</div>',unsafe_allow_html=True)
        else: st.markdown(f'<div class="nt nt-red"><b>The determining factor was {p2["label"].lower()}.</b> {p2["insight"]}</div>',unsafe_allow_html=True)
        if idx<total-1:
            if st.button("Next comparison",use_container_width=True):
                st.session_state.r2_idx+=1; st.session_state.r2_feedback=None; st.session_state.r2_decided=False; st.rerun()
        else:
            if st.button("View Assessment 2 results",type="primary",use_container_width=True):
                st.session_state.phase="r2_results"; st.rerun()
    st.progress((idx+1)/total)

# ═══════════════════ R2 RESULTS ═══════════════════
elif phase=="r2_results":
    sc=st.session_state.r2_score; total=len(R2_PAIRS)
    st.markdown(f'<div class="ph-strip"><span class="ph-badge">Assessment 2 Results</span>'
        f'<span class="ph-title">{sc} of {total} correctly identified</span></div>',unsafe_allow_html=True)
    st.markdown('<div class="nt nt-blue"><b>The pattern is consistent.</b> Two of the four reversals were caused by age alone, a factor the position criteria explicitly exclude. The AI also assigns disproportionate weight to languages and formal education beyond what the role requires. Assessment 3 allows you to explore these biases directly.</div>',unsafe_allow_html=True)
    if st.button("Continue to Assessment 3",type="primary",use_container_width=True):
        st.session_state.phase="round3"; st.rerun()

# ═══════════════════ ROUND 3 ═══════════════════
elif phase=="round3":
    st.markdown('<div class="ph-strip"><span class="ph-badge">Assessment 3 of 3</span>'
        '<span class="ph-title">Uncovering hidden biases</span></div>',unsafe_allow_html=True)

    st.markdown("The candidate below was recommended for interview. Adjust the parameters of their application. Determine which factors the AI penalises inappropriately.")

    BASE=dict(exp=12,edu=3,lang=4,age=41); photo=PHOTOS["Elena Richter"]
    st.markdown(f'<div class="cand-card"><div class="cand-top">'
        f'<img class="cand-photo" src="{photo}" alt="">'
        f'<div><div class="cand-name">Elena Richter</div>'
        f'<div class="cand-sub">12 years at European Commission. Master\'s degree. Four languages. Age 41.</div>'
        f'</div></div></div>',unsafe_allow_html=True)

    exp=st.slider("Years of experience (position requires 3 or more)",0,20,BASE["exp"])
    edu=st.slider("Education level (position requires bachelor's or higher)",0,4,BASE["edu"],
        help="0 = No degree, 1 = Vocational, 2 = Bachelor's, 3 = Master's, 4 = Doctorate")
    st.caption(f"Selected: {EDU[edu]}")
    lang=st.slider("Languages spoken (position requires 2)",1,4,BASE["lang"])
    st.caption(f"Selected: {LANG_NAMES[lang]}")
    age=st.slider("Age (should not affect the decision)",22,62,BASE["age"])

    cur=dict(exp=exp,edu=edu,lang=lang,age=age); prob=ai_prob(cur); dec=1 if prob>0.5 else 0
    if dec: st.success(f"AI decision: **Invite to interview** (confidence: {prob:.0%})")
    else: st.error(f"AI decision: **Pass** (confidence: {1-prob:.0%})")

    disc=list(st.session_state.r3_discoveries)
    age_only=dict(**BASE); age_only["age"]=age
    if ai_pred(age_only)==0 and age>BASE["age"] and "age" not in disc: disc.append("age")
    lang_only=dict(**BASE); lang_only["lang"]=lang
    if ai_pred(lang_only)==0 and lang<BASE["lang"] and "lang" not in disc: disc.append("lang")
    st.session_state.r3_discoveries=disc

    if "age" in disc:
        st.markdown('<div class="nt nt-red"><b>Bias identified: age discrimination.</b> Increasing this candidate\'s age while holding all other qualifications constant caused the AI to reject them. The position criteria state that age is not a relevant factor.</div>',unsafe_allow_html=True)
    if "lang" in disc:
        st.markdown('<div class="nt nt-amber"><b>Disproportionate weighting: languages.</b> Reducing languages to 2, the number the position actually requires, reversed the AI\'s decision. The system treats a non-essential qualification as decisive.</div>',unsafe_allow_html=True)

    if len(disc)<2:
        if "age" in disc: st.markdown('<div class="nt nt-blue">You have identified the age bias. Now reduce the number of languages to 2, which meets the position requirement, and observe the result.</div>',unsafe_allow_html=True)
        elif "lang" in disc: st.markdown('<div class="nt nt-blue">You have identified the language weighting issue. Now increase the candidate\'s age and observe whether the AI penalises older applicants.</div>',unsafe_allow_html=True)
        else: st.markdown('<div class="nt nt-blue">Adjust one parameter at a time. Begin with age: increase it while keeping all other factors unchanged.</div>',unsafe_allow_html=True)
    else:
        if st.button("View complete findings",type="primary",use_container_width=True):
            st.session_state.phase="finale"; st.rerun()

# ═══════════════════ FINALE ═══════════════════
elif phase=="finale":
    st.markdown(f'<div class="hero-wrap" style="height:200px;"><img src="{HERO_IMG}" alt="">'
        f'<div class="hero-content" style="text-align:center;padding-bottom:2rem;">'
        f'<div class="hero-eyebrow">Stress Test Complete</div>'
        f'<div class="hero-h1" style="font-size:1.8rem;">Assessment Summary</div>'
        f'</div></div>',unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)
    with c1: st.markdown(f'<div class="s-card"><div class="s-val">{st.session_state.r1_you}/{len(PEOPLE)}</div><div class="s-label">Assessment 1</div></div>',unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="s-card"><div class="s-val">{st.session_state.r2_score}/{len(R2_PAIRS)}</div><div class="s-label">Assessment 2</div></div>',unsafe_allow_html=True)
    with c3:
        n=len(st.session_state.r3_discoveries)
        st.markdown(f'<div class="s-card"><div class="s-val">{n} bias{"es" if n!=1 else ""}</div><div class="s-label">Assessment 3</div></div>',unsafe_allow_html=True)

    st.markdown("### How the AI weights its decisions")
    st.markdown("The system was trained on historical hiring data. It learned decision patterns from previous outcomes, including biases embedded in past decisions.")

    weights=[
        ("Education level",85,True,"Appropriate: aligns with requirements"),
        ("Languages spoken",55,False,"Over-weighted: role requires 2, AI treats 3+ as essential"),
        ("Age",38,False,"Should carry zero weight: age discrimination"),
        ("Years of experience",14,True,"Under-weighted: AI favours credentials over practice"),
    ]
    for label,w,fair,note in weights:
        color="#7ab87a" if fair else "#d4827a"
        st.markdown(f'<div style="margin-bottom:0.8rem;"><div style="display:flex;justify-content:space-between;font-size:0.8rem;margin-bottom:3px;">'
            f'<span style="font-weight:600;color:#d4d0c8;">{label}</span>'
            f'<span style="font-size:0.75rem;color:{color};">{note}</span></div>'
            f'<div class="wb-bg"><div class="wb-fill" style="width:{w}%;background:{color};"></div></div></div>',unsafe_allow_html=True)

    st.markdown("The position criteria state that age is not relevant. However, the AI learned from data in which older candidates were selected less frequently, and reproduced this pattern as though it were a legitimate criterion. **The AI did not create the bias. It inherited it from historical decisions and applied it at scale.**")

    st.markdown("---")
    st.markdown("### Regulatory implications")
    st.markdown('<div class="nt nt-blue"><b>Accuracy does not indicate fairness.</b> The AI achieved 92% accuracy while systematically discriminating by age. A system can produce mostly correct outcomes and still embed impermissible biases.</div>',unsafe_allow_html=True)
    st.markdown('<div class="nt nt-blue"><b>Historical data encodes historical biases.</b> AI trained on past decisions will reproduce past discrimination unless specific technical countermeasures are applied. Automated systems scale bias at speeds that manual processes never could.</div>',unsafe_allow_html=True)
    st.markdown('<div class="nt nt-blue"><b>Effective regulation requires more than accuracy benchmarks.</b> Three categories of testing are necessary: robustness testing, bias auditing, and explainability requirements.</div>',unsafe_allow_html=True)
    st.markdown('<div class="nt nt-amber"><b>Regulatory consideration:</b> approving an AI system on the basis of accuracy alone is comparable to evaluating a hiring manager solely by the number of positions filled, without examining whether they discriminated in the process.</div>',unsafe_allow_html=True)

    st.markdown("---")
    if st.button("Restart assessment",use_container_width=True):
        for k,v in _defaults.items(): st.session_state[k]=v
        st.rerun()

st.markdown('<div class="footer-text">AI Regulatory Stress Test. Stanford SAFE prototype. '
    'Developed to demonstrate how interactive tools can support technically informed '
    'policy decisions on AI systems.</div>',unsafe_allow_html=True)
