from mcp.server import MCPServer

mcp = MCPServer("AURA IT Tools", instructions="Synthetic enterprise IT tools for AURA")

TICKETS = {
    "1001": {"id":"1001", "requester":"alice", "title":"VPN disconnects", "priority":"P2", "status":"open"},
}

ASSETS = {
    "LT-1001": {"asset_tag":"LT-1001", "owner":"alice", "type":"laptop", "health":94},
    "LT-1002": {"asset_tag":"LT-1002", "owner":"bob", "type":"laptop", "health":72},
}

@mcp.tool()
def get_ticket(ticket_id: str) -> dict:
    """Get a synthetic IT ticket by ID."""
    return TICKETS.get(ticket_id, {"error":"ticket_not_found"})

@mcp.tool()
def create_ticket(requester: str, title: str, description: str, priority: str = "P3") -> dict:
    """Create a synthetic IT ticket."""
    new_id = str(1000 + len(TICKETS) + 1)
    TICKETS[new_id] = {"id":new_id, "requester":requester, "title":title, "description":description, "priority":priority, "status":"open"}
    return TICKETS[new_id]

@mcp.tool()
def get_asset(asset_tag: str) -> dict:
    """Get synthetic asset health information."""
    return ASSETS.get(asset_tag, {"error":"asset_not_found"})

@mcp.tool()
def get_device_health(asset_tag: str) -> dict:
    """Get synthetic health indicators for an endpoint."""
    asset = ASSETS.get(asset_tag)
    if not asset:
        return {"error":"asset_not_found"}
    score = asset["health"]
    return {"asset_tag":asset_tag, "health":score, "signals":{"cpu":41, "memory":58, "disk":63, "restarts":0}}

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=9001)