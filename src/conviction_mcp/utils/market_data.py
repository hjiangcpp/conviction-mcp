"""Market data abstraction — yfinance by default, optional upgrades via config."""

from conviction_mcp.utils.config import load_config


def get_price(symbol: str) -> float:
    """Get current price for a symbol. Falls back to yfinance if provider unavailable."""
    config = load_config()
    provider = config.get("market_data", {}).get("provider", "yfinance")

    if provider == "yfinance":
        return _from_yfinance(symbol)
    elif provider == "moomoo":
        return _from_moomoo(symbol, config["market_data"])
    elif provider == "polygon":
        return _from_polygon(symbol, config["market_data"]["polygon_api_key"])
    elif provider == "finnhub":
        return _from_finnhub(symbol, config["market_data"]["finnhub_api_key"])
    else:
        return _from_yfinance(symbol)


def _from_yfinance(symbol: str) -> float:
    import yfinance as yf
    ticker = yf.Ticker(symbol)
    return ticker.fast_info["last_price"]


def _from_moomoo(symbol: str, cfg: dict) -> float:
    # TODO: implement moomoo OpenD client
    raise NotImplementedError("moomoo OpenD not yet implemented.")


def _from_polygon(symbol: str, api_key: str) -> float:
    # TODO: implement Polygon.io client
    raise NotImplementedError("Polygon.io not yet implemented.")


def _from_finnhub(symbol: str, api_key: str) -> float:
    # TODO: implement Finnhub client
    raise NotImplementedError("Finnhub not yet implemented.")
