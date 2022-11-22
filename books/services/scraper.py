from selenium import webdriver
from selenium.webdriver.common.by import By
# takes in the url for the amazon page and returns a dictionary of the book's title, description, rating, image, and url
# creates a headless chrome browser to scrape the page
# TODO: separate into a function that takes in the url and sets up the browser
# and a function that takes in the browser and returns the specific data
# scrape_amazon(url)
# and:
# get_book_data_by_id(driver, element_id)
# get_book_data_by_class(driver, element_class)
# get_book_data_by_css_selector(driver, css_selector)
# get_book_data_by_xpath(driver, xpath)
# get_book_data_by_tag_name(driver, tag_name)


def scrape_amazon(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    title = driver.find_element(By.ID, 'productTitle').text
    # description = driver.find_element(By.ID, 'productDescription').text
    # rating = driver.find_element(By.ID, 'acrCustomerReviewText').text
    # image = driver.find_element(By.ID, 'imgBlkFront').get_attribute('src')
    driver.quit()
    return {'title': title, 
    # 'description': description, 'rating': rating, 'image': image, 
    'url': url
    }