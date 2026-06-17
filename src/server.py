import mcp.server.stdio
from mcp.server import Server
from src.tools.data_scrubber import scrub_data_tool
from src.tools.policy_matcher import evaluate_policy_tool

server = Server("localai-data-gateway")

@server.list_tools()
async def handle_list_tools():
    return [
        {
            "name": "scrub_and_validate",
            "description": "Validates big data file freshness, structural schema, and redacts PII locally.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "file_path": {"type": "string"},
                    "schema_type": {"type": "string"}
                },
                "required": ["file_path"]
            }
        },
        {
            "name": "evaluate_policy_eligibility",
            "description": "Applies the ReliefAI hybrid matching logic to compute eligibility matrices safely.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "criteria": {"type": "object"},
                    "resource_type": {"type": "string"}
                },
                "required": ["criteria", "resource_type"]
            }
        }
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict):
    if name == "scrub_and_validate":
        return await scrub_data_tool(arguments)
    elif name == "evaluate_policy_eligibility":
        return await evaluate_policy_tool(arguments)
    raise ValueError(f"Unknown tool requested: {name}")

def run_server():
    mcp.server.stdio.start_server(server)
