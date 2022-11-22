import pytest

#  tests the scraper.py file
from books.services.scraper import scrape_amazon #  tests the scrape_amazon function
# TODO: separate into multiple tests
def test_scrape_amazon_title():
    #  test the scraper with a valid url
    url = 'https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280/ref=sr_1_1?dchild=1&keywords=python+crash+course&qid=1605078487&sr=8-1'
    result = scrape_amazon(url)
    assert result['title'] == 'Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming'

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