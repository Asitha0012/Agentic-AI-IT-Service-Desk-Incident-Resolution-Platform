import asyncio
from mcp import Client

async def main():
    async with Client("http://127.0.0.1:9001/mcp") as client:
        tools = await client.list_tools()
        print([t.name for t in tools.tools])
        
        result = await client.call_tool("get_asset", {"asset_tag":"LT-1001"})
        print(result)

asyncio.run(main())