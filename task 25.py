import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_imdb_search(driver):
    # 1. Go to IMDb search page
    driver.get("https://www.imdb.com/search/name/")

    # 2. Fill the data in input boxes, select boxes, and drop-down menu
    name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "name")))
    name_input.send_keys("Brad Pitt")

    birth_year_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "birth_year")))
    birth_year_input.send_keys("1963")

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Search')]")))
    search_button.click()

    # 3. Verify the search results
    search_results_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Search results')]")))
    assert "Search results" in search_results_title.text

    # Add more assertions or validations as needed
    # For example, you can check for specific search results or other elements on the page


if __name__ == "__main__":
    pytest.main(["-v"])
