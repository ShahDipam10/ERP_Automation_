import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from utilities.read_properties import ReadConfig
from test_cases.conftest import setup
from test_cases.login_manager import LoginManager
from utilities.custom_logger import LogGen
from page_objects.create_task_page import CreateTask
from page_objects.login_page import HubLogin
from page_objects.board_view_page import BoardView

@pytest.mark.usefixtures("setup")
class TestBoardView:
    """Test case of performing action in Board View will be here."""

    # Read configuration details such as base URL and user credentials
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    # Initialize logger
    logger = LogGen.loggen()

    def test_dragndrop_task_by_status(self, setup):
        """Automated test case to create a new task and change its status in Board view to change status."""
        try:
            self.logger.info("-------- Test Case: Board View -----------")
            self.logger.info("--------- Logging into website ----------")

            # Initialize WebDriver
            self.driver = setup
            login_manager = LoginManager(self.driver)

            # Perform login operation
            login_manager.login()

            # Initialize page objects
            self.hub_login = HubLogin(self.driver)
            self.ct = CreateTask(self.driver)
            self.bv = BoardView(self.driver)

            # Navigate to the project page
            self.ct.project_page_link()
            self.logger.info("****** Navigated to Project Page ******")

            #Navigate to Board View
            self.bv.click_on_boardview_btn()
            self.logger.info("****** Navigated to Board View ******")

            #drag first element to the given status
            # Choose from 'todo', 'in progress', 'in review' , 'backlog', 'done' , or 'complete'
            #pass source and target elements
            self.bv.dragndrop_by_status("in progress", "in review")
            self.logger.info("--------- Drag first element of TODO to given status area ----------")
            print("Test case Passed.")

        except Exception as e:
            # Log and fail the test if an unexpected error occurs
            self.logger.error(f"Unexpected error: {e}")
            pytest.fail(f"Test failed due to unexpected error: {e}")

        finally:
            # Close the browser session
            self.driver.close()
            self.logger.info("Browser closed.")


    def test_dragndrop_task_by_priority(self, setup):
        """Automated test case to create a new task and change its priority in Board view to change status."""
        try:
            self.logger.info("-------- Test Case: Board View -----------")
            self.logger.info("--------- Logging into website ----------")

            # Initialize WebDriver
            self.driver = setup
            login_manager = LoginManager(self.driver)

            # Perform login operation
            login_manager.login()

            # Initialize page objects
            self.hub_login = HubLogin(self.driver)
            self.ct = CreateTask(self.driver)
            self.bv = BoardView(self.driver)

            # Navigate to the project page
            self.ct.project_page_link()
            self.logger.info("****** Navigated to Project Page ******")

            #Navigate to Board View
            self.bv.click_on_boardview_btn()
            self.logger.info("****** Navigated to Board View ******")

            #navigate to priority based board
            self.bv.change_groupby_priority()

            # drag first element to the given priority
            # Choose from 'high', 'medium', 'low'
            # pass source and target elements
            self.bv.dragndrop_by_priority("medium", "high")
            self.logger.info("--------- Drag first element to given priority area ----------")
            print("Test case Passed.")

        except Exception as e:
            # Log and fail the test if an unexpected error occurs
            self.logger.error(f"Unexpected error: {e}")
            pytest.fail(f"Test failed due to unexpected error: {e}")

        finally:
            # Close the browser session
            self.driver.close()
            self.logger.info("Browser closed.")