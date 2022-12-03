import pytest

#  tests the scraper.py file
from books.services.scraper import AmazonScrape # tests the AmazonScraper class
# TODO: separate into multiple tests

py_crash_url = "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280/ref=sr_1_1?dchild=1&keywords=python+crash+course&qid=1605078487&sr=8-1"
scraper = AmazonScrape(py_crash_url)

def test_scrape_title():
    result = scraper.get_title()
    assert result == "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming"

def test_scrape_description():
    result = scraper.get_description()
    assert result == '''If you've been thinking about learning how to code or picking up Python, this internationally bestselling guide to the most popular programming language is your quickest, easiest way to get started and go! Even if you have no experience whatsoever, Python Crash Course, 2nd Edition, will have you writing programs, solving problems, building computer games, and creating data visualizations in no time.

                        You’ll begin with basic concepts like variables, lists, classes, and loops—with the help of fun skill-strengthening exercises for every topic—then move on to making interactive programs and best practices for testing your code. Later chapters put your new knowledge into play with three cool projects: a 2D Space Invaders-style arcade game, a set of responsive data visualizations you’ll build with Python's handy libraries (Pygame, Matplotlib, Plotly, Django), and a customized web app you can deploy online.

                         Why wait any longer? Start your engine and code!'''

def test_scrape_rating():
    result = scraper.get_rating()
    assert "out of 5" in result

def test_scrape_rating_pop():
    result = scraper.get_rating_pop()
    assert "ratings" in result

def test_scrape_image():
    result = scraper.get_image()
    assert result == "https://m.media-amazon.com/images/I/51OOCVBfCQL._SX377_BO1,204,203,200_.jpg"


abs_url = "https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=pd_bxgy_img_sccl_2/134-3464273-1606430?pd_rd_w=FtGyW&content-id=amzn1.sym.7f0cf323-50c6-49e3-b3f9-63546bb79c92&pf_rd_p=7f0cf323-50c6-49e3-b3f9-63546bb79c92&pf_rd_r=18HCR33KA6JMNTHCVY44&pd_rd_wg=CO0gU&pd_rd_r=edebd344-02f6-4085-92bf-0667eaa7c005&pd_rd_i=1593279922&psc=1"
abs_scraper = AmazonScrape(abs_url)

def test_abs_scrape_title():
    result = abs_scraper.get_title()
    assert result == "Automate the Boring Stuff with Python, 2nd Edition: Practical Programming for Total Beginners"

def test_abs_scrape_description():
    result = abs_scraper.get_description()
    assert result == '''Learn how to code while you write programs that effortlessly perform useful feats of automation!

                        The second edition of this international fan favorite includes a brand-new chapter on input validation, Gmail and Google Sheets automations, tips for updating CSV files, and more.

                        If you've ever spent hours renaming files or updating spreadsheet cells, you know how tedious tasks like these can be. But what if you could have your computer do them for you? Automate the Boring Stuff with Python, 2nd Edition teaches even the technically uninclined how to write programs that do in minutes what would take hours to do by hand—no prior coding experience required!

                        This new, fully revised edition of Al Sweigart’s bestselling Pythonic classic, Automate the Boring Stuff with Python, covers all the basics of Python 3 while exploring its rich library of modules for performing specific tasks, like scraping data off the Web, filling out forms, renaming files, organizing folders, sending email responses, and merging, splitting, or encrypting PDFs. There’s also a brand-new chapter on input validation, tutorials on automating Gmail and Google Sheets, tips on automatically updating CSV files, and other recent feats of automations that improve your efficiency.

                        Detailed, step-by-step instructions walk you through each program, allowing you to create useful tools as you build out your programming skills, and updated practice projects at the end of each chapter challenge you to improve those programs and use your newfound skills to automate similar tasks. Boring tasks no longer have to take to get through—and neither does learning Python!'''

def test_abs_scrape_rating():
    result = abs_scraper.get_rating()
    assert "out of 5" in result

def test_abs_scrape_rating_pop():
    result = abs_scraper.get_rating_pop()
    assert "ratings" in result

def test_abs_scrape_image():
    result = abs_scraper.get_image()
    assert result == "https://m.media-amazon.com/images/I/51B161E04DL._SX375_BO1,204,203,200_.jpg"

# #  tests the scrape_amazon function
# def test_scrape_amazon():
#     #  test the scraper with a valid url
#     url = 'https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280/ref=sr_1_1?dchild=1&keywords=python+crash+course&qid=1605078487&sr=8-1'
#     result = scrape_amazon(url)
#     assert result['title'] == 'Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming'
#     # assert result['description'] == 'Python Crash Course is a fast-paced, no-nonsense guide to programming in Python that will have you writing programs, solving problems, and making things that work in no time.'
#     # assert result['rating'] == '4.8 out of 5 stars'
#     # assert result['image'] == 'https://m.media-amazon.com/images/I/51a1G6OyCZL.jpg'
#     assert result['url'] == url

    #  test the scraper with an invalid url
    # url = 'https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280/ref=sr_1_1?dchild=1&keywords=python+crash+course&qid=1605078487&sr=8-1'
    # result = scrape_amazon(url)
    # assert result == None