import cv2
import autopy
import numpy as np


#def check_screen_on_all_browsers():
#driver as global?

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


###### Helpers section, later to be moved to separate file
def is_a_picture(picture):
    """Provides simple check if 
    argument is a picture """
    pass

def turn_to_bitmap():

###### End of helpers sections




def picture_is_on_page(driver, picture):
    ''' returns boolean: True if found'''
    #if is_a_picture(picture):
            #heere we start matching pics
    #else:
    #    raise TypeError("Image expected, got rotten cabbage instead!")
    # better approach then the above: piggyback on bitmap functionalities
    # turn_to_bitmap will check if arg is a picture and throw error if not
    if not is_instance(driver, selenium.webdriver.webdriver):
        raise TypeError("Webdriver instance was expected, got rotten cabbage instead!")
    try:
        picture = turn_to_bitmap(picture):
        screen = take_screenshot(driver)

        if picture 

    except:
        raise TypeError("Image expected, got rotten cabbage instead!")

def text_is_on_page(element):
    ''' returns boolean: true if found'''
    if is_instance(element, [str, unicode]):
        if len(str)<1:
            raise TypeError("Got empty string!")
    else:
        try:
            element = str(element)
        except:
            raise TypeError("String or stringable thing expected, got rotten cabbage instead!")
    if element in read_screen:
        return True 
    #or maybe better:
    x = get_coordinates(element)
    if x['y']>0 and x['x']>0: #(only when coordinates are number higher than 0 text is visible on page)
        return True 
    return False


def find_on_screen(element):
    '''Finds element by visible text '''
    if is_on_page(element):
        return element
    else
        return None

def get_coordinates(driver, element):
    """ Finds and returns coordinates
    of a html element
    by the way:
    if 
    """
    elem = driver.find_element_by_god_knows_what('')
    coordinates = elem.location
    # 

def find_and_click():
    pass

def find_and_type_into():
    pass

def find_clickable(driver, element):
    ''' Find clickable thing: like a button
    or a link - None if not found
    args :: driver - instance of a webdriver class'''
    if not is_instance(driver, webdriver):
        raise TypeError("")
    clickable = browser.find_elements_by_tag_name("a")
    for t in browser.find_elements_by_tag_name("button"):
        clickable.append(t)
    for w in clickable:
        if w.text == element:
            return element
    return None




def count_elements():
    ''' returns integer - no of elements '''

def read_screen(driver):
    '''Returns all text elements from the screen
    visible to the user
    as a list of strings
    '''
    screentext = 
    return screentext

def layout_check_with_canny(file_name):
    """
    Code used for cross browser checks
    of layout bugs with canny edge detections
    """
    # step 1: open the webpage with all browsers
    # and take screenshots

    # step 2: treat screenshots with a healthy dose of Canny edge detection

    # step 3: compare all files by calculating distance by pixelwise comparison 

def fuzzy_match_with_canny(file_name):
    """
    Code used for cross browser checks
    """

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


