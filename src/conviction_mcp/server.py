"""MCP server entry point."""

import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server

from conviction_mcp.tools.portfolio import sync_portfolio
from conviction_mcp.tools.zsxq import sync_zsxq
from conviction_mcp.tools.analyze import analyze

app = Server("conviction-mcp")

app.add_tool(sync_portfolio)
app.add_tool(sync_zsxq)
app.add_tool(analyze)


async def _main():
    async with stdio_server() as (read, write):
        await app.run(read, write, app.create_initialization_options())


def main():
    asyncio.run(_main())


if __name__ == "__main__":
    main()
