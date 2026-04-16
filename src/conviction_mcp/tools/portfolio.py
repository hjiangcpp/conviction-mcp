"""sync_portfolio tool — parse broker screenshot or sync via SnapTrade."""

from mcp.server.fastmcp import tool
from conviction_mcp.utils.ocr import parse_screenshot
from conviction_mcp.utils.config import load_config


@tool
async def sync_portfolio(image_path: str | None = None, broker: str | None = None) -> dict:
    """
    Sync broker positions into portfolio.json.

    Phase 1: Pass image_path to parse a broker screenshot via OCR.
    Phase 2: Pass broker name to sync via SnapTrade OAuth.

    Args:
        image_path: Path to a broker screenshot image (Phase 1).
        broker: Broker name for SnapTrade sync — schwab | robinhood (Phase 2).

    Returns:
        Current portfolio as structured JSON.
    """
    # Phase 1: screenshot OCR
    if image_path:
        return await parse_screenshot(image_path)

    # Phase 2: SnapTrade (not yet implemented)
    raise NotImplementedError("SnapTrade sync coming in Phase 2. Please provide image_path.")
