# Function to extract Product Title
def get_title(soup):
    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'}).text.strip()

    except AttributeError:
        title = ""

    return title

# Function to extract discounted Product Price
def get_discounted_price(soup):
    try:
        discounted_price = soup.find("div", attrs={"class":'a-section a-spacing-micro'}).find("span", attrs={"class": "a-price aok-align-center"}).find("span", attrs={"class": "a-offscreen"}).text.strip()

    except AttributeError:
        discounted_price = ""

    return discounted_price

# Function to extract discount
def get_discount(soup):
    try:
        discount = soup.find("div", attrs={"class",'a-section a-spacing-none aok-align-center'}).find("span", attrs={"class":'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'}).text.strip()
        
    except AttributeError:
        discount = ""

    return discount

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("div", attrs={"class",'a-section a-spacing-small aok-align-center'}).find("span", attrs={"class",'a-size-small a-color-secondary aok-align-center basisPrice'}).find("span", attrs={"class", 'a-offscreen'}).text.strip()

    except AttributeError:
        price = ""

    return price

# Function to extract Product Rating
def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).text.strip()
    
    except AttributeError:
            rating = ""

    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).text.strip()

    except AttributeError:
        review_count = ""

    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'}).text.strip()

    except AttributeError:
        available = "Not Available"

    return available
