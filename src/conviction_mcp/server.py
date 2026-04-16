"""MCP server entry point."""

from mcp.server.fastmcp import FastMCP

from conviction_mcp.tools.portfolio import sync_portfolio
from conviction_mcp.tools.zsxq import sync_zsxq
from conviction_mcp.tools.analyze import analyze

app = FastMCP("conviction-mcp")

app.add_tool(sync_portfolio)
app.add_tool(sync_zsxq)
app.add_tool(analyze)


def main():
    app.run()


if __name__ == "__main__":
    main()
