import datetime
import time
import uuid
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timedelta
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

# Configure logging at the top of the file (can be customized as needed)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
    handlers=[
        logging.FileHandler('logs/automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class CreateProject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = driver.wait

    # Locators
    project_page_link = (By.XPATH, "//a[@class='cursor-pointer link-item white h-100']")
    new_project_button = (By.XPATH, "//button[@id='createproject_driver']")
    blank_project_option = (By.XPATH, "//div[@id='createblankproject_driver']//button[@type='button']")
    project_name_input = (By.XPATH, "//div[@id='createprojectname_driver']//input[@id='inputId']")
    project_key_input = (By.XPATH, "//div[@id='createprojectkey_driver']//input[@id='inputId']")
    category_input = (By.XPATH, "//div[@id='createprojectcategory_driver']//input[@id='inputId']")
    category_in_house_option = (By.XPATH, "//div[@id='item2']")
    next_button = (By.XPATH, "//button[@class='cursor-pointer conditional-next-step btn border-radius-4-px white border-0 bg-blue']")
    create_project_button = (By.XPATH, "//button[@id='createprojectbtn_driver']")
    add_user_icon = (By.XPATH, "//img[@title='Add User']") 
    select_user_name = (By.XPATH, "//div[@id='item0']")
    close_button = (By.XPATH, "//img[@alt='closeButton']")
    color_option = (By.XPATH, "//li[13]")
    file_input_xpath = (By.XPATH, "//input[@type='file']") #(An assumed XPATH but still worked!!)
    select_private_option = (By.XPATH, "//p[normalize-space()='Private']")
    add_task_type = (By.XPATH, "//button[@id='createprojecttasktypenew_driver']")
    add_task_type_link = (By.XPATH, "//span[@class='add_status font-size-12 font-weight-400']")
    task_type_name = (By.XPATH, "//input[@id='inputId']")
    upload_button = (By.XPATH, "//input[@type='file']") # Very useful XPATH to upload files
    green_check = (By.XPATH, "//img[@class='greenCheck_sidebar vertical-middle mr-13px']")
    close_button23 = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/img")
    task_selection = (By.XPATH, "//div[@id='my-sidebar']//div[6]")
    status_new_template = (By.XPATH, "//button[normalize-space()='+ New Template']")
    enter_template_name = (By.XPATH, "//input[@placeholder='Enter Template']")
    green_check2 = (By.XPATH, "//span[@class='position-ab edit-rightinput save__closeimg-wrapper']//img[@class='cursor-pointer']")
    marketing_statuses_for_tasks = (By.XPATH, "//span[@title='Marketing']")
    toggle = (By.XPATH, "//div[@class='toggle bg-green mr-10px']")
    board = (By.XPATH, "//div[@class='align-items-center justify-content-space-between mobile-reuired-views']//div[2]//div[2]//div[2]//div[1]")
    three_dots = (By.XPATH, "//img[@id='projectoptions_driver']")
    delete_button = (By.XPATH, "//div[@id='my-dropdown']//div[6]")
    type_delete_field = (By.XPATH, "//input[@id='inputId']")
    final_delete_button = (By.XPATH, "//button[@class='btn-danger px-1 font-size-16 font-roboto-sans']")
    rename_option = (By.XPATH, "//span[normalize-space()='Rename']")
    rename_field = (By.XPATH, "//input[@placeholder='Project name']")
    color_avatar = (By.XPATH, "//span[normalize-space()='Color & Avatar']")
    project_color = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[6]")
    save_button = (By.XPATH, "//button[@class='btn-primary p0x-10px']")
    due_date = (By.XPATH, "//input[@placeholder='Select Project Due Date']")
    save_as_template = (By.XPATH, "//button[@id='createprojectsavetemp_driver']")
    image_upload = (By.XPATH, "//img[@class='create-workspace-sidebar-image']")  # Assuming this is for uploading images in the template creation
    template_field = (By.XPATH, "//input[@id='inputId']")
    template_description = (By.XPATH, "//textarea[@placeholder='Enter Description']")  # Assuming this is for entering template description
    save_continue_button = (By.XPATH, "//button[@class='submit-btn cursor-pointer conditional__save-create btn border-radius-4-px bg-blue white border-0']")
    use_template_option = (By.XPATH, "//div[@id='createprojectusingtemplate_driver']//button[@type='button']")
    company_name_template = (By.XPATH, "//div[@class='mainLeftside']//p[1]")
    template_selection = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]")
    use_template_final_button = (By.XPATH, "//button[@type='button']")
    lead_selection_in_template = (By.XPATH, "//li[@class='addIcon ml-0px']//img[@title='Add User']")
    select_private_project_option_template = (By.XPATH, "//div[@class='shareGraphicPrivate font-size-13 border-radius-5-px']//img[@alt='images']")
    only_share_with_lead = (By.XPATH, "//li[@class='ml--5px']//img[@title='Add User']")
    create_project_button2 = (By.XPATH, "//button[@class='submit-btn templateall__submit-btn cursor-pointer conditional-submit btn']")
    first_project_from_list = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]")
    options_of_project = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]")
    create_new_sprint = (By.XPATH, "//div[contains(text(),'Create New Sprint')]")
    sprint_name_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]")
    create_new_folder = (By.XPATH, "/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]")
    folder_name_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]")
    rename_field_from_list_view = (By.XPATH, "//div[contains(@class, 'project-mobile-desc') and contains(., 'Rename')]")
    project_rename_text_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]")
    project_popup_cancel = (By.XPATH, "//img[@alt='close']")
    color_avatar_list = (By.XPATH, "/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[4]/div[1]")
    new_image_save_button = (By.XPATH, "//button[@class='btn-primary p0x-10px']")
    close_project = (By.XPATH, "/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[5]/div[1]")
    close_project_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
    close_button2 = (By.XPATH, "//button[@class='btn-danger px-1 font-size-16 font-roboto-sans']") 
    delete_project_from_list = (By.XPATH, "/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[6]/div[1]")
    delete_text_field = (By.XPATH, "//input[@id='inputId']")
    delete_button3 = (By.XPATH, "//button[@class='btn-danger px-1 font-size-16 font-roboto-sans']")
    project_rename_top_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]") 
    project_rename_text_field2 = (By.XPATH, "//input[@placeholder='Project name']")
    # calendar_option = (By.XPATH, "//div[5]//div[2]//div[2]")  

    def navigate_to_project_page(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.project_page_link)).click()
        except Exception as e:
            logger.error(f"Error navigating to project page: {e}")

    def click_project_popup_cancel(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.project_popup_cancel)).click()
        except Exception as e:
            logger.error(f"Popup cancel button not found or not clickable: {e}")
            # Optionally, you can take a screenshot for debugging
            # self.driver.save_screenshot("project_popup_cancel_error.png")  # <-- Remove or comment out this line

    def click_new_project(self):
        """
        Clicks the 'New Project' button on the project page.
        """
        try:
            self.wait.until(EC.element_to_be_clickable(self.new_project_button)).click()
        except Exception as exc:
            logger.error(f"Error clicking 'New Project' button: {exc}")

    def select_blank_project(self):
        """
        Selects the 'Blank Project' option when creating a new project.
        """
        try:
            self.wait.until(EC.element_to_be_clickable(self.blank_project_option)).click()
        except Exception as exc:
            logger.error(f"Error selecting 'Blank Project' option: {exc}")

    def enter_project_details(self):
        """
        Enters random project name and key in the respective input fields.
        """
        project_name = f"Project-{uuid.uuid4().hex[:6]}"
        project_key = f"Key-{uuid.uuid4().hex[:4]}"
        try:
            self.wait.until(EC.visibility_of_element_located(self.project_name_input)).send_keys(project_name)
            self.wait.until(EC.visibility_of_element_located(self.project_key_input)).send_keys(project_key)
        except Exception as exc:
            logger.error(f"Error entering project details: {exc}")

    def select_category(self):
        """
        Selects the 'In House' category for the project.
        """
        try:
            self.wait.until(EC.element_to_be_clickable(self.category_input)).click()
            self.wait.until(EC.element_to_be_clickable(self.category_in_house_option)).click()
        except Exception as exc:
            logger.error(f"Error selecting project category: {exc}")

    def select_due_date(self, days_ahead):
        """
        Selects a due date for the project, days ahead from today.
        """
        future_date = (datetime.today() + timedelta(days=days_ahead)).date()
        try:
            date_input = self.wait.until(EC.element_to_be_clickable(self.due_date))
            self.set_date(date_input, future_date)
        except Exception as exc:
            logger.error(f"Error selecting due date: {exc}")

    def set_date(self, date_input_element, desired_date):
        """
        Sets the date in the date picker by clicking the cell with the given date ID.
        """
        date_id = desired_date.strftime("%Y-%m-%d")
        try:
            date_input_element.click()
            date_cell = self.driver.find_element(By.ID, date_id)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", date_cell)
            date_cell.click()
        except Exception as exc:
            logger.error(f"Failed to select the date {date_id}: {exc}")

    def click_add_lead(self):
        try:
            self.wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, "v-overlay__scrim")))
        except:
            pass
        try:
            add_user_elem = self.wait.until(EC.element_to_be_clickable(self.add_user_icon))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", add_user_elem)
            try:
                add_user_elem.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", add_user_elem)
            self.wait.until(EC.element_to_be_clickable(self.select_user_name)).click()
            self.wait.until(EC.element_to_be_clickable(self.close_button)).click()
        except Exception as e:
            logger.error(f"Error adding lead: {e}")

    def click_next_button_once(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.next_button)).click()
        except Exception as e:
            logger.error(f"Error clicking next button: {e}")
            
    def select_color(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.color_option)).click()
        except Exception as e:
            logger.error(f"Error selecting color: {e}")

    def upload_project_image(self, image_path):
        try:
            file_input = self.wait.until(EC.presence_of_element_located(self.file_input_xpath))
            file_input.send_keys(image_path)
        except Exception as e:
            logger.error(f"Error uploading project image: {e}")

    def select_private_project_type(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.select_private_option)).click()
        except Exception as e:
            logger.error(f"Error selecting private project type: {e}")

    def click_add_task_type(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.add_task_type)).click()
        except Exception as e:
            logger.error(f"Error clicking add task type: {e}")

    def click_add_task_type_link(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.add_task_type_link)).click()
        except Exception as e:
            logger.error(f"Error clicking add task type link: {e}")

    def click_task_type_name(self):
        random_task_name = f"task-{uuid.uuid4().hex[:6]}"
        try:
            self.wait.until(EC.visibility_of_element_located(self.task_type_name)).send_keys(random_task_name)
        except Exception as e:
            logger.error(f"Error entering task type name: {e}")

    def click_upload_button(self, file_path, locator=None):
        try:
            if locator is None:
                locator = self.upload_button
            upload_element = self.driver.find_element(*locator)
            upload_element.send_keys(file_path)
        except Exception as e:
            logger.error(f"Error clicking upload button: {e}")

    def click_green_check(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.green_check)).click()
        except Exception as e:
            logger.error(f"Error clicking green check: {e}")

    def click_task_selection(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.task_selection)).click()
            try:
                self.wait.until(EC.element_to_be_clickable(self.close_button23)).click()
            except Exception as e:
                logger.warning(f"close_button23 not found or not clickable after green check: {e}")
        except Exception as e:
            logger.error(f"Error clicking task selection: {e}")

    def click_status_new_template(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.status_new_template)).click()
        except Exception as e:
            logger.error(f"Error clicking status new template: {e}")

    def click_enter_template_name(self):
        random_template_name = f"template_name-{uuid.uuid4().hex[:6]}"
        try:
            self.wait.until(EC.element_to_be_clickable(self.enter_template_name)).send_keys(random_template_name)
            self.wait.until(EC.element_to_be_clickable(self.green_check2)).click()
        except Exception as e:
            logger.error(f"Error entering template name: {e}")

    def click_marketing_statuses_for_tasks(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.marketing_statuses_for_tasks)).click()
        except Exception as e:
            logger.error(f"Error clicking marketing statuses for tasks: {e}")

    def click_toggle(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.toggle)).click()
        except Exception as e:
            logger.error(f"Error clicking toggle: {e}")

    def click_selected_apps(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.board)).click()
        except Exception as e:
            logger.error(f"Error clicking selected apps: {e}")

    def click_save_template(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.save_as_template)).click()
        except Exception as e:
            logger.error(f"Error clicking save template: {e}")

    def upload_template_image(self, image_path):
        try:
            file_input = self.wait.until(EC.presence_of_element_located(self.upload_button))
            file_input.send_keys(image_path)
        except Exception as e:
            logger.error(f"Error uploading template image: {e}")

    def click_template_name(self):
        random_template_name = f"template-{uuid.uuid4().hex[:6]}"
        try:
            self.wait.until(EC.visibility_of_element_located(self.template_field)).send_keys(random_template_name)
        except Exception as e:
            logger.error(f"Error entering template name: {e}")

    def click_template_description(self):
        random_template_description = f"Description-{uuid.uuid4().hex[:6]}"
        try:
            self.wait.until(EC.visibility_of_element_located(self.template_description)).send_keys(random_template_description)
        except Exception as e:
            logger.error(f"Error entering template description: {e}")

    def click_save_continue_button(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.save_continue_button)).click()
        except Exception as e:
            logger.error(f"Error clicking save continue button: {e}")

    def click_next_until_create_project(self, max_attempts=10):
        """
        Tries to click 'Create Project' directly; if not possible, tries 'Next' directly.
        No explicit waits are used.
        """
        from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

        for attempt in range(max_attempts):
            try:
                btn = self.driver.find_element(*self.create_project_button)
                if btn.is_displayed() and btn.is_enabled():
                    btn.click()
                    return
            except (NoSuchElementException, ElementNotInteractableException):
                pass
            try:
                next_btn = self.driver.find_element(*self.next_button)
                if next_btn.is_displayed() and next_btn.is_enabled():
                    next_btn.click()
            except (NoSuchElementException, ElementNotInteractableException) as e2:
                logger.warning(f"Error clicking next in loop: {e2}")
                break
        else:
            logger.error(f"Failed to find and click 'Create Project' after {max_attempts} attempts.")

    def delete_project(self):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.ID, "projectoptions_driver")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            try:
                self.wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, "v-overlay__scrim")))
            except:
                pass
            try:
                clickable = self.wait.until(EC.element_to_be_clickable((By.ID, "projectoptions_driver")))
                clickable.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", element)
            self.wait.until(EC.element_to_be_clickable(self.delete_button)).click()
            self.wait.until(EC.element_to_be_clickable(self.type_delete_field)).send_keys("delete")
            self.wait.until(EC.element_to_be_clickable(self.final_delete_button)).click()
        except Exception as e:
            logger.error(f"Error deleting project: {e}")

    def edit_project(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.ID, "projectoptions_driver")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            try:
                self.wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, "v-overlay__scrim")))
            except:
                pass
            try:
                clickable = self.wait.until(EC.element_to_be_clickable((By.ID, "projectoptions_driver")))
                clickable.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", element)
            self.wait.until(EC.element_to_be_clickable(self.color_avatar)).click()
            self.wait.until(EC.element_to_be_clickable(self.project_color)).click()
            try:
                self.wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, "v-overlay__scrim")))
            except:
                pass
            save_btn_elem = self.wait.until(EC.visibility_of_element_located(self.save_button))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn_elem)
            def not_obscured(driver):
                btn = driver.find_element(*self.save_button)
                return btn.is_displayed() and btn.size['height'] > 0 and btn.size['width'] > 0
            self.wait.until(not_obscured)
            self.wait.until(EC.element_to_be_clickable(self.save_button)).click()
        except Exception as e:
            logger.error(f"Error editing project: {e}")

    def template_usage(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.use_template_option)).click()
            self.wait.until(EC.element_to_be_clickable(self.company_name_template)).click()
            self.wait.until(EC.element_to_be_clickable(self.template_selection)).click()
            self.wait.until(EC.element_to_be_clickable(self.use_template_final_button)).click()
            random_project_name = f"Project-{uuid.uuid4().hex[:6]}"
            random_project_key = f"Key-{uuid.uuid4().hex[:4]}"
            self.wait.until(EC.visibility_of_element_located(self.project_name_input)).send_keys(random_project_name)
            self.wait.until(EC.visibility_of_element_located(self.project_key_input)).send_keys(random_project_key)
            self.wait.until(EC.element_to_be_clickable(self.category_input)).click()
            self.wait.until(EC.element_to_be_clickable(self.category_in_house_option)).click()
            self.wait.until(EC.element_to_be_clickable(self.lead_selection_in_template)).click()
            self.wait.until(EC.element_to_be_clickable(self.select_user_name)).click()
            self.wait.until(EC.element_to_be_clickable(self.close_button)).click()
        except Exception as e:
            logger.error(f"Error using template: {e}")

    def pvt_proj(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.select_private_project_option_template)).click()
            self.wait.until(EC.element_to_be_clickable(self.only_share_with_lead)).click()
            self.wait.until(EC.element_to_be_clickable(self.select_user_name)).click()
            self.wait.until(EC.element_to_be_clickable(self.close_button)).click()
            self.wait.until(EC.element_to_be_clickable(self.create_project_button2)).click()
        except Exception as e:
            logger.error(f"Error creating private project: {e}")

    def click_new_sprint(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.first_project_from_list)).click()
            self.wait.until(EC.element_to_be_clickable(self.options_of_project)).click()
            self.wait.until(EC.element_to_be_clickable(self.create_new_sprint)).click()
            random_sprint_name = f"Sprint-{uuid.uuid4().hex[:6]}"
            sprint_input = self.wait.until(EC.visibility_of_element_located(self.sprint_name_field))
            sprint_input.clear()
            sprint_input.send_keys(random_sprint_name + Keys.ENTER)
        except Exception as e:
            logger.error(f"Error creating new sprint: {e}")

    def click_create_new_folder(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.first_project_from_list)).click()
            self.wait.until(EC.element_to_be_clickable(self.options_of_project)).click()
            self.wait.until(EC.element_to_be_clickable(self.create_new_folder)).click()
            random_folder_name = f"Folder-{uuid.uuid4().hex[:6]}"
            folder_input = self.wait.until(EC.visibility_of_element_located(self.sprint_name_field))
            folder_input.clear()
            folder_input.send_keys(random_folder_name + Keys.ENTER)
        except Exception as e:
            logger.error(f"Error creating new folder: {e}")

    def click_rename_field_from_list_view(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.first_project_from_list)).click()
            self.wait.until(EC.element_to_be_clickable(self.options_of_project)).click()
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()[normalize-space()='Rename']]"))
            ).click()
            input_elem = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Project Name' or @placeholder='Project name']"))
            )
            input_elem.click()
            time.sleep(5)
            input_elem.send_keys(Keys.CONTROL, "a")
            input_elem.send_keys(Keys.BACKSPACE)
            input_elem.send_keys("bjfasbabga")
            input_elem.send_keys(Keys.ENTER)
            return "bjfasbabga"
        except Exception as e:
            logger.error(f"Error renaming project from list view: {e}")
            return None

    def click_color_avatar_list(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.first_project_from_list)).click()
            self.wait.until(EC.element_to_be_clickable(self.options_of_project)).click()
            self.wait.until(EC.element_to_be_clickable(self.color_avatar_list)).click()
        except Exception as e:
            logger.error(f"Error clicking color avatar list: {e}")

    def click_upload_button(self, image_path, wait_for_save=True):
        try:
            file_input = self.wait.until(EC.presence_of_element_located(self.file_input_xpath))
            file_input.send_keys(image_path)
            if wait_for_save:
                self.wait.until(EC.visibility_of_element_located(self.new_image_save_button))
                self.wait.until(EC.element_to_be_clickable(self.new_image_save_button)).click()
        except Exception as e:
            logger.error(f"Error clicking upload button (image): {e}")

    def click_close_project(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.first_project_from_list)).click()
            self.wait.until(EC.element_to_be_clickable(self.options_of_project)).click()
            self.wait.until(EC.element_to_be_clickable(self.close_project)).click()
            self.wait.until(EC.element_to_be_clickable(self.close_project_field)).send_keys("close")
            self.wait.until(EC.element_to_be_clickable(self.close_button2)).click()
        except Exception as e:
            logger.error(f"Error closing project: {e}")

    def click_delete_project_from_list(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.first_project_from_list)).click()
            self.wait.until(EC.element_to_be_clickable(self.options_of_project)).click()
            self.wait.until(EC.element_to_be_clickable(self.delete_project_from_list)).click()
            self.wait.until(EC.element_to_be_clickable(self.delete_text_field)).send_keys("delete")
            self.wait.until(EC.element_to_be_clickable(self.delete_button3)).click()
        except Exception as e:
            logger.error(f"Error deleting project from list: {e}")

    def click_rename_project_by_name(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.project_rename_top_field))
            ActionChains(self.driver).double_click(element).perform()
            input_elem = self.wait.until(
                EC.visibility_of_element_located(self.project_rename_text_field2)
            )
            input_elem.click()
            input_elem.send_keys(Keys.CONTROL, "a")
            input_elem.send_keys(Keys.BACKSPACE)
            random_name = f"Project-{uuid.uuid4().hex[:6]}"
            input_elem.send_keys(random_name)
            input_elem.send_keys(Keys.ENTER)
            return random_name
        except Exception as e:
            logger.error(f"Error renaming project by name: {e}")
            return None