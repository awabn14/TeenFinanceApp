"""
Money Mastery — Financial Literacy App for Teens
A single-file Streamlit application teaching smart money habits worldwide.
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

    .category-badge {
        display: inline-block;
        background: rgba(0, 212, 170, 0.12);
        border: 1px solid rgba(0, 212, 170, 0.35);
        border-radius: 8px;
        padding: 0.15rem 0.55rem;
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        color: var(--accent-cyan);
        margin-left: 0.5rem;
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
# Global currency registry — thresholds tuned per local teen allowance scale
# ---------------------------------------------------------------------------

CURRENCIES = {
    "USD": {
        "name": "US Dollar",
        "symbol": "$",
        "decimals": 2,
        "step": 5.0,
        "max_allowance": 2000.0,
        "max_expense": 500.0,
        "weekly_low": 15,
        "weekly_medium": 50,
        "micro_save": 5,
        "snack_cost": 8,
        "impulse_big": 40,
    },
    "EUR": {
        "name": "Euro",
        "symbol": "€",
        "decimals": 2,
        "step": 5.0,
        "max_allowance": 1800.0,
        "max_expense": 450.0,
        "weekly_low": 14,
        "weekly_medium": 45,
        "micro_save": 5,
        "snack_cost": 7,
        "impulse_big": 35,
    },
    "GBP": {
        "name": "British Pound",
        "symbol": "£",
        "decimals": 2,
        "step": 5.0,
        "max_allowance": 1600.0,
        "max_expense": 400.0,
        "weekly_low": 12,
        "weekly_medium": 40,
        "micro_save": 4,
        "snack_cost": 6,
        "impulse_big": 30,
    },
    "CAD": {
        "name": "Canadian Dollar",
        "symbol": "C$",
        "decimals": 2,
        "step": 5.0,
        "max_allowance": 2200.0,
        "max_expense": 550.0,
        "weekly_low": 18,
        "weekly_medium": 55,
        "micro_save": 5,
        "snack_cost": 9,
        "impulse_big": 45,
    },
    "AUD": {
        "name": "Australian Dollar",
        "symbol": "A$",
        "decimals": 2,
        "step": 5.0,
        "max_allowance": 2400.0,
        "max_expense": 600.0,
        "weekly_low": 20,
        "weekly_medium": 60,
        "micro_save": 5,
        "snack_cost": 10,
        "impulse_big": 50,
    },
    "INR": {
        "name": "Indian Rupee",
        "symbol": "₹",
        "decimals": 0,
        "step": 100.0,
        "max_allowance": 100000.0,
        "max_expense": 5000.0,
        "weekly_low": 500,
        "weekly_medium": 2000,
        "micro_save": 100,
        "snack_cost": 150,
        "impulse_big": 800,
    },
    "JPY": {
        "name": "Japanese Yen",
        "symbol": "¥",
        "decimals": 0,
        "step": 500.0,
        "max_allowance": 200000.0,
        "max_expense": 20000.0,
        "weekly_low": 1500,
        "weekly_medium": 5000,
        "micro_save": 500,
        "snack_cost": 600,
        "impulse_big": 3000,
    },
    "AED": {
        "name": "UAE Dirham",
        "symbol": "د.إ",
        "decimals": 2,
        "step": 10.0,
        "max_allowance": 5000.0,
        "max_expense": 1200.0,
        "weekly_low": 50,
        "weekly_medium": 180,
        "micro_save": 20,
        "snack_cost": 25,
        "impulse_big": 150,
    },
    "ZAR": {
        "name": "South African Rand",
        "symbol": "R",
        "decimals": 2,
        "step": 20.0,
        "max_allowance": 15000.0,
        "max_expense": 3000.0,
        "weekly_low": 200,
        "weekly_medium": 800,
        "micro_save": 50,
        "snack_cost": 80,
        "impulse_big": 400,
    },
    "MXN": {
        "name": "Mexican Peso",
        "symbol": "MX$",
        "decimals": 2,
        "step": 20.0,
        "max_allowance": 15000.0,
        "max_expense": 3000.0,
        "weekly_low": 250,
        "weekly_medium": 900,
        "micro_save": 50,
        "snack_cost": 80,
        "impulse_big": 500,
    },
    "BRL": {
        "name": "Brazilian Real",
        "symbol": "R$",
        "decimals": 2,
        "step": 10.0,
        "max_allowance": 5000.0,
        "max_expense": 1200.0,
        "weekly_low": 70,
        "weekly_medium": 250,
        "micro_save": 20,
        "snack_cost": 25,
        "impulse_big": 150,
    },
    "SGD": {
        "name": "Singapore Dollar",
        "symbol": "S$",
        "decimals": 2,
        "step": 5.0,
        "max_allowance": 2200.0,
        "max_expense": 550.0,
        "weekly_low": 18,
        "weekly_medium": 60,
        "micro_save": 5,
        "snack_cost": 8,
        "impulse_big": 45,
    },
    "OTHER": {
        "name": "Other Currency",
        "symbol": "",
        "decimals": 2,
        "step": 5.0,
        "max_allowance": 2000.0,
        "max_expense": 500.0,
        "weekly_low": 15,
        "weekly_medium": 50,
        "micro_save": 5,
        "snack_cost": 8,
        "impulse_big": 40,
    },
}

CURRENCY_OPTIONS = [
    "USD — US Dollar ($)",
    "EUR — Euro (€)",
    "GBP — British Pound (£)",
    "CAD — Canadian Dollar (C$)",
    "AUD — Australian Dollar (A$)",
    "INR — Indian Rupee (₹)",
    "JPY — Japanese Yen (¥)",
    "AED — UAE Dirham (د.إ)",
    "ZAR — South African Rand (R)",
    "MXN — Mexican Peso (MX$)",
    "BRL — Brazilian Real (R$)",
    "SGD — Singapore Dollar (S$)",
    "OTHER — Other Currency",
]

CURRENCY_CODE_MAP = {opt.split(" — ")[0]: opt for opt in CURRENCY_OPTIONS}


# ---------------------------------------------------------------------------
# Session state initialization — persists across tab switches & reruns
# ---------------------------------------------------------------------------

def init_session_state() -> None:
    """Initialize all session keys with defaults if missing."""
    defaults = {
        "age": 15,
        "allowance_amount": 25.0,
        "allowance_frequency": "Weekly",
        "currency_code": "USD",
        "custom_currency_symbol": "¤",
        "custom_currency_name": "Local",
        "coach_messages": [],
        "profile_analyzed": False,
        "expense_name": "",
        "expense_amount": 0.0,
        "expense_log": [],
        "dict_category_filter": "All",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()


# ---------------------------------------------------------------------------
# Currency helpers — single source of truth for formatting & scale
# ---------------------------------------------------------------------------

def get_currency_meta(code: str | None = None) -> dict:
    """Return currency metadata, resolving custom symbol for OTHER."""
    code = code or st.session_state.currency_code
    meta = dict(CURRENCIES.get(code, CURRENCIES["USD"]))
    if code == "OTHER":
        sym = st.session_state.custom_currency_symbol.strip() or "¤"
        name = st.session_state.custom_currency_name.strip() or "Local"
        meta["symbol"] = sym
        meta["name"] = name
    return meta


def fmt_money(amount: float, code: str | None = None, suffix: str = "") -> str:
    """Format an amount with the correct symbol, decimals, and grouping."""
    meta = get_currency_meta(code)
    sym = meta["symbol"]
    if meta["decimals"] == 0:
        formatted = f"{sym}{amount:,.0f}"
    else:
        formatted = f"{sym}{amount:,.2f}"
    return f"{formatted}{suffix}"


def weekly_equivalent(amount: float, frequency: str) -> float:
    """Normalize allowance to a weekly figure for consistent analysis."""
    if frequency == "Monthly":
        return amount / 4.33
    return amount


def classify_income_tier(weekly: float, code: str) -> str:
    """Bucket weekly income using currency-specific teen baseline thresholds."""
    meta = get_currency_meta(code)
    if weekly < meta["weekly_low"]:
        return "low"
    if weekly < meta["weekly_medium"]:
        return "medium"
    return "high"


def classify_age_group(age: int) -> str:
    """Map age to developmental spending context."""
    if age <= 14:
        return "early_teen"
    if age <= 16:
        return "mid_teen"
    return "late_teen"


def currency_scale_note(code: str, weekly: float) -> str:
    """Contextual note so users understand local purchasing power."""
    meta = get_currency_meta(code)
    tier = classify_income_tier(weekly, code)
    snack = fmt_money(meta["snack_cost"], code)
    impulse = fmt_money(meta["impulse_big"], code)

    notes = {
        "JPY": (
            f"In Japan, numbers look big but buying power is different — "
            f"a snack might be {snack}, while {impulse} is a major splurge."
        ),
        "INR": (
            f"In India, even {fmt_money(meta['micro_save'], code)}/week savings adds up fast — "
            f"but {impulse} on one impulse buy can hurt when your weekly baseline is "
            f"{fmt_money(weekly, code)}."
        ),
        "GBP": (
            f"In the UK, {fmt_money(weekly, code)}/week goes further than the same number in yen — "
            f"treat {impulse} as a serious fun-budget hit, not pocket change."
        ),
        "EUR": (
            f"In the Eurozone, prices vary by country — budget using YOUR local prices, "
            f"not what friends abroad pay."
        ),
        "AED": (
            f"In the UAE, dining and entertainment add up quickly — "
            f"a {snack} coffee run every day can eat half your fun budget."
        ),
        "OTHER": (
            f"You're using a custom currency — I've set thresholds based on typical teen budgets. "
            f"Adjust your mental 'snack cost' to around {snack} and 'big splurge' to {impulse}."
        ),
    }

    base = notes.get(
        code,
        f"Your {meta['name']} baseline: a typical snack runs ~{snack}, "
        f"and spending {impulse} in one go is a serious habit flag.",
    )

    tier_add = {
        "low": " You're on a tight budget — micro-savings and needs-first spending are essential.",
        "medium": " You're in a balanced range — smart splits will build great habits.",
        "high": " You have strong spending power — avoid lifestyle creep and save aggressively.",
    }
    return base + tier_add[tier]


# ---------------------------------------------------------------------------
# Financial dictionary — Banking & Economics Masterclass
# ---------------------------------------------------------------------------

FINANCIAL_TERMS = [
    {
        "term": "Interest",
        "emoji": "📈",
        "category": "Banking",
        "simple": (
            "Imagine you lend a friend money for a new game skin, and they pay you back a little extra "
            "next month. That extra? That's interest — a reward for letting someone use your money. "
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
        "term": "Compound Interest",
        "emoji": "🌱",
        "category": "Banking",
        "simple": (
            "It's interest on your interest — like a snowball rolling downhill. Save money, earn interest, "
            "then earn interest on the NEW total. Start at 15 and this snowball becomes an avalanche by 25. "
            "Start at 25 and you're chasing it uphill. Time is your cheat code."
        ),
        "pro": (
            "Compound interest is interest calculated on the initial principal and on all accumulated "
            "interest from previous periods. The formula A = P(1 + r/n)^(nt) governs growth, where "
            "compounding frequency (n) and time (t) dramatically amplify returns — the foundation of "
            "long-term wealth building and retirement accounts."
        ),
    },
    {
        "term": "Checking vs. Savings Accounts",
        "emoji": "🏦",
        "category": "Banking",
        "simple": (
            "Checking = your daily wallet. Money in, money out, debit card, UPI, tap-to-pay — "
            "built for spending. Savings = your vault. Harder to access, but it earns interest and "
            "grows. Pro move: checking for this week's needs, savings for goals that matter."
        ),
        "pro": (
            "A checking (current) account is a deposit account designed for frequent transactions — "
            "deposits, withdrawals, debit payments, and transfers — typically offering minimal or no "
            "interest. A savings account holds funds intended for accumulation, paying interest while "
            "limiting withdrawals. Regulatory frameworks (e.g., Regulation D in the US) may restrict "
            "savings account transaction frequency."
        ),
    },
    {
        "term": "Overdraft Fees & Credit Risk",
        "emoji": "⚠️",
        "category": "Banking",
        "simple": (
            "Overdraft = spending money you don't have. The bank covers you, then slaps on a fee that "
            "can cost more than what you bought. It's like borrowing lunch money and owing double. "
            "Credit risk is the chance you won't pay back — banks track this and it follows you for years."
        ),
        "pro": (
            "An overdraft occurs when a financial institution covers a transaction exceeding available "
            "account balance, often triggering overdraft fees or interest on the negative balance. "
            "Credit risk is the probability of default on borrowed funds; lenders assess it via credit "
            "scores, debt-to-income ratios, and payment history to price loans and set credit limits."
        ),
    },
    {
        "term": "Inflation",
        "emoji": "🎮",
        "category": "Economics",
        "simple": (
            "Remember when your favorite game bundle felt like a steal? Over time, the same amount buys "
            "fewer snacks, fewer skins, and smaller portions. That's inflation — prices creep up while "
            "your money buys less. Your allowance needs to grow too, or you're technically getting a "
            "pay cut every year."
        ),
        "pro": (
            "Inflation is the sustained increase in the general price level of goods and services in an "
            "economy over time, eroding purchasing power per unit of currency. Central banks monitor "
            "inflation via indices such as the Consumer Price Index (CPI) and target moderate, stable "
            "rates (typically ~2% annually in developed economies)."
        ),
    },
    {
        "term": "Central Banks & Interest Rates",
        "emoji": "🏛️",
        "category": "Economics",
        "simple": (
            "Think of the central bank (like the US Federal Reserve, ECB, or Bank of England) as the "
            "economy's DJ — it adjusts the 'beat' (interest rates) to keep the party from overheating "
            "(inflation) or dying (recession). When rates go up, borrowing gets expensive and saving "
            "pays more. When rates drop, loans are cheaper but savings earn less."
        ),
        "pro": (
            "A central bank is the institution responsible for monetary policy, currency issuance, and "
            "financial system stability. By setting benchmark interest rates (e.g., the Federal Funds Rate), "
            "it influences borrowing costs, inflation expectations, and economic growth. Rate hikes typically "
            "cool inflation; cuts stimulate borrowing and investment."
        ),
    },
    {
        "term": "Supply and Demand",
        "emoji": "⚖️",
        "category": "Economics",
        "simple": (
            "Limited-edition sneakers drop → everyone wants them → price skyrockets. That's demand beating "
            "supply. Last season's hoodie nobody wants? Stores slash prices. When supply is high and demand "
            "is low, prices fall. Every price tag you see is this tug-of-war in action."
        ),
        "pro": (
            "Supply and demand is the fundamental economic model describing how the quantity of a good "
            "supplied and the quantity demanded interact to determine market equilibrium price and quantity. "
            "Shifts in either curve — caused by income changes, preferences, production costs, or "
            "regulations — alter equilibrium outcomes across all markets."
        ),
    },
    {
        "term": "Gross Domestic Product (GDP)",
        "emoji": "🌍",
        "category": "Economics",
        "simple": (
            "GDP is basically a country's report card for economic activity — everything produced and "
            "sold inside that country in a year. Rising GDP? More jobs, more opportunities, generally "
            "good vibes. Shrinking GDP? Recession territory — harder to find work, tighter wallets everywhere."
        ),
        "pro": (
            "Gross Domestic Product (GDP) measures the total monetary value of all final goods and services "
            "produced within a country's borders during a specific period. It is calculated via the "
            "expenditure approach (C + I + G + NX), the income approach, or the production approach. "
            "Real GDP adjusts for inflation; GDP per capita indicates average economic output per person."
        ),
    },
    {
        "term": "Credit Score",
        "emoji": "⭐",
        "category": "Banking",
        "simple": (
            "Think of it like your GPA, but for money. Pay bills on time, don't max out cards, and "
            "your score climbs — unlocking better loan rates and apartment approvals later. Miss payments "
            "or borrow too much? Your 'money GPA' tanks, and adult-you will feel it."
        ),
        "pro": (
            "A credit score is a numerical representation (typically 300–850 via FICO or VantageScore) "
            "of a consumer's creditworthiness, derived from payment history, credit utilization, account "
            "age, credit mix, and recent inquiries. Lenders use scores to assess default risk and "
            "determine interest rates."
        ),
    },
    {
        "term": "Liquidity",
        "emoji": "💧",
        "category": "Banking",
        "simple": (
            "Cash in your wallet = super liquid — grab it and buy boba instantly. Money locked in a "
            "6-month savings bond? Not liquid — you can't touch it without penalties. Liquidity is "
            "how fast you can turn something into spendable cash without losing value."
        ),
        "pro": (
            "Liquidity refers to the ease and speed with which an asset can be converted into cash "
            "without significantly affecting its market price. Highly liquid assets include cash and "
            "checking accounts; illiquid assets include real estate, private equity, and long-term "
            "certificates of deposit."
        ),
    },
    {
        "term": "Index Funds",
        "emoji": "🎯",
        "category": "Banking",
        "simple": (
            "Instead of betting on one company's stock (risky!), an index fund buys a slice of "
            "hundreds of companies at once — like getting the whole playlist instead of one song. "
            "Boring? Maybe. But historically, it's one of the smartest long-term moves young "
            "investors can make."
        ),
        "pro": (
            "An index fund is a passively managed mutual fund or ETF designed to replicate the "
            "performance of a market index (e.g., S&P 500, FTSE 100, Nikkei 225) by holding constituent "
            "securities in proportional weights. Index funds offer broad diversification, low expense "
            "ratios, and historically competitive returns relative to active management."
        ),
    },
]


# ---------------------------------------------------------------------------
# AI Coach — currency-aware rule-based advisory engine
# ---------------------------------------------------------------------------

def generate_coach_advice(
    age: int,
    amount: float,
    frequency: str,
    currency_code: str,
) -> dict:
    """
    Rule-based coach that cross-references age, allowance, AND currency scale.
    Thresholds and examples adapt to local purchasing power (JPY vs GBP, etc.).
    """
    meta = get_currency_meta(currency_code)
    weekly = weekly_equivalent(amount, frequency)
    income_tier = classify_income_tier(weekly, currency_code)
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
    micro = meta["micro_save"]
    yearly_save = save_amt * 52

    rules = [
        f"Save **{fmt_money(save_amt, currency_code)}/week** ({save_pct:.0%}) — "
        f"that's **{fmt_money(yearly_save, currency_code)}/year** in your vault.",
        f"Spend **{fmt_money(needs_amt, currency_code)}/week** ({spend_pct:.0%}) on needs: "
        "food, transport, school essentials.",
        f"Keep **{fmt_money(fun_amt, currency_code)}/week** ({fun_pct:.0%}) for fun — "
        "gaming, clothes, hangouts.",
    ]

    # --- Currency-aware tips ---
    tips_by_age = {
        "early_teen": [
            f"Start saving now — even {fmt_money(micro, currency_code)}/week compounds into real money.",
            f"Before buying, wait 48 hours. A {fmt_money(meta['impulse_big'], currency_code)} "
            "impulse buy can wipe your fun budget.",
            "Track every purchase for one week. You'll be shocked where money disappears.",
        ],
        "mid_teen": [
            "Open a teen checking/savings account — learn banking before you need it.",
            f"A side hustle can 2× your income. Even {fmt_money(weekly * 0.5, currency_code)} "
            "extra/week changes the game.",
            f"Never lend money you can't afford to lose — friendships beat "
            f"{fmt_money(meta['snack_cost'] * 2, currency_code)}.",
        ],
        "late_teen": [
            "Start building credit responsibly — authorized user on a parent's card works.",
            "Learn about index funds now; starting at 17 beats starting at 27 by a massive margin.",
            f"Create a 'future fund' — auto-transfer {fmt_money(save_amt, currency_code)} "
            "every allowance day before spending.",
        ],
    }

    tier_tips = {
        "low": (
            f"Every {meta['name']} counts — prioritize needs, hunt student discounts, "
            f"and celebrate saving even {fmt_money(micro, currency_code)} at a time."
        ),
        "medium": (
            f"Your {fmt_money(weekly, currency_code)}/week is a solid baseline — "
            "balance saving with experiences that actually matter to you."
        ),
        "high": (
            f"With {fmt_money(weekly, currency_code)}/week you have real power — "
            "avoid lifestyle creep and lock in aggressive savings first."
        ),
    }

    # --- Currency-scale-aware warnings ---
    warnings = []
    scale_msg = currency_scale_note(currency_code, weekly)

    if fun_amt > weekly * 0.35:
        warnings.append(
            f"Your fun budget ({fmt_money(fun_amt, currency_code)}) is high — "
            f"one {fmt_money(meta['impulse_big'], currency_code)} splurge can wipe the week."
        )
    if weekly < meta["weekly_low"] * 0.6:
        warnings.append(
            f"Tight budget alert: focus on needs first, then micro-savings of "
            f"{fmt_money(micro, currency_code)} at a time."
        )
    if currency_code == "JPY" and amount >= 10000 and frequency == "Weekly":
        warnings.append(
            "Big yen numbers can feel normal — but track percentages, not just the number size."
        )
    if currency_code == "GBP" and weekly >= 80:
        warnings.append(
            f"In pounds, {fmt_money(50, currency_code)} feels small but it's a full day's budget "
            "for many teens — don't let low numbers trick you into overspending."
        )
    if income_tier == "high" and age <= 15:
        warnings.append(
            "Big allowance + young age = easy to overspend. Auto-save BEFORE you touch anything."
        )
    warnings.append("Red flag: spending more than you earn every week (dipping into savings).")
    warnings.append("Red flag: hiding purchases — honesty keeps your money habits on track.")

    greeting = (
        f"Hey! I'm your Money Coach. At **{age}** earning "
        f"**{fmt_money(amount, currency_code)}/{frequency.lower()}** "
        f"(~**{fmt_money(weekly, currency_code)}/week** in **{meta['name']}**), "
        f"here's your personalized game plan:"
    )

    return {
        "greeting": greeting,
        "scale_note": scale_msg,
        "rules": rules,
        "tips": tips_by_age[age_group] + [tier_tips[income_tier]],
        "warnings": warnings,
        "weekly": weekly,
        "save_amt": save_amt,
        "fun_amt": fun_amt,
        "currency_code": currency_code,
        "currency_name": meta["name"],
    }


def process_coach_question(question: str, profile: dict) -> str:
    """
    Placeholder for LLM integration — handles common questions via rules.
    All monetary answers use the user's selected currency formatting.
    """
    q = question.lower().strip()
    code = profile.get("currency_code", st.session_state.currency_code)
    weekly = profile["weekly"]
    meta = get_currency_meta(code)

    if any(w in q for w in ["save", "saving", "savings"]):
        return (
            f"Aim to save at least **{fmt_money(profile['save_amt'], code)}/week** "
            f"(~**{fmt_money(profile['save_amt'] * 52, code)}/year**). "
            "Set up automatic transfers on allowance day so you never 'forget.' "
            "The best savers pay themselves first."
        )
    if any(w in q for w in ["budget", "spend", "spending"]):
        return (
            f"Your weekly fun budget is **{fmt_money(profile['fun_amt'], code)}**. "
            f"A single purchase over **{fmt_money(meta['impulse_big'], code)}** should trigger "
            "a pause. Try the envelope method: once it's gone, it's gone."
        )
    if any(w in q for w in ["invest", "stock", "index"]):
        return (
            "At your age, learning beats earning. Read about index funds (Dictionary tab!), "
            "open a custodial account with a parent, and start with small amounts in your "
            f"local currency. Even {fmt_money(meta['micro_save'] * 4, code)}/month builds the habit."
        )
    if any(w in q for w in ["credit", "card", "debt", "overdraft"]):
        return (
            "Credit cards and overdrafts aren't free money — fees and interest can exceed 20%. "
            f"One overdraft fee can cost more than {fmt_money(meta['snack_cost'] * 3, code)}. "
            "Build credit slowly: one small recurring charge, paid in full every month."
        )
    if any(w in q for w in ["currency", "yen", "pound", "euro", "rupee"]):
        return profile.get("scale_note", currency_scale_note(code, weekly))
    if any(w in q for w in ["job", "work", "earn", "money"]):
        return (
            f"With **{fmt_money(weekly, code)}/week** from allowance, a side gig could change everything. "
            "Tutoring, reselling, freelancing — pick something you enjoy. "
            "Extra income split: 50% save, 30% invest/learn, 20% treat yourself."
        )

    return (
        f"Based on your **{profile.get('currency_name', meta['name'])}** profile "
        f"(~{fmt_money(weekly, code)}/week): save first, spend intentionally, and keep learning. "
        "Try asking about saving, budgeting, investing, credit, or your currency!"
    )


# ---------------------------------------------------------------------------
# Spending monitor logic — percentage-based, currency-agnostic thresholds
# ---------------------------------------------------------------------------

def evaluate_habit(
    expense: float,
    weekly_allowance: float,
    currency_code: str,
) -> tuple[str, str, float]:
    """Return (alert_level, message, percentage) for a single expense."""
    if weekly_allowance <= 0:
        return "red", "Set your allowance in the Coach tab first!", 100.0

    pct = (expense / weekly_allowance) * 100
    meta = get_currency_meta(currency_code)
    expense_fmt = fmt_money(expense, currency_code)

    if pct <= 15:
        return (
            "green",
            f"Safe zone! {expense_fmt} uses only {pct:.0f}% of your weekly budget. Keep it up!",
            pct,
        )
    if pct <= 35:
        return (
            "orange",
            f"Caution — {expense_fmt} ({pct:.0f}% of weekly) is a big hit. "
            f"That's like {fmt_money(meta['impulse_big'], currency_code)}-level spending pressure.",
            pct,
        )
    return (
        "red",
        f"Overspending alert! {expense_fmt} = {pct:.0f}% of your weekly budget in one purchase. Pause and reconsider.",
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
        '<p class="hero-subtitle">Level up your money game worldwide — built for Gen Z, powered by smart habits.</p>',
        unsafe_allow_html=True,
    )


def render_profile_inputs() -> None:
    """Shared profile panel — persists across all tabs via session state."""
    st.markdown("### 👤 Your Profile")
    meta = get_currency_meta()

    row1 = st.columns([1, 1, 1, 1.4])
    with row1[0]:
        st.session_state.age = st.selectbox(
            "Your Age",
            options=list(range(13, 20)),
            index=list(range(13, 20)).index(st.session_state.age)
            if st.session_state.age in range(13, 20)
            else 2,
            key="profile_age_select",
        )
    with row1[1]:
        selected = st.selectbox(
            "Currency",
            options=CURRENCY_OPTIONS,
            index=CURRENCY_OPTIONS.index(CURRENCY_CODE_MAP.get(st.session_state.currency_code, CURRENCY_OPTIONS[0])),
            key="profile_currency_select",
        )
        st.session_state.currency_code = selected.split(" — ")[0]
        meta = get_currency_meta()

    with row1[2]:
        st.session_state.allowance_frequency = st.radio(
            "Allowance Frequency",
            options=["Weekly", "Monthly"],
            index=0 if st.session_state.allowance_frequency == "Weekly" else 1,
            horizontal=True,
            key="profile_frequency_radio",
        )

    with row1[3]:
        st.session_state.allowance_amount = st.number_input(
            f"Allowance Amount ({meta['symbol']})",
            min_value=0.0,
            max_value=float(meta["max_allowance"]),
            value=float(st.session_state.allowance_amount),
            step=float(meta["step"]),
            key="profile_allowance_input",
        )

    if st.session_state.currency_code == "OTHER":
        other1, other2 = st.columns(2)
        with other1:
            st.session_state.custom_currency_symbol = st.text_input(
                "Custom Currency Symbol",
                value=st.session_state.custom_currency_symbol,
                max_chars=6,
                placeholder="e.g. ₩, kr, CHF",
                key="profile_custom_symbol",
            )
        with other2:
            st.session_state.custom_currency_name = st.text_input(
                "Custom Currency Name",
                value=st.session_state.custom_currency_name,
                max_chars=30,
                placeholder="e.g. Won, Krona",
                key="profile_custom_name",
            )


def render_profile_stats() -> None:
    """Dashboard strip showing current profile at a glance."""
    code = st.session_state.currency_code
    meta = get_currency_meta(code)
    weekly = weekly_equivalent(
        st.session_state.allowance_amount,
        st.session_state.allowance_frequency,
    )
    cols = st.columns(5)
    stats = [
        ("Age", f"{st.session_state.age}"),
        ("Currency", f"{code} ({meta['symbol']})"),
        ("Allowance", fmt_money(st.session_state.allowance_amount, code)),
        ("Frequency", st.session_state.allowance_frequency),
        ("Weekly Equiv.", fmt_money(weekly, code)),
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
    st.caption(
        f"Coach adapts to **{get_currency_meta()['name']}** purchasing power — "
        "the same number means different things in yen vs. pounds."
    )

    if st.button("✨ Analyze My Profile", type="primary", use_container_width=True):
        advice = generate_coach_advice(
            st.session_state.age,
            st.session_state.allowance_amount,
            st.session_state.allowance_frequency,
            st.session_state.currency_code,
        )
        st.session_state.coach_messages = [
            {"role": "coach", "text": advice["greeting"]},
            {"role": "coach", "text": f"**🌍 Currency Context:** {advice['scale_note']}"},
            {
                "role": "coach",
                "text": "**Your Spending Rules:**\n" + "\n".join(f"• {r}" for r in advice["rules"]),
            },
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
        st.session_state._coach_profile = advice

    for msg in st.session_state.coach_messages:
        css_class = "coach-bubble user" if msg["role"] == "user" else "coach-bubble"
        st.markdown(f'<div class="{css_class}">{msg["text"]}</div>', unsafe_allow_html=True)

    if st.session_state.profile_analyzed:
        st.markdown("---")
        st.markdown("#### 💬 Ask Your Coach")
        user_q = st.text_input(
            "Type a question (try: saving, budget, currency, investing...)",
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
                    st.session_state.currency_code,
                )
            st.session_state.coach_messages.append({"role": "user", "text": user_q})
            answer = process_coach_question(user_q, profile)
            st.session_state.coach_messages.append({"role": "coach", "text": answer})
            st.rerun()


def render_dictionary_tab() -> None:
    """Feature 2: Banking & Economics Masterclass Dictionary."""
    st.markdown("### 📚 Banking & Economics Masterclass")
    st.markdown(
        "Toggle each term between **teen-friendly analogies** and **pro-level definitions**."
    )

    categories = ["All"] + sorted({t["category"] for t in FINANCIAL_TERMS})
    st.session_state.dict_category_filter = st.pills(
        "Filter by topic",
        options=categories,
        default=st.session_state.dict_category_filter
        if st.session_state.dict_category_filter in categories
        else "All",
        key="dict_category_pills",
    )

    filtered = (
        FINANCIAL_TERMS
        if st.session_state.dict_category_filter == "All"
        else [t for t in FINANCIAL_TERMS if t["category"] == st.session_state.dict_category_filter]
    )

    for i, term in enumerate(filtered):
        badge = f'<span class="category-badge">{term["category"]}</span>'
        with st.expander(f"{term['emoji']} {term['term']}", expanded=False):
            st.markdown(badge, unsafe_allow_html=True)
            view_mode = st.toggle(
                "Show Pro Definition",
                value=False,
                key=f"term_toggle_{term['term']}",
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
    code = st.session_state.currency_code
    meta = get_currency_meta(code)
    st.markdown("### 📊 Live Spending & Habit Monitor")

    weekly = weekly_equivalent(
        st.session_state.allowance_amount,
        st.session_state.allowance_frequency,
    )

    total_spent = total_spent_this_period(st.session_state.expense_log)
    remaining = max(weekly - total_spent, 0)
    used_pct = min((total_spent / weekly * 100) if weekly > 0 else 0, 100)

    prog_col1, prog_col2, prog_col3 = st.columns(3)
    prog_col1.metric("Weekly Budget", fmt_money(weekly, code))
    prog_col2.metric("Total Logged", fmt_money(total_spent, code))
    prog_col3.metric("Remaining", fmt_money(remaining, code))

    st.progress(used_pct / 100 if used_pct else 0)
    st.caption(f"You've used **{used_pct:.0f}%** of your weekly allowance so far.")

    st.markdown("---")
    st.markdown("#### Log an Expense")

    exp_col1, exp_col2 = st.columns([2, 1])
    with exp_col1:
        st.session_state.expense_name = st.text_input(
            "What did you buy?",
            value=st.session_state.expense_name,
            placeholder="e.g., Bubble tea, game credits, bus pass",
            key="expense_name_input",
        )
    with exp_col2:
        st.session_state.expense_amount = st.number_input(
            f"Amount ({meta['symbol']})",
            min_value=0.0,
            max_value=float(meta["max_expense"]),
            value=float(st.session_state.expense_amount),
            step=float(meta["step"]) if meta["step"] <= 10 else float(meta["step"]) / 10,
            key="expense_amount_input",
        )

    if st.button("➕ Log Expense", type="primary", use_container_width=True):
        if st.session_state.expense_amount > 0:
            level, message, pct = evaluate_habit(
                st.session_state.expense_amount,
                weekly,
                code,
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
            st.warning(f"Enter an amount greater than {fmt_money(0, code)}.")

    if "_last_habit" in st.session_state:
        h = st.session_state._last_habit
        css = f"habit-{h['level']}"
        st.markdown(
            f'<div class="habit-alert {css}">{h["message"]}</div>',
            unsafe_allow_html=True,
        )

    if st.session_state.expense_log:
        st.markdown("---")
        st.markdown("#### 📋 Today's Log")
        for entry in reversed(st.session_state.expense_log):
            icon = {"green": "🟢", "orange": "🟠", "red": "🔴"}.get(entry["level"], "⚪")
            st.markdown(
                f"{icon} **{entry['name']}** — {fmt_money(entry['amount'], code)} "
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
    render_profile_inputs()
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
