import pytest
from _pytest.stash import StashKey
from _pytest.reports import CollectReport
from typing import Dict
from tests.mobile.flows import MobileFlows

# Define a StashKey to store and retrieve reports during the test run
phase_report_key = StashKey[Dict[str, CollectReport]]()


@pytest.fixture
def valid_login_setup(request, report, mobile):
    """Fixture for setting up a valid login scenario"""
    report.info('#######   TEST SETUP: valid_login_setup   #######')
    mobile.click_already_a_member_login()
    report.info(f'#######   START TEST: {request.node.nodeid}   #######')
    yield
    report.info('#######   TEST TEARDOWN: valid_login_setup   #######')
    stash = request.node.stash[phase_report_key]
    # in case of failure during setup phase
    if stash["setup"].failed:
        report.info('#######   TEST TEARDOWN, Reason: setup failed   #######')
        # add teardown flow to bring back to valid initial state
    # in case of failure during test running
    elif ("call" not in stash) or stash["call"].failed:
        report.info('#######   TEST TEARDOWN, Reason: test failed   #######')
        report.info('#######   COLLECTING FAILURE DATA   #######')
        # add teardown flow to bring back to valid initial state
    # in case test passes:
    else:
        MobileFlows(mobile).logout()  # TODO need to add more logic to to logout method for example, logout only if user is logged-in


@pytest.mark.sanity
@pytest.mark.parametrize("email,passw", [("appstest485@gmail.com", "Yeswecan2023"), ("another_email", "another_passw")])
def test_login_invalid_credentials(mobile, login_assertion, email, passw, valid_login_setup):
    """Fixture for setting up an invalid login scenario"""
    MobileFlows(mobile).login(email, passw)
    login_assertion.assert_login_successful()


@pytest.fixture
def invalid_login_setup(request, report, mobile):
    report.info('#######   TEST SETUP: invalid_login_setup   #######')
    mobile.click_already_a_member_login()
    report.info(f'#######   START TEST: {request.node.nodeid}   #######')
    yield
    report.info('#######   TEST TEARDOWN: invalid_login_setup   #######')
    stash = request.node.stash[phase_report_key]
    # in case of failure during setup phase
    if stash["setup"].failed:
        report.info('#######   TEST TEARDOWN, Reason: setup failed   #######')
        # add teardown flow to bring back to valid initial state
    # in case of failure during test running
    elif ("call" not in stash) or stash["call"].failed:
        report.info('#######   TEST TEARDOWN, Reason: test failed   #######')
        report.info('#######   COLLECTING FAILURE DATA   #######')
        # add teardown flow to bring back to valid initial state
    # in case test passes:
    else:
        mobile.approve_failed_login_ok_button()


@pytest.mark.sanity
@pytest.mark.parametrize("email,passw", [("appstest485@gmail.com", "wrong_password"),
                                         ("wrong_email@gmail.com", "Yeswecan2023")])
def test_login_invalid_credentials(mobile, login_assertion, email, passw, invalid_login_setup):
    MobileFlows(mobile).login(email, passw)
    login_assertion.assert_wrong_credentials_popup()