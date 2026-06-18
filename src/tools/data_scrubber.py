import os
from src.services.validator import BulkDataValidator
from src.services.freshness import DataFreshnessEngine

async def scrub_data_tool(arguments: dict) -> list:
    file_path = arguments.get("file_path")
    schema_type = arguments.get("schema_type", "generic_finance")
    
    if not os.path.exists(file_path):
        return [{"type": "text", "text": f"Error: Target path {file_path} not found locally."}]
        
    v_res = BulkDataValidator.validate_schema(file_path, schema_type)
    m_time = os.path.getmtime(file_path)
    f_res = DataFreshnessEngine.check_staleness(m_time)
    
    summary = f"Pipeline Execution: {v_res['status']} | Columns Checked: {len(v_res.get('columns', []))} | Fresh: {f_res['is_fresh']}"
    return [{"type": "text", "text": summary}]
