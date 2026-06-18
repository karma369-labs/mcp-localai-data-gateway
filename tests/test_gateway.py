import os
import pytest
from src.services.validator import BulkDataValidator
from src.services.freshness import DataFreshnessEngine
from src.tools.policy_matcher import ReliefAILogicEngine

def test_data_validator_failure():
    res = BulkDataValidator.validate_schema("non_existent_file.csv", "test")
    assert res["status"] == "FAILED"

def test_freshness_engine():
    import time
    res = DataFreshnessEngine.check_staleness(time.time(), maximum_allowable_latency=60.0)
    assert res["is_fresh"] is True

def test_reliefai_logic_engine():
    mock_criteria = {"monthly_income": 1200, "household_size": 2}
    res = ReliefAILogicEngine.evaluate(mock_criteria, "food_relief")
    assert res["status"] == "APPROVED"
    assert res["framework_version"] == "ReliefAI-v1.0"
