from app.utils.ConvertScript.Node_Structures.AutomatedTest import reduced_automated_test
from app.utils.ConvertScript.Node_Structures.BackendIntegrationTest import reduced_backend_integration_test
from app.utils.ConvertScript.Node_Structures.BackendUnitTest import reduced_backend_unit_test
from app.utils.ConvertScript.Node_Structures.BddTest import reduced_bdd_test
from app.utils.ConvertScript.Node_Structures.CodeQualityChecks import reduced_code_quality_checks
from app.utils.ConvertScript.Node_Structures.ExecutionDetails import reduced_execution_details
from app.utils.ConvertScript.Node_Structures.FrontendIntegrationTest import reduced_frontend_integration_test
from app.utils.ConvertScript.Node_Structures.FrontendUnitTest import reduced_frontend_unit_test
from app.utils.ConvertScript.Node_Structures.Integration import reduced_integration
from app.utils.ConvertScript.Node_Structures.IntegrationTest import reduced_integration_test
from app.utils.ConvertScript.Node_Structures.ManualStep import reduced_manual_step
from app.utils.ConvertScript.Node_Structures.ManualTest import reduced_manual_test
from app.utils.ConvertScript.Node_Structures.Note import reduced_note
from app.utils.ConvertScript.Node_Structures.PerformanceTest import reduced_performance_test
from app.utils.ConvertScript.Node_Structures.SecurityTest import reduced_security_test
from app.utils.ConvertScript.Node_Structures.TestEnvironment import reduced_test_environment
from app.utils.ConvertScript.Node_Structures.TestPhase import reduced_test_phase
from app.utils.ConvertScript.Node_Structures.TestPlan import reduced_test_plan
from app.utils.ConvertScript.Node_Structures.TestStrategy import reduced_test_strategy
from app.utils.ConvertScript.Node_Structures.TestSuite import reduced_test_suite
from app.utils.ConvertScript.Node_Structures.ThirdPartyChecksTest import reduced_third_party_checks_test_structure
from app.utils.ConvertScript.Node_Structures.UIInteraction import reduced_ui_interaction_structure
from app.utils.ConvertScript.Node_Structures.UnitTest import reduced_unit_test

def edge_destructure(workflow_edges):
    edge_list = []
    for edge in workflow_edges:
        edge_list.append({
            "source": edge["source"],
            "target": edge["target"]
        })
    return edge_list


def destructure(workflow_nodes, workflow_edges):
    deconstructed_workflow = []
    for node in workflow_nodes:
        if node["data"]["type"] == "AutomatedTestCaseNode":
            deconstructed_workflow.append(reduced_automated_test(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "BackendIntegrationTestNode":
            deconstructed_workflow.append(reduced_backend_integration_test(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "BackendUnitTestNode":
            deconstructed_workflow.append(reduced_backend_unit_test(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "BDDTestCaseNode":
            deconstructed_workflow.append(reduced_bdd_test(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "CodeQualityChecksNode":
            deconstructed_workflow.append(reduced_code_quality_checks(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "ExecutionDetailsNode":
            deconstructed_workflow.append(reduced_execution_details(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "FrontEndIntegrationTestNode":
            deconstructed_workflow.append(reduced_frontend_integration_test(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "FrontEndUnitTestNode":
            deconstructed_workflow.append(reduced_frontend_unit_test(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "IntegrationNode":
            deconstructed_workflow.append(reduced_integration(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "IntegrationTestNode":
            deconstructed_workflow.append(reduced_integration_test(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "TestStepNode":
            deconstructed_workflow.append(reduced_manual_step(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "ManualTestCaseNode":
            deconstructed_workflow.append(reduced_manual_test(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "StickyNote":
            deconstructed_workflow.append(reduced_note(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "PerformanceTestNode":
            deconstructed_workflow.append(reduced_performance_test(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "SecurityTestNode":
            deconstructed_workflow.append(reduced_security_test(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "TestEnvironmentNode":
            deconstructed_workflow.append(reduced_test_environment(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "TestingPhaseNode":
            deconstructed_workflow.append(reduced_test_phase(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "TestPlanNode":
            deconstructed_workflow.append(reduced_test_plan(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "TestStrategyNode":
            deconstructed_workflow.append(reduced_test_strategy(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "TestSuiteNode":
            deconstructed_workflow.append(reduced_test_suite(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "ThridPartyChecksNode":
            deconstructed_workflow.append(reduced_third_party_checks_test_structure(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "UIInteractionNode":
            deconstructed_workflow.append(reduced_ui_interaction_structure(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        elif node["data"]["type"] == "UnitTestNode":
            deconstructed_workflow.append(reduced_unit_test(node["data"]["id"], node["data"]["inputs"], workflow_edges))
        else:
            return "Error: One or more node types were not found"
    return deconstructed_workflow