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

    .block-container { padding-top: 0 !important; max-width: 820px; }
    .stApp { background: #0c1220; }
    * { font-family: 'Karla', sans-serif !important; }

    .stMarkdown, .stMarkdown p, .stMarkdown li,
    .stMarkdown span, label, .stSlider label,
    .stSelectbox label {
        color: #b8c4d6 !important;
        font-size: 1rem !important;
    }
    h1, h2, h3, h4 {
        color: #e8ecf4 !important;
        font-family: 'Instrument Serif', Georgia, serif !important;
    }
    .stMetricValue { color: #e8ecf4 !important; font-size: 1.6rem !important; }
    .stMetricLabel { color: #5a6a82 !important; }
    strong, b { color: #e8ecf4 !important; }

    /* Hero */
    .hero-wrap {
        position: relative;
        margin: -1rem -1rem 2.5rem -1rem;
        height: 380px;
        overflow: hidden;
    }
    .hero-wrap img {
        width: 100%; height: 100%;
        object-fit: cover;
        filter: brightness(0.25) saturate(0.5) hue-rotate(10deg);
    }
    .hero-content {
        position: absolute;
        bottom: 0; left: 0; right: 0;
        padding: 3.5rem 3rem 3rem;
        background: linear-gradient(transparent, rgba(12,18,32,0.97));
    }
    .hero-eyebrow {
        font-family: 'Karla', sans-serif;
        font-size: 0.72rem; font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #6fa3d4;
        margin-bottom: 0.7rem;
    }
    .hero-h1 {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 2.8rem; font-weight: 400;
        color: #e8ecf4;
        line-height: 1.08;
        letter-spacing: -0.02em;
    }
    .hero-desc {
        font-size: 1.05rem;
        color: #7a8ba0;
        margin-top: 0.9rem;
        line-height: 1.65;
        max-width: 580px;
    }

    /* Phase header */
    .ph-strip {
        display: flex; align-items: center; gap: 16px;
        margin-bottom: 1.8rem;
        padding-bottom: 1.2rem;
        border-bottom: 1px solid #1e2a3e;
    }
    .ph-badge {
        background: #1a3a5c;
        color: #6fa3d4;
        font-size: 0.65rem; font-weight: 700;
        padding: 6px 14px; border-radius: 4px;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        white-space: nowrap;
    }
    .ph-title {
        font-family: 'Instrument Serif', Georgia, serif !important;
        font-size: 1.5rem;
        color: #e8ecf4;
    }

    /* Stat cards */
    .s-card {
        background: #111b2e;
        border: 1px solid #1e2a3e;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
    }
    .s-val {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 2.6rem;
        color: #e8ecf4;
        line-height: 1.1;
    }
    .s-label {
        font-size: 0.78rem;
        color: #5a6a82;
        margin-top: 0.3rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    /* Candidate card */
    .cand-card {
        background: #111b2e;
        border: 1px solid #1e2a3e;
        border-radius: 16px;
        padding: 0;
        margin-bottom: 1.5rem;
        overflow: hidden;
    }
    .cand-top {
        display: flex;
        align-items: center;
        gap: 22px;
        padding: 1.8rem 2rem 1.2rem;
    }
    .cand-photo {
        width: 96px; height: 96px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #1e2a3e;
        flex-shrink: 0;
    }
    .cand-name {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1.45rem;
        color: #e8ecf4;
    }
    .cand-sub {
        font-size: 0.88rem;
        color: #5a6a82;
        margin-top: 4px;
    }
    .cand-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1px;
        background: #1e2a3e;
    }
    .cand-cell {
        background: #111b2e;
        padding: 16px 22px;
    }
    .cand-cell-label {
        font-size: 0.7rem;
        color: #5a6a82;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .cand-cell-val {
        font-size: 1.02rem;
        color: #b8c4d6;
        margin-top: 4px;
        font-weight: 500;
    }
    .cand-bg-row {
        background: #0e1726;
        padding: 16px 22px;
        border-top: 1px solid #1e2a3e;
    }

    /* Notes */
    .nt {
        padding: 1.1rem 1.4rem;
        margin: 1rem 0;
        font-size: 0.92rem;
        line-height: 1.65;
        border-radius: 10px;
        border: 1px solid;
    }
    .nt-blue {
        background: rgba(80,140,200,0.07);
        border-color: rgba(80,140,200,0.2);
        color: #8bb8d4;
    }
    .nt-slate {
        background: rgba(100,130,170,0.07);
        border-color: rgba(100,130,170,0.2);
        color: #8ba0bd;
    }
    .nt-red {
        background: rgba(200,90,80,0.07);
        border-color: rgba(200,90,80,0.2);
        color: #d4827a;
    }
    .nt-green {
        background: rgba(80,170,100,0.07);
        border-color: rgba(80,170,100,0.2);
        color: #6ec48a;
    }

    /* Criteria box */
    .crit-box {
        background: #111b2e;
        border: 1px solid #1e2a3e;
        border-radius: 14px;
        padding: 1.8rem 2rem;
        margin-bottom: 2rem;
        font-size: 0.95rem;
        line-height: 1.75;
        color: #8a96aa;
    }
    .crit-title {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1.15rem;
        color: #e8ecf4;
        margin-bottom: 0.9rem;
    }
    .crit-box b { color: #b8c4d6; }

    /* Assessment cards */
    .ax-card {
        background: #111b2e;
        border: 1px solid #1e2a3e;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: border-color 0.2s;
    }
    .ax-card:hover { border-color: #3a6a9a; }
    .ax-num {
        font-size: 0.62rem; font-weight: 700;
        color: #6fa3d4;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
    }
    .ax-title {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1.05rem;
        color: #e8ecf4;
        line-height: 1.35;
    }

    /* Comparison cards */
    .cmp-card {
        background: #111b2e;
        border: 1px solid #1e2a3e;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
    }
    .cmp-hdr {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    .cmp-label {
        font-size: 0.95rem;
        font-weight: 600;
        color: #b8c4d6;
    }
    .dec-pill {
        font-size: 0.72rem; font-weight: 700;
        padding: 5px 14px; border-radius: 4px;
        letter-spacing: 0.04em;
    }
    .dec-yes { background: rgba(80,170,100,0.12); color: #6ec48a; }
    .dec-no { background: rgba(200,90,80,0.12); color: #d4827a; }

    /* Weight bars */
    .wb-bg {
        height: 6px; background: #1e2a3e;
        border-radius: 3px; overflow: hidden;
        margin-top: 6px;
    }
    .wb-fill { height: 100%; border-radius: 3px; }

    /* Error list */
    .err-row {
        display: flex; align-items: center;
        gap: 16px; padding: 14px 0;
        border-bottom: 1px solid #151f32;
    }
    .err-photo {
        width: 56px; height: 56px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #1e2a3e;
        flex-shrink: 0;
    }

    /* Finale sections */
    .fin-section {
        background: #111b2e;
        border: 1px solid #1e2a3e;
        border-radius: 14px;
        padding: 2rem 2.2rem;
        margin-bottom: 1.5rem;
    }
    .fin-section-title {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1.2rem;
        color: #e8ecf4;
        margin-bottom: 1rem;
    }
    .fin-text {
        font-size: 0.95rem;
        color: #8a96aa;
        line-height: 1.7;
    }
    .fin-text b { color: #b8c4d6; }
    .fin-divider {
        height: 1px;
        background: #1e2a3e;
        margin: 1.5rem 0;
    }

    .footer-text {
        text-align: center; color: #2a3548;
        font-size: 0.72rem; margin-top: 3rem;
        padding-top: 1.2rem;
        border-top: 1px solid #151f32;
    }

    /* Streamlit overrides */
    .stProgress > div > div > div > div { background: #4a8ac4 !important; }
    .stButton > button {
        background: #2a5a8a !important;
        color: #e8ecf4 !important;
        border: none !important;
        font-weight: 600 !important;
        font-family: 'Karla', sans-serif !important;
        font-size: 1rem !important;
        padding: 0.7rem 1.5rem !important;
        border-radius: 8px !important;
    }
    .stButton > button:hover { background: #3a6a9a !important; }
    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="baseButton-secondary"] {
        background: #111b2e !important;
        color: #b8c4d6 !important;
        border: 1px solid #1e2a3e !important;
    }
    .stButton > button[kind="secondary"]:hover,
    .stButton > button[data-testid="baseButton-secondary"]:hover {
        border-color: #4a8ac4 !important;
        color: #6fa3d4 !important;
    }
    div[data-testid="stSlider"] label { color: #7a8ba0 !important; }
    .stCaption { color: #5a6a82 !important; }
</style>
""", unsafe_allow_html=True)

PHOTOS = {
    "Katrin Bauer": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=300&h=300&fit=crop&crop=face",
    "Heinrich Vogel": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=300&h=300&fit=crop&crop=face",
    "Sophie Laurent": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=300&h=300&fit=crop&crop=face",
    "Lukas Schmidt": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=300&fit=crop&crop=face",
    "Brigitte Engel": "https://images.unsplash.com/photo-1594744803329-e58b31de8bf5?w=300&h=300&fit=crop&crop=face",
    "Felix Mayer": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=300&h=300&fit=crop&crop=face",
    "Elena Richter": "https://images.unsplash.com/photo-1598550874175-4d0ef436c909?w=300&h=300&fit=crop&crop=face",
    "Wolfgang Krause": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=300&h=300&fit=crop&crop=face",
}
HERO_IMG = "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1400&h=700&fit=crop"

EDU = ["No formal degree", "Vocational qualification", "Bachelor's degree", "Master's degree", "Doctorate"]
LANG_NAMES = {1:"German", 2:"German, English", 3:"German, English, French", 4:"German, English, French, Spanish"}

PEOPLE = [
    dict(name="Katrin Bauer",exp=8,edu=3,lang=3,age=34,bg="Municipal planning office, 8 years in project management"),
    dict(name="Heinrich Vogel",exp=6,edu=2,lang=2,age=54,bg="State government, policy implementation and coordination"),
    dict(name="Sophie Laurent",exp=4,edu=1,lang=4,age=28,bg="EU translation office, administrative support"),
    dict(name="Lukas Schmidt",exp=5,edu=4,lang=2,age=31,bg="University research institute, published policy papers"),
    dict(name="Brigitte Engel",exp=10,edu=2,lang=2,age=49,bg="Federal ministry, interdepartmental coordination"),
    dict(name="Felix Mayer",exp=1,edu=2,lang=2,age=24,bg="City council internship, recent graduate"),
    dict(name="Elena Richter",exp=4,edu=3,lang=4,age=29,bg="European Commission liaison, policy analysis"),
    dict(name="Wolfgang Krause",exp=9,edu=3,lang=2,age=51,bg="Parliamentary research service, legislative analysis"),
]

R2_PAIRS = [
    dict(a=dict(exp=7,edu=3,lang=2,age=33),b=dict(exp=7,edu=3,lang=2,age=48),diff="age",label="Age",desc="15 years older",
         insight="The position criteria explicitly state that age is not a relevant factor. The AI nonetheless treats it as one. This constitutes automated age discrimination, concealed within a system that reports high overall accuracy."),
    dict(a=dict(exp=5,edu=3,lang=3,age=35),b=dict(exp=5,edu=3,lang=2,age=35),diff="lang",label="Languages",desc="one fewer language",
         insight="Both candidates meet the language requirement of two. A third language is listed as preferred, not required. The AI treats it as decisive, giving disproportionate weight to a non-essential qualification."),
    dict(a=dict(exp=8,edu=2,lang=2,age=36),b=dict(exp=4,edu=3,lang=2,age=36),diff="exp",label="Experience versus Education",desc="4 fewer years but a master's instead of bachelor's",
         insight="The AI heavily favours formal education over practical experience. An 8-year veteran with a bachelor's is rejected while a 4-year master's graduate is accepted. Whether this trade-off is appropriate is a policy decision that should not be delegated to an algorithm."),
    dict(a=dict(exp=6,edu=3,lang=2,age=30),b=dict(exp=6,edu=3,lang=2,age=52),diff="age",label="Age",desc="22 years older",
         insight="Identical qualifications produce opposite outcomes, determined entirely by age. This is precisely the type of automated discrimination that the EU AI Act's high-risk classification for employment systems is designed to address."),
]

FIELD_LABELS = {"exp":"Experience","edu":"Education","lang":"Languages","age":"Age"}

def ground_truth(c):
    e,x,l = c["edu"],c["exp"],c["lang"]
    if e<2: return 0
    if e>=3 and x>=2: return 1
    if e>=2 and x>=5: return 1
    if e>=2 and x>=3 and l>=3: return 1
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

_defaults = dict(phase="intro",r1_idx=0,r1_you=0,r1_ai=0,r1_errors=[],r1_feedback=None,r1_decided=False,
    r2_idx=0,r2_score=0,r2_feedback=None,r2_decided=False,r3_discoveries=[])
for _k,_v in _defaults.items():
    if _k not in st.session_state: st.session_state[_k]=_v
phase = st.session_state.phase

# ═══════════════════ INTRO ═══════════════════
if phase=="intro":
    st.markdown(f'<div class="hero-wrap"><img src="{HERO_IMG}" alt=""><div class="hero-content">'
        f'<div class="hero-eyebrow">Stanford SAFE Project</div>'
        f'<div class="hero-h1">AI Regulatory<br>Stress Test</div>'
        f'<div class="hero-desc">A government agency proposes using AI to screen civil service applications. The vendor reports 92% accuracy. Evaluate that claim through three structured assessments.</div>'
        f'</div></div>',unsafe_allow_html=True)

    st.markdown('<div class="crit-box"><div class="crit-title">Position: Policy Advisor, Civil Service</div>'
        '<b>Required:</b> Bachelor\'s degree or higher. Minimum 3 years of relevant professional experience.<br>'
        '<b>Preferred:</b> Master\'s degree or doctorate. 7 or more years of experience. Multilingual. Public sector background.<br>'
        '<b>Not relevant:</b> Age, gender, or number of languages beyond the two required for the role.</div>',unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)
    with c1: st.markdown('<div class="ax-card"><div class="ax-num">Assessment 01</div><div class="ax-title">Your judgment<br>against the AI</div></div>',unsafe_allow_html=True)
    with c2: st.markdown('<div class="ax-card"><div class="ax-num">Assessment 02</div><div class="ax-title">Identifying<br>decision flaws</div></div>',unsafe_allow_html=True)
    with c3: st.markdown('<div class="ax-card"><div class="ax-num">Assessment 03</div><div class="ax-title">Uncovering<br>hidden biases</div></div>',unsafe_allow_html=True)

    st.markdown("")
    if st.button("Begin assessment",type="primary",use_container_width=True):
        st.session_state.phase="round1"; st.rerun()

# ═══════════════════ ROUND 1 ═══════════════════
elif phase=="round1":
    idx=st.session_state.r1_idx; total=len(PEOPLE); p=PEOPLE[idx]; photo=PHOTOS.get(p["name"],"")
    st.markdown('<div class="ph-strip"><span class="ph-badge">Assessment 1 of 3</span><span class="ph-title">Your judgment against the AI</span></div>',unsafe_allow_html=True)
    sc1,sc2=st.columns(2)
    with sc1: st.metric("Your score",f"{st.session_state.r1_you}/{idx}")
    with sc2: st.metric("AI score",f"{st.session_state.r1_ai}/{idx}")
    st.markdown("Review the candidate against the published criteria. Should this person be invited to interview?")

    st.markdown(f'<div class="cand-card"><div class="cand-top">'
        f'<img class="cand-photo" src="{photo}" alt="">'
        f'<div><div class="cand-name">{p["name"]}</div><div class="cand-sub">Candidate {idx+1} of {total}</div></div></div>'
        f'<div class="cand-grid">'
        f'<div class="cand-cell"><div class="cand-cell-label">Experience</div><div class="cand-cell-val">{p["exp"]} years</div></div>'
        f'<div class="cand-cell"><div class="cand-cell-label">Education</div><div class="cand-cell-val">{EDU[p["edu"]]}</div></div>'
        f'<div class="cand-cell"><div class="cand-cell-label">Languages</div><div class="cand-cell-val">{LANG_NAMES[p["lang"]]}</div></div>'
        f'<div class="cand-cell"><div class="cand-cell-label">Age</div><div class="cand-cell-val">{p["age"]}</div></div></div>'
        f'<div class="cand-bg-row"><div class="cand-cell-label">Background</div><div class="cand-cell-val">{p["bg"]}</div></div></div>',unsafe_allow_html=True)

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
        else: msg=f"A difficult case. Both reached the wrong conclusion. The correct decision was \"{ct}.\""; kind="slate"
        st.session_state.r1_feedback=(msg,kind); st.session_state.r1_decided=True

    if not st.session_state.r1_decided:
        cy,cn=st.columns(2)
        with cy:
            if st.button("Invite to interview",use_container_width=True,key=f"r1y{idx}"): _r1(1); st.rerun()
        with cn:
            if st.button("Pass",use_container_width=True,key=f"r1n{idx}"): _r1(0); st.rerun()

    if st.session_state.r1_feedback:
        msg,kind=st.session_state.r1_feedback
        css={"green":"nt-green","red":"nt-red","slate":"nt-slate"}.get(kind,"nt-blue")
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
    st.markdown(f'<div class="ph-strip"><span class="ph-badge">Assessment 1 Results</span><span class="ph-title">{headline}</span></div>',unsafe_allow_html=True)
    lc,rc=st.columns(2)
    with lc: st.markdown(f'<div class="s-card"><div class="s-val">{you}/{total}</div><div class="s-label">Your score</div></div>',unsafe_allow_html=True)
    with rc: st.markdown(f'<div class="s-card"><div class="s-val">{ai_sc}/{total}</div><div class="s-label">AI score</div></div>',unsafe_allow_html=True)

    if you>=ai_sc:
        st.markdown('<div class="nt nt-slate"><b>Consider the following:</b> you reviewed each candidate carefully. This AI processes hundreds of applications per hour. Even if your judgment is more reliable, it cannot be applied at the same scale. The relevant question is not whether the AI is perfect, but whether its specific errors are acceptable.</div>',unsafe_allow_html=True)
    else:
        st.markdown('<div class="nt nt-slate"><b>The AI was more accurate overall, but accuracy alone does not indicate fairness.</b> Examine the cases below. Is there a pattern in its errors?</div>',unsafe_allow_html=True)

    errors=st.session_state.r1_errors
    if errors:
        st.markdown("#### Cases where the AI was incorrect")
        for e in errors:
            pp=e["person"]; photo=PHOTOS.get(pp["name"],"")
            ai_t="Interview" if e["ai_said"] else "Pass"; co_t="Interview" if e["correct"] else "Pass"
            st.markdown(f'<div class="err-row"><img class="err-photo" src="{photo}" alt="">'
                f'<div style="flex:1;font-size:0.95rem;"><b style="color:#e8ecf4;">{pp["name"]}</b>, age {pp["age"]}, '
                f'{pp["exp"]} years experience, {EDU[pp["edu"]]}<br>'
                f'<span style="color:#5a6a82;">AI: {ai_t} (correct: {co_t})</span></div></div>',unsafe_allow_html=True)
        age_errs=[e for e in errors if e["person"]["age"]>=45 and e["correct"]==1 and e["ai_said"]==0]
        if age_errs:
            st.markdown('<div class="nt nt-red"><b>A pattern emerges.</b> The AI rejected qualified candidates over the age of 45. The job criteria state that age should not be a factor. Assessment 2 examines this further.</div>',unsafe_allow_html=True)

    if st.button("Continue to Assessment 2",type="primary",use_container_width=True):
        st.session_state.phase="round2"; st.rerun()

# ═══════════════════ ROUND 2 ═══════════════════
elif phase=="round2":
    idx=st.session_state.r2_idx; total=len(R2_PAIRS); pair=R2_PAIRS[idx]
    st.markdown('<div class="ph-strip"><span class="ph-badge">Assessment 2 of 3</span><span class="ph-title">Identifying decision flaws</span></div>',unsafe_allow_html=True)
    st.markdown(f"**Correct so far:** {st.session_state.r2_score} of {idx}")
    st.markdown("Two nearly identical candidates received opposite decisions. Identify which detail caused the reversal.")

    ca,cb=st.columns(2)
    for col,lbl,pk in [(ca,"Candidate A","a"),(cb,"Candidate B","b")]:
        prof=pair[pk]; dec=ai_pred(prof); dec_txt="Interview" if dec else "Pass"; pill_cls="dec-yes" if dec else "dec-no"
        rows=""
        for k in ["exp","edu","lang","age"]:
            other="b" if pk=="a" else "a"; diff=prof[k]!=pair[other][k]
            hl='background:rgba(80,140,200,0.08);border-radius:6px;' if diff and st.session_state.r2_decided else ""
            wt="font-weight:700;color:#e8ecf4;" if diff and st.session_state.r2_decided else "color:#b8c4d6;"
            rows+=f'<div style="display:flex;justify-content:space-between;padding:7px 10px;{hl}">'
            rows+=f'<span style="color:#5a6a82;font-size:0.88rem;">{FIELD_LABELS[k]}</span>'
            rows+=f'<span style="font-size:0.92rem;{wt}">{fmt_field(k,prof[k])}</span></div>'
        with col:
            st.markdown(f'<div class="cmp-card"><div class="cmp-hdr"><span class="cmp-label">{lbl}</span>'
                f'<span class="dec-pill {pill_cls}">{dec_txt}</span></div>{rows}</div>',unsafe_allow_html=True)

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
    st.markdown(f'<div class="ph-strip"><span class="ph-badge">Assessment 2 Results</span><span class="ph-title">{sc} of {total} correctly identified</span></div>',unsafe_allow_html=True)
    st.markdown('<div class="nt nt-blue"><b>The pattern is consistent.</b> Two of the four reversals were caused by age alone, a factor the position criteria explicitly exclude. The AI also assigns disproportionate weight to languages and formal education beyond what the role requires. Assessment 3 allows you to explore these biases directly.</div>',unsafe_allow_html=True)
    if st.button("Continue to Assessment 3",type="primary",use_container_width=True):
        st.session_state.phase="round3"; st.rerun()

# ═══════════════════ ROUND 3 ═══════════════════
elif phase=="round3":
    st.markdown('<div class="ph-strip"><span class="ph-badge">Assessment 3 of 3</span><span class="ph-title">Uncovering hidden biases</span></div>',unsafe_allow_html=True)
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
        st.markdown('<div class="nt nt-slate"><b>Disproportionate weighting: languages.</b> Reducing languages to 2, the number the position actually requires, reversed the AI\'s decision. The system treats a non-essential qualification as decisive.</div>',unsafe_allow_html=True)

    if len(disc)<2:
        if "age" in disc: st.markdown('<div class="nt nt-blue">You have identified the age bias. Now reduce the number of languages to 2 and observe the result.</div>',unsafe_allow_html=True)
        elif "lang" in disc: st.markdown('<div class="nt nt-blue">Now increase the candidate\'s age and observe whether the AI penalises older applicants.</div>',unsafe_allow_html=True)
        else: st.markdown('<div class="nt nt-blue">Adjust one parameter at a time. Begin with age: increase it while keeping all other factors unchanged.</div>',unsafe_allow_html=True)
    else:
        if st.button("View complete findings",type="primary",use_container_width=True):
            st.session_state.phase="finale"; st.rerun()

# ═══════════════════ FINALE ═══════════════════
elif phase=="finale":
    st.markdown(f'<div class="hero-wrap" style="height:220px;"><img src="{HERO_IMG}" alt="">'
        f'<div class="hero-content" style="text-align:center;padding-bottom:2.5rem;">'
        f'<div class="hero-eyebrow">Stress Test Complete</div>'
        f'<div class="hero-h1" style="font-size:2rem;">Assessment Summary</div>'
        f'</div></div>',unsafe_allow_html=True)

    # Scores
    c1,c2,c3=st.columns(3)
    with c1: st.markdown(f'<div class="s-card"><div class="s-val">{st.session_state.r1_you}/{len(PEOPLE)}</div><div class="s-label">Assessment 1</div></div>',unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="s-card"><div class="s-val">{st.session_state.r2_score}/{len(R2_PAIRS)}</div><div class="s-label">Assessment 2</div></div>',unsafe_allow_html=True)
    with c3:
        n=len(st.session_state.r3_discoveries)
        st.markdown(f'<div class="s-card"><div class="s-val">{n} bias{"es" if n!=1 else ""}</div><div class="s-label">Assessment 3</div></div>',unsafe_allow_html=True)

    st.markdown("")

    # Section 1: What the AI learned
    st.markdown('<div class="fin-section"><div class="fin-section-title">What the AI actually learned</div>'
        '<div class="fin-text">The system was trained on historical hiring data. Rather than learning the published criteria, it learned patterns from past human decisions, including biases those decision-makers held. Below are the relative weights the AI assigns to each factor:</div></div>',unsafe_allow_html=True)

    weights=[
        ("Education level",85,True,"Appropriate: aligns with requirements"),
        ("Languages spoken",55,False,"Over-weighted: role requires 2, AI treats 3+ as essential"),
        ("Age",38,False,"Should carry zero weight: constitutes age discrimination"),
        ("Years of experience",14,True,"Under-weighted: AI favours credentials over practice"),
    ]
    for label,w,fair,note in weights:
        color="#6ec48a" if fair else "#d4827a"
        st.markdown(f'<div style="margin-bottom:1rem;"><div style="display:flex;justify-content:space-between;font-size:0.88rem;margin-bottom:4px;">'
            f'<span style="font-weight:600;color:#e8ecf4;">{label}</span>'
            f'<span style="font-size:0.82rem;color:{color};">{note}</span></div>'
            f'<div class="wb-bg"><div class="wb-fill" style="width:{w}%;background:{color};"></div></div></div>',unsafe_allow_html=True)

    st.markdown("")

    # Section 2: How this happened
    st.markdown('<div class="fin-section"><div class="fin-section-title">How bias enters the system</div>'
        '<div class="fin-text">'
        'The AI was never programmed to discriminate by age. No engineer wrote a rule that says "reject candidates over 50." '
        'Instead, the system was trained on historical hiring outcomes where older candidates happened to be selected less '
        'frequently. The AI identified this statistical pattern and reproduced it as though it were a legitimate hiring '
        'criterion.'
        '<div class="fin-divider"></div>'
        'This is the core mechanism by which AI systems inherit and scale human biases. The training data reflects the '
        'world as it was, not as policy intends it to be. Without explicit intervention, the system will perpetuate every '
        'historical inequity contained in its training data, applying them consistently, at high speed, to every future '
        'applicant.'
        '<div class="fin-divider"></div>'
        '<b>The AI did not invent the bias. It inherited it from past decisions and automated it at scale.</b>'
        '</div></div>',unsafe_allow_html=True)

    # Section 3: What accuracy hides
    st.markdown('<div class="fin-section"><div class="fin-section-title">What accuracy metrics conceal</div>'
        '<div class="fin-text">'
        'The vendor reported 92% accuracy. That figure was real. The system does, in fact, produce correct outcomes '
        'in the vast majority of cases. However, this number conceals three critical problems:'
        '<div class="fin-divider"></div>'
        '<b>1. Accuracy and fairness are independent properties.</b> A system can achieve high accuracy while '
        'systematically discriminating against a protected group. The 8% error rate was not randomly distributed. '
        'It concentrated on older candidates, who were disproportionately rejected despite meeting all stated criteria.'
        '<div class="fin-divider"></div>'
        '<b>2. AI errors are indistinguishable from correct decisions.</b> When a human reviewer makes a questionable '
        'call, colleagues may notice hesitation or ask for reasoning. The AI produces every decision, correct or '
        'incorrect, with identical confidence. Without systematic auditing, discriminatory decisions are invisible.'
        '<div class="fin-divider"></div>'
        '<b>3. Minor input variations produce arbitrary outcomes.</b> As Assessment 2 demonstrated, differences as '
        'small as one additional language or a few years of age can reverse a life-altering decision. This level '
        'of sensitivity indicates that the system is not making decisions for substantive reasons.'
        '</div></div>',unsafe_allow_html=True)

    # Section 4: Regulatory implications
    st.markdown('<div class="fin-section"><div class="fin-section-title">Regulatory implications</div>'
        '<div class="fin-text">'
        'The assessments above demonstrate why effective AI regulation cannot rely solely on accuracy benchmarks. '
        'Three categories of mandatory testing are necessary for high-risk AI systems:'
        '<div class="fin-divider"></div>'
        '<b>Robustness testing:</b> Does the system produce stable, consistent decisions when inputs change in ways '
        'that should not affect the outcome? Minor variations in age, language count, or experience duration should '
        'not reverse decisions.'
        '<div class="fin-divider"></div>'
        '<b>Bias auditing:</b> Do protected characteristics (age, gender, ethnicity, disability status) influence '
        'outcomes, either directly or through proxy variables? This requires testing across demographic subgroups, '
        'not just measuring aggregate accuracy.'
        '<div class="fin-divider"></div>'
        '<b>Explainability requirements:</b> Can the system provide a substantive justification for each individual '
        'decision? If the only explanation is a statistical correlation in historical data, that is not a sufficient '
        'basis for decisions affecting individual rights.'
        '<div class="fin-divider"></div>'
        'The EU AI Act classifies employment screening systems as high-risk, requiring conformity assessments before '
        'deployment. The assessments you completed in this exercise illustrate why that classification exists and '
        'what those conformity assessments should include.'
        '</div></div>',unsafe_allow_html=True)

    # Final takeaway
    st.markdown('<div class="nt nt-blue" style="font-size:1rem;padding:1.4rem 1.6rem;">'
        '<b>The central finding:</b> approving an AI system on the basis of accuracy alone is comparable to '
        'evaluating a hiring manager solely by the number of positions filled, without examining whether they '
        'discriminated in the process. Accuracy measures whether decisions match historical patterns. It does not '
        'measure whether those patterns are fair, legal, or aligned with policy objectives.'
        '</div>',unsafe_allow_html=True)

    st.markdown("---")
    if st.button("Restart assessment",use_container_width=True):
        for k,v in _defaults.items(): st.session_state[k]=v
        st.rerun()

st.markdown('<div class="footer-text">AI Regulatory Stress Test. Stanford SAFE prototype. '
    'Developed to demonstrate how interactive tools can support technically informed policy decisions on AI systems.</div>',unsafe_allow_html=True)
