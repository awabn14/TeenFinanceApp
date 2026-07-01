"""
Money Mastery — Financial Literacy App for Teens
A single-file Streamlit application teaching smart money habits.
"""

import streamlit as st
from datetime import datetime

# ---------------------------------------------------------------------------
# Page config & global styling
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Money Mastery",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

    :root {
        --bg-deep: #0a0e17;
        --bg-card: #141b2d;
        --bg-card-hover: #1a2340;
        --accent-cyan: #00d4aa;
        --accent-purple: #a855f7;
        --accent-pink: #ec4899;
        --accent-orange: #f97316;
        --text-primary: #f1f5f9;
        --text-muted: #94a3b8;
        --border-subtle: rgba(148, 163, 184, 0.15);
        --green-safe: #22c55e;
        --orange-caution: #f59e0b;
        --red-danger: #ef4444;
    }

    .stApp {
        background: linear-gradient(135deg, var(--bg-deep) 0%, #0f172a 50%, #1a1033 100%);
        font-family: 'Space Grotesk', sans-serif;
    }

    #MainMenu, footer, header { visibility: hidden; }

    .hero-title {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(90deg, var(--accent-cyan), var(--accent-purple), var(--accent-pink));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.25rem;
        line-height: 1.2;
    }

    .hero-subtitle {
        color: var(--text-muted);
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .stat-card {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 16px;
        padding: 1.25rem 1.5rem;
        text-align: center;
        transition: transform 0.2s, border-color 0.2s;
    }

    .stat-card:hover {
        transform: translateY(-2px);
        border-color: var(--accent-cyan);
    }

    .stat-value {
        font-size: 1.75rem;
        font-weight: 700;
        color: var(--accent-cyan);
    }

    .stat-label {
        color: var(--text-muted);
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .coach-bubble {
        background: var(--bg-card);
        border-left: 4px solid var(--accent-purple);
        border-radius: 0 12px 12px 0;
        padding: 1rem 1.25rem;
        margin: 0.75rem 0;
        color: var(--text-primary);
        line-height: 1.6;
    }

    .coach-bubble.user {
        border-left-color: var(--accent-cyan);
        background: rgba(0, 212, 170, 0.08);
    }

    .tip-chip {
        display: inline-block;
        background: rgba(168, 85, 247, 0.15);
        border: 1px solid rgba(168, 85, 247, 0.3);
        border-radius: 20px;
        padding: 0.35rem 0.85rem;
        margin: 0.25rem;
        font-size: 0.85rem;
        color: var(--accent-purple);
    }

    .warning-chip {
        display: inline-block;
        background: rgba(249, 115, 22, 0.15);
        border: 1px solid rgba(249, 115, 22, 0.3);
        border-radius: 20px;
        padding: 0.35rem 0.85rem;
        margin: 0.25rem;
        font-size: 0.85rem;
        color: var(--accent-orange);
    }

    .habit-alert {
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        font-weight: 600;
        font-size: 1.1rem;
        margin-top: 1rem;
    }

    .habit-green {
        background: rgba(34, 197, 94, 0.15);
        border: 2px solid var(--green-safe);
        color: var(--green-safe);
    }

    .habit-orange {
        background: rgba(245, 158, 11, 0.15);
        border: 2px solid var(--orange-caution);
        color: var(--orange-caution);
    }

    .habit-red {
        background: rgba(239, 68, 68, 0.15);
        border: 2px solid var(--red-danger);
        color: var(--red-danger);
    }

    .term-card-header {
        font-size: 1.15rem;
        font-weight: 600;
        color: var(--accent-cyan);
    }

    .simple-box {
        background: rgba(0, 212, 170, 0.08);
        border-radius: 12px;
        padding: 1rem;
        border-left: 3px solid var(--accent-cyan);
        margin: 0.5rem 0;
    }

    .pro-box {
        background: rgba(168, 85, 247, 0.08);
        border-radius: 12px;
        padding: 1rem;
        border-left: 3px solid var(--accent-purple);
        margin: 0.5rem 0;
    }

    div[data-testid="stMetric"] {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 12px;
        padding: 1rem;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        background: var(--bg-card);
        border-radius: 12px;
        border: 1px solid var(--border-subtle);
        color: var(--text-muted);
        padding: 0.75rem 1.5rem;
        font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0,212,170,0.2), rgba(168,85,247,0.2));
        border-color: var(--accent-cyan);
        color: var(--text-primary);
    }

    div[data-testid="stExpander"] {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 16px;
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Session state initialization — persists across tab switches & reruns
# ---------------------------------------------------------------------------

def init_session_state() -> None:
    """Initialize all session keys with defaults if missing."""
    defaults = {
        "age": 15,
        "allowance_amount": 25.0,
        "allowance_frequency": "Weekly",
        "coach_messages": [],
        "profile_analyzed": False,
        "expense_name": "",
        "expense_amount": 0.0,
        "expense_log": [],
        "expanded_terms": set(),
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()


# ---------------------------------------------------------------------------
# Financial dictionary data
# ---------------------------------------------------------------------------

FINANCIAL_TERMS = [
    {
        "term": "Interest",
        "emoji": "📈",
        "simple": (
            "Imagine you lend your friend $20 for a new game skin, and they agree to pay you back "
            "$22 next month. That extra $2? That's interest — a reward for letting someone use your money. "
            "Banks work the same way: save money and they pay YOU interest. Borrow money and YOU pay THEM."
        ),
        "pro": (
            "Interest is the cost of borrowing money or the return earned on deposited or invested capital, "
            "expressed as a percentage of the principal over a specified time period. Simple interest is "
            "calculated on the original principal only; compound interest accrues on both principal and "
            "previously accumulated interest."
        ),
    },
    {
        "term": "Inflation",
        "emoji": "🎮",
        "simple": (
            "Remember when a Fortnite V-Bucks bundle felt like a steal? Over time, the same $10 buys "
            "fewer snacks, fewer skins, and smaller portions at your favorite spot. That's inflation — "
            "prices creeping up while your dollar buys less. Your allowance needs to grow too, or "
            "you're technically getting a pay cut every year."
        ),
        "pro": (
            "Inflation is the sustained increase in the general price level of goods and services in an "
            "economy over time, resulting in a decline in purchasing power per unit of currency. Central "
            "banks monitor inflation using indices such as the Consumer Price Index (CPI) and target "
            "stable, moderate inflation rates (typically ~2% annually in developed economies)."
        ),
    },
    {
        "term": "Credit Score",
        "emoji": "⭐",
        "simple": (
            "Think of it like your GPA, but for money. Pay bills on time, don't max out cards, and "
            "your score climbs — unlocking better loan rates and apartment approvals later. Miss payments "
            "or borrow too much? Your 'money GPA' tanks, and adult-you will feel it when buying a car "
            "or renting a place."
        ),
        "pro": (
            "A credit score is a numerical representation (typically 300–850 via FICO or VantageScore) "
            "of a consumer's creditworthiness, derived from credit history including payment history, "
            "credit utilization ratio, length of credit history, types of credit, and recent inquiries. "
            "Lenders use scores to assess default risk and determine interest rates."
        ),
    },
    {
        "term": "Liquidity",
        "emoji": "💧",
        "simple": (
            "Cash in your wallet = super liquid — grab it and buy boba instantly. Money locked in a "
            "6-month savings bond? Not liquid — you can't touch it without penalties. Liquidity is "
            "how fast you can turn something into spendable cash without losing value."
        ),
        "pro": (
            "Liquidity refers to the ease and speed with which an asset can be converted into cash "
            "without significantly affecting its market price. Highly liquid assets include cash, "
            "checking accounts, and publicly traded securities; illiquid assets include real estate, "
            "private equity, and long-term certificates of deposit."
        ),
    },
    {
        "term": "Index Funds",
        "emoji": "🎯",
        "simple": (
            "Instead of betting on one company's stock (risky!), an index fund buys a slice of "
            "hundreds of companies at once — like getting the whole playlist instead of one song. "
            "The S&P 500 fund tracks America's 500 biggest companies. Boring? Maybe. But historically, "
            "it's one of the smartest long-term moves young investors can make."
        ),
        "pro": (
            "An index fund is a passively managed mutual fund or ETF designed to replicate the "
            "performance of a specific market index (e.g., S&P 500, NASDAQ-100) by holding the same "
            "securities in proportional weights. Index funds offer broad diversification, low expense "
            "ratios, and historically competitive returns relative to actively managed funds."
        ),
    },
    {
        "term": "Compound Interest",
        "emoji": "🌱",
        "simple": (
            "It's interest on your interest — like a snowball rolling downhill. Save $100 and earn "
            "$5 interest. Next round, you earn interest on $105, not just $100. Start early and "
            "this snowball becomes an avalanche. Start late and you're chasing it uphill."
        ),
        "pro": (
            "Compound interest is interest calculated on the initial principal and on all accumulated "
            "interest from previous periods. The formula A = P(1 + r/n)^(nt) governs growth, where "
            "time (t) and compounding frequency (n) dramatically amplify returns — a principle central "
            "to long-term wealth accumulation and retirement planning."
        ),
    },
]


# ---------------------------------------------------------------------------
# AI Coach — rule-based advisory engine
# ---------------------------------------------------------------------------

def weekly_equivalent(amount: float, frequency: str) -> float:
    """Normalize allowance to a weekly figure for consistent analysis."""
    if frequency == "Monthly":
        return amount / 4.33
    return amount


def classify_income_tier(weekly: float) -> str:
    """Bucket weekly income into low / medium / high for teens."""
    if weekly < 15:
        return "low"
    if weekly < 50:
        return "medium"
    return "high"


def classify_age_group(age: int) -> str:
    """Map age to developmental spending context."""
    if age <= 14:
        return "early_teen"
    if age <= 16:
        return "mid_teen"
    return "late_teen"


def generate_coach_advice(age: int, amount: float, frequency: str) -> dict:
    """
    Rule-based 'AI' coach that returns personalized financial guidance.
    Structured as a dict for clean rendering in the UI.
    """
    weekly = weekly_equivalent(amount, frequency)
    income_tier = classify_income_tier(weekly)
    age_group = classify_age_group(age)

    # --- Spending rules (50/30/20 adapted for teens) ---
    save_pct, spend_pct, fun_pct = 0.30, 0.40, 0.30
    if age_group == "early_teen":
        save_pct, spend_pct, fun_pct = 0.40, 0.35, 0.25
    elif age_group == "late_teen":
        save_pct, spend_pct, fun_pct = 0.25, 0.45, 0.30

    if income_tier == "low":
        save_pct += 0.05
        fun_pct -= 0.05

    save_amt = weekly * save_pct
    needs_amt = weekly * spend_pct
    fun_amt = weekly * fun_pct

    rules = [
        f"Save **${save_amt:.2f}/week** ({save_pct:.0%}) — future-you will thank present-you.",
        f"Spend **${needs_amt:.2f}/week** ({spend_pct:.0%}) on needs: food, transport, school stuff.",
        f"Keep **${fun_amt:.2f}/week** ({fun_pct:.0%}) for fun — gaming, clothes, hangouts.",
    ]

    # --- Age-specific tips ---
    tips_by_age = {
        "early_teen": [
            "Start a savings jar or app now — even $5/week adds up to $260/year.",
            "Before buying, wait 48 hours. Impulse buys are the #1 budget killer at your age.",
            "Track every purchase for one week. You'll be shocked where money disappears.",
        ],
        "mid_teen": [
            "Open a teen checking/savings account — learn banking before you need it.",
            "Side hustle idea: tutoring, reselling, or freelancing can 2× your income.",
            "Never lend money you can't afford to lose. Friendships > $20.",
        ],
        "late_teen": [
            "Start building credit responsibly — authorized user on a parent's card works.",
            "Learn about index funds now; investing at 17 beats starting at 27 by ~$100K+.",
            "Create a 'future fund' for car, college, or moving out — automate transfers.",
        ],
    }

    # --- Income-tier adjustments ---
    tier_tips = {
        "low": "Every dollar counts — prioritize needs, hunt student discounts, and celebrate small wins.",
        "medium": "You're in a sweet spot — balance saving with experiences that matter to you.",
        "high": "With more income comes more responsibility — avoid lifestyle creep and save aggressively.",
    }

    # --- Warning signs ---
    warnings = []
    if fun_amt > weekly * 0.35:
        warnings.append("Your fun budget is high — one big weekend can wipe out the whole week.")
    if weekly < 10:
        warnings.append("Tight budget alert: focus on needs first, then micro-savings ($1–2 at a time).")
    if age >= 17 and save_pct < 0.25:
        warnings.append("At your age, saving under 25% makes adult milestones harder to hit.")
    if income_tier == "high" and age <= 15:
        warnings.append("Big allowance + young age = easy to overspend. Set auto-save BEFORE spending.")
    warnings.append("Red flag: spending more than you earn (dipping into savings every week).")
    warnings.append("Red flag: hiding purchases or lying about spending — honesty keeps you on track.")

    greeting = (
        f"Hey! I'm your Money Coach. At **{age}** with **${amount:.2f}/{frequency.lower()}** "
        f"(~**${weekly:.2f}/week**), here's your personalized game plan:"
    )

    return {
        "greeting": greeting,
        "rules": rules,
        "tips": tips_by_age[age_group] + [tier_tips[income_tier]],
        "warnings": warnings,
        "weekly": weekly,
        "save_amt": save_amt,
        "fun_amt": fun_amt,
    }


def process_coach_question(question: str, profile: dict) -> str:
    """
    Placeholder for LLM integration — handles common questions via rules.
    Replace `return` body with an API call to OpenAI/Anthropic when ready.
    """
    q = question.lower().strip()
    weekly = profile["weekly"]

    if any(w in q for w in ["save", "saving", "savings"]):
        return (
            f"Aim to save at least **${profile['save_amt']:.2f}/week**. "
            "Set up automatic transfers on allowance day so you never 'forget.' "
            "The best savers pay themselves first — savings happen before spending."
        )
    if any(w in q for w in ["budget", "spend", "spending"]):
        return (
            f"Your weekly fun budget is **${profile['fun_amt']:.2f}**. "
            "Try the envelope method: once it's gone, it's gone. "
            "Use a notes app to log every purchase — awareness is half the battle."
        )
    if any(w in q for w in ["invest", "stock", "index"]):
        return (
            "At your age, learning beats earning. Read about index funds (check our Dictionary tab!), "
            "open a custodial account with a parent, and start with small amounts. "
            "Time in the market beats timing the market — starting now is your superpower."
        )
    if any(w in q for w in ["credit", "card", "debt"]):
        return (
            "Credit cards aren't free money — they're loans with 20%+ interest if you miss payments. "
            "Build credit slowly: one small recurring charge, paid in full every month. "
            "Your future self needs a good credit score for apartments, cars, and loans."
        )
    if any(w in q for w in ["job", "work", "earn", "money"]):
        return (
            f"With **${weekly:.2f}/week** from allowance, a side gig could change everything. "
            "Babysitting, tutoring, lawn care, reselling, content creation — pick something you enjoy. "
            "Extra income should be split: 50% save, 30% invest/learn, 20% treat yourself."
        )

    return (
        f"Great question! Based on your profile (~${weekly:.2f}/week), I'd say: "
        "save first, spend intentionally, and never stop learning. "
        "Try asking about saving, budgeting, investing, credit, or earning more!"
    )


# ---------------------------------------------------------------------------
# Spending monitor logic
# ---------------------------------------------------------------------------

def evaluate_habit(expense: float, weekly_allowance: float) -> tuple[str, str, float]:
    """
    Return (alert_level, message, percentage) for a single expense.
    Levels: green | orange | red
    """
    if weekly_allowance <= 0:
        return "red", "Set your allowance in the Coach tab first!", 100.0

    pct = (expense / weekly_allowance) * 100

    if pct <= 15:
        return (
            "green",
            f"Safe zone! This purchase uses only {pct:.0f}% of your weekly budget. Keep it up!",
            pct,
        )
    if pct <= 35:
        return (
            "orange",
            f"Caution — {pct:.0f}% of your weekly allowance gone in one purchase. Plan the rest of your week.",
            pct,
        )
    return (
        "red",
        f"Overspending alert! {pct:.0f}% of your weekly budget in one hit. Pause and reconsider.",
        pct,
    )


def total_spent_this_period(expense_log: list) -> float:
    """Sum all logged expenses."""
    return sum(e["amount"] for e in expense_log)


# ---------------------------------------------------------------------------
# UI Components
# ---------------------------------------------------------------------------

def render_hero() -> None:
    """Top banner with app branding."""
    st.markdown('<p class="hero-title">💸 Money Mastery</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hero-subtitle">Level up your money game — built for Gen Z, powered by smart habits.</p>',
        unsafe_allow_html=True,
    )


def render_profile_stats() -> None:
    """Dashboard strip showing current profile at a glance."""
    weekly = weekly_equivalent(
        st.session_state.allowance_amount,
        st.session_state.allowance_frequency,
    )
    cols = st.columns(4)
    stats = [
        ("Age", f"{st.session_state.age}"),
        ("Allowance", f"${st.session_state.allowance_amount:.2f}"),
        ("Frequency", st.session_state.allowance_frequency),
        ("Weekly Equiv.", f"${weekly:.2f}"),
    ]
    for col, (label, value) in zip(cols, stats):
        with col:
            st.markdown(
                f'<div class="stat-card"><div class="stat-value">{value}</div>'
                f'<div class="stat-label">{label}</div></div>',
                unsafe_allow_html=True,
            )


def render_coach_tab() -> None:
    """Feature 1: Personalized AI Financial Coach."""
    st.markdown("### 🤖 Your AI Money Coach")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.session_state.age = st.selectbox(
            "Your Age",
            options=list(range(13, 20)),
            index=list(range(13, 20)).index(st.session_state.age)
            if st.session_state.age in range(13, 20)
            else 2,
            key="coach_age_select",
        )

    with col2:
        st.session_state.allowance_amount = st.number_input(
            "Allowance Amount ($)",
            min_value=0.0,
            max_value=2000.0,
            value=float(st.session_state.allowance_amount),
            step=5.0,
            key="coach_allowance_input",
        )

    with col3:
        st.session_state.allowance_frequency = st.radio(
            "Allowance Frequency",
            options=["Weekly", "Monthly"],
            index=0 if st.session_state.allowance_frequency == "Weekly" else 1,
            horizontal=True,
            key="coach_frequency_radio",
        )

    if st.button("✨ Analyze My Profile", type="primary", use_container_width=True):
        advice = generate_coach_advice(
            st.session_state.age,
            st.session_state.allowance_amount,
            st.session_state.allowance_frequency,
        )
        st.session_state.coach_messages = [
            {"role": "coach", "text": advice["greeting"]},
            {"role": "coach", "text": "**Your Spending Rules:**\n" + "\n".join(f"• {r}" for r in advice["rules"])},
            {
                "role": "coach",
                "text": "**Actionable Tips:**<br>"
                + " ".join(f'<span class="tip-chip">{t}</span>' for t in advice["tips"]),
            },
            {
                "role": "coach",
                "text": "**Warning Signs to Watch:**<br>"
                + " ".join(f'<span class="warning-chip">{w}</span>' for w in advice["warnings"]),
            },
        ]
        st.session_state.profile_analyzed = True
        st.session_state._coach_profile = advice  # cache for Q&A

    # Display coach conversation
    for msg in st.session_state.coach_messages:
        css_class = "coach-bubble user" if msg["role"] == "user" else "coach-bubble"
        st.markdown(f'<div class="{css_class}">{msg["text"]}</div>', unsafe_allow_html=True)

    if st.session_state.profile_analyzed:
        st.markdown("---")
        st.markdown("#### 💬 Ask Your Coach")
        user_q = st.text_input(
            "Type a question (try: saving, budget, investing, credit...)",
            key="coach_question_input",
            placeholder="How much should I save each week?",
        )
        if st.button("Send", key="coach_send_btn") and user_q.strip():
            profile = st.session_state.get("_coach_profile", {})
            if not profile:
                profile = generate_coach_advice(
                    st.session_state.age,
                    st.session_state.allowance_amount,
                    st.session_state.allowance_frequency,
                )
            st.session_state.coach_messages.append({"role": "user", "text": user_q})
            answer = process_coach_question(user_q, profile)
            st.session_state.coach_messages.append({"role": "coach", "text": answer})
            st.rerun()


def render_dictionary_tab() -> None:
    """Feature 2: Dual-Depth Financial Dictionary."""
    st.markdown("### 📚 Financial Terms Masterclass")
    st.markdown(
        "Tap each term to toggle between **teen-friendly analogies** and **pro-level definitions**."
    )

    for i, term in enumerate(FINANCIAL_TERMS):
        with st.expander(f"{term['emoji']} {term['term']}", expanded=False):
            view_mode = st.toggle(
                "Show Pro Definition",
                value=False,
                key=f"term_toggle_{i}",
            )

            if view_mode:
                st.markdown(
                    f'<div class="pro-box"><strong>🎓 The Pro Definition</strong><br><br>{term["pro"]}</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f'<div class="simple-box"><strong>✨ The Simple Breakdown</strong><br><br>{term["simple"]}</div>',
                    unsafe_allow_html=True,
                )


def render_spending_tab() -> None:
    """Feature 3: Live Spending & Habit Monitor."""
    st.markdown("### 📊 Live Spending & Habit Monitor")

    weekly = weekly_equivalent(
        st.session_state.allowance_amount,
        st.session_state.allowance_frequency,
    )

    # Progress overview
    total_spent = total_spent_this_period(st.session_state.expense_log)
    remaining = max(weekly - total_spent, 0)
    used_pct = min((total_spent / weekly * 100) if weekly > 0 else 0, 100)

    prog_col1, prog_col2, prog_col3 = st.columns(3)
    prog_col1.metric("Weekly Budget", f"${weekly:.2f}")
    prog_col2.metric("Total Logged", f"${total_spent:.2f}")
    prog_col3.metric("Remaining", f"${remaining:.2f}")

    st.progress(used_pct / 100 if used_pct else 0)
    st.caption(f"You've used **{used_pct:.0f}%** of your weekly allowance so far.")

    st.markdown("---")
    st.markdown("#### Log an Expense")

    exp_col1, exp_col2 = st.columns([2, 1])
    with exp_col1:
        st.session_state.expense_name = st.text_input(
            "What did you buy?",
            value=st.session_state.expense_name,
            placeholder="e.g., Bubble tea, Fortnite V-Bucks, Gas",
            key="expense_name_input",
        )
    with exp_col2:
        st.session_state.expense_amount = st.number_input(
            "Amount ($)",
            min_value=0.0,
            max_value=500.0,
            value=float(st.session_state.expense_amount),
            step=1.0,
            key="expense_amount_input",
        )

    if st.button("➕ Log Expense", type="primary", use_container_width=True):
        if st.session_state.expense_amount > 0:
            level, message, pct = evaluate_habit(
                st.session_state.expense_amount, weekly
            )
            st.session_state.expense_log.append(
                {
                    "name": st.session_state.expense_name or "Unnamed purchase",
                    "amount": st.session_state.expense_amount,
                    "level": level,
                    "pct": pct,
                    "time": datetime.now().strftime("%I:%M %p"),
                }
            )
            st.session_state._last_habit = {"level": level, "message": message, "pct": pct}
            st.session_state.expense_name = ""
            st.session_state.expense_amount = 0.0
            st.rerun()
        else:
            st.warning("Enter an amount greater than $0.")

    # Habit alert for last logged expense
    if "_last_habit" in st.session_state:
        h = st.session_state._last_habit
        css = f"habit-{h['level']}"
        st.markdown(
            f'<div class="habit-alert {css}">{h["message"]}</div>',
            unsafe_allow_html=True,
        )

    # Expense history
    if st.session_state.expense_log:
        st.markdown("---")
        st.markdown("#### 📋 Today's Log")
        for entry in reversed(st.session_state.expense_log):
            icon = {"green": "🟢", "orange": "🟠", "red": "🔴"}.get(entry["level"], "⚪")
            st.markdown(
                f"{icon} **{entry['name']}** — ${entry['amount']:.2f} "
                f"({entry['pct']:.0f}% of weekly) · _{entry['time']}_"
            )

        if st.button("🗑️ Clear Log", key="clear_expense_log"):
            st.session_state.expense_log = []
            st.session_state.pop("_last_habit", None)
            st.rerun()


# ---------------------------------------------------------------------------
# Main app entry
# ---------------------------------------------------------------------------

def main() -> None:
    render_hero()
    render_profile_stats()

    tab_coach, tab_dict, tab_spend = st.tabs(
        ["🤖 AI Coach", "📚 Dictionary", "📊 Spending Monitor"]
    )

    with tab_coach:
        render_coach_tab()

    with tab_dict:
        render_dictionary_tab()

    with tab_spend:
        render_spending_tab()


if __name__ == "__main__":
    main()
