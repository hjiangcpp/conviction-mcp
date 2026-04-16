"""Parse broker screenshots into structured position data using LLM vision."""

from pathlib import Path
from conviction_mcp.utils.config import load_config


async def parse_screenshot(image_path: str) -> dict:
    """
    Send a broker screenshot to the LLM vision model and extract positions.

    Returns portfolio.json-compatible structure:
    {
        "date": "...",
        "accounts": [{"broker": "...", "positions": [...]}]
    }
    """
    config = load_config()
    provider = config["ai"]["provider"]
    api_key = config["ai"]["api_key"]

    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Screenshot not found: {image_path}")

    # TODO: implement vision API call (Anthropic or OpenAI)
    raise NotImplementedError("Screenshot OCR not yet implemented.")
