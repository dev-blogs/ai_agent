from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("time-server")

@mcp.tool()
def get_current_time() -> str:
    """Returns current UTC time."""
    return datetime.utcnow().isoformat()

if __name__ == "__main__":
    mcp.run()