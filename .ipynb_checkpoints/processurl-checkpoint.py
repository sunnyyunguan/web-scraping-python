def get_response(product):
    
    output_csv = product["name"] + "web_data.csv"    
    
    alert = False
    
    # add user agent 
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
                         
    # HTTP Request
    webpage = requests.get(url, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

    # Store the links
    links_list = []

    d = {"title":[], "discounted_price":[], "discount_percent":[], "price":[], "rating":[], "reviews":[],"availability":[]}

    # Loop for extracting links from Tag Objects
    for link in links:
            links_list.append(link.get('href'))

    # Loop for extracting product details from each link 
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Function calls to display all necessary product information if discount >= threshold
        if get_discount(new_soup) >= product["alert_discount"]
            alert = True        
            d['title'].append(get_title(new_soup))
            d['discounted_price'].append(get_discounted_price(new_soup))
            d['discount_percent'].append(get_discount(new_soup))
            d['price'].append(get_price(new_soup))
            d['rating'].append(get_rating(new_soup))
            d['reviews'].append(get_review_count(new_soup))
            d['availability'].append(get_availability(new_soup))
        else
            continue

    # check if data exists -> generate csv file and send email
    if not d:
        # no data available
        with open("output.txt", "w") as text_file:
            text_file.write("no product meets threshold.")
    else
        df = pd.DataFrame.from_dict(d)
        df['title'].replace('', np.nan, inplace=True)
        df = df.dropna(subset=['title'])

        df['discounted_price'] = pd.to_numeric(df['discounted_price'].replace(r'\$', '',regex=True))
        df['discount_percent'] = pd.to_numeric(df['discount_percent'].map(lambda x: x.rstrip('%')))
        df['price'] = pd.to_numeric(df['price'].replace(r'\$', '',regex=True))
        df['rating'] = df['rating'].replace(r'\ out of 5 stars', '',regex=True)
        df['reviews'] = pd.to_numeric(df['reviews'].replace(r'\ ratings', '',regex=True).replace(r'\ rating','',regex=True).replace(r'\,','',regex=True),downcast ='signed')
        df['availability'] = df['availability'].replace(r'\.', '',regex=True)

        df.to_csv(output_csv, header=True, index=False)
        
        alert = True
        
        return alert
    
    