import logging
# For test_CreateTask.py
#contains objects on Project Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

class CreateTask:
    project_page = "//a[normalize-space()='Projects']"
    new_task_btn = "//button[@id='createtask_driver']"

    task_type_btn = "//div[@class='task__type-width task__type-width-list']"
    tasktype_task = "//span[normalize-space()='Task']"
    tasktype_subtask = "//span[normalize-space()='Sub Task']"
    tasktype_bug = "//span[normalize-space()='Bug']"

    task_name_txtbox = "//input[@id='inputId']"
    save_task_btn = "//button[normalize-space()='Save']"

    assignee_btn = "(//span[@class='assignee-main-new task_right']//img[@title='Add User'])[1]"
    assignee_person_btn = "//div[@id='item0']"
    user_list_close_btn = "//div[@class='cursor-pointer d-flex align-items-center text-nowrap']"

    set_task_priority_btn = "(//*[@id='singletaskdisply']/div[2]/div/span[4]/div/div/img)[1]"
    priority_high = "//span[normalize-space()='High']"
    priority_medium = "//span[normalize-space()='Medium']"
    priority_low = "//span[normalize-space()='Low']"

    task_key_txt = "(//*[@id='subtasklist_driver undefined']/div[1]//span[contains(@class, 'key-new') and contains(@class, 'task_right') and starts-with(text(), 'P')])[last()]"

    #Delete Task
    last_created_task = "(//div//img[@id='taskquickmenudriver'])[1]"
    delete_option_btn = "//span[normalize-space()='Delete']"
    type_delete_txtbox = "//input[contains(@id,'inputId') and contains(@placeholder,'delete')]"
    delete_task_btn = "//button[normalize-space()='Delete']"
    task_deleted_toast_msg = "//p[@class='v-toast__text' and contains(text(), 'Task deleted successfully')]"

    #Archive Task
    archive_option_btn = "//span[normalize-space()='Archive']"
    type_archive_txtbox = "//input[contains(@id,'inputId') and contains(@placeholder,'archive')]"
    archive_task_btn = "//button[normalize-space()='Archive']"
    task_archived_toast_msg = "//p[@class='v-toast__text' and contains(text(), 'Task archived successfully')]"
    setting_btn = "//img[@id='projectleftsidsetting_driver']"
    show_archive_btn = "//div[@class='overflow-y-auto overflow-x-hidden drop-down-options black']"
    archived_tasks = "//*[@id='singletaskdisply']/div[1]"
    hide_archive_btn = "//div[normalize-space()='Hide Archive']"


    def __init__(self,driver):
        self.driver = driver
        self.wait = driver.wait

    def project_page_link(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,self.project_page))).click()
        except Exception as e:
            logger.error(f"Error clicking project page link: {e}")

    def click_new_task_btn(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.new_task_btn))).click()
        except Exception as e:
            logger.error(f"Error clicking new task button: {e}")

    def set_task_type(self,task_type):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.task_type_btn))).click()
            task_type_mapping = {
                "task": self.tasktype_task,
                "subtask": self.tasktype_subtask,
                "bug": self.tasktype_bug
            }
            if task_type in task_type_mapping:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, task_type_mapping[task_type]))).click()
            else:
                raise ValueError(f"Invalid task type: {task_type}. Choose from 'task', 'subtask', or 'bug'.")
        except Exception as e:
            logger.error(f"Error setting task type: {e}")

    def set_task_name(self,task_name):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.task_name_txtbox))).send_keys(task_name)
        except Exception as e:
            logger.error(f"Error setting task name: {e}")

    def save_task(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.save_task_btn))).click()
        except Exception as e:
            logger.error(f"Error saving task: {e}")

    def select_assignee(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,self.assignee_btn))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.assignee_person_btn))).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.user_list_close_btn)))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.user_list_close_btn))).click()
        except Exception as e:
            logger.error(f"Error selecting assignee: {e}")

    def set_task_priority(self, priority_type):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.set_task_priority_btn))).click()
            priority_type_mapping = {
                "high": self.priority_high,
                "medium": self.priority_medium,
                "low": self.priority_low
            }
            if priority_type in priority_type_mapping:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, priority_type_mapping[priority_type]))).click()
            else:
                raise ValueError(f"Invalid Priority type: {priority_type}. Choose from 'high', 'medium', or 'low'.")
        except Exception as e:
            logger.error(f"Error setting task priority: {e}")

    def get_task_key(self):
        try:
            task_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.task_key_txt)))
            if task_elements:
                task_keys = [task.text for task in task_elements]
                latest_task_key = task_keys[-1]
                logger.info(f"Task Key: {latest_task_key}")
                return latest_task_key
            else:
                logger.warning("No tasks found.")
                return None
        except Exception as e:
            logger.error(f"Error getting task key: {e}")
            return None

    def delete_task(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,self.last_created_task))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.delete_option_btn))).click()
            delete_txtbox = self.wait.until(EC.presence_of_element_located((By.XPATH, self.type_delete_txtbox)))
            delete_txtbox.send_keys("delete")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.delete_task_btn))).click()
            toast = self.wait.until(EC.presence_of_element_located((By.XPATH, self.task_deleted_toast_msg)))
            assert toast.is_displayed(), "Toast message not displayed"
            logger.info("Task deleted toast message verified successfully.")
        except Exception as e:
            logger.error(f"Error deleting task: {e}")

    def archive_task(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.last_created_task))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.archive_option_btn))).click()
            archive_txtbox = self.wait.until(EC.presence_of_element_located((By.XPATH, self.type_archive_txtbox)))
            archive_txtbox.send_keys("archive")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.archive_task_btn))).click()
            toast = self.wait.until(EC.presence_of_element_located((By.XPATH, self.task_archived_toast_msg)))
            assert toast.is_displayed(), "Toast message not displayed"
            logger.info("Task archived toast message verified successfully.")
        except Exception as e:
            logger.error(f"Error archiving task: {e}")

    def show_archived_task(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.setting_btn))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.show_archive_btn))).click()
            tasks = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.archived_tasks)))
            logger.info(f"No. of archived tasks: {len(tasks)}")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.hide_archive_btn))).click()
        except Exception as e:
            logger.error(f"Error showing archived tasks: {e}")