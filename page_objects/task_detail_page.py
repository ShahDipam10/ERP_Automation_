import logging
# For test_CreateTask.py
#contains objects on Task Detail Page
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime,timedelta

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

class TaskDetail:

    click_latest_task = "(// span[contains(@class , 'edit__taskname')])[1]"  # clicks latest added task
    copy_task_name_btn = "(//img[@class='copy-icon cursor-pointer'])[1]"
    tag_btn = "//div[@class='d-flex mobile__bg--withPadding']//div[@class='d-flex taglist__dropdown-mobile__margin']" # tag button
    tag_name_textbox = "//div[@class='tagInputwrapper']//input[@id='inputId']" #Tag textbox

    add_description_textbox = "//button[normalize-space()='Add description']"
    add_description_textbox1 = "//div[contains(@data-placeholder-active, 'Write something or type')][1]"
    description_text = "This is an automated test description"

    add_subtask_btn = "//span[@class='blue font-size-14 font-weight-500 cursor-pointer pl-20px text-decoration-underline']"
    subtask_key = "(//span[@class='cursor-pointer blue text-nowrap mr-5px'])[1]"

    #Subtask Status
    subtask_status_btn = "(//div[contains(@class,'overflow-y-auto style-scroll border-bottom subtask-mobile-width sub__task-item')]//span//div[@class='cursor-pointer'])[1]"
    subtask_status_todo= "//span[@class='ml-5px'][normalize-space()='To Do']"
    subtask_status_inprogress= "//span[@class='ml-5px'][normalize-space()='In Progress']"
    subtask_status_inreview= "//span[@class='ml-5px'][normalize-space()='In Review']"
    subtask_status_backlog= "//span[@class='ml-5px'][normalize-space()='Backlog']"
    subtask_status_done= "//span[@class='ml-5px'][normalize-space()='Done']"
    subtask_status_complete= "//span[@class='ml-5px'][normalize-space()='Complete']"
    #Task Status
    task_status_btn = "//span[@class='task-status-name']"
    task_status_todo = "//span[contains(@class,'d-block emp_label font-weight-500 font-size-13')][normalize-space()='To Do']"
    task_status_inprogress = "//span[contains(@class,'d-block emp_label font-weight-500 font-size-13')][normalize-space()='In Progress']"
    task_status_inreview = " //span[contains(@class,'d-block emp_label font-weight-500 font-size-13')][normalize-space()='In Review']"
    task_status_backlog = " //span[contains(@class,'d-block emp_label font-weight-500 font-size-13')][normalize-space()='Backlog']"
    task_status_done = " //span[contains(@class,'d-block emp_label font-weight-500 font-size-13')][normalize-space()='Done']"
    task_status_complete = " //span[contains(@class,'d-block emp_label font-weight-500 font-size-13')][normalize-space()='Complete']"

    #add checklist
    create_checklist_btn =  "(//span[@class='d-flex'])[1]"
    add_checklist_item =  "(//textarea[@id='inputId'])[1]"
    checklist_dropdown_button = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[1]/img[1]"
    check_checklist_item_checkbox = "(//*[contains(@id ,'checkbox_sub_')])[1]"

    #section buttons
    comments_section_btn = "//a[normalize-space()='Comments']"
    task_detail_section_btn = "//a[normalize-space()='Task Details']"

    #Comment Section
    textarea_of_comment_section = "//textarea[@id='message-box']"
    send_message_btn_in_comment = "//img[@alt='sendIcon']"

    #subtask button
    first_in_row_subtask_btn = "(//span[contains(@class, 'cursor-pointer blue text-nowrap mr-5px')])[1]"
    last_created_subtask_btn = "(//span[contains(@class, 'cursor-pointer blue text-nowrap mr-5px')])[last()]"

    back_btn = "//img[contains(@alt,'sidebarArrowIcon')]"

    #start and due date
    start_date_datepicker = "//h4[normalize-space()='Start Date']/following-sibling::div//input[@id='inputId']"
    due_date_datepicker = "//h4[normalize-space()='Due Date']/following-sibling::div//input[@id='inputId']"
    next_month_btn = "button[aria-label='Next month']"

    #Create Custom Field
    custom_field_link = "//h4[normalize-space()='+ Custom Field']"
    custom_field_mapping = {
        "text": ("//h5[normalize-space()='Text']", "create_text_field"),
        "date": ("//h5[normalize-space()='Date']", "create_date_field"),
        "number": ("//h5[normalize-space()='Number']", "create_number_field"),
        "text area" : ("//h5[normalize-space()='Text Area (Long Text)']", "create_text_area_field"),
        "money" : ("//h5[normalize-space()='Money']", "create_money_field"),
        "email" : ("//h5[normalize-space()='Email']", "create_email_field"),
        "dropdown" : ("//h5[normalize-space()='Dropdown']", "create_dropdown_field"),
        "phone number": ("//h5[normalize-space()='Phone Number']", "create_phone_number_field"),
        "checkbox" : ("//h5[normalize-space()='Checkbox']", "create_checkbox_field")
    }

    customfield_name = "//input[contains(@placeholder,'Enter Field Label')]"
    customfield_placeholder = "//input[@placeholder='Enter Placeholder']"
    customfield_description = "//textarea[@id='text']"
    customfield_save_btn = "//button[contains(@class,'formkit-input') and normalize-space()='Save']"

    customfield_options_tab_btn = "//h4[normalize-space()='Options']"

    customfield_date_format_ddmmyyyy = "//span[normalize-space()='DD-MM-YYYY']"
    customfield_date_time_tab_btn = "//h4[normalize-space()='Time']"
    customfield_date_time_formate_am_pm = "//span[normalize-space()='AM/PM']"

    customfield_dropdown_btn = "//div[@class='dropdown-select']"
    customfield_dropdown_predefined_options_mapping = {
        "none": "//span[normalize-space()='None']",
        "gender": "//span[normalize-space()='Gender']",
        "days": "//span[normalize-space()='Days']",
        "months": "//span[normalize-space()='Months']",
        "time zone": "//span[normalize-space()='Time Zone']",
        "country": "//span[normalize_space()='Country']"
    }
    customfield_dropdwon_create_item_btn = "//a[normalize-space()='+ Add another item']"
    customfield_dropdown_last_option_added_txtbox = "//*[contains(@class,'option-container')][last()]//child::input[@type = 'text']"


    customfield_phone_number_country_dropdown = "//div[@class='cursor-pointer']//div[@class='formkit__form-wrapper']"
    customfield_phone_number_country_dropdown_search_txtbox = "//input[@class='customfield__form-control']"
    customfield_phone_number_country_dropdown_option_india = "//span[normalize-space()='India']"

    #estimated time
    estimated_time_btn = "//span[@class='task-esitmate-hours cursor-pointer']"
    save_btn = "//button[@class='btn-primary font-size-16' and normalize-space()='Save']"
    cancel_btn = "//button[normalize-space()='Cancel']"
    # table_date_headers = "//tr[contains(@class,'estimate__daysdate-tr')]/th"  #states the table headers where dates are present to find today's date
    estimation_time_cell = "(//table[contains(@class, 'table-astimated-hour')]//tbody//tr)[1]//td[contains(@style, 'background-color: rgb(219, 241, 255);')]"


    def __init__(self,driver):
        self.driver = driver
        self.wait = driver.wait

    def click_task(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,self.click_latest_task))).click()
        except Exception as e:
            logger.error(f"Error clicking latest task: {e}")

    def copy_task_name(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,self.copy_task_name_btn))).click()
        except Exception as e:
            logger.error(f"Error copying task name: {e}")

    def add_tag(self): #here can call value from testcase if needed
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,self.tag_btn))).click()
            tag = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.tag_name_textbox)))
            tag.click()
            tag.send_keys(Keys.CONTROL, 'v')
            tag.send_keys(Keys.ENTER)
            logger.info("Tag Created and added")
            self.driver.find_element(By.TAG_NAME, "body").click()
        except Exception as e:
            logger.error(f"Error adding tag: {e}")

    def add_description(self):
        try:
            desc = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.add_description_textbox)))
            desc.click()
            desc1 = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.add_description_textbox1)))
            desc1.click()
            desc1.send_keys(self.description_text)
            time.sleep(2)
            logger.info("Description added")
        except NoSuchElementException as e:
            logger.error(f"Error finding the element: {e}")
        except Exception as e:
            logger.error(f"Error setting description: {e}")

    def clickon_add_subtask(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,self.add_subtask_btn))).click()
        except Exception as e:
            logger.error(f"Error clicking add subtask: {e}")

    def fetch_subtast_key(self):
        try:
            subtask_key_text = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.subtask_key))).text
            logger.info(f"SubTask Key: {subtask_key_text}")
            return subtask_key_text
        except Exception as e:
            logger.error(f"Error fetching subtask key: {e}")
            return None

    def set_subtask_status(self, status_name):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.subtask_status_btn))).click()
            status_name_mapping={
                "todo": self.subtask_status_todo,
                "in progress": self.subtask_status_inprogress,
                "in review": self.subtask_status_inreview,
                "backlog": self.subtask_status_backlog,
                "done": self.subtask_status_done,
                "complete": self.subtask_status_complete
            }
            if status_name in status_name_mapping:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, status_name_mapping[status_name]))).click()
            else:
                raise ValueError(f"Invalid status: {status_name}. Choose from 'todo', 'in progress', 'in review' , 'backlog', 'done' , or 'complete'.")
        except Exception as e:
            logger.error(f"Error setting subtask status: {e}")

    def set_task_status(self,task_status):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.task_status_btn))).click()
            task_status_mapping={
                "todo": self.task_status_todo,
                "in progress": self.task_status_inprogress,
                "in review": self.task_status_inreview,
                "backlog": self.task_status_backlog,
                "done": self.task_status_done,
                "complete": self.task_status_complete
            }
            if task_status in task_status_mapping:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, task_status_mapping[task_status]))).click()
            else:
                raise ValueError(f"Invalid status: {task_status}. Choose from 'todo', 'in progress', 'in review' , 'backlog', 'done' , or 'complete'.")
        except Exception as e:
            logger.error(f"Error setting task status: {e}")

    def create_custom_field(self, field_type : str, value = None):
        try:
            if field_type not in self.custom_field_mapping:
                raise ValueError(f"Unsupported field type: {field_type}")
            xpath, handler = self.custom_field_mapping[field_type]
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.custom_field_link))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            if hasattr(self, handler):
                getattr(self, handler)(value)
        except Exception as e:
            logger.error(f"Error creating custom field: {e}")

    def fill_field_label_txtbox(self,value):
        try:
            field_label_textbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_name)))
            field_label_textbox.send_keys(value)
        except Exception as e:
            logger.error(f"Error filling field label textbox: {e}")

    def fill_placeholder_txtbox(self, value):
        try:
            placeholder_textbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_placeholder)))
            placeholder_textbox.send_keys(value)
        except Exception as e:
            logger.error(f"Error filling placeholder textbox: {e}")

    def fill_description_txtbox(self,value):
        try:
            description_textbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_description)))
            description_textbox.send_keys(value)
        except Exception as e:
            logger.error(f"Error filling description textbox: {e}")

    def customfield_click_save_btn(self):
        try:
            save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_save_btn)))
            self.driver.execute_script("arguments[0].click();", save_button)
        except Exception as e:
            logger.error(f"Error clicking custom field save button: {e}")

    def create_text_field(self, value = None):
        try:
            self.fill_field_label_txtbox("Task Name")
            self.fill_placeholder_txtbox("Enter Task Name")
            self.fill_description_txtbox("Enter current Task Name")
            self.customfield_click_save_btn()
        except Exception as e:
            logger.error(f"Error creating text field: {e}")

    def create_date_field(self, value):
        try:
            self.fill_field_label_txtbox("Enter Date")
            self.fill_description_txtbox("Enter test Date")
            option_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_options_tab_btn)))
            option_btn.click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_date_format_ddmmyyyy))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_date_time_tab_btn))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_date_time_formate_am_pm))).click()
            self.customfield_click_save_btn()
        except Exception as e:
            logger.error(f"Error creating date field: {e}")

    def create_number_field(self, value):
        try:
            self.fill_field_label_txtbox("Number :")
            self.fill_placeholder_txtbox("Enter number")
            self.fill_description_txtbox("Enter number")
            self.customfield_click_save_btn()
        except Exception as e:
            logger.error(f"Error creating number field: {e}")

    def create_text_area_field(self,value=None):
        try:
            self.fill_field_label_txtbox("Text: ")
            self.fill_placeholder_txtbox("Enter your text here ")
            self.fill_description_txtbox("Enter your text in this field")
            self.customfield_click_save_btn()
        except Exception as e:
            logger.error(f"Error creating text area field: {e}")

    def create_money_field(self, value=None):
        try:
            self.fill_field_label_txtbox("Money Amount :")
            self.fill_placeholder_txtbox("Enter your money amount here")
            self.fill_description_txtbox("Enter your money amount in this field")
            self.customfield_click_save_btn()
        except Exception as e:
            logger.error(f"Error creating money field: {e}")

    def create_email_field(self, value=None):
        try:
            self.fill_field_label_txtbox("Email Id: ")
            self.fill_placeholder_txtbox("Enter your email id here")
            self.fill_description_txtbox("Enter your Email ID in this field")
            self.customfield_click_save_btn()
        except Exception as e:
            logger.error(f"Error creating email field: {e}")

    def create_dropdown_field(self, value):
        try:
            self.fill_field_label_txtbox("Dropdown menu:")
            self.fill_placeholder_txtbox("Here are the dropdown options")
            self.fill_description_txtbox("Select from Dropdown menu")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_options_tab_btn))).click()
            if isinstance(value, list):
                for index, option in enumerate(value):
                    if index > 0:
                        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_dropdwon_create_item_btn))).click()
                    self.add_dropdown_option(option)
            elif isinstance(value, str):
                self.set_predefined_option_dropdown(value)
            else:
                raise ValueError("Unsupported value type for dropdown options")
            self.customfield_click_save_btn()
        except Exception as e:
            logger.error(f"Error creating dropdown field: {e}")

    def add_dropdown_option(self,value):
        try:
            textbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_dropdown_last_option_added_txtbox)))
            textbox.send_keys(value)
        except Exception as e:
            logger.error(f"Error adding dropdown option: {e}")

    def set_predefined_option_dropdown(self, value):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_dropdown_btn))).click()
            if value in self.customfield_dropdown_predefined_options_mapping:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_dropdown_predefined_options_mapping[value]))).click()
            else:
                raise ValueError(
                    f"Invalid status: {value}. Choose from 'none','gender','days','months','time zone','country'.")
        except Exception as e:
            logger.error(f"Error setting predefined option dropdown: {e}")

    def create_phone_number_field(self,value = None):
        try:
            self.fill_field_label_txtbox("Phone Number :")
            self.fill_placeholder_txtbox("Enter phone number number")
            self.fill_description_txtbox("Enter the phone number")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_options_tab_btn))).click()
            country_drpdwn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_phone_number_country_dropdown)))
            country_drpdwn.click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_phone_number_country_dropdown_search_txtbox))).send_keys("India")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.customfield_phone_number_country_dropdown_option_india))).click()
            self.customfield_click_save_btn()
        except Exception as e:
            logger.error(f"Error creating phone number field: {e}")

    def create_checkbox_field(self, value=None):
        try:
            self.fill_field_label_txtbox("Checkbox label:")
            self.fill_placeholder_txtbox("Enter your text here")
            self.fill_description_txtbox("Create checkbox")
            self.customfield_click_save_btn()
        except Exception as e:
            logger.error(f"Error creating checkbox field: {e}")

    def create_checklist(self, item_name):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.create_checklist_btn))).click()
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_checklist_item)))
            element.send_keys(item_name)
            element.send_keys(Keys.RETURN)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            # self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checklist_dropdown_button))).click()
        except Exception as e:
            logger.error(f"Error creating checklist: {e}")

    def check_checklist_item(self):
        try:
            # self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checklist_dropdown_button))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.check_checklist_item_checkbox))).click()
        except Exception as e:
            logger.error(f"Error checking checklist item: {e}")

    def navigate_to_comments(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.comments_section_btn))).click()
        except Exception as e:
            logger.error(f"Error navigating to comments: {e}")

    def navigate_to_task_detail(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.task_detail_section_btn))).click()
        except Exception as e:
            logger.error(f"Error navigating to task detail: {e}")

    def sending_message_in_comment_section(self, chat_message):
        try:
            textarea_in_comment = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.textarea_of_comment_section)))
            textarea_in_comment.click()
            textarea_in_comment.send_keys(chat_message)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.send_message_btn_in_comment))).click()
        except Exception as e:
            logger.error(f"Error sending message in comment section: {e}")

    def navigate_to_first_subtask(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.first_in_row_subtask_btn))).click()
        except Exception as e:
            logger.error(f"Error navigating to first subtask: {e}")

    def navigate_to_last_created_subtask(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.last_created_subtask_btn))).click()
        except Exception as e:
            logger.error(f"Error navigating to last created subtask: {e}")

    def click_on_back_btn(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.back_btn))).click()
        except Exception as e:
            logger.error(f"Error clicking back button: {e}")

    def select_start_date(self):
        try:
            today_date = datetime.today().date()
            date_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.start_date_datepicker)))
            self.set_date(date_input, today_date)
        except Exception as e:
            logger.error(f"Error selecting start date: {e}")

    def select_due_date(self, days_ahead):
        try:
            future_date = (datetime.today() + timedelta(days=days_ahead)).date()
            date_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.due_date_datepicker)))
            self.set_date(date_input, future_date)
        except Exception as e:
            logger.error(f"Error selecting due date: {e}")

    def set_date(self, date_input_element, desired_date):
        date_id = desired_date.strftime("%Y-%m-%d")
        try:
            date_input_element.click()
            while True:
                try:
                    date_cell = self.driver.find_element(By.ID, date_id)
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", date_cell)
                    date_cell.click()
                    break
                except:
                    next_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-dp-element='action-next']")
                    next_button.click()
        except Exception as e:
            logger.error(f"Failed to select the date {date_id}: {e}")

    def upload_file(self, file_path):
        try:
            upload = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", upload)
            upload.send_keys(file_path)
            logger.info("File uploaded successfully")
        except Exception as e:
            self.driver.save_screenshot("before_click_error.png")
            logger.error(f"File upload failed: {e}")
            raise

    def set_estimated_time(self,value):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "v-toast__text")))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.estimated_time_btn))).click()
            est_time_cell = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.estimation_time_cell)))
            est_time_cell.click()
            input_box = est_time_cell.find_element(By.TAG_NAME, "input")
            input_box.clear()
            input_box.send_keys(value)
            input_box.send_keys(Keys.TAB)
            save = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.save_btn)))
            save.click()
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "v-toast__text")))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cancel_btn))).click()
            logger.info(f"Estimated Time for task is set to: {value}")
        except Exception as e:
            logger.error(f"Error setting estimated time: {e}")