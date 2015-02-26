import cv2
import autopy
import numpy as np


#def check_screen_on_all_browsers():

def click():
    ''' uses autopy to click element'''

def login(login_page):
    '''Performs login assuming that
    there is a form with input type password
    and input type submit
    on the page and that
    this is the login form'''


    return




def check_links(page):
    '''checks all links on a page'''


def picture_is_on_page(picture):
    ''' returns boolean: true if found'''
    if not picture:
        return False
    else:
        if is_a_picture(picture):
            #heere we start matching pics

        else:
            return False

def text_is_on_page(element):
    ''' returns boolean: true if found'''
    if not element:
        return False
    elif element:
        #here we start to search
        #the best way would be to press ctrl-a and copy to clipboard
    else
        return False

def find_on_screen(element):
    '''Finds element by visible text '''
    if is_on_page(element):
        return element
    else
        return None

def find_clickable(browser, element):
    ''' Find clickable thing: like a button
    or a link - None if not found
    args :: browser- instance of a webdriver class'''
    clickable = browser.find_elements_by_tag_name("a")
    for t in browser.find_elements_by_tag_name("button"):
        clickable.append(t)
    for w in clickable:
        if w.text == element:
            return element
    return None




def count_elements():
    ''' returns integer - no of elements '''

def read_screen():
    '''Returns all text elements from the screen
    visible to the user
    as a list of strings
    '''

def fuzzy_match(file_name):
    """Fuzzy image match - takes filename file
    from the folder and tries to find that
    picture on the screen"""
    #take the screenshot first
    threshold = 0.9
    screen = autopy.bitmap.capture_screen()
    #now open the file
    a_file = autopy.bitmap.Bitmap.open(file_name)
    #first we attempt non-fuzzy search
    result = screen.find_bitmap(a_file)# result to postac (int, int)
    if result is None: # then we start fuzzy search
        a_file = cv2.imread(a_file)
        (a_fileHeight, a_fileWidth) = a_file.shape[:2]
        screen = cv2.imread(screen)
        match = cv2.matchTemplate(screen, a_file, cv2.TM_CCOEFF)
        (_, _, minLoc, maxLoc) = cv2.minMaxLoc(match)
        # grab the bounding box of waldo and extract him from
        # the puzzle image
        topLeft = maxLoc
        botRight = (topLeft[0] + a_fileWidth, topLeft[1] + a_fileHeight)
        #
        #img = cv2.imread(sys.argv[1])
        #template = cv2.imread(sys.argv[2])
        #th, tw = template.shape[:2]
        #result = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
        loc = numpy.where(match >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen, pt, (pt[0] + a_fileHeight, pt[1] + a_fileWidth), 0, 2)
        # we got a sqare, now lets find its middle
        #halfWidth = a_fileWidth/2
        #halfHeight = a_fileHeight/2
        #center = result = topLeft[0]+halfWidth, topLeft[1]+halfHeight
        #center is what we've been looking for!
        cv2.imwrite('/home/winnetou/Pictues/new_one.png', screen)
    return result

def fuzzy_match_and_click(img):
    ''' '''
    place = fuzzy_match(img)
    place = click(img)


class Screen(object):
    """Moze by dziedziczyl po """
    def __init__(self, url):
        super(Screen, self).__init__()
        screenshot = browser.take_screenshot()
        self.screenshot = screenshot


