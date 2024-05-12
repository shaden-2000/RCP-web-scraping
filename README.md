# RCP-web-scraping

- It's real client project in the data engineering bootcamp facilitated by the Saudi Digital Academy in
cooperation with Weclouddata Academy. 

### After communicating with the client and understanding his needs and goals, we began dividing and understanding the tasks

- ### we have 4 major tasks

1. we have a target website (Bremont) and we have to define what data must be collected
2. we have to extract and analyze the source code
3. we have to save the data into csv file 
4. we have to clean the csv file 


<img width="1419" alt="Screenshot 1445-11-04 at 10 13 39 PM" src="https://github.com/shaden-2000/RCP-web-scraping/assets/100734021/22827df2-a039-4a72-9e1e-cef6a3292c11">




### Let's break down the tasks further, let's start with the first task

1. so we know the target website is ( Bremont ) and this is the data that must be collected

<img width="172" alt="Screenshot 1445-11-04 at 10 02 06 PM" src="https://github.com/shaden-2000/RCP-web-scraping/assets/100734021/6eb4305d-ad89-490c-a9f8-9492372ed1b3">



2. we have to extract and analyze the source code by using Web Inspector

<img width="1512" alt="Screenshot 1445-11-04 at 10 35 00 PM" src="https://github.com/shaden-2000/RCP-web-scraping/assets/100734021/160dbc3c-a6f6-448f-bee9-c6df1a386eb3">



3. we have to build a scraper in python , we used python's Beautiful Soup library, to do the scraping we have to use :
1.  requests : A user-friendly HTTP library for sending HTTP/1.1 requests simply.
2.  BeautifulSoup: A library for parsing HTML and XML documents, enabling easy navigation and search through the parse tree for web scraping.
  - BeautifulSoup parses HTML/XML data.
- we need to install them

``` pip install requests```
``` pip install BeautifulSoup4```

- The first step in web scraping is to access the target website.
- We use the ```requests.get()``` method to make a GET request to the website.

```
import requests
URL ='https://us.bremont.com'
page = requests.get(URL)
```
- Parse the Content: Utilize BeautifulSoup to parse the fetched webpage content. After fetching the webpage content, we need a way to parse and extract the information we need. This is where `BeautifulSoup` comes into play.
```soup = BeautifulSoup(html.content, "html.parser")```

- Extract Data: Navigate the parse tree to find and extract the desired data. Once we've created a `BeautifulSoup` object, i can find specific data by navigating through the parse tree. i can search for data using tag names, IDs, classes, and much more.
```
 image_div = _soup.find('div' , class_ = 'rsp-Image rsp-Image-contain')
 image = image_div.find('img', class_ = 'rsp-Image_Image')
 url = image.get('src') 
 https = "https:"
 image_url = https+url
```

3. we have to save the data into csv file

```
new_columns =['reference_number','watch_URL','made_in','brand','parent','marketing_name','weight','currency','price','image_URL', 'case_material','caseback','diameter','between_lugs','lug_to_lug','case_thickness','bezel_material','bezel_color','dial_color','numerals','bracelet_material','bracelet_color','clasp_type','movement','caliber','power_reserve','frequency','jewels','features','water_resistance','description','short_description','crystal','type','year_introduced','specific_model','nickname','style','case_shape','case_finish']

file_path = '/Users/*/*/final_client_project/sea.csv'
with open(file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sea_list)

sea = read_csv('/Users/shadenalshehri/Documents/final_client_project/sea.csv',header=None)
sea.to_csv('/Users/*/*/final_client_project/sea.csv',index=True)


```

4. we have to clean the csv file
```
# Clean up
sea_air_land = sea_air_land.applymap(lambda x: x.strip("'") if isinstance(x, str) else x)
# Remove non-numeric characters from the 'price' column
sea_air_land['price'] = sea_air_land['price'].replace({'\$': '', ',': ''}, regex=True)
# Convert the cleaned 'price' column to float
sea_air_land['price'] = sea_air_land['price'].astype(float)
sea_air_land['diameter'] = sea_air_land['diameter'].str.extract(r'(\d+mm)')
sea_air_land['between_lugs'] = sea_air_land['between_lugs'].str.extract(r'(?i)(Strap fitting|Strap width|Lug width)[:\s]+(\d+)\s*mm')[1] + 'mm'
sea_air_land['lug_to_lug'] = sea_air_land['lug_to_lug'].astype(str).str.extract(r'(?:Case Length:|lug to lug)\s*(\d+mm)')
sea_air_land['case_thickness'] = sea_air_land['case_thickness'].apply(lambda x: re.search(r'(?:Case Depth:|Case Depth|Depth:|Depth)\s*([\d.]+)mm', x).group(1) if re.search(r'(?:Case Depth:|Case Depth|Depth:|Depth)\s*([\d.]+)mm', x) else None)
sea_air_land.loc[sea_air_land['crystal'].str.contains(r'sapphire crystal', case=False, na=False), 'crystal'] = 'Sapphire Crystal'
sea_air_land['weight'] = sea_air_land['weight'].str.extract(r'(\d+g)')
sea_air_land['water_resistance'] = sea_air_land['water_resistance'].str.extract(r'(\d+\s*(?:ATM|atm)?[\/,]?\s*\d+\s*(?:Metres|metres)?)')

# Save the modified DataFrame to a new CSV file
sea_air_land.to_csv('/Users/*/*/*/sea_air_land_cleaned.csv', index=False)
```





#### Skills Applied:
1. Web scraping using Python's Beautiful Soup library
2. Data cleaning and preprocessing with Pandas
3. Team collaboration and communication
4. Client interaction and stakeholder engagement
5. Delivered high-quality, cleaned datasets to the client within agreed-upon timelines.








