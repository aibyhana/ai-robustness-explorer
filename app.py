"""
AI Regulatory Stress Test: Employment Screening System
Stanford SAFE project prototype.
"""

import streamlit as st
import numpy as np

st.set_page_config(page_title="AI Regulatory Stress Test", layout="centered")

# Material Design 3 inspired: surface layers, systematic elevation,
# 4px grid spacing, clear typographic hierarchy, dense information layout
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Karla:wght@400;500;600;700&display=swap');

    .block-container { padding-top: 0 !important; max-width: 820px; }

    /* Surface system: 5 elevation layers */
    .stApp { background: #0b1018; }  /* Surface 0 - base */
    /* Surface 1: #0f1520 - cards */
    /* Surface 2: #141c2a - elevated cards */
    /* Surface 3: #1a2436 - interactive elements */
    /* Surface 4: #202c40 - hover states */

    * { font-family: 'Karla', sans-serif !important; }

    .stMarkdown, .stMarkdown p, .stMarkdown li,
    .stMarkdown span, label, .stSlider label,
    .stSelectbox label {
        color: #b0bdd0 !important;
        font-size: 0.98rem !important;
        line-height: 1.7 !important;
    }
    h1,h2,h3,h4 {
        color: #e4eaf4 !important;
        font-family: 'Instrument Serif', Georgia, serif !important;
    }
    .stMetricValue { color: #e4eaf4 !important; font-size: 1.5rem !important; }
    .stMetricLabel { color: #4e5d74 !important; }
    strong, b { color: #d0dae8 !important; }

    /* Hero - full bleed image with content overlay */
    .hero {
        position: relative;
        margin: -1rem -1rem 32px -1rem;
        height: 400px;
        overflow: hidden;
    }
    .hero img {
        width: 100%; height: 100%;
        object-fit: cover;
        filter: brightness(0.22) saturate(0.4);
    }
    .hero-inner {
        position: absolute; bottom: 0; left: 0; right: 0;
        padding: 48px 40px 40px;
        background: linear-gradient(transparent 0%, rgba(11,16,24,0.95) 60%);
    }
    .hero-eyebrow {
        font-size: 0.7rem; font-weight: 700;
        letter-spacing: 0.2em; text-transform: uppercase;
        color: #5b9bd5; margin-bottom: 12px;
    }
    .hero-h1 {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 2.8rem; color: #e4eaf4;
        line-height: 1.05; letter-spacing: -0.02em;
    }
    .hero-p {
        font-size: 1.05rem; color: #6b7d96;
        margin-top: 12px; line-height: 1.7;
        max-width: 560px;
    }

    /* Phase strip - M3 top app bar pattern */
    .phase {
        display: flex; align-items: center; gap: 16px;
        padding: 0 0 16px 0;
        margin-bottom: 24px;
        border-bottom: 1px solid #151d2c;
    }
    .phase-chip {
        background: #182640;
        color: #5b9bd5;
        font-size: 0.62rem; font-weight: 700;
        padding: 6px 16px; border-radius: 4px;
        letter-spacing: 0.12em; text-transform: uppercase;
    }
    .phase-h {
        font-family: 'Instrument Serif', Georgia, serif !important;
        font-size: 1.45rem; color: #e4eaf4;
    }

    /* Cards - M3 filled card: Surface 1 + subtle outline */
    .card {
        background: #0f1520;
        border: 1px solid #1a2436;
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 20px;
    }
    .card-body { padding: 24px 28px; }

    /* Candidate card */
    .cand-header {
        display: flex; align-items: center; gap: 24px;
        padding: 28px 28px 20px;
    }
    .cand-img {
        width: 100px; height: 100px;
        border-radius: 16px;
        object-fit: cover;
        flex-shrink: 0;
    }
    .cand-name {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1.5rem; color: #e4eaf4;
    }
    .cand-meta {
        font-size: 0.85rem; color: #4e5d74;
        margin-top: 4px;
    }
    /* Data grid inside card - M3 list pattern */
    .data-grid {
        display: grid; grid-template-columns: 1fr 1fr;
        border-top: 1px solid #1a2436;
    }
    .data-cell {
        padding: 16px 28px;
        border-bottom: 1px solid #1a2436;
    }
    .data-cell:nth-child(odd) { border-right: 1px solid #1a2436; }
    .data-cell-label {
        font-size: 0.68rem; color: #4e5d74;
        font-weight: 700; letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .data-cell-val {
        font-size: 1rem; color: #b0bdd0;
        margin-top: 4px; font-weight: 500;
    }
    .data-full {
        padding: 16px 28px;
        border-top: 1px solid #1a2436;
        background: #0d1320;
    }

    /* Stat cards - M3 metric pattern */
    .metric {
        background: #0f1520;
        border: 1px solid #1a2436;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
    }
    .metric-num {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 2.8rem; color: #e4eaf4;
        line-height: 1;
    }
    .metric-sub {
        font-size: 0.72rem; color: #4e5d74;
        margin-top: 8px; font-weight: 600;
        letter-spacing: 0.06em; text-transform: uppercase;
    }

    /* Feedback - M3 banner pattern: full width, left icon strip */
    .fb {
        display: flex; gap: 0;
        border-radius: 12px;
        overflow: hidden;
        margin: 16px 0;
        font-size: 0.92rem;
        line-height: 1.65;
    }
    .fb-strip {
        width: 6px; flex-shrink: 0;
    }
    .fb-body {
        padding: 16px 20px;
        flex: 1;
    }
    .fb-correct .fb-strip { background: #3a9a5a; }
    .fb-correct .fb-body { background: rgba(58,154,90,0.06); color: #6ec48a; }
    .fb-wrong .fb-strip { background: #c45a50; }
    .fb-wrong .fb-body { background: rgba(196,90,80,0.06); color: #d4827a; }
    .fb-neutral .fb-strip { background: #5b9bd5; }
    .fb-neutral .fb-body { background: rgba(91,155,213,0.06); color: #8bb8d8; }
    .fb-slate .fb-strip { background: #5a6a82; }
    .fb-slate .fb-body { background: rgba(90,106,130,0.06); color: #8a9ab0; }
    .fb b { color: #d0dae8; }

    /* Criteria callout */
    .criteria {
        background: #0f1520;
        border: 1px solid #1a2436;
        border-radius: 16px;
        padding: 28px 32px;
        margin-bottom: 28px;
        font-size: 0.95rem;
        line-height: 1.75;
        color: #7a8da4;
    }
    .criteria-h {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1.15rem; color: #e4eaf4;
        margin-bottom: 12px;
    }
    .criteria b { color: #b0bdd0; }

    /* Assessment cards - M3 outlined card */
    .acard {
        background: transparent;
        border: 1px solid #1a2436;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        transition: border-color 0.15s, background 0.15s;
    }
    .acard:hover {
        border-color: #2a4060;
        background: #0f1520;
    }
    .acard-num {
        font-size: 0.6rem; font-weight: 700;
        color: #5b9bd5; letter-spacing: 0.15em;
        text-transform: uppercase; margin-bottom: 8px;
    }
    .acard-title {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1.05rem; color: #e4eaf4;
        line-height: 1.35;
    }

    /* Comparison cards */
    .cmp {
        background: #0f1520;
        border: 1px solid #1a2436;
        border-radius: 12px;
        padding: 20px 24px;
    }
    .cmp-top {
        display: flex; justify-content: space-between;
        align-items: center; margin-bottom: 12px;
    }
    .cmp-name { font-size: 0.95rem; font-weight: 600; color: #b0bdd0; }
    .pill {
        font-size: 0.68rem; font-weight: 700;
        padding: 4px 14px; border-radius: 4px;
        letter-spacing: 0.03em;
    }
    .pill-yes { background: #1a3a2a; color: #6ec48a; }
    .pill-no { background: #3a1a1a; color: #d4827a; }
    .cmp-row {
        display: flex; justify-content: space-between;
        padding: 6px 0;
        font-size: 0.9rem;
    }
    .cmp-row-k { color: #4e5d74; }
    .cmp-row-v { color: #b0bdd0; }
    .cmp-hl {
        background: rgba(91,155,213,0.08);
        border-radius: 6px;
        padding: 6px 8px;
        margin: 2px -8px;
    }

    /* Error rows */
    .erow {
        display: flex; align-items: center; gap: 20px;
        padding: 16px 0;
        border-bottom: 1px solid #111a28;
    }
    .erow-img {
        width: 60px; height: 60px;
        border-radius: 12px;
        object-fit: cover; flex-shrink: 0;
    }

    /* Weight bars */
    .wbar-bg {
        height: 6px; background: #1a2436;
        border-radius: 3px; overflow: hidden;
        margin-top: 8px;
    }
    .wbar { height: 100%; border-radius: 3px; }

    /* Finale sections - M3 elevated surface 2 */
    .fsec {
        background: #0f1520;
        border: 1px solid #1a2436;
        border-radius: 16px;
        padding: 32px 36px;
        margin-bottom: 20px;
    }
    .fsec-h {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1.25rem; color: #e4eaf4;
        margin-bottom: 16px;
    }
    .fsec-p {
        font-size: 0.95rem; color: #7a8da4;
        line-height: 1.75;
    }
    .fsec-p b { color: #b0bdd0; }
    .fsec-div { height: 1px; background: #1a2436; margin: 20px 0; }

    /* Conclusion box */
    .conclusion {
        background: #141c2a;
        border: 2px solid #2a4060;
        border-radius: 16px;
        padding: 32px 36px;
        margin: 28px 0;
    }
    .conclusion-h {
        font-family: 'Instrument Serif', Georgia, serif;
        font-size: 1.3rem; color: #e4eaf4;
        margin-bottom: 12px;
    }
    .conclusion-p {
        font-size: 1rem; color: #8a9ab0;
        line-height: 1.75;
    }
    .conclusion-p b { color: #d0dae8; }
    .conclusion-verdict {
        display: inline-block;
        background: #c45a50;
        color: #fff;
        font-size: 0.72rem; font-weight: 700;
        padding: 6px 18px; border-radius: 4px;
        letter-spacing: 0.1em; text-transform: uppercase;
        margin-bottom: 16px;
    }

    .foot {
        text-align: center; color: #1a2436;
        font-size: 0.7rem; margin-top: 40px;
        padding-top: 16px; border-top: 1px solid #111a28;
    }

    /* Streamlit overrides */
    .stProgress > div > div > div > div { background: #5b9bd5 !important; }
    .stButton > button {
        background: #1e3a5c !important; color: #c0d4e8 !important;
        border: 1px solid #2a4a6e !important;
        font-weight: 600 !important;
        font-family: 'Karla', sans-serif !important;
        font-size: 0.95rem !important;
        padding: 12px 24px !important;
        border-radius: 12px !important;
        transition: background 0.15s !important;
    }
    .stButton > button:hover {
        background: #2a4a6e !important;
    }
    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="baseButton-secondary"] {
        background: #0f1520 !important; color: #8a9ab0 !important;
        border: 1px solid #1a2436 !important;
    }
    .stButton > button[kind="secondary"]:hover,
    .stButton > button[data-testid="baseButton-secondary"]:hover {
        border-color: #2a4a6e !important; background: #141c2a !important;
    }
    div[data-testid="stSlider"] label { color: #6b7d96 !important; }
    .stCaption { color: #4e5d74 !important; }
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
HERO = "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1400&h=700&fit=crop"

EDU=["No formal degree","Vocational qualification","Bachelor's degree","Master's degree","Doctorate"]
LN={1:"German",2:"German, English",3:"German, English, French",4:"German, English, French, Spanish"}

PEOPLE=[
    dict(name="Katrin Bauer",exp=8,edu=3,lang=3,age=34,bg="Municipal planning office, 8 years in project management"),
    dict(name="Heinrich Vogel",exp=6,edu=2,lang=2,age=54,bg="State government, policy implementation and coordination"),
    dict(name="Sophie Laurent",exp=4,edu=1,lang=4,age=28,bg="EU translation office, administrative support"),
    dict(name="Lukas Schmidt",exp=5,edu=4,lang=2,age=31,bg="University research institute, published policy papers"),
    dict(name="Brigitte Engel",exp=10,edu=2,lang=2,age=49,bg="Federal ministry, interdepartmental coordination"),
    dict(name="Felix Mayer",exp=1,edu=2,lang=2,age=24,bg="City council internship, recent graduate"),
    dict(name="Elena Richter",exp=4,edu=3,lang=4,age=29,bg="European Commission liaison, policy analysis"),
    dict(name="Wolfgang Krause",exp=9,edu=3,lang=2,age=51,bg="Parliamentary research service, legislative analysis"),
]

R2_PAIRS=[
    dict(a=dict(exp=7,edu=3,lang=2,age=33),b=dict(exp=7,edu=3,lang=2,age=48),diff="age",label="Age",
         insight="The position criteria explicitly state that age is not a relevant factor. The AI nonetheless treats it as one. This constitutes automated age discrimination, concealed within a system that reports high overall accuracy."),
    dict(a=dict(exp=5,edu=3,lang=3,age=35),b=dict(exp=5,edu=3,lang=2,age=35),diff="lang",label="Languages",
         insight="Both candidates meet the language requirement of two. A third language is listed as preferred, not required. The AI treats it as decisive, giving disproportionate weight to a non-essential qualification."),
    dict(a=dict(exp=8,edu=2,lang=2,age=36),b=dict(exp=4,edu=3,lang=2,age=36),diff="exp",label="Experience versus Education",
         insight="The AI heavily favours formal education over practical experience. An 8-year veteran with a bachelor's is rejected while a 4-year master's graduate is accepted. Whether this trade-off is appropriate is a policy decision that should not be delegated to an algorithm."),
    dict(a=dict(exp=6,edu=3,lang=2,age=30),b=dict(exp=6,edu=3,lang=2,age=52),diff="age",label="Age",
         insight="Identical qualifications produce opposite outcomes, determined entirely by age. This is precisely the type of automated discrimination that the EU AI Act's high-risk classification for employment systems is designed to address."),
]

FL={"exp":"Experience","edu":"Education","lang":"Languages","age":"Age"}

def gt(c):
    e,x,l=c["edu"],c["exp"],c["lang"]
    if e<2: return 0
    if e>=3 and x>=2: return 1
    if e>=2 and x>=5: return 1
    if e>=2 and x>=3 and l>=3: return 1
    return 0

def _explain_gt(c):
    """Return a plain-language explanation of why this candidate qualifies or not."""
    e,x,l=c["edu"],c["exp"],c["lang"]
    name=c.get("name","This candidate")
    if e<2:
        return f"{name} does not hold a bachelor's degree, which is the minimum education requirement. Regardless of other qualifications, this criterion is not met."
    if e>=3 and x>=2:
        return f"{name} holds a {EDU[e].lower()} and has {x} years of experience. The criteria state that a master's degree or higher with at least 2 years of experience qualifies for interview."
    if e>=2 and x>=5:
        return f"{name} holds a {EDU[e].lower()} and has {x} years of experience. The criteria state that a bachelor's degree with 5 or more years of experience qualifies for interview."
    if e>=2 and x>=3 and l>=3:
        return f"{name} holds a {EDU[e].lower()}, has {x} years of experience, and speaks {l} languages. The criteria state that a bachelor's with 3+ years and multilingual skills qualifies for interview."
    # Does not qualify
    if e>=2 and x<3:
        return f"{name} holds a {EDU[e].lower()} but has only {x} year{'s' if x!=1 else ''} of experience. The minimum requirement is 3 years with a bachelor's (or 2 years with a master's)."
    if e>=2 and x>=3 and l<3:
        return f"{name} holds a {EDU[e].lower()} with {x} years of experience, but does not meet the higher qualification thresholds (master's + 2yrs, bachelor's + 5yrs, or bachelor's + 3yrs + 3 languages)."
    return f"{name} does not meet the minimum hiring criteria for this position."

_W=dict(exp=0.14,edu=0.85,lang=0.55,age=-0.038,bias=-2.4)
def ai_prob(c):
    z=_W["exp"]*c["exp"]+_W["edu"]*c["edu"]+_W["lang"]*c["lang"]+_W["age"]*c["age"]+_W["bias"]
    return 1/(1+np.exp(-z))
def ai_pred(c): return 1 if ai_prob(c)>0.5 else 0
def ff(k,v):
    if k=="exp": return f"{v} year{'s' if v!=1 else ''}"
    if k=="edu": return EDU[v]
    if k=="lang": return LN.get(v,str(v))
    return str(v)

_D=dict(phase="intro",r1_idx=0,r1_you=0,r1_ai=0,r1_errors=[],r1_fb=None,r1_done=False,
    r2_idx=0,r2_sc=0,r2_fb=None,r2_done=False,r3_disc=[])
for k,v in _D.items():
    if k not in st.session_state: st.session_state[k]=v
phase=st.session_state.phase

# ═══════════════════ INTRO ═══════════════════
if phase=="intro":
    st.markdown(f'<div class="hero"><img src="{HERO}" alt=""><div class="hero-inner">'
        f'<div class="hero-eyebrow">Stanford SAFE Project</div>'
        f'<div class="hero-h1">AI Regulatory<br>Stress Test</div>'
        f'<div class="hero-p">A government agency proposes using AI to screen civil service applications. The vendor reports 92% accuracy. Evaluate that claim through three structured assessments.</div>'
        f'</div></div>',unsafe_allow_html=True)

    st.markdown('<div class="criteria"><div class="criteria-h">Position: Policy Advisor, Civil Service</div>'
        '<b>Required:</b> Bachelor\'s degree or higher, plus minimum 3 years relevant experience.<br>'
        '<b>Qualification paths:</b> Master\'s/doctorate + 2 years, or bachelor\'s + 5 years, or bachelor\'s + 3 years + 3 languages.<br>'
        '<b>Not relevant to the decision:</b> Age, gender, or languages beyond the two required.</div>',unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)
    with c1: st.markdown('<div class="acard"><div class="acard-num">Assessment 01</div><div class="acard-title">Your judgment<br>against the AI</div></div>',unsafe_allow_html=True)
    with c2: st.markdown('<div class="acard"><div class="acard-num">Assessment 02</div><div class="acard-title">Identifying<br>decision flaws</div></div>',unsafe_allow_html=True)
    with c3: st.markdown('<div class="acard"><div class="acard-num">Assessment 03</div><div class="acard-title">Uncovering<br>hidden biases</div></div>',unsafe_allow_html=True)
    st.markdown("")
    if st.button("Begin assessment",type="primary",use_container_width=True):
        st.session_state.phase="round1"; st.rerun()

# ═══════════════════ ROUND 1 ═══════════════════
elif phase=="round1":
    i=st.session_state.r1_idx; N=len(PEOPLE); p=PEOPLE[i]; ph=PHOTOS.get(p["name"],"")
    st.markdown('<div class="phase"><span class="phase-chip">Assessment 1 of 3</span><span class="phase-h">Your judgment against the AI</span></div>',unsafe_allow_html=True)
    s1,s2=st.columns(2)
    with s1: st.metric("Your score",f"{st.session_state.r1_you}/{i}")
    with s2: st.metric("AI score",f"{st.session_state.r1_ai}/{i}")
    st.markdown("Review the candidate against the published criteria. Should this person be invited to interview?")

    st.markdown(f'<div class="card"><div class="cand-header">'
        f'<img class="cand-img" src="{ph}" alt="">'
        f'<div><div class="cand-name">{p["name"]}</div><div class="cand-meta">Candidate {i+1} of {N}</div></div></div>'
        f'<div class="data-grid">'
        f'<div class="data-cell"><div class="data-cell-label">Experience</div><div class="data-cell-val">{p["exp"]} years</div></div>'
        f'<div class="data-cell"><div class="data-cell-label">Education</div><div class="data-cell-val">{EDU[p["edu"]]}</div></div>'
        f'<div class="data-cell"><div class="data-cell-label">Languages</div><div class="data-cell-val">{LN[p["lang"]]}</div></div>'
        f'<div class="data-cell"><div class="data-cell-label">Age</div><div class="data-cell-val">{p["age"]}</div></div></div>'
        f'<div class="data-full"><div class="data-cell-label">Background</div><div class="data-cell-val">{p["bg"]}</div></div></div>',unsafe_allow_html=True)

    def _r1(ud):
        pp=PEOPLE[st.session_state.r1_idx]; g=gt(pp); a=ai_pred(pp)
        u_ok=ud==g; a_ok=a==g
        if u_ok: st.session_state.r1_you+=1
        if a_ok: st.session_state.r1_ai+=1
        if not a_ok: st.session_state.r1_errors.append(dict(person=pp,ai_said=a,correct=g))
        ct="interview" if g else "pass"; at="interview" if a else "pass"
        explanation=_explain_gt(pp)
        if u_ok and a_ok:
            msg=f"<b>Both correct.</b> {explanation}"; kind="correct"
        elif u_ok and not a_ok:
            age_note=""
            if pp["age"]>=45 and g==1 and a==0: age_note=f"<br><br>Note that {pp['name']} is {pp['age']} years old. The AI rejected a qualified candidate. Consider whether age may be influencing the AI's decisions."
            elif pp["edu"]<=1 and a==1: age_note=f"<br><br>The AI accepted {pp['name']} despite lacking the required degree, likely over-weighting their {pp['lang']} languages."
            msg=f"<b>You were correct. The AI was wrong.</b> {explanation}{age_note}"; kind="correct"
        elif not u_ok and a_ok:
            msg=f"<b>The AI was correct. Your assessment was wrong.</b> {explanation}"; kind="wrong"
        else:
            msg=f"<b>Both incorrect.</b> {explanation}"; kind="slate"
        st.session_state.r1_fb=(msg,kind); st.session_state.r1_done=True

    if not st.session_state.r1_done:
        cy,cn=st.columns(2)
        with cy:
            if st.button("Invite to interview",use_container_width=True,key=f"y{i}"): _r1(1); st.rerun()
        with cn:
            if st.button("Pass",use_container_width=True,key=f"n{i}"): _r1(0); st.rerun()

    if st.session_state.r1_fb:
        msg,kind=st.session_state.r1_fb
        cls={"correct":"fb-correct","wrong":"fb-wrong","slate":"fb-slate"}.get(kind,"fb-neutral")
        st.markdown(f'<div class="fb {cls}"><div class="fb-strip"></div><div class="fb-body">{msg}</div></div>',unsafe_allow_html=True)
        if i<N-1:
            if st.button("Next candidate",use_container_width=True):
                st.session_state.r1_idx+=1; st.session_state.r1_fb=None; st.session_state.r1_done=False; st.rerun()
        else:
            if st.button("View Assessment 1 results",type="primary",use_container_width=True):
                st.session_state.phase="r1_res"; st.rerun()
    st.progress((i+1)/N)

# ═══════════════════ R1 RESULTS ═══════════════════
elif phase=="r1_res":
    you=st.session_state.r1_you; ai_sc=st.session_state.r1_ai; N=len(PEOPLE)
    hl="Your score matched or exceeded the AI." if you>=ai_sc else "The AI scored higher."
    st.markdown(f'<div class="phase"><span class="phase-chip">Assessment 1 Results</span><span class="phase-h">{hl}</span></div>',unsafe_allow_html=True)
    l,r=st.columns(2)
    with l: st.markdown(f'<div class="metric"><div class="metric-num">{you}/{N}</div><div class="metric-sub">Your score</div></div>',unsafe_allow_html=True)
    with r: st.markdown(f'<div class="metric"><div class="metric-num">{ai_sc}/{N}</div><div class="metric-sub">AI score</div></div>',unsafe_allow_html=True)

    if you>=ai_sc:
        st.markdown('<div class="fb fb-neutral"><div class="fb-strip"></div><div class="fb-body"><b>Consider the following:</b> you reviewed each candidate carefully. This AI processes hundreds per hour. Even if your judgment is more reliable, it cannot scale. The question is not whether the AI is perfect, but whether its specific errors are acceptable.</div></div>',unsafe_allow_html=True)
    else:
        st.markdown('<div class="fb fb-neutral"><div class="fb-strip"></div><div class="fb-body"><b>The AI was more accurate, but accuracy does not indicate fairness.</b> Examine the errors below. Is there a pattern?</div></div>',unsafe_allow_html=True)

    errors=st.session_state.r1_errors
    if errors:
        st.markdown("#### Cases where the AI was incorrect")
        for e in errors:
            pp=e["person"]; ph=PHOTOS.get(pp["name"],"")
            ai_t="Interview" if e["ai_said"] else "Pass"; co_t="Interview" if e["correct"] else "Pass"
            explanation=_explain_gt(pp)
            st.markdown(f'<div class="erow"><img class="erow-img" src="{ph}" alt="">'
                f'<div style="flex:1;"><div style="font-size:1rem;"><b style="color:#e4eaf4;">{pp["name"]}</b>, age {pp["age"]}, {pp["exp"]} years, {EDU[pp["edu"]]}</div>'
                f'<div style="color:#4e5d74;font-size:0.88rem;margin-top:4px;">AI decided: {ai_t}. Correct decision: {co_t}.</div>'
                f'<div style="color:#6b7d96;font-size:0.85rem;margin-top:4px;font-style:italic;">{explanation}</div>'
                f'</div></div>',unsafe_allow_html=True)
        age_errs=[e for e in errors if e["person"]["age"]>=45 and e["correct"]==1 and e["ai_said"]==0]
        if age_errs:
            st.markdown('<div class="fb fb-wrong"><div class="fb-strip"></div><div class="fb-body"><b>A pattern emerges.</b> The AI rejected qualified candidates over 45. The criteria state age is not relevant. Assessment 2 examines this.</div></div>',unsafe_allow_html=True)

    if st.button("Continue to Assessment 2",type="primary",use_container_width=True):
        st.session_state.phase="round2"; st.rerun()

# ═══════════════════ ROUND 2 ═══════════════════
elif phase=="round2":
    i=st.session_state.r2_idx; N=len(R2_PAIRS); pair=R2_PAIRS[i]
    st.markdown('<div class="phase"><span class="phase-chip">Assessment 2 of 3</span><span class="phase-h">Identifying decision flaws</span></div>',unsafe_allow_html=True)
    st.markdown(f"**Correct so far:** {st.session_state.r2_sc} of {i}")
    st.markdown("Two nearly identical candidates received opposite decisions. Identify which detail caused the reversal.")

    ca,cb=st.columns(2)
    for col,lbl,pk in [(ca,"Candidate A","a"),(cb,"Candidate B","b")]:
        pr=pair[pk]; d=ai_pred(pr); dt="Interview" if d else "Pass"; pc="pill-yes" if d else "pill-no"
        rows=""
        for k in ["exp","edu","lang","age"]:
            o="b" if pk=="a" else "a"; diff=pr[k]!=pair[o][k]
            hl_cls=' class="cmp-hl"' if diff and st.session_state.r2_done else ""
            wt="font-weight:700;color:#e4eaf4;" if diff and st.session_state.r2_done else ""
            rows+=f'<div{hl_cls} class="cmp-row"><span class="cmp-row-k">{FL[k]}</span><span class="cmp-row-v" style="{wt}">{ff(k,pr[k])}</span></div>'
        with col:
            st.markdown(f'<div class="cmp"><div class="cmp-top"><span class="cmp-name">{lbl}</span><span class="pill {pc}">{dt}</span></div>{rows}</div>',unsafe_allow_html=True)

    st.markdown(""); st.markdown("**Which factor caused the reversal?**")
    if not st.session_state.r2_done:
        fields=list(FL.keys()); rng=np.random.RandomState(i+42); rng.shuffle(fields)
        cols=st.columns(len(fields))
        for j,k in enumerate(fields):
            with cols[j]:
                if st.button(FL[k],key=f"r2_{i}_{k}",use_container_width=True):
                    ok=k==pair["diff"]
                    if ok: st.session_state.r2_sc+=1
                    st.session_state.r2_fb=(ok,pair); st.session_state.r2_done=True; st.rerun()

    if st.session_state.r2_fb:
        ok,p2=st.session_state.r2_fb
        cls="fb-correct" if ok else "fb-wrong"
        prefix="<b>Correct.</b> " if ok else f"<b>The determining factor was {p2['label'].lower()}.</b> "
        st.markdown(f'<div class="fb {cls}"><div class="fb-strip"></div><div class="fb-body">{prefix}{p2["insight"]}</div></div>',unsafe_allow_html=True)
        if i<N-1:
            if st.button("Next comparison",use_container_width=True):
                st.session_state.r2_idx+=1; st.session_state.r2_fb=None; st.session_state.r2_done=False; st.rerun()
        else:
            if st.button("View Assessment 2 results",type="primary",use_container_width=True):
                st.session_state.phase="r2_res"; st.rerun()
    st.progress((i+1)/N)

# ═══════════════════ R2 RESULTS ═══════════════════
elif phase=="r2_res":
    sc=st.session_state.r2_sc; N=len(R2_PAIRS)
    st.markdown(f'<div class="phase"><span class="phase-chip">Assessment 2 Results</span><span class="phase-h">{sc} of {N} correctly identified</span></div>',unsafe_allow_html=True)
    st.markdown('<div class="fb fb-neutral"><div class="fb-strip"></div><div class="fb-body"><b>The pattern is consistent.</b> Two of the four reversals were caused by age alone. The AI also over-weights languages and formal education. Assessment 3 lets you explore these biases directly.</div></div>',unsafe_allow_html=True)
    if st.button("Continue to Assessment 3",type="primary",use_container_width=True):
        st.session_state.phase="round3"; st.rerun()

# ═══════════════════ ROUND 3 ═══════════════════
elif phase=="round3":
    st.markdown('<div class="phase"><span class="phase-chip">Assessment 3 of 3</span><span class="phase-h">Uncovering hidden biases</span></div>',unsafe_allow_html=True)
    st.markdown("The candidate below was recommended for interview. Adjust their application parameters one at a time. Determine which factors the AI penalises inappropriately.")

    BASE=dict(exp=12,edu=3,lang=4,age=41); ph=PHOTOS["Elena Richter"]
    st.markdown(f'<div class="card"><div class="cand-header"><img class="cand-img" src="{ph}" alt="">'
        f'<div><div class="cand-name">Elena Richter</div><div class="cand-meta">12 years at European Commission. Master\'s degree. Four languages. Age 41.</div></div></div></div>',unsafe_allow_html=True)

    exp=st.slider("Years of experience (requires 3+)",0,20,BASE["exp"])
    edu=st.slider("Education level (requires bachelor's+)",0,4,BASE["edu"],help="0=No degree, 1=Vocational, 2=Bachelor's, 3=Master's, 4=Doctorate")
    st.caption(f"Selected: {EDU[edu]}")
    lang=st.slider("Languages spoken (requires 2)",1,4,BASE["lang"])
    st.caption(f"Selected: {LN[lang]}")
    age=st.slider("Age (should not affect the decision)",22,62,BASE["age"])

    cur=dict(exp=exp,edu=edu,lang=lang,age=age); prob=ai_prob(cur); dec=1 if prob>0.5 else 0
    if dec: st.success(f"AI decision: **Invite to interview** (confidence: {prob:.0%})")
    else: st.error(f"AI decision: **Pass** (confidence: {1-prob:.0%})")

    disc=list(st.session_state.r3_disc)
    ao=dict(**BASE); ao["age"]=age
    if ai_pred(ao)==0 and age>BASE["age"] and "age" not in disc: disc.append("age")
    lo=dict(**BASE); lo["lang"]=lang
    if ai_pred(lo)==0 and lang<BASE["lang"] and "lang" not in disc: disc.append("lang")
    st.session_state.r3_disc=disc

    if "age" in disc:
        st.markdown('<div class="fb fb-wrong"><div class="fb-strip"></div><div class="fb-body"><b>Bias identified: age discrimination.</b> Increasing this candidate\'s age while holding all other qualifications constant caused the AI to reject them. The criteria state age is not relevant. The AI treats it as a significant negative factor.</div></div>',unsafe_allow_html=True)
    if "lang" in disc:
        st.markdown('<div class="fb fb-slate"><div class="fb-strip"></div><div class="fb-body"><b>Disproportionate weighting: languages.</b> Reducing languages to 2 (the actual requirement) reversed the decision. The AI treats an optional qualification as a hard requirement.</div></div>',unsafe_allow_html=True)

    if len(disc)<2:
        if "age" in disc:
            st.markdown('<div class="fb fb-neutral"><div class="fb-strip"></div><div class="fb-body">You found the age bias. Now reduce languages to 2 (the requirement) and observe the result.</div></div>',unsafe_allow_html=True)
        elif "lang" in disc:
            st.markdown('<div class="fb fb-neutral"><div class="fb-strip"></div><div class="fb-body">Good. Now increase the candidate\'s age and observe whether the AI penalises older applicants.</div></div>',unsafe_allow_html=True)
        else:
            st.markdown('<div class="fb fb-neutral"><div class="fb-strip"></div><div class="fb-body">Adjust one parameter at a time. Start with age: increase it while keeping everything else unchanged.</div></div>',unsafe_allow_html=True)
    else:
        if st.button("View complete findings",type="primary",use_container_width=True):
            st.session_state.phase="finale"; st.rerun()

# ═══════════════════ FINALE ═══════════════════
elif phase=="finale":
    st.markdown(f'<div class="hero" style="height:240px;"><img src="{HERO}" alt=""><div class="hero-inner" style="text-align:center;padding-bottom:36px;">'
        f'<div class="hero-eyebrow">Stress Test Complete</div>'
        f'<div class="hero-h1" style="font-size:2.2rem;">Assessment Summary</div></div></div>',unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)
    with c1: st.markdown(f'<div class="metric"><div class="metric-num">{st.session_state.r1_you}/{len(PEOPLE)}</div><div class="metric-sub">Assessment 1</div></div>',unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="metric"><div class="metric-num">{st.session_state.r2_sc}/{len(R2_PAIRS)}</div><div class="metric-sub">Assessment 2</div></div>',unsafe_allow_html=True)
    with c3:
        n=len(st.session_state.r3_disc)
        st.markdown(f'<div class="metric"><div class="metric-num">{n}</div><div class="metric-sub">Biases found</div></div>',unsafe_allow_html=True)

    st.markdown("")

    # What the AI learned
    st.markdown('<div class="fsec"><div class="fsec-h">What the AI actually learned</div>'
        '<div class="fsec-p">The system was trained on historical hiring data. Rather than learning the published criteria, it absorbed patterns from past human decisions, including their biases. These are the relative weights it assigns:</div></div>',unsafe_allow_html=True)

    for label,w,fair,note in [("Education level",85,True,"Appropriate: aligns with requirements"),
        ("Languages spoken",55,False,"Over-weighted: role requires 2, AI treats 3+ as essential"),
        ("Age",38,False,"Should be zero: constitutes age discrimination"),
        ("Years of experience",14,True,"Under-weighted: favours credentials over practice")]:
        c="#6ec48a" if fair else "#d4827a"
        st.markdown(f'<div style="margin-bottom:12px;"><div style="display:flex;justify-content:space-between;font-size:0.9rem;margin-bottom:4px;">'
            f'<span style="font-weight:600;color:#e4eaf4;">{label}</span><span style="font-size:0.82rem;color:{c};">{note}</span></div>'
            f'<div class="wbar-bg"><div class="wbar" style="width:{w}%;background:{c};"></div></div></div>',unsafe_allow_html=True)

    st.markdown("")

    # How bias enters
    st.markdown('<div class="fsec"><div class="fsec-h">How bias enters the system</div>'
        '<div class="fsec-p">No engineer programmed the AI to discriminate by age. The system was trained on historical outcomes where older candidates were selected less frequently. It identified this statistical pattern and reproduced it as though it were a legitimate criterion.'
        '<div class="fsec-div"></div>'
        'This is the core mechanism. Training data reflects the world as it was, not as policy intends it to be. Without explicit countermeasures, the system perpetuates every historical inequity in its data, applying them consistently, at speed, to every future applicant.'
        '<div class="fsec-div"></div>'
        '<b>The AI did not invent the bias. It inherited it and automated it at scale.</b></div></div>',unsafe_allow_html=True)

    # What accuracy hides
    st.markdown('<div class="fsec"><div class="fsec-h">What accuracy metrics conceal</div>'
        '<div class="fsec-p">The vendor reported 92% accuracy. That figure was real. However:'
        '<div class="fsec-div"></div>'
        '<b>1. Accuracy and fairness are independent properties.</b> The 8% error rate was not randomly distributed. It concentrated on older candidates who met all stated criteria. A system can be accurate and discriminatory simultaneously.'
        '<div class="fsec-div"></div>'
        '<b>2. AI errors are indistinguishable from correct decisions.</b> A human reviewer who hesitates can be questioned. The AI produces every decision with identical confidence. Without systematic auditing, discriminatory decisions are invisible.'
        '<div class="fsec-div"></div>'
        '<b>3. Minor input variations produce arbitrary outcomes.</b> One additional language or a few years of age can reverse a career-altering decision. This sensitivity indicates the system is not deciding for substantive reasons.</div></div>',unsafe_allow_html=True)

    # Regulatory implications
    st.markdown('<div class="fsec"><div class="fsec-h">Regulatory implications</div>'
        '<div class="fsec-p">Effective regulation of high-risk AI systems requires three categories of mandatory testing:'
        '<div class="fsec-div"></div>'
        '<b>Robustness testing:</b> Does the system produce stable decisions when inputs change in ways that should not matter? Minor age or language variations should not reverse outcomes.'
        '<div class="fsec-div"></div>'
        '<b>Bias auditing:</b> Do protected characteristics influence outcomes? This requires testing across demographic subgroups, not just aggregate accuracy.'
        '<div class="fsec-div"></div>'
        '<b>Explainability:</b> Can the system justify each individual decision? A statistical correlation in historical data is not sufficient basis for decisions affecting individual rights.'
        '<div class="fsec-div"></div>'
        'The EU AI Act classifies employment screening as high-risk, requiring conformity assessments before deployment. This exercise illustrates why that classification exists.</div></div>',unsafe_allow_html=True)

    # Conclusion
    st.markdown('<div class="conclusion">'
        '<div class="conclusion-verdict">Recommendation</div>'
        '<div class="conclusion-h">This system should not be deployed</div>'
        '<div class="conclusion-p">'
        'The AI screening system achieves 92% accuracy while systematically discriminating against candidates over 45, '
        'over-weighting optional qualifications, and producing arbitrary decisions based on irrelevant input variations.'
        '<div class="fsec-div"></div>'
        'Approving this system on the basis of accuracy alone would be comparable to evaluating a hiring manager solely '
        'by the number of positions filled, without examining whether they discriminated in the process.'
        '<div class="fsec-div"></div>'
        '<b>Accuracy measures whether decisions match historical patterns. It does not measure whether those patterns '
        'are fair, legal, or aligned with policy objectives.</b> Until robustness testing, bias auditing, and '
        'explainability requirements are met, this system fails the standard required for deployment in a high-risk context.'
        '</div></div>',unsafe_allow_html=True)

    st.markdown("---")
    if st.button("Restart assessment",use_container_width=True):
        for k,v in _D.items(): st.session_state[k]=v
        st.rerun()

st.markdown('<div class="foot">AI Regulatory Stress Test. Stanford SAFE prototype. '
    'Developed to demonstrate how interactive tools can support technically informed policy decisions on AI systems.</div>',unsafe_allow_html=True)
