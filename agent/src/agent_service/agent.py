from google.adk import Agent
from google.adk.models import Gemini
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams

INSTRACTIONS = """
You are a helpful assistant
"""

def create_agent():
    mcp_toolset = MCPToolset(
        connection_params=SseConnectionParams(
            url="http://<MCP_SERVER_IP>:8081/sse"
        )
    )

    return Agent(
        name="my_agent",
        model="gemini-2.5-flash",
        description="Example agent",
        tools=[mcp_toolset],
        instruction="""
You are a helpful assistant.
When user asks about time, call the tool get_current_time.
""",
    )