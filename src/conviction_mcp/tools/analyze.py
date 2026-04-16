"""analyze tool — check position alignment with investment philosophy and blogger opinions."""

from conviction_mcp.utils.config import load_config


async def analyze(portfolio: dict, posts: list[dict]) -> str:
    """
    Analyze current positions against the user's investment philosophy and blogger opinions.

    Checks:
    - Actual allocation vs target allocation per account style
    - Position sizing rule violations (max single position, max sector exposure)
    - Strategy alignment: blogger signals vs current holdings
    - Rebalancing suggestions

    Uses classic frameworks (Kelly Criterion, 60/40, concentration limits) from
    the LLM's built-in knowledge — no external knowledge base required.

    Args:
        portfolio: Structured portfolio data (from sync_portfolio).
        posts: Recent blogger posts (from sync_zsxq).

    Returns:
        Conversational analysis with alignment gaps and rebalancing suggestions.
    """
    config = load_config()
    accounts = config.get("accounts", [])
    investment_profile = config.get("investment_profile", {})

    # TODO: call LLM with portfolio + posts + config as context
    raise NotImplementedError("Analysis not yet implemented.")
