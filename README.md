# conviction-mcp

A Model Context Protocol (MCP) server that acts as your **Personal CIO Agent** — aggregating broker positions, syncing paid financial blogger content, and analyzing alignment with your investment philosophy.

## What it does

Ask your agent natural questions:

> "How do my current positions compare to my target allocation?"
> "Does my portfolio align with what the blogger has been saying this week?"
> "Am I overweight tech in my conservative account?"

The MCP server fetches your positions and blogger content, then your agent analyzes everything against your stated investment philosophy and risk profile.

## Features (Phase 1 — in progress)

- **Screenshot OCR position sync** — parse a broker screenshot to extract your positions (any broker)
- **Zsxq content scraping** — scrape paid financial blogger content using your session cookie
- **Investment philosophy checks** — validates positions against your target allocation, position sizing rules, and sector limits per account
- **Strategy alignment** — compares blogger opinions with your actual holdings
- **Classic framework analysis** — Kelly Criterion, 60/40, max drawdown, concentration rules
- **Market data** — yfinance (free, built-in)

## What you need to bring (BYOC)

| Credential | Required | Purpose |
|------------|----------|---------|
| LLM API key (Anthropic or OpenAI) | Yes | Analysis engine |
| Zsxq session cookie | Yes | Scrape blogger content |
| SnapTrade account | Optional | Auto-sync broker positions |
| moomoo / Tiger / IBKR / Polygon / Finnhub | Optional | Richer market data |

No account passwords are stored or passed to any agent.

## Installation

**Requirements:** Python 3.11+, `uv` or `pip`

```bash
git clone https://github.com/hjiangcpp/conviction-mcp.git
cd conviction-mcp

# install dependencies
uv sync

# install Playwright browser
playwright install chromium

# set up config
cp config.example.yaml data/config.yaml
# edit data/config.yaml with your credentials
```

## Configuration

See [config.example.yaml](config.example.yaml) for the full reference.

Minimum config for Phase 1:

```yaml
zsxq:
  cookie: "your-session-cookie"
  group_ids: ["your-group-id"]

ai:
  provider: "anthropic"
  api_key: "sk-ant-..."

accounts:
  - broker: "Schwab"
    style: "conservative"
    target_allocation:
      equity: 50
      bond: 40
      cash: 10
```

## Add to your agent

### Claude Code

```json
{
  "mcpServers": {
    "portfolio": {
      "command": "uv",
      "args": ["run", "python", "-m", "conviction_mcp.server"],
      "cwd": "/path/to/conviction-mcp"
    }
  }
}
```

### Cursor / Windsurf

Same config format — refer to your agent's MCP documentation.

## Available tools

| Tool | Description |
|------|-------------|
| `sync_portfolio` | Sync positions via SnapTrade or parse a broker screenshot |
| `sync_zsxq` | Scrape latest posts from a Zsxq group |
| `analyze` | Analyze position alignment with your investment philosophy and blogger opinions |

## Security

- Credentials live in `data/config.yaml` — never committed (gitignored)
- No automated trading, ever
- Zsxq scraping is rate-limited (1 page / 5s) and only accesses content you have paid access to
- Broker positions are read-only via OAuth

## Roadmap

- [ ] Phase 1 — On-demand query: screenshot OCR + Zsxq cookie + conversational analysis
- [ ] Phase 2 — Automation: SnapTrade sync, scheduled Zsxq scraping, richer market data
- [ ] Phase 3 — SaaS wrapper: web UI, auth, database

## License

MIT
