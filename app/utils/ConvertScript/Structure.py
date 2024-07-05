from app.utils.ConvertScript.Node_Structures.AutomatedTest import generate_automated_test_structure
from app.utils.ConvertScript.Node_Structures.BackendIntegrationTest import generate_backend_integration_test_structure
from app.utils.ConvertScript.Node_Structures.BackendUnitTest import generate_backend_unit_test_structure
from app.utils.ConvertScript.Node_Structures.BddTest import generate_bdd_test_structure
from app.utils.ConvertScript.Node_Structures.CodeQualityChecks import generate_code_quality_checks_structure
from app.utils.ConvertScript.Node_Structures.ExecutionDetails import generate_execution_details_structure
from app.utils.ConvertScript.Node_Structures.FrontendIntegrationTest import generate_frontend_integration_test_structure
from app.utils.ConvertScript.Node_Structures.FrontendUnitTest import generate_frontend_unit_test_structure
from app.utils.ConvertScript.Node_Structures.IntegrationTest import generate_integration_test_structure
from app.utils.ConvertScript.Node_Structures.ManualStep import generate_manual_step_structure
from app.utils.ConvertScript.Node_Structures.ManualTest import generate_manual_test_structure
from app.utils.ConvertScript.Node_Structures.Note import generate_note_structure
from app.utils.ConvertScript.Node_Structures.PerformanceTest import generate_performance_test_structure
from app.utils.ConvertScript.Node_Structures.SecurityTest import generate_security_test_structure
from app.utils.ConvertScript.Node_Structures.TestEnvironment import generate_test_environment_structure
from app.utils.ConvertScript.Node_Structures.TestPhase import generate_test_phase_structure
from app.utils.ConvertScript.Node_Structures.TestPlan import generate_test_plan_structure 
from app.utils.ConvertScript.Node_Structures.TestStrategy import generate_test_strategy_structure
from app.utils.ConvertScript.Node_Structures.TestSuite import generate_test_suite_structure
from app.utils.ConvertScript.Node_Structures.ThirdPartyChecksTest import generate_third_party_checks_test_structure
from app.utils.ConvertScript.Node_Structures.UIInteraction import generate_ui_interaction_structure
from app.utils.ConvertScript.Node_Structures.UnitTest import generate_unit_test_structure

def generate_node_structure(node):
    if node["node_type"] == "AutomatedTestCaseNode":
        return generate_automated_test_structure(node["node_id"])
    elif node["node_type"] == "BackEndIntegrationTestNode":
        return generate_backend_integration_test_structure(node["node_id"])
    elif node["node_type"] == "BackendUnitTestNode":
        return generate_backend_unit_test_structure(node["node_id"])
    elif node["node_type"] == "BDDTestCaseNode":
        return generate_bdd_test_structure(node["node_id"])
    elif node["node_type"] == "CodeQualityChecksNode":
        return generate_code_quality_checks_structure(node["node_id"])
    elif node["node_type"] == "ExecutionDetailsNode":
        return generate_execution_details_structure(node["node_id"])
    elif node["node_type"] == "FrontEndIntegrationTestNode":
        return generate_frontend_integration_test_structure(node["node_id"])
    elif node["node_type"] == "FrontEndUnitTestNode":
        return generate_frontend_unit_test_structure(node["node_id"])
    elif node["node_type"] == "IntegrationTestNode":
        return generate_integration_test_structure(node["node_id"])
    elif node["node_type"] == "TestStepNode":
        return generate_manual_step_structure(node["node_id"])
    elif node["node_type"] == "ManualTestCaseNode":
        return generate_manual_test_structure(node["node_id"])
    elif node["node_type"] == "StickyNote":
        return generate_note_structure(node["node_id"])
    elif node["node_type"] == "PerformanceTestNode":
        return generate_performance_test_structure(node["node_id"])
    elif node["node_type"] == "SecurityTestNode":
        return generate_security_test_structure(node["node_id"])
    elif node["node_type"] == "TestEnvironmentNode":
        return generate_test_environment_structure(node["node_id"])
    elif node["node_type"] == "TestingPhaseNode":
        return generate_test_phase_structure(node["node_id"])
    elif node["node_type"] == "TestPlanNode":
        return generate_test_plan_structure(node["node_id"])
    elif node["node_type"] == "TestStrategyNode":
        return generate_test_strategy_structure(node["node_id"])
    elif node["node_type"] == "TestSuiteNode":
        return generate_test_suite_structure(node["node_id"])
    elif node["node_type"] == "ThirdPartyChecksTestNode":
        return generate_third_party_checks_test_structure(node["node_id"])
    elif node["node_type"] == "UIInteractionNode":
        return generate_ui_interaction_structure(node["node_id"])
    elif node["node_type"] == "UnitTestNode":
        return generate_unit_test_structure(node["node_id"])
    else:  
        return {"error": "Unknown node type"}
    
def generate_source_handle(node):
    source_handle = generate_node_structure(node)["data"]["outputAnchors"][0]["id"]
    return source_handle

def generate_target_handle(node):
    target_handle = generate_node_structure(node)["data"]["inputAnchors"][0]["id"]
    return target_handle

def generate_edge_structure(source_node, target_node):
    edge = {
        "source": source_node["node_id"],
        "sourceHandle": generate_source_handle(source_node),
        "target": target_node["node_id"],
        "targetHandle": generate_target_handle(target_node),
        "type": "buttonedge",
        "id": f"{generate_source_handle(source_node)}-{generate_target_handle(target_node)}",
    }
    return edge