from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BoardView:
    board_view_btn = "//*[@id='ProjectKanban']/div"

    # first_task_card = "(//div[@class='list-group-kanban-item-wrapper'])[1]//div[@class='list-group-kanban-item']"

    #first element of statuses
    first_element_todo = "(//span[normalize-space()='To Do']/following::div[@class='list-group-kanban-item-wrapper'])[1]//div[@class='list-group-kanban-item']"
    first_element_in_progress = "(//span[normalize-space()='In Progress']/following::div[@class='list-group-kanban-item-wrapper'])[1]//div[@class='list-group-kanban-item']"
    first_element_in_review = "(//span[normalize-space()='In Review']/following::div[@class='list-group-kanban-item-wrapper'])[1]//div[@class='list-group-kanban-item']"
    first_element_backlog = "(//span[normalize-space()='Backlog']/following::div[@class='list-group-kanban-item-wrapper'])[1]//div[@class='list-group-kanban-item']"
    first_element_done = "(//span[normalize-space()='Done']/following::div[@class='list-group-kanban-item-wrapper'])[1]//div[@class='list-group-kanban-item']"
    first_element_complete = "(//span[normalize-space()='Complete']/following::div[@class='list-group-kanban-item-wrapper'])[1]//div[@class='list-group-kanban-item']"

    # first element of Priorities
    first_element_High = "(//span[normalize-space()='High']/following::div[@class='list-group-kanban-item-wrapper'])[1]//div[@class='list-group-kanban-item']"
    first_element_Medium = "(//span[normalize-space()='Medium']/following::div[@class='list-group-kanban-item-wrapper'])[1]//div[@class='list-group-kanban-item']"
    first_element_Low = "(//span[normalize-space()='Low']/following::div[@class='list-group-kanban-item-wrapper'])[1]//div[@class='list-group-kanban-item']"

    #task status areas
    todo_status_area = "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[1]"
    in_progress_status_area = "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]"
    in_review_status_area = "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[3]"
    backlog_status_area = "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[4]"
    done_status_area = "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[5]"
    complete_status_area= "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[5]"

    #task priority areas
    high_priority_area = "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[1]"
    medium_priority_area = "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]"
    low_priority_area = "//*[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[3]"

    #group by dropdown option
    groupby_dropdown = "//div[@class='group-by-dropdown']"
    dropdown_option_status = "//span[normalize-space()='Status']"
    dropdown_option_priority = "//span[normalize-space()='Priority']"


    def __init__(self,driver):
        self.driver = driver
        self.wait = driver.wait

    def click_on_boardview_btn(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.board_view_btn))).click()
        print("Navigated to Board View")

    def change_groupby_priority(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.groupby_dropdown))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.dropdown_option_priority))).click()
        self.driver.find_element(By.TAG_NAME, "body").click()


    def change_groupby_status(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.groupby_dropdown))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.dropdown_option_status))).click()
        self.driver.find_element(By.TAG_NAME, "body").click()


    def dragndrop_by_status(self, source, target):

        first_element_by_status_mapping = {
            "todo": self.first_element_todo,
            "in progress": self.first_element_in_progress,
            "in review": self.first_element_in_review,
            "backlog": self.first_element_backlog,
            "done": self.first_element_done,
            "complete": self.first_element_complete
        }
        status_name_mapping = {
            "todo": self.todo_status_area,
            "in progress": self.in_progress_status_area,
            "in review": self.in_review_status_area,
            "backlog": self.backlog_status_area,
            "done": self.done_status_area,
            "complete": self.complete_status_area
        }

        # Wait for the source element to be visible
        source_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, first_element_by_status_mapping[source])))
        # Wait for the target element to be visible
        target_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, status_name_mapping[target])))
        # Create the ActionChains object and perform drag and drop
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()


    def dragndrop_by_priority(self, source, target):
        first_element_by_priority_mapping = {
            "high" : self.first_element_High,
            "medium" : self.first_element_Medium,
            "low" : self.first_element_Low
        }
        priority_name_mapping = {
            "high" : self.high_priority_area,
            "medium" : self.medium_priority_area,
            "low" : self.low_priority_area
        }

        # Wait for the source element to be visible
        source_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, first_element_by_priority_mapping[source])))
        # Wait for the target element to be visible
        target_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, priority_name_mapping[target])))
        # Create the ActionChains object and perform drag and drop
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()