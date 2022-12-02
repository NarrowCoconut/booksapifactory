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

class AmazonScrape():
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)
        self.scrape_dict = {}

    def get_title(self):
        title = self.driver.find_element(By.ID, 'productTitle').text
        self.scrape_dict["title"] = title
        return(title)

    # working ok 5/10. Need to get it into the read more part though
    def get_description(self):
        description = self.driver.find_element(By.ID, 'bookDescription_feature_div').text
        description = description.replace("\n", '') # we might want new lines later. Depends on how we want to display it on the webpage
        self.scrape_dict["description"] = description
        return(description)
    
    def get_rating(self):
        rating = self.driver.find_element(By.CSS_SELECTOR, "span.a-size-medium.a-color-base").text
        self.scrape_dict['rating'] = rating
        return(rating)

    def get_rating_pop(self):
        rating_pop = self.driver.find_element(By.ID, 'acrCustomerReviewText').text
        self.scrape_dict['rating_pop'] = rating_pop
        return(rating_pop)
    
    def get_image(self):
        image = self.driver.find_element(By.ID, 'imgBlkFront').get_attribute('src')
        self.scrape_dict['image'] = image
        return(image)
    
    '''
    description = driver.find_element(By.ID, 'productDescription').text
    rating = driver.find_element(By.ID, 'acrCustomerReviewText').text
    image = driver.find_element(By.ID, 'imgBlkFront').get_attribute('src')
    '''

def scrape_amazon(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    title = driver.find_element(By.ID, 'productTitle').text
    #description = driver.find_element(By.ID, 'productDescription').text
    #rating = driver.find_element(By.ID, 'acrCustomerReviewText').text
    #image = driver.find_element(By.ID, 'imgBlkFront').get_attribute('src')
    driver.quit()
    return {'title': title, 
    # 'description': description, 'rating': rating, 'image': image, 
    'url': url
    }

scraper = AmazonScrape("https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280/ref=sr_1_1?dchild=1&keywords=python+crash+course&qid=1605078487&sr=8-1")
print("\n\n", scraper.get_title())
print(scraper.get_description())
print(scraper.get_rating())
print(scraper.get_rating_pop())
print(scraper.get_image())
print(scraper.scrape_dict)