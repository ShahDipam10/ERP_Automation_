import sys
import os
import random
import time

import pytest
from page_objects.create_task_page import CreateTask
from page_objects.task_detail_page import TaskDetail
from utilities.read_properties import ReadConfig
from test_cases.conftest import setup
from test_cases.login_manager import LoginManager
from utilities.custom_logger import LogGen
from page_objects.login_page import HubLogin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Add the project root to the system path to resolve module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.mark.usefixtures("setup")
class TestCreateTask001:
    """Test case for creating a new task in the Alian Hub project management system."""

    # Read configuration details such as base URL and user credentials
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    # Initialize logger
    logger = LogGen.loggen()

    def generate_task_name(self):
        """Generate a unique task name using a random number."""
        task_number = random.randint(1, 100)  # Generate a random number between 1 and 100
        return f"Task {task_number}"

    def test_create_new_task(self, setup):
        """Automated test case to create a new task and assign it to a user."""
        try:
            self.logger.info("-------- Test Case 001: Create Task -----------")
            self.logger.info("--------- Logging into website ----------")

            # Initialize WebDriver
            self.driver = setup
            wait = WebDriverWait(self.driver, 20)

            login_manager = LoginManager(self.driver, wait)
            # Perform login operation
            self.hub_login = HubLogin(self.driver, 10)
            login_manager.login()

            # Initialize page objects
            self.ct = CreateTask(self.driver)

            # Navigate to the project page
            self.ct.project_page_link()
            self.logger.info("****** Navigated to Project Page ******")

            # Generate a random task name for uniqueness
            task_name = self.generate_task_name()
            self.logger.info(f"Generated Task Name: {task_name}")

            # Create a new task by setting task type, task name
            self.ct.click_new_task_btn()
                #task type----------------- Copy this to set task type ✔
            task_type = "task"  # Change this to "task" or "subtask" or "bug" as needed
            self.ct.set_task_type(task_type)
            self.logger.info(f"Task Type Set to: {task_type}")  #--------------
            self.ct.set_task_name(task_name) #set taskname
            self.ct.save_task()
            self.logger.info("------------ Task Created --------")

            # Select an assignee from the user list
            self.ct.select_assignee()
            self.logger.info("-------------- Task Assigned Successfully ------------------")

            # Validate that the page title is as expected
            self.act_title = self.driver.title
            if self.act_title == "Alian Hub | Projects":
                self.logger.info("---------- Title Matched ----------")
                print("Page Title Matched")
            else:
                self.logger.info("--------- Title Not Matched ----------")
                print("Page Title Not Matched")

            # Print the generated task name for reference
            print(f"Task Name: {task_name}")

            # #Priority set : high , medium or low
            # priority_type = "high"
            # self.ct.set_task_priority(priority_type)
            # self.logger.info(f"Priority set to: {priority_type}")

            # Retrieve and print the latest task key
            self.logger.info("--------- Getting latest TaskKey ---------------")
            self.ct.get_task_key()

        except Exception as e:
            # Log and fail the test if an unexpected error occurs
            self.logger.error(f"Unexpected error: {e}")
            pytest.fail(f"Test failed due to unexpected error: {e}")

        finally:
            # Close the browser session
            self.driver.close()
            self.logger.info("Browser closed.")

    def test_edit_task_details(self, setup):
        """Automated test case to edit the task details"""
        try:
            self.logger.info("-------- Test Case 002: Edit Task Details -----------")
            self.logger.info("--------- Logging into website ----------")

            # Initialize WebDriver
            self.driver = setup
            wait = WebDriverWait(self.driver, 20)

            login_manager = LoginManager(self.driver, wait)

            # Perform login operation
            self.hub_login = HubLogin(self.driver, 10)
            login_manager.login()

            # Initialize page objects
            self.ct = CreateTask(self.driver)
            self.td = TaskDetail(self.driver)

            # Navigate to the project page
            self.ct.project_page_link()
            self.logger.info("****** Navigated to Project Page ******")

            # Clicking on created task
            self.td.click_task()
            self.logger.info("--------- On Task Detail Page ----------")

            #Creating and adding tag
            self.td.copy_task_name()
            self.td.add_tag()
            self.logger.info("--------- Tag added on task ----------")

            #Adding description
            self.td.add_description()
            self.logger.info("--------- Description added to task ----------")

            # Generate a random task name for uniqueness
            subtask_name = self.generate_task_name()
            self.logger.info(f"Generated SubTask Name: {subtask_name}")

            # #Create subtask and fetch the key
            # self.td.clickon_add_subtask()
            # task_type = "bug"  # Change this to "task" or "subtask" or "bug" as needed
            # self.ct.set_task_type(task_type)
            # self.ct.set_task_name(subtask_name)  # set subtask name
            # self.ct.save_task()
            # self.td.fetch_subtast_key()
            # print(f"SubTask Name: {subtask_name}")
            # self.logger.info("------------ SubTask Created --------")
            #
            # #changing subtask status
            # status_name = "backlog"
            # self.td.set_subtask_status(status_name)
            # print(f"Subtask status changed to: {status_name}")
            # self.logger.info("------------ SubTask Status changed --------")

            # Create subtask and fetch the key
            self.td.clickon_add_subtask()
            task_type = "bug"  # Change this to "task" or "subtask" or "bug" as needed
            self.ct.set_task_type(task_type)
            self.ct.set_task_name(subtask_name)  # set subtask name
            self.ct.save_task()
            self.td.fetch_subtast_key()
            print(f"SubTask Name: {subtask_name}")
            self.logger.info("------------ SubTask Created --------")

            # changing subtask status
            status_name = "backlog"
            self.td.set_subtask_status(status_name)
            print(f"Subtask status changed to: {status_name}")
            self.logger.info("------------ SubTask Status changed --------")

            #Creating Custom Field
            # Before creating custom field, wait for toast to disappear
            try:
                wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "v-toast__text")))
            except Exception:
                pass  # If not present, continue

            self.td.create_custom_field("text")  # text, date, number,text area, phone number
            self.td.create_custom_field("date")
            self.td.create_custom_field("number")
            self.td.create_custom_field("phone number")
            self.td.create_custom_field("text area")
            self.td.create_custom_field("money")
            self.td.create_custom_field("email")
            self.td.create_custom_field("checkbox")

            #here pass the value in string format to choose from predefined options for dropdown menu
            #  For predefined --> Choose from 'none','gender','days','months','time zone','country'
            #To add custom options for dropdown , pass list of options (list format)
            self.td.create_custom_field("dropdown",['QA','Dev','UI'])

            #Creating checklist and check an item
            self.td.create_checklist("Test")
            # After creating checklist, wait for overlays/toasts to disappear
            # try:
            #     wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "v-toast__text")))
            # except Exception:
            #     pass

            self.td.check_checklist_item()

            # self.td.create_checklist("Test")
            self.logger.info("------------ Checklist Item Checked --------")

            #Uploading a file
            file_path = "C:/Users/Alian-172/Desktop/Hub Alian/sf25_LH.jpg"
            self.td.upload_file(file_path)

            #Changing task status
            task_status = "in progress" # Choose from 'todo', 'in progress', 'in review' , 'backlog', 'done' , or 'complete'.
            # task_status = "in progress"
            self.td.set_task_status(task_status)
            print(f"Task Status changed to: {task_status}")
            self.logger.info("------------ Task Status changed --------")

            #Assigning Start and Due date to task
            self.td.select_start_date() #Select today's date
            self.td.select_due_date(15) #Select a due date 15 days ahead
            print("Task Date Set")
            self.logger.info("------------ Date Set --------")

            #Setting Estimated Time for task
            # self.td.set_estimated_time("00:30") #here enter the time in hh:mm format

            #navigate to comments section and send a message
            chat_message = "Tested and Bug added"
            self.td.navigate_to_comments()
            self.td.sending_message_in_comment_section(chat_message)
            print("Messaged in Comment Section>>>")
            self.logger.info("------------ Comment Section: Messaged in chat --------")

            #navigate back to task detail
            self.td.navigate_to_task_detail()

            #navigate to last created subtask and perform same actions as on task>>>
            self.td.navigate_to_last_created_subtask()
            self.td.copy_task_name()
            self.td.add_tag()
            print("Tag added to Subtask")
            self.td.add_description()
            self.td.create_checklist("Demo")
            # self.td.check_checklist_item()
            self.td.navigate_to_comments()
            self.td.sending_message_in_comment_section("Tested and Passed")
            self.td.navigate_to_task_detail()
            self.td.click_on_back_btn()
            self.logger.info("------------ Performed actions on Subtask --------")

        except Exception as e:
            # Log and fail the test if an unexpected error occurs
            self.logger.error(f"Unexpected error: {e}")
            pytest.fail(f"Test failed due to unexpected error: {e}")

        finally:
            # Close the browser session
            self.driver.close()
            self.logger.info("Browser closed.")