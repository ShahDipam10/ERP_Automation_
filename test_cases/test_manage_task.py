import sys
import os
import pytest
from page_objects.create_task_page import CreateTask
from utilities.read_properties import ReadConfig
from test_cases.conftest import setup
from utilities.custom_logger import LogGen
from test_cases.login_manager import LoginManager

# Add the project root to the system path to resolve module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.usefixtures("setup")
class TestTaskManager:
    """Manages Task functionalities"""
    # Read configuration details such as base URL and user credentials
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    #Initialize logger
    logger = LogGen.loggen()

    def test_delete_task(self,setup):
        try:
            self.logger.info("--------- Delete Task ----------")

            self.logger.info("--------- Logging into website ----------")
            # Initialize WebDriver
            self.driver = setup
            login_manager = LoginManager(self.driver)
            #perform login operation
            login_manager.login()

            #initialize page objects
            self.ct = CreateTask(self.driver)

            # Navigate to the project page
            self.ct.project_page_link()
            self.logger.info("****** Navigated to Project Page ******")

            #deleting task
            self.ct.delete_task()
            self.logger.info("--------- Task Deleted successfully ----------")

        except Exception as e:
            # Log and fail the test if an unexpected error occurs
            self.logger.error(f"Unexpected error: {e}")
            pytest.fail(f"Test failed due to unexpected error: {e}")

    def test_archive_test(self,setup):
        try:
            self.logger.info("--------- Delete Task ----------")

            self.logger.info("--------- Logging into website ----------")
            # Initialize WebDriver
            self.driver = setup
            login_manager = LoginManager(self.driver)
            # perform login operation
            login_manager.login()

            # initialize page objects
            self.ct = CreateTask(self.driver)

            # Navigate to the project page
            self.ct.project_page_link()
            self.logger.info("****** Navigated to Project Page ******")

            #archive task
            self.ct.archive_task()
            self.logger.info("--------- Task Archived successfully ----------")

            self.ct.show_archived_task()
            self.logger.info("--------- printed number of archived elements ----------")


        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            pytest.fail(f"Test failed due to unexpected error: {e}")



