"""sync_zsxq tool — scrape paid content from a Zsxq group."""

from mcp.server.fastmcp import tool
from conviction_mcp.utils.config import load_config


@tool
async def sync_zsxq(group_id: str | None = None, limit: int = 20) -> list[dict]:
    """
    Scrape the latest posts from a Zsxq group using the session cookie in config.yaml.

    Rate-limited to 1 page per 5 seconds to avoid triggering platform defenses.
    Only accesses content you have paid access to.

    Args:
        group_id: Zsxq group ID to scrape. Defaults to first group in config.
        limit: Maximum number of posts to return (default 20).

    Returns:
        List of structured posts with date, content, summary, signal, tags.
    """
    config = load_config()
    cookie = config["zsxq"]["cookie"]
    target_group = group_id or config["zsxq"]["group_ids"][0]

    # TODO: implement Playwright scraping
    raise NotImplementedError("Zsxq scraping not yet implemented.")
