
# Standard library imports
import sys
import os
import time

# Third-party imports
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Project imports
from page_objects.create_project import CreateProject
from utilities.read_properties import ReadConfig
from test_cases.login_manager import LoginManager
from utilities.custom_logger import LogGen
from page_objects.login_page import HubLogin


@pytest.mark.usefixtures("setup")
class TestProjectFeatures:
    """
    Test suite for Project-related features.
    """
    base_url = ReadConfig.get_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_create_new_project(self, setup):
        """
        Test creating a new project with minimal required fields.
        """
        try:
            self.logger.info("-------- Test Case 001: Create Project -----------")
            self.driver = setup
            wait = WebDriverWait(self.driver, 20)

            # Login
            login_manager = LoginManager(self.driver, wait)
            login_manager.login()

            # Page object initialization
            self.hub_login = HubLogin(self.driver, 10)
            self.cp = CreateProject(self.driver)

            # Navigate and create project
            self.cp.navigate_to_project_page()
            self.logger.info("****** Navigated to Project Page ******")

            self.cp.click_new_project()
            self.logger.info("------------ Clicked on 'New Project' button --------")

            self.cp.select_blank_project()
            self.logger.info("------------ Selected 'Blank Project' option --------")

            self.cp.enter_project_details()
            self.logger.info("------------ Entered project details --------")

            self.cp.select_category()
            self.logger.info("------------ Selected 'In House' category --------")

            self.cp.click_next_until_create_project()
            self.logger.info("------------ Clicked 'Create Project' button --------")

            # Optional: Uncomment to edit or delete the created project
            # self.cp.edit_project()
            # self.logger.info("------------ Edited the created project --------")
            # self.cp.delete_project()
            # self.logger.info("------------ Deleted the created project --------")

        except Exception as exc:
            self.logger.error(f"Unexpected error: {exc}")
            pytest.fail(f"Test failed due to unexpected error: {exc}")

        input("Press Enter to close the browser...")

    def test_create_new_project_with_multiple_fields(self, setup):
        """
        Test creating a new project with multiple fields and options.
        """
        try:
            self.logger.info("-------- Test Case 002: Create Project with multiple fields -----------")
            self.driver = setup
            wait = WebDriverWait(self.driver, 20)

            # Login
            login_manager = LoginManager(self.driver, wait)
            login_manager.login()

            # Page object initialization
            self.hub_login = HubLogin(self.driver, 10)
            self.cp = CreateProject(self.driver)

            # Navigate and create project with more options
            self.cp.navigate_to_project_page()
            self.logger.info("****** Navigated to Project Page ******")

            self.cp.click_new_project()
            self.logger.info("------------ Clicked on 'New Project' button --------")

            self.cp.select_blank_project()
            self.logger.info("------------ Selected 'Blank Project' option --------")

            self.cp.enter_project_details()
            self.logger.info("------------ Entered project details --------")

            self.cp.select_category()
            self.logger.info("------------ Selected 'In House' category --------")

            self.cp.select_due_date(2)
            self.logger.info("------------ Selected due date --------")

            self.cp.click_add_lead()
            self.logger.info("------------ Added lead user --------")

            self.cp.click_next_button_once()
            self.logger.info("------------ Clicked 'Next' to proceed to color selection --------")

            self.cp.select_color()
            self.logger.info("------------ Selected project color --------")

            self.cp.upload_project_image("D:/sf25_LH.jpg")
            self.logger.info("------------ Uploaded project image --------")

            self.cp.click_next_button_once()
            self.logger.info("------------ Clicked 'Next' after uploading image --------")

            self.cp.select_private_project_type()
            self.logger.info("------------ Selected 'Private' project type --------")

            self.cp.click_next_button_once()
            self.logger.info("------------ Clicked 'Next' after selecting project type --------")

            self.cp.click_add_task_type()
            self.logger.info("------------ Clicked the Add Task Type Button --------")

            self.cp.click_add_task_type_link()
            self.logger.info("------------ Clicked sub link to add new task --------")

            self.cp.click_task_type_name()
            self.logger.info("------------ Entered task name --------")

            self.cp.click_upload_button("D:/sf25_LH.jpg", wait_for_save=False)
            self.logger.info("------------ Uploaded task image --------")

            self.cp.click_green_check()
            self.logger.info("------------ Clicked Green Tick --------")

            self.cp.click_task_selection()
            self.logger.info("------------ Selected task to add --------")

            self.cp.click_next_button_once()
            self.logger.info("------------ Clicked 'Next' button --------")

            self.cp.click_status_new_template()
            self.logger.info("------------ Clicked 'New Template' link --------")

            self.cp.click_enter_template_name()
            self.logger.info("------------ Entered random template name --------")

            self.cp.click_next_button_once()
            self.logger.info("------------ Clicked 'Next' button --------")

            self.cp.click_marketing_statuses_for_tasks()
            self.logger.info("------------ Clicked 'Marketing' option --------")

            self.cp.click_next_button_once()
            self.logger.info("------------ Clicked Next Button --------")

            self.cp.click_toggle()
            self.logger.info("------------ Clicked Toggle switch --------")

            self.cp.click_next_button_once()
            self.logger.info("------------ Clicked 'Next' button --------")

            self.cp.click_selected_apps()
            self.logger.info("------------ Selected some apps --------")

            # Optional: Uncomment to test template creation and saving functionality
            # self.cp.click_next_button_once()
            # self.logger.info("------------ Clicked 'Next' button --------")
            # self.cp.click_save_template()
            # self.logger.info("------------ Clicked 'Save Template' button --------")
            # self.cp.upload_template_image("D:/sf25_LH.jpg")
            # self.logger.info("------------ Uploaded project image --------")
            # self.cp.click_template_name()
            # self.logger.info("------------ Entered template name --------")
            # self.cp.click_template_description()
            # self.logger.info("------------ Entered template description --------")
            # self.cp.click_save_continue_button()
            # self.logger.info("------------ Clicked 'Save & Continue' button --------")

            # To reach the project creation step
            self.cp.click_next_until_create_project()
            self.logger.info("------------ Clicked 'Create Project' button --------")

            # Optional: Uncomment to test editing and deleting the project
            # self.cp.edit_project()
            # self.logger.info("------------ Edited the created project --------")
            # self.cp.delete_project()
            # self.logger.info("------------ Deleted the created project --------")

        except Exception as exc:
            self.logger.error(f"Unexpected error: {exc}")
            pytest.fail(f"Test failed due to unexpected error: {exc}")

        input("Press Enter to close the browser...")

    def test_create_new_project_using_custom_template(self, setup):
        """
        Test creating a new project using a saved template.
        """
        try:
            self.logger.info("-------- Test Case 003: Create Project using saved template -----------")
            self.driver = setup
            wait = WebDriverWait(self.driver, 20)

            # Login
            login_manager = LoginManager(self.driver, wait)
            login_manager.login()

            # Page object initialization
            self.hub_login = HubLogin(self.driver, 10)
            self.cp = CreateProject(self.driver)

            # Navigate and use template
            self.cp.navigate_to_project_page()
            self.logger.info("****** Navigated to Project Page ******")

            self.cp.click_new_project()
            self.logger.info("------------ Clicked on 'New Project' button --------")

            self.cp.template_usage()
            self.logger.info("------------ Selected 'Use Template' option --------")

            self.cp.upload_project_image("D:/sf25_LH.jpg")
            self.logger.info("------------ Uploaded project image --------")

            self.cp.pvt_proj()
            self.logger.info("------------ Selected 'Private' project type --------")

        except Exception as exc:
            self.logger.error(f"Unexpected error: {exc}")
            pytest.fail(f"Test failed due to unexpected error: {exc}")

        input("Press Enter to close the browser...")

    def test_modify_project(self, setup):
        """
        Test modifying a project from the project list (e.g., rename).
        """
        try:
            self.logger.info("-------- Test Case 004: Modify Project from Project List -----------")
            self.driver = setup
            wait = WebDriverWait(self.driver, 20)

            # Login
            login_manager = LoginManager(self.driver, wait)
            login_manager.login()

            # Page object initialization
            self.hub_login = HubLogin(self.driver, 10)
            self.cp = CreateProject(self.driver)

            # Navigate and modify project
            self.cp.navigate_to_project_page()
            self.logger.info("****** Navigated to Project Page ******")

            # Optional: Uncomment to test other project modifications
            # self.cp.click_project_popup_cancel()
            # self.logger.info("------------ Clicked on 'Cancel' button in project popup --------")
            # self.cp.click_new_sprint()
            # self.logger.info("------------ Clicked on 'New Sprint' option --------")
            # self.cp.click_create_new_folder()
            # self.logger.info("------------ Clicked on 'Create New Folder' option --------")
            # self.cp.click_rename_field_from_list_view()
            # self.logger.info("------------ Clicked on 'Rename' field from list view --------")
            # self.cp.click_color_avatar_list()
            # self.logger.info("------------ Clicked on 'Color Avatar' from list view --------")
            # self.cp.click_upload_button("D:/Lewishamilton.jpg")
            # self.logger.info("------------ Uploaded task image --------")
            # self.cp.click_close_project()
            # self.logger.info("------------ Closed the project --------")
            # self.cp.click_delete_project_from_list()
            # self.logger.info("------------ Clicked on 'Delete Project' from list view --------")

            self.cp.click_rename_project_by_name()
            self.logger.info("------------ Renamed the project from list view --------")

        except Exception as exc:
            self.logger.error(f"Unexpected error: {exc}")
            pytest.fail(f"Test failed due to unexpected error: {exc}")

        input("Press Enter to close the browser...")