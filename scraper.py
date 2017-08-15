import scraperwiki
import lxml.html

from splinter import Browser

with Browser("phantomjs") as browser:
    # Optional, but make sure large enough that responsive pages don't
    # hide elements on you...
    browser.driver.set_window_size(1280, 1024)

    # Open the page you want...
    browser.visit("https://www.racingpost.com/profile/owner/127223/ballymacoll-stud/entries")

    print "visited"
    
    # Scrape the data you like...
    entries = browser.find_by_css(".pp-entries__item")
    for entry in entries:
        print entry['div.pp-entries__item__header']
