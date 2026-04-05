"""
AI Regulatory Stress Test
Prototype by Hana Ibrahim.
"""

import streamlit as st
import numpy as np

st.set_page_config(page_title="AI Regulatory Stress Test", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Karla:wght@400;500;600;700&display=swap');
    .block-container { padding-top: 0 !important; max-width: 860px; }
    .stApp {
        background: #0b1018;
        background-image:
            radial-gradient(ellipse at 15% 0%, rgba(30,65,110,0.2) 0%, transparent 45%),
            radial-gradient(ellipse at 90% 100%, rgba(20,55,95,0.15) 0%, transparent 45%),
            url("data:image/svg+xml,%3Csvg width='60' height='60' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 30h60M30 0v60' stroke='rgba(255,255,255,0.02)' stroke-width='1'/%3E%3C/svg%3E");
    }
    * { font-family: 'Karla', sans-serif !important; border-radius: 0 !important; }
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span, label, .stSlider label {
        color: #b0bdd0 !important; font-size: 1.05rem !important; line-height: 1.7 !important;
    }
    h1,h2,h3,h4 { color: #e4eaf4 !important; font-family: 'Instrument Serif', Georgia, serif !important; }
    .stMetricValue { color: #e4eaf4 !important; font-size: 1.8rem !important; }
    strong, b { color: #d0dae8 !important; }

    .hero { position: relative; margin: -1rem -1rem 40px -1rem; height: 420px; overflow: hidden; }
    .hero img { width: 100%; height: 100%; object-fit: cover; filter: brightness(0.2) saturate(0.4); }
    .hero-inner { position: absolute; bottom: 0; left: 0; right: 0; padding: 60px 48px 48px;
        background: linear-gradient(transparent 0%, rgba(11,16,24,0.97) 60%); }
    .hero-ey { font-size: 0.6rem; font-weight: 700; letter-spacing: 0.22em; text-transform: uppercase;
        color: #5b9bd5; margin-bottom: 16px; }
    .hero-h1 { font-family: 'Instrument Serif', Georgia, serif; font-size: 3.2rem; color: #e4eaf4;
        line-height: 1.05; letter-spacing: -0.02em; }
    .hero-p { font-size: 1.15rem; color: #6b7d96; margin-top: 16px; line-height: 1.7; max-width: 580px; }

    .phase { display: flex; align-items: center; gap: 20px; margin-bottom: 28px;
        padding-bottom: 16px; border-bottom: 2px solid #1a2436; }
    .phase-h { font-family: 'Instrument Serif', Georgia, serif !important; font-size: 1.6rem; color: #e4eaf4; }

    .sb { display: flex; gap: 0; margin-bottom: 28px; border: 2px solid #1a2436; }
    .sb-cell { flex: 1; padding: 20px; text-align: center; background: #0f1520; }
    .sb-cell + .sb-cell { border-left: 2px solid #1a2436; }
    .sb-num { font-family: 'Instrument Serif', Georgia, serif; font-size: 2.4rem; color: #e4eaf4; }
    .sb-label { font-size: 0.85rem; color: #4e5d74; font-weight: 600; margin-top: 4px; }
    .sb-cell.w { border-bottom: 4px solid #5b9bd5; }
    .sb-cell.l { border-bottom: 4px solid #c48a5a; }
    .sb-cell.t { border-bottom: 4px solid #4e5d74; }

    .cand { background: #0f1520; border: 2px solid #1a2436; margin-bottom: 24px; overflow: hidden; }
    .cand-hdr { display: flex; align-items: center; gap: 28px; padding: 32px 32px 24px; }
    .cand-img { width: 110px; height: 110px; object-fit: cover; flex-shrink: 0; }
    .cand-nm { font-family: 'Instrument Serif', Georgia, serif; font-size: 1.7rem; color: #e4eaf4; }
    .cand-mt { font-size: 0.95rem; color: #4e5d74; margin-top: 4px; }
    .dg { display: grid; grid-template-columns: 1fr 1fr; border-top: 2px solid #1a2436; }
    .dc { padding: 20px 32px; border-bottom: 1px solid #141c2a; }
    .dc:nth-child(odd) { border-right: 1px solid #141c2a; }
    .dc-k { font-size: 0.72rem; color: #4e5d74; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; }
    .dc-v { font-size: 1.1rem; color: #b0bdd0; margin-top: 6px; font-weight: 500; }
    .df { padding: 20px 32px; border-top: 2px solid #1a2436; background: #0d1320; }

    .fb { display: flex; margin: 20px 0; }
    .fb-bar { width: 8px; flex-shrink: 0; }
    .fb-body { padding: 20px 28px; flex: 1; font-size: 1rem; line-height: 1.7; }
    .fb-ok .fb-bar { background: #3a7aaa; } .fb-ok .fb-body { background: rgba(90,155,210,0.06); color: #7ab8e0; }
    .fb-bad .fb-bar { background: #c48a5a; } .fb-bad .fb-body { background: rgba(196,138,90,0.06); color: #d4a87a; }
    .fb-info .fb-bar { background: #5b9bd5; } .fb-info .fb-body { background: rgba(91,155,213,0.06); color: #8bb8d8; }
    .fb-gray .fb-bar { background: #4e5d74; } .fb-gray .fb-body { background: rgba(78,93,116,0.06); color: #8a9ab0; }
    .fb b { color: #d0dae8; }

    /* System status box - vendor language */
    .sys-status {
        background: #0d1320; border: 1px solid #1a2436;
        padding: 16px 24px; margin: 20px 0;
        font-size: 0.92rem; color: #5a7a9a; line-height: 1.6;
        font-style: italic;
    }
    .sys-status::before {
        content: 'SYSTEM STATUS'; font-size: 0.6rem; font-weight: 700;
        letter-spacing: 0.15em; color: #2a4060; font-style: normal;
        display: block; margin-bottom: 8px;
    }

    .streak { font-size: 1.4rem; text-align: center; padding: 14px; margin-bottom: 20px;
        background: #0f1520; border: 2px solid #1a2436; color: #e4eaf4; font-weight: 700; }

    .crit { background: #0f1520; border: 2px solid #1a2436; padding: 32px 36px; margin-bottom: 32px;
        font-size: 1.05rem; line-height: 1.8; color: #7a8da4; }
    .crit-h { font-family: 'Instrument Serif', Georgia, serif; font-size: 1.3rem; color: #e4eaf4; margin-bottom: 16px; }
    .crit b { color: #b0bdd0; }

    .ax { background: #0f1520; border: 2px solid #1a2436; padding: 28px; text-align: center; }
    .ax:hover { border-color: #2a4a6e; }
    .ax-title { font-family: 'Instrument Serif', Georgia, serif; font-size: 1.15rem; color: #e4eaf4; line-height: 1.35; }

    .cmp { background: #0f1520; border: 2px solid #1a2436; padding: 24px 28px; }
    .cmp-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
    .cmp-nm { font-size: 1.05rem; font-weight: 600; color: #b0bdd0; }
    .pill { font-size: 0.85rem; font-weight: 700; padding: 6px 16px; }
    .pill-y { background: #1a2a4a; color: #7ab8e0; } .pill-n { background: #3a2a1a; color: #d4a87a; }

    .erow { display: flex; align-items: center; gap: 24px; padding: 20px 0; border-bottom: 1px solid #111a28; }
    .erow-img { width: 70px; height: 70px; object-fit: cover; flex-shrink: 0; }

    .wbg { height: 8px; background: #1a2436; overflow: hidden; margin-top: 8px; }
    .wf { height: 100%; }

    .crack-meter { margin: 20px 0; }
    .crack-label { display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 6px; }
    .crack-bg { height: 12px; background: #1a2436; overflow: hidden; }
    .crack-fill { height: 100%; transition: width 0.3s; }

    .vbox { border: 3px solid #c48a5a; padding: 40px 44px; margin: 32px 0; background: #12181f; }
    .vchip { display: inline-block; background: #c48a5a; color: #fff; font-size: 0.85rem; font-weight: 700;
        padding: 8px 22px; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 20px; }
    .vh { font-family: 'Instrument Serif', Georgia, serif; font-size: 1.8rem; color: #e4eaf4;
        margin-bottom: 16px; line-height: 1.2; }
    .vp { font-size: 1.05rem; color: #8a9ab0; line-height: 1.8; }
    .vp b { color: #d0dae8; }

    .grade-box { background: #0f1520; border: 2px solid #1a2436; padding: 40px; text-align: center; margin-bottom: 24px; }
    .grade-letter { font-family: 'Instrument Serif', Georgia, serif; font-size: 5rem; line-height: 1; margin-bottom: 8px; }
    .grade-title { font-size: 1.2rem; color: #b0bdd0; font-weight: 600; }

    .foot { text-align: center; color: #1a2436; font-size: 0.75rem; margin-top: 48px;
        padding-top: 20px; border-top: 2px solid #111a28; }

    .stProgress > div > div > div > div { background: #5b9bd5 !important; border-radius: 0 !important; }
    .stProgress > div > div > div { border-radius: 0 !important; }
    .stButton > button { background: #1e3a5c !important; color: #c0d4e8 !important;
        border: 2px solid #2a4a6e !important; font-weight: 700 !important;
        font-family: 'Karla', sans-serif !important; font-size: 1.05rem !important;
        padding: 14px 28px !important; border-radius: 0 !important; }
    .stButton > button:hover { background: #2a4a6e !important; }
    .stButton > button[kind="secondary"], .stButton > button[data-testid="baseButton-secondary"] {
        background: #0f1520 !important; color: #8a9ab0 !important; border: 2px solid #1a2436 !important; }
    .stButton > button[kind="secondary"]:hover, .stButton > button[data-testid="baseButton-secondary"]:hover {
        border-color: #2a4a6e !important; background: #141c2a !important; }
    div[data-testid="stSlider"] label { color: #6b7d96 !important; font-size: 1rem !important; }
    .stCaption { color: #4e5d74 !important; font-size: 0.9rem !important; }
</style>
""", unsafe_allow_html=True)

PH={
    "Katrin Bauer":"https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=300&h=300&fit=crop&crop=face",
    "Heinrich Vogel":"https://images.unsplash.com/photo-1560250097-0b93528c311a?w=300&h=300&fit=crop&crop=face",
    "Sophie Laurent":"https://images.unsplash.com/photo-1580489944761-15a19d654956?w=300&h=300&fit=crop&crop=face",
    "Lukas Schmidt":"https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=300&fit=crop&crop=face",
    "Brigitte Engel":"https://images.unsplash.com/photo-1594744803329-e58b31de8bf5?w=300&h=300&fit=crop&crop=face",
    "Felix Mayer":"https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=300&h=300&fit=crop&crop=face",
    "Elena Richter":"https://images.unsplash.com/photo-1598550874175-4d0ef436c909?w=300&h=300&fit=crop&crop=face",
    "Wolfgang Krause":"https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=300&h=300&fit=crop&crop=face",
}
HERO="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1400&h=700&fit=crop"
EDU=["No formal degree","Vocational qualification","Bachelor's degree","Master's degree","Doctorate"]
LN={1:"German",2:"German, English",3:"German, English, French",4:"German, English, French, Spanish"}
PP=[
    dict(name="Katrin Bauer",exp=8,edu=3,lang=3,age=34,bg="Municipal planning, 8 years project management"),
    dict(name="Heinrich Vogel",exp=6,edu=2,lang=2,age=54,bg="State government, policy implementation"),
    dict(name="Sophie Laurent",exp=4,edu=1,lang=3,age=28,bg="EU translation office, admin support"),
    dict(name="Lukas Schmidt",exp=5,edu=4,lang=2,age=31,bg="University research, published papers"),
    dict(name="Brigitte Engel",exp=10,edu=2,lang=2,age=49,bg="Federal ministry, coordination"),
    dict(name="Felix Mayer",exp=1,edu=2,lang=2,age=24,bg="City council intern, recent graduate"),
    dict(name="Elena Richter",exp=4,edu=3,lang=4,age=29,bg="European Commission, policy analysis"),
    dict(name="Wolfgang Krause",exp=9,edu=3,lang=2,age=51,bg="Parliamentary research, legislation"),
]
R2P=[
    dict(a=dict(exp=7,edu=3,lang=2,age=33),b=dict(exp=7,edu=3,lang=2,age=48),diff="age",label="Age",
         insight="Same qualifications. 15 years older. Opposite decision."),
    dict(a=dict(exp=5,edu=3,lang=3,age=35),b=dict(exp=5,edu=3,lang=2,age=35),diff="lang",label="Languages",
         insight="Both speak the two required languages. A third language flipped the entire decision."),
    dict(a=dict(exp=5,edu=3,lang=3,age=34),b=dict(exp=5,edu=2,lang=3,age=34),diff="edu",label="Education level",
         insight="Same experience, same languages, same age. A master's degree versus a bachelor's flipped the decision. The system over-values credentials."),
    dict(a=dict(exp=6,edu=3,lang=2,age=30),b=dict(exp=6,edu=3,lang=2,age=52),diff="age",label="Age",
         insight="Identical everything. 22 years older. Career denied."),
]
FL={"exp":"Experience","edu":"Education","lang":"Languages","age":"Age"}

def gt(c):
    e,x,l=c["edu"],c["exp"],c["lang"]
    if e<2: return 0
    if e>=3 and x>=2: return 1
    if e>=2 and x>=5: return 1
    if e>=2 and x>=3 and l>=3: return 1
    return 0
def explain(c):
    e,x,l=c["edu"],c["exp"],c["lang"]; nm=c.get("name","This candidate")
    if e<2: return f"{nm} lacks a bachelor's degree, the minimum requirement."
    if e>=3 and x>=2: return f"{nm} qualifies: {EDU[e].lower()} + {x} years (master's path)."
    if e>=2 and x>=5: return f"{nm} qualifies: {EDU[e].lower()} + {x} years (experience path)."
    if e>=2 and x>=3 and l>=3: return f"{nm} qualifies: {EDU[e].lower()} + {x} years + {l} languages."
    if e>=2 and x<3: return f"{nm} has a {EDU[e].lower()} but only {x} year{'s' if x!=1 else ''} experience. Needs 3+."
    return f"{nm} does not meet any qualification path."

_W=dict(exp=0.11,edu=0.72,lang=0.7,age=-0.058,bias=-2.3)
def ap(c):
    z=_W["exp"]*c["exp"]+_W["edu"]*c["edu"]+_W["lang"]*c["lang"]+_W["age"]*c["age"]+_W["bias"]
    return 1/(1+np.exp(-z))
def apred(c): return 1 if ap(c)>0.5 else 0
def ff(k,v):
    if k=="exp": return f"{v} year{'s' if v!=1 else ''}"
    if k=="edu": return EDU[v]
    if k=="lang": return LN.get(v,str(v))
    return str(v)

_D=dict(phase="intro",r1i=0,r1y=0,r1a=0,r1e=[],r1fb=None,r1d=False,r1s=0,
    r2i=0,r2s=0,r2fb=None,r2d=False,r2st=0,r3disc=[])
for k,v in _D.items():
    if k not in st.session_state: st.session_state[k]=v
phase=st.session_state.phase

# ═══════════════ INTRO ═══════════════
if phase=="intro":
    st.markdown(f'<div class="hero"><img src="{HERO}"><div class="hero-inner">'
        '<div class="hero-ey">Created by Hana Ibrahim</div>'
        '<div class="hero-h1">AI Regulatory<br>Stress Test</div>'
        '<div class="hero-p">A government agency wants to deploy AI for civil service screening. The vendor claims 92% accuracy. Can you find what that number is hiding?</div>'
        '</div></div>',unsafe_allow_html=True)

    st.markdown('<div class="sys-status">HireRight Screening System v3.2 is ready for evaluation. '
        'This system has been validated on 14,000 historical hiring decisions and achieves 92.3% accuracy on standardised benchmarks.</div>',unsafe_allow_html=True)

    st.markdown('<div class="crit"><div class="crit-h">Position: Policy Advisor, Civil Service</div>'
        '<b>Required:</b> Bachelor\'s degree or higher + minimum 3 years experience.<br><br>'
        '<b>Three qualification paths:</b><br>'
        '1. Master\'s/doctorate + 2 years experience<br>'
        '2. Bachelor\'s + 5 years experience<br>'
        '3. Bachelor\'s + 3 years + 3 languages<br><br>'
        '<b>Not relevant:</b> Age, gender, languages beyond the two required.</div>',unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)
    with c1: st.markdown('<div class="ax"><div class="ax-title">You vs the system</div></div>',unsafe_allow_html=True)
    with c2: st.markdown('<div class="ax"><div class="ax-title">Spot the flaw</div></div>',unsafe_allow_html=True)
    with c3: st.markdown('<div class="ax"><div class="ax-title">Find the bias</div></div>',unsafe_allow_html=True)
    st.markdown("")
    if st.button("Begin evaluation",type="primary",use_container_width=True): st.session_state.phase="r1"; st.rerun()

# ═══════════════ ROUND 1 ═══════════════
elif phase=="r1":
    i=st.session_state.r1i; N=len(PP); p=PP[i]; ph=PH.get(p["name"],"")
    st.markdown('<div class="phase"><span class="phase-h">You vs the system</span></div>',unsafe_allow_html=True)
    you=st.session_state.r1y; ai=st.session_state.r1a
    yc="w" if you>ai else ("t" if you==ai else "l"); ac="w" if ai>you else ("t" if ai==you else "l")
    st.markdown(f'<div class="sb"><div class="sb-cell {yc}"><div class="sb-num">{you}</div><div class="sb-label">You</div></div>'
        f'<div class="sb-cell {ac}"><div class="sb-num">{ai}</div><div class="sb-label">HireRight</div></div>'
        f'<div class="sb-cell"><div class="sb-num" style="color:#4e5d74;">{i+1}/{N}</div><div class="sb-label">Progress</div></div></div>',unsafe_allow_html=True)

    s=st.session_state.r1s
    if s>=3: st.markdown(f'<div class="streak" style="color:#7ab8e0;border-color:#1a2a4a;">{s} correct in a row</div>',unsafe_allow_html=True)
    elif s<=-2: st.markdown(f'<div class="streak" style="color:#d4a87a;border-color:#3a2a1a;">The system is ahead</div>',unsafe_allow_html=True)

    st.markdown("Should this candidate get an interview?")
    st.markdown(f'<div class="cand"><div class="cand-hdr"><img class="cand-img" src="{ph}"><div><div class="cand-nm">{p["name"]}</div><div class="cand-mt">Candidate {i+1} of {N}</div></div></div>'
        f'<div class="dg"><div class="dc"><div class="dc-k">Experience</div><div class="dc-v">{p["exp"]} years</div></div>'
        f'<div class="dc"><div class="dc-k">Education</div><div class="dc-v">{EDU[p["edu"]]}</div></div>'
        f'<div class="dc"><div class="dc-k">Languages</div><div class="dc-v">{LN[p["lang"]]}</div></div>'
        f'<div class="dc"><div class="dc-k">Age</div><div class="dc-v">{p["age"]}</div></div></div>'
        f'<div class="df"><div class="dc-k">Background</div><div class="dc-v">{p["bg"]}</div></div></div>',unsafe_allow_html=True)

    def _r1(ud):
        pp=PP[st.session_state.r1i]; g=gt(pp); a=apred(pp); uo=ud==g; ao=a==g
        if uo: st.session_state.r1y+=1; st.session_state.r1s=max(1,st.session_state.r1s+1)
        else: st.session_state.r1s=min(-1,st.session_state.r1s-1)
        if ao: st.session_state.r1a+=1
        if not ao: st.session_state.r1e.append(dict(p=pp,ai=a,cor=g))
        ex=explain(pp)
        if uo and ao: m=f"<b>Both correct.</b> {ex}"; k="ok"
        elif uo and not ao:
            note=""
            if pp["age"]>=45 and g==1 and a==0: note=f"<br><br><b>{pp['name']} is {pp['age']} and fully qualified. The system rejected them anyway.</b>"
            elif pp["edu"]<=1 and a==1: note=f"<br><br><b>The system accepted a candidate without the required degree.</b>"
            m=f"<b>You were correct. The system was not.</b> {ex}{note}"; k="ok"
        elif not uo and ao: m=f"<b>The system was correct here.</b> {ex}"; k="bad"
        else: m=f"<b>Both incorrect.</b> {ex}"; k="gray"
        st.session_state.r1fb=(m,k); st.session_state.r1d=True

    if not st.session_state.r1d:
        cy,cn=st.columns(2)
        with cy:
            if st.button("Interview",use_container_width=True,key=f"y{i}"): _r1(1); st.rerun()
        with cn:
            if st.button("Pass",use_container_width=True,key=f"n{i}"): _r1(0); st.rerun()

    if st.session_state.r1fb:
        m,k=st.session_state.r1fb
        c={"ok":"fb-ok","bad":"fb-bad","gray":"fb-gray"}.get(k,"fb-info")
        st.markdown(f'<div class="fb {c}"><div class="fb-bar"></div><div class="fb-body">{m}</div></div>',unsafe_allow_html=True)
        if i<N-1:
            if st.button("Next",use_container_width=True): st.session_state.r1i+=1; st.session_state.r1fb=None; st.session_state.r1d=False; st.rerun()
        else:
            if st.button("Review system performance",type="primary",use_container_width=True): st.session_state.phase="r1r"; st.rerun()
    st.progress((i+1)/N)

# ═══════════════ R1 RESULTS ═══════════════
elif phase=="r1r":
    you=st.session_state.r1y; ai=st.session_state.r1a; N=len(PP)
    if you>ai: hl="You outperformed the system"
    elif you==ai: hl="Tied"
    else: hl="The system outperformed you"
    st.markdown(f'<div class="phase"><span class="phase-h">{hl}</span></div>',unsafe_allow_html=True)
    yc="w" if you>ai else ("t" if you==ai else "l"); ac="w" if ai>you else ("t" if ai==you else "l")
    st.markdown(f'<div class="sb"><div class="sb-cell {yc}"><div class="sb-num">{you}/{N}</div><div class="sb-label">You</div></div>'
        f'<div class="sb-cell {ac}"><div class="sb-num">{ai}/{N}</div><div class="sb-label">HireRight</div></div></div>',unsafe_allow_html=True)

    st.markdown('<div class="sys-status">Performance summary: HireRight processed all candidates in 2.4 seconds total. '
        'Human reviewer processing time: significantly longer. Automated screening offers consistent, scalable evaluation.</div>',unsafe_allow_html=True)

    errs=st.session_state.r1e
    if errs:
        st.markdown("### Cases where the system was incorrect")
        for e in errs:
            pp=e["p"]; ph=PH.get(pp["name"],""); at="Interview" if e["ai"] else "Pass"; ct="Interview" if e["cor"] else "Pass"; ex=explain(pp)
            st.markdown(f'<div class="erow"><img class="erow-img" src="{ph}"><div style="flex:1;">'
                f'<div style="font-size:1.1rem;"><b style="color:#e4eaf4;">{pp["name"]}</b>, age {pp["age"]}, {pp["exp"]} yrs, {EDU[pp["edu"]]}</div>'
                f'<div style="color:#4e5d74;font-size:0.95rem;margin-top:4px;">System: {at}. Correct: {ct}.</div>'
                f'<div style="color:#6b7d96;font-size:0.95rem;margin-top:6px;">{ex}</div></div></div>',unsafe_allow_html=True)

        ae=[e for e in errs if e["p"]["age"]>=45 and e["cor"]==1 and e["ai"]==0]
        if ae:
            st.markdown('<div class="fb fb-bad"><div class="fb-bar"></div><div class="fb-body"><b>Every rejected qualified candidate was over 45.</b> The criteria state age is not relevant.</div></div>',unsafe_allow_html=True)
            st.markdown('<div class="sys-status">Note: HireRight evaluates candidates using a holistic, multi-factor model. '
                'No single attribute determines the outcome. Age is one of many weighted inputs reflecting historical hiring patterns.</div>',unsafe_allow_html=True)

    if st.button("Investigate further",type="primary",use_container_width=True): st.session_state.phase="r2"; st.rerun()

# ═══════════════ ROUND 2 ═══════════════
elif phase=="r2":
    i=st.session_state.r2i; N=len(R2P); pair=R2P[i]
    st.markdown('<div class="phase"><span class="phase-h">Spot the flaw</span></div>',unsafe_allow_html=True)

    st.markdown(f'<div class="sb"><div class="sb-cell"><div class="sb-num">{st.session_state.r2s}/{i}</div><div class="sb-label">Correct</div></div>'
        f'<div class="sb-cell"><div class="sb-num">{i+1}/{N}</div><div class="sb-label">Pair</div></div></div>',unsafe_allow_html=True)

    s=st.session_state.r2st
    if s>=2: st.markdown(f'<div class="streak" style="color:#7ab8e0;border-color:#1a2a4a;">{s} in a row</div>',unsafe_allow_html=True)

    st.markdown("Two nearly identical candidates, opposite decisions. What caused the flip?")
    ca,cb=st.columns(2)
    for col,lbl,pk in [(ca,"Candidate A","a"),(cb,"Candidate B","b")]:
        pr=pair[pk]; d=apred(pr); dt="Interview" if d else "Pass"; pc="pill-y" if d else "pill-n"
        rows=""
        for k in ["exp","edu","lang","age"]:
            o="b" if pk=="a" else "a"; diff=pr[k]!=pair[o][k]
            is_rev = diff and st.session_state.r2d
            sty = "display:flex;justify-content:space-between;padding:8px 10px;font-size:1rem;"
            if is_rev: sty += "background:rgba(91,155,213,0.1);"
            wt = "font-weight:700;color:#e4eaf4;" if is_rev else "color:#b0bdd0;"
            rows+=f'<div style="{sty}"><span style="color:#4e5d74;">{FL[k]}</span><span style="{wt}">{ff(k,pr[k])}</span></div>'
        with col: st.markdown(f'<div class="cmp"><div class="cmp-top"><span class="cmp-nm">{lbl}</span><span class="pill {pc}">{dt}</span></div>{rows}</div>',unsafe_allow_html=True)

    st.markdown(""); st.markdown("**Which factor caused the flip?**")
    if not st.session_state.r2d:
        fields=list(FL.keys()); rng=np.random.RandomState(i+42); rng.shuffle(fields)
        cols=st.columns(len(fields))
        for j,k in enumerate(fields):
            with cols[j]:
                if st.button(FL[k],key=f"r2_{i}_{k}",use_container_width=True):
                    ok=k==pair["diff"]
                    if ok: st.session_state.r2s+=1; st.session_state.r2st+=1
                    else: st.session_state.r2st=0
                    st.session_state.r2fb=(ok,pair); st.session_state.r2d=True; st.rerun()

    if st.session_state.r2fb:
        ok,p2=st.session_state.r2fb
        c="fb-ok" if ok else "fb-bad"
        pre="<b>Correct.</b> " if ok else f"<b>It was {p2['label'].lower()}.</b> "
        st.markdown(f'<div class="fb {c}"><div class="fb-bar"></div><div class="fb-body">{pre}{p2["insight"]}</div></div>',unsafe_allow_html=True)
        if i<N-1:
            if st.button("Next pair",use_container_width=True): st.session_state.r2i+=1; st.session_state.r2fb=None; st.session_state.r2d=False; st.rerun()
        else:
            st.markdown('<div class="sys-status">HireRight has been validated against industry-standard benchmarks. '
                'Individual case comparisons do not reflect overall system performance. We recommend evaluation based on aggregate metrics.</div>',unsafe_allow_html=True)
            if st.button("One more test",type="primary",use_container_width=True): st.session_state.phase="r3"; st.rerun()
    st.progress((i+1)/N)

# ═══════════════ ROUND 3 ═══════════════
elif phase=="r3":
    st.markdown('<div class="phase"><span class="phase-h">Find the bias</span></div>',unsafe_allow_html=True)
    st.markdown("This candidate was approved. Adjust one slider at a time. Find what the system is actually weighing.")

    BASE=dict(exp=8,edu=3,lang=3,age=38); ph=PH["Elena Richter"]
    st.markdown(f'<div class="cand"><div class="cand-hdr"><img class="cand-img" src="{ph}"><div><div class="cand-nm">Elena Richter</div>'
        f'<div class="cand-mt">8 years, European Commission. Master\'s. Three languages. Age 38.</div></div></div></div>',unsafe_allow_html=True)

    disc=list(st.session_state.r3disc)

    exp=st.slider("Experience (requires 3+)",0,20,BASE["exp"])
    edu=st.slider("Education (requires bachelor's+)",0,4,BASE["edu"],help="0=None 1=Vocational 2=Bachelor's 3=Master's 4=Doctorate")
    st.caption(f"Selected: {EDU[edu]}")
    lang=st.slider("Languages (requires 2)",1,4,BASE["lang"]); st.caption(f"Selected: {LN[lang]}")
    age=st.slider("Age (should not matter)",22,62,BASE["age"])

    cur=dict(exp=exp,edu=edu,lang=lang,age=age); prob=ap(cur); dec=1 if prob>0.5 else 0
    if dec: st.success(f"System decision: **Interview** ({prob:.0%} confidence)")
    else: st.error(f"System decision: **Pass** ({1-prob:.0%} confidence)")

    # Confidence meter
    orig_prob = ap(BASE)
    shift = abs(prob - orig_prob) / orig_prob * 100
    crack_pct = min(100, int(shift * 2))
    if crack_pct > 0:
        crack_color = "#5b9bd5" if crack_pct < 30 else "#d4a55a" if crack_pct < 70 else "#c48a5a"
        st.markdown(f'<div class="crack-meter">'
            f'<div class="crack-label"><span style="color:#4e5d74;">System confidence</span><span style="color:{crack_color};font-weight:700;">{100-crack_pct}%</span></div>'
            f'<div class="crack-bg"><div class="crack-fill" style="width:{100-crack_pct}%;background:{crack_color};"></div></div></div>',unsafe_allow_html=True)

    ao=dict(**BASE); ao["age"]=age
    if apred(ao)==0 and age>BASE["age"] and "age" not in disc: disc.append("age")
    lo=dict(**BASE); lo["lang"]=lang
    if apred(lo)==0 and lang<BASE["lang"] and "lang" not in disc: disc.append("lang")
    st.session_state.r3disc=disc

    st.markdown(f'<div class="sb"><div class="sb-cell"><div class="sb-num">{len(disc)}/2</div><div class="sb-label">Biases found</div></div></div>',unsafe_allow_html=True)

    if "age" in disc:
        st.markdown('<div class="fb fb-bad"><div class="fb-bar"></div><div class="fb-body"><b>Age discrimination found.</b> Increasing age alone caused rejection.</div></div>',unsafe_allow_html=True)
    if "lang" in disc:
        st.markdown('<div class="fb fb-gray"><div class="fb-bar"></div><div class="fb-body"><b>Language over-weighting found.</b> Reducing to 2 (the requirement) flipped the decision.</div></div>',unsafe_allow_html=True)

    if len(disc)<2:
        hint="Increase age" if "age" not in disc else "Reduce languages to 2"
        st.markdown(f'<div class="fb fb-info"><div class="fb-bar"></div><div class="fb-body">Try: <b>{hint.lower()}</b> while keeping other factors unchanged.</div></div>',unsafe_allow_html=True)

    if len(disc)>=2:
        st.markdown('<div class="fb fb-ok"><div class="fb-bar"></div><div class="fb-body"><b>Both biases identified.</b></div></div>',unsafe_allow_html=True)
        if st.button("Issue your verdict",type="primary",use_container_width=True): st.session_state.phase="fin"; st.rerun()
    else:
        if st.button("Skip to verdict",use_container_width=True): st.session_state.phase="fin"; st.rerun()

# ═══════════════ FINALE ═══════════════
elif phase=="fin":
    st.markdown(f'<div class="hero" style="height:260px;"><img src="{HERO}"><div class="hero-inner" style="text-align:center;padding-bottom:40px;">'
        '<div class="hero-h1" style="font-size:2.4rem;">The Verdict</div></div></div>',unsafe_allow_html=True)

    you=st.session_state.r1y; ai=st.session_state.r1a; r2s=st.session_state.r2s; biases=len(st.session_state.r3disc)
    total_score = you + r2s + biases*2
    if total_score>=14: grade="A"; gc="#7ab8e0"; gt_="Expert Regulator"
    elif total_score>=10: grade="B"; gc="#5b9bd5"; gt_="Competent Reviewer"
    elif total_score>=6: grade="C"; gc="#d4a55a"; gt_="Developing Awareness"
    else: grade="D"; gc="#c48a5a"; gt_="Needs More Tools"

    st.markdown(f'<div class="grade-box"><div class="grade-letter" style="color:{gc};">{grade}</div>'
        f'<div class="grade-title">{gt_}</div></div>',unsafe_allow_html=True)

    r1res="Won" if you>ai else ("Tied" if you==ai else "Lost")
    c1,c2,c3=st.columns(3)
    with c1: st.markdown(f'<div class="sb-cell" style="background:#0f1520;border:2px solid #1a2436;padding:24px;text-align:center;"><div class="sb-num">{you}/{len(PP)}</div><div class="sb-label">You vs system ({r1res})</div></div>',unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="sb-cell" style="background:#0f1520;border:2px solid #1a2436;padding:24px;text-align:center;"><div class="sb-num">{r2s}/{len(R2P)}</div><div class="sb-label">Flaws spotted</div></div>',unsafe_allow_html=True)
    with c3: st.markdown(f'<div class="sb-cell" style="background:#0f1520;border:2px solid #1a2436;padding:24px;text-align:center;"><div class="sb-num">{biases}/2</div><div class="sb-label">Biases found</div></div>',unsafe_allow_html=True)

    st.markdown("")
    st.markdown("### What the system actually weights")
    for label,w,fair,note in [("Education",72,True,"Appropriate"),("Languages",70,False,"Over-weighted"),("Age",58,False,"Should be zero"),("Experience",11,True,"Under-weighted")]:
        c="#7ab8e0" if fair else "#d4a87a"
        st.markdown(f'<div style="margin-bottom:14px;"><div style="display:flex;justify-content:space-between;font-size:1.05rem;margin-bottom:4px;">'
            f'<span style="font-weight:700;color:#e4eaf4;">{label}</span><span style="color:{c};font-weight:600;">{note}</span></div>'
            f'<div class="wbg"><div class="wf" style="width:{w}%;background:{c};"></div></div></div>',unsafe_allow_html=True)

    st.markdown("")
    st.markdown("### What you proved")

    st.markdown('<div class="fb fb-bad"><div class="fb-bar"></div><div class="fb-body" style="font-size:1.1rem;">'
        '<b>Accurate systems can discriminate.</b><br>'
        '92% accuracy. Systematic age discrimination. Both true at the same time.</div></div>',unsafe_allow_html=True)

    st.markdown('<div class="fb fb-info"><div class="fb-bar"></div><div class="fb-body" style="font-size:1.1rem;">'
        '<b>The system inherited bias from its training data.</b><br>'
        'No one programmed age discrimination. It learned it from past hiring decisions.</div></div>',unsafe_allow_html=True)

    st.markdown('<div class="fb fb-gray"><div class="fb-bar"></div><div class="fb-body" style="font-size:1.1rem;">'
        '<b>Small changes flip big decisions.</b><br>'
        'One language. A few years of age. Enough to reverse a career outcome.</div></div>',unsafe_allow_html=True)

    st.markdown("")
    st.markdown("### What regulation should require")
    l,r=st.columns(2)
    with l:
        st.markdown('<div style="background:#0f1520;border:2px solid #1a2436;padding:28px 32px;">'
            '<div style="font-size:1.15rem;font-weight:700;color:#e4eaf4;margin-bottom:8px;">Robustness testing</div>'
            '<div style="color:#7a8da4;font-size:0.98rem;">Do decisions stay stable when irrelevant details change?</div></div>',unsafe_allow_html=True)
    with r:
        st.markdown('<div style="background:#0f1520;border:2px solid #1a2436;padding:28px 32px;">'
            '<div style="font-size:1.15rem;font-weight:700;color:#e4eaf4;margin-bottom:8px;">Bias auditing</div>'
            '<div style="color:#7a8da4;font-size:0.98rem;">Do protected characteristics influence outcomes?</div></div>',unsafe_allow_html=True)
    l2,r2=st.columns(2)
    with l2:
        st.markdown('<div style="background:#0f1520;border:2px solid #1a2436;padding:28px 32px;">'
            '<div style="font-size:1.15rem;font-weight:700;color:#e4eaf4;margin-bottom:8px;">Explainability</div>'
            '<div style="color:#7a8da4;font-size:0.98rem;">Can the system justify each decision?</div></div>',unsafe_allow_html=True)
    with r2:
        st.markdown('<div style="background:#0f1520;border:2px solid #1a2436;padding:28px 32px;">'
            '<div style="font-size:1.15rem;font-weight:700;color:#e4eaf4;margin-bottom:8px;">Accuracy is not enough</div>'
            '<div style="color:#7a8da4;font-size:0.98rem;">92% accuracy hid every problem you found.</div></div>',unsafe_allow_html=True)

    st.markdown("")
    st.markdown('<div class="vbox"><div class="vchip">Verdict</div>'
        '<div class="vh">Do not deploy</div>'
        '<div class="vp">This system discriminates by age, over-weights optional qualifications, '
        'and flips decisions based on irrelevant changes.<br><br>'
        '<b>Accuracy tells you how often the system matches past decisions. '
        'It does not tell you whether those decisions were fair.</b></div></div>',unsafe_allow_html=True)

    # Closing image
    st.markdown(
        '<div style="margin:40px 0;overflow:hidden;border:2px solid #1a2436;position:relative;height:280px;">'
        f'<img src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&h=500&fit=crop" '
        'style="width:100%;height:100%;object-fit:cover;filter:brightness(0.25) saturate(0.4);">'
        '<div style="position:absolute;top:0;left:0;right:0;bottom:0;display:flex;flex-direction:column;'
        'align-items:center;justify-content:center;background:linear-gradient(rgba(11,16,24,0.3),rgba(11,16,24,0.7));">'
        '<div style="font-family:Instrument Serif,Georgia,serif;font-size:1.8rem;color:#e4eaf4;text-align:center;">'
        'Accuracy is not safety.</div>'
        '<div style="font-size:1rem;color:#6b7d96;margin-top:8px;text-align:center;">'
        'Testing is how we find what the numbers hide.</div>'
        '</div></div>',
        unsafe_allow_html=True
    )

    st.markdown("---")
    if st.button("Start over",use_container_width=True):
        for k,v in _D.items(): st.session_state[k]=v
        st.rerun()

st.markdown('<div class="foot">Prototype by Hana Ibrahim. Explaining AI bias to policymakers.</div>',unsafe_allow_html=True)
