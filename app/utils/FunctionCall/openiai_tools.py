from app.utils.FunctionCall.AutomatedTestJSON import automated_test_json
from app.utils.FunctionCall.BackendIntegrationTestJSON import backend_integration_test_json
from app.utils.FunctionCall.BackendUnitTestJSON import backend_unit_test_json
from app.utils.FunctionCall.BddTestJSON import bdd_test_json
from app.utils.FunctionCall.CodeQualityChecksJSON import code_quality_checks_json
from app.utils.FunctionCall.ExecutionDetailsJSON import execution_details_json
from app.utils.FunctionCall.FrontendIntegrationTestJSON import frontend_integration_test_json
from app.utils.FunctionCall.FrontendUnitTestJSON import frontend_unit_test_json
from app.utils.FunctionCall.IntegrationJSON import integration_json
from app.utils.FunctionCall.IntegrationTestJSON import integration_test_json
from app.utils.FunctionCall.ManualStepJSON import manual_step_json
from app.utils.FunctionCall.ManualTestJSON import manual_test_json
from app.utils.FunctionCall.NoteJSON import note_json
from app.utils.FunctionCall.PerformanceTestJSON import performance_test_json
from app.utils.FunctionCall.SecurityTestJSON import security_test_json
from app.utils.FunctionCall.TestEnvironmentJSON import test_environment_json
from app.utils.FunctionCall.TestPhaseJSON import test_phase_json
from app.utils.FunctionCall.TestPlanJSON import test_plan_json
from app.utils.FunctionCall.TestStrategyJSON import test_strategy_json
from app.utils.FunctionCall.TestSuiteJSON import test_suite_json
from app.utils.FunctionCall.ThirdPartyChecksTestJSON import thrid_party_checks_test_json
from app.utils.FunctionCall.UIInteractionJSON import ui_interactions_json
from app.utils.FunctionCall.UnitTestJSON import unit_test_json


def get_function_call_json():
    tools = [
        automated_test_json(),
        backend_integration_test_json(),
        backend_unit_test_json(),
        bdd_test_json(),
        code_quality_checks_json(),
        execution_details_json(),
        frontend_integration_test_json(),
        frontend_unit_test_json(),
        integration_json(),
        integration_test_json(),
        manual_step_json(),
        manual_test_json(),
        note_json(),
        performance_test_json(),
        security_test_json(),
        test_environment_json(),
        test_phase_json(),
        test_plan_json(),
        test_strategy_json(),
        test_suite_json(),
        thrid_party_checks_test_json(),
        ui_interactions_json(),
        unit_test_json()
    ]
    return tools