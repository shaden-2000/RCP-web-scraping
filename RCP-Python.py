#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from lxml import etree
import re


# In[2]:


#headers

#to get parent_model with out the home , we save the (li) html tag that contain the parent_models in a list and index the parents with out the home 
def get_parent_model(_soup):
        lists = _soup.find_all('li', class_ ='bdc-Breadcrumb_Item')
        x = []
        for item in lists[1:]:
            x.append(item.find('span').text)
        return x
    

def get_marketing_name(dom):
    marketing_name = dom.xpath('/html/body/main/section[1]/section/div/div/div/div[2]/div/div[1]/header/p/text()')
    return marketing_name


  
def get_weight(dom):
    weight=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[10]/div[2]/div/p/text()')
    return weight



def get_currency(dom):
    currency=dom.xpath('/html/body/header/div[2]/div[1]/div/div/div/div/div/select/option[1]/text()')
    return currency



def get_price(soup):
    price_elemnt = soup.find('span' , class_='prd-Price_Item prd-Price_Item-regular')
    price =  price_elemnt.get_text(strip=True)
    return price



def get_image_URL(_soup , url):
    image_div = _soup.find('div' , class_ = 'rsp-Image rsp-Image-contain')
    image = image_div.find('img', class_ = 'rsp-Image_Image')
    url = image.get('src') 
    https = "https:"
    image_url = https+url

    return image_url


def get_short_description(dom, url):
    if url == 'https://us.bremont.com/products/s302-jet-r-s':
        short_description=dom.xpath('/html/body/main/section[1]/section/div/div/div/div[2]/div/div[4]/p[2]/text()')
    elif url=='https://us.bremont.com/products/mbii-savanna' or url=='https://us.bremont.com/products/fury-blue':
        short_description=dom.xpath('/html/body/main/section[1]/section/div/div/div/div[2]/div/div[3]/p/text()')
    else:
        short_description=soup.find_all(class_='prd-Product_ShortDesc fz-14_24 rte-RichText')[0].select('div p:nth-of-type(2)')[0].text
    return short_description


# we use the elif because these 5 watches have one different path from the others so we call the get_reference_numbe function to get the reference_number for these 5 watches so we can assign there own path to them
def get_case_material(dom,url):
    case_material1 =dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/span/text()')
    case_material2= dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/text()')
    
    if get_reference_number(soup,url,dom) == 'mbii-bk-jet':
        return case_material1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue':
        return case_material1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-orange-bracelet':
        return case_material1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-jet-bracelet':
        return case_material1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue-bracelet':
        return case_material1
    else:
        return case_material2

# we use the elif because these 5 watches have one different path from the others so we call the get_reference_numbe function to get the reference_number for these 5 watches so we can assign there own path to them
def get_caseback(dom,url):
    caseback1 =dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[4]/div[2]/div/p/span/text()')
    caseback2=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[4]/div[2]/div/p/text()')
    if get_reference_number(soup,url,dom) == 'mbii-bk-jet':
        return caseback1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue':
        return caseback1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-orange-bracelet':
        return caseback1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-jet-bracelet':
        return caseback1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue-bracelet':
        return caseback1
    else:
        return  caseback2
    
# we use the elif because these 5 watches have one different path from the others so we call the get_reference_numbe function to get the reference_number for these 5 watches so we can assign there own path to them
def get_diameter(dom,url):
    diameter1 =dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/span/text()')
    diameter2=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/text()')
    if get_reference_number(soup,url,dom) == 'mbii-bk-jet':
        return diameter1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue':
        return diameter1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-orange-bracelet':
        return diameter1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-jet-bracelet':
        return diameter1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue-bracelet':
        return diameter1
    else:
        return  diameter2

# we use the elif because these 5 watches have one different path from the others so we call the get_reference_numbe function to get the reference_number for these 5 watches so we can assign there own path to them
def get_between_lugs(dom,url):
    between_lugs1 =dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/span/text()')
    between_lugs2=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/text()')
    if get_reference_number(soup,url,dom) == 'mbii-bk-jet':
        return between_lugs1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue':
        return between_lugs1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-orange-bracelet':
        return between_lugs1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-jet-bracelet':
        return between_lugs1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue-bracelet':
        return between_lugs1
    else:
        return between_lugs2
# we use the elif because these 5 watches have one different path from the others so we call the get_reference_numbe function to get the reference_number for these 5 watches so we can assign there own path to them
def get_lug_to_lug(dom,url):
    lug_to_lug1 =dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/span/text()')
    lug_to_lug2=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/text()')
    if get_reference_number(soup,url,dom) == 'mbii-bk-jet':
        return lug_to_lug1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue':
        return lug_to_lug1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-orange-bracelet':
        return lug_to_lug1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-jet-bracelet':
        return lug_to_lug1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue-bracelet':
        return lug_to_lug1
    else:
        return lug_to_lug2
# we use the elif because these 5 watches have one different path from the others so we call the get_reference_numbe function to get the reference_number for these 5 watches so we can assign there own path to them
def get_case_thickness(dom,url):
    case_thickness1 =dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/span/text()')
    case_thickness2=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/text()')
    if get_reference_number(soup,url,dom) == 'mbii-bk-jet':
        return case_thickness1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue':
        return case_thickness1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-orange-bracelet':
        return case_thickness1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-jet-bracelet':
        return case_thickness1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue-bracelet':
        return case_thickness1
    else:
        return case_thickness2


    
#we have to chechif 'bazel' word in the 'case' if yes return the 'case' if no 'return empty'
def get_bezel_material(dom,url):
    bezel_material2=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/text()')
    bezel_material1 =dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/span/text()')
    if check_bezel(bezel_material1) == 'YES!':
        return bezel_material1
    
    elif check_bezel(bezel_material2) == 'YES!':
            return bezel_material2
    else:
        return ' '
        
        
        
#we have to check if 'bazel' word in the 'case' if yes return the 'case' if no 'return empty'
def get_bezel_color(dom,url):
    bezel_material2=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/text()')
    bezel_material1 =dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[3]/div[2]/div/p/span/text()')
    if check_bezel(bezel_material1) == 'YES!':
        return bezel_material1
    
    elif check_bezel(bezel_material2) == 'YES!':
            return bezel_material2
    else:
        return ' '

#this is a method used with get_bezel_color and get_bezel_material 
def check_bezel(bezel_material):
    bezel_material_str = str(bezel_material)
    x = re.search(".*bezel", bezel_material_str,re.IGNORECASE)
    if x:
        return 'YES!'
    else:
        return 'No'




    

# we use the elif because these 5 watches have one different path from the others so we call the get_reference_numbe function to get the reference_number for these 5 watches so we can assign there own path to them
def get_dial_color(dom,url):
    dial_color1 =dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[5]/div[2]/div/p/span/text()')
    dial_color2=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[5]/div[2]/div/p/text()')
    
    if get_reference_number(soup,url,dom) == 'mbii-bk-jet':
        return  dial_color1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue':
        return  dial_color1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-orange-bracelet':
        return  dial_color1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-jet-bracelet':
        return  dial_color1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue-bracelet':
        return  dial_color1
    else:
        return dial_color2
# we use the elif because these 5 watches have one different path from the others so we call the get_reference_numbe function to get the reference_number for these 5 watches so we can assign there own path to them   
def get_numerals(dom,url):
    numerals1=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[5]/div[2]/div/p/span/text()')
    numerals2=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[5]/div[2]/div/p/text()')
    if get_reference_number(soup,url,dom) == 'mbii-bk-jet':
        return  numerals1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue':
        return  numerals1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-orange-bracelet':
        return  numerals1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-jet-bracelet':
        return  numerals1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue-bracelet':
        return  numerals1
    else:
        return numerals2





#some watches have diffrante paths because the element 'bracelet' in a list and sometime the list order is different from watch to other  , we notice that when we used 1 path for all watches some watches that have diffrante path for 'bracelet' element it gives me the information of the data below the 'bracelet' which is the 'water_resistance' element , so we use regex to search if it gives me the information of the data below the 'bracelet' if yes then use the other path that it works , if no just give me the original path 
def get_bracelet_material(dom,url):
    
    braclate8 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[8]/div[2]/div/p/text()')
    braclate7 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[7]/div[2]/div/p/text()')
    braclate9 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[9]/div[2]/div/p/text()')
    
    if url == 'https://us.bremont.com/products/s302-blgn-r-s' or url =='https://us.bremont.com/products/s302-blgn-l-s' or url =='https://us.bremont.com/products/s302-gr-r-s' or url =='https://us.bremont.com/products/s302-gr-l-s' or url == 'https://us.bremont.com/products/s302-jet-l-s' or url =='https://us.bremont.com/products/s302-jet-r-s':
        return braclate9
    elif url == 'https://us.bremont.com/products/s502-dlc-bamford-l-s' or url =='https://us.bremont.com/products/w-apexii-bkr-s' or url =='https://us.bremont.com/products/w-apexii-hbr-s' or url =='https://us.bremont.com/products/w-apexii-b' or url =='https://us.bremont.com/products/s502-bk-l-s' or url =='https://us.bremont.com/products/s502-bk-r-s' or url=='https://us.bremont.com/products/s502-bk-b' or url =='https://us.bremont.com/products/supermarine-chrono-jet':
        return braclate8
    elif url == 'https://us.bremont.com/products/s300-vigo-strap' or url =='https://us.bremont.com/products/s300-kaimu-strap':
        return braclate7
    else:
        return ' '

#some watches have diffrante paths because the element 'bracelet' in a list and sometime the list order is different from watch to other  , we notice that when we used 1 path for all watches some watches that have diffrante path for 'bracelet' element it gives me the information of the data below the 'bracelet' which is the 'water_resistance' element , so we use regex to search if it gives me the information of the data below the 'bracelet' if yes then use the other path that it works , if no just give me the original path 
def get_bracelet_color(dom,url):
    
    braclate8 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[8]/div[2]/div/p/text()')
    braclate7 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[7]/div[2]/div/p/text()')
    braclate9 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[9]/div[2]/div/p/text()')
    
    if url == 'https://us.bremont.com/products/s302-blgn-r-s' or url =='https://us.bremont.com/products/s302-blgn-l-s' or url =='https://us.bremont.com/products/s302-gr-r-s' or url =='https://us.bremont.com/products/s302-gr-l-s' or url == 'https://us.bremont.com/products/s302-jet-l-s' or url =='https://us.bremont.com/products/s302-jet-r-s':
        return braclate9
    elif url == 'https://us.bremont.com/products/s502-dlc-bamford-l-s' or url =='https://us.bremont.com/products/w-apexii-bkr-s' or url =='https://us.bremont.com/products/w-apexii-hbr-s' or url =='https://us.bremont.com/products/w-apexii-b' or url =='https://us.bremont.com/products/s502-bk-l-s' or url =='https://us.bremont.com/products/s502-bk-r-s' or url=='https://us.bremont.com/products/s502-bk-b' or url =='https://us.bremont.com/products/supermarine-chrono-jet':
        return braclate8
    elif url == 'https://us.bremont.com/products/s300-vigo-strap' or url =='https://us.bremont.com/products/s300-kaimu-strap':
        return braclate7
    else:
        return ' '
    
    
#some watches have diffrante paths because the element 'bracelet' in a list and sometime the list order is different from watch to other  , we notice that when we used 1 path for all watches some watches that have diffrante path for 'bracelet' element it gives me the information of the data below the 'bracelet' which is the 'water_resistance' element , so we use regex to search if it gives me the information of the data below the 'bracelet' if yes then use the other path that it works , if no just give me the original path 
def get_clasp_type(dom,url):
    
    braclate8 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[8]/div[2]/div/p/text()')
    braclate7 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[7]/div[2]/div/p/text()')
    braclate9 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[9]/div[2]/div/p/text()')
    
    if url == 'https://us.bremont.com/products/s302-blgn-r-s' or url =='https://us.bremont.com/products/s302-blgn-l-s' or url =='https://us.bremont.com/products/s302-gr-r-s' or url =='https://us.bremont.com/products/s302-gr-l-s' or url == 'https://us.bremont.com/products/s302-jet-l-s' or url =='https://us.bremont.com/products/s302-jet-r-s':
        return braclate9
    elif url == 'https://us.bremont.com/products/s502-dlc-bamford-l-s' or url =='https://us.bremont.com/products/w-apexii-bkr-s' or url =='https://us.bremont.com/products/w-apexii-hbr-s' or url =='https://us.bremont.com/products/w-apexii-b' or url =='https://us.bremont.com/products/s502-bk-l-s' or url =='https://us.bremont.com/products/s502-bk-r-s' or url=='https://us.bremont.com/products/s502-bk-b' or url =='https://us.bremont.com/products/supermarine-chrono-jet':
        return braclate8
    elif url == 'https://us.bremont.com/products/s300-vigo-strap' or url =='https://us.bremont.com/products/s300-kaimu-strap':
        return braclate7
    else:
        return ' '






    

# We must clarify two things in this method
#1-#some watches have diffrante paths because the element 'water_resistance' in a list and sometime the list order is different from watch to other  , we notice that when we used 1 path for all watches some watches that have diffrante path for 'water_resistance' element it gives me the information of the data below the 'bracelet'  , so we use regex to search if it gives me the information of the data below the 'water_resistance' if yes then use the other path that it works , if no just give me the original path 
#2-# we use the elif because these 5 watches have one different path from the others so we call the get_reference_numbe function to get the reference_number for these 5 watches so we can assign there own path to them   
def get_water_resistance(dom):
    water1 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[6]/div[2]/div/p/text()')
    water2 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[7]/div[2]/div/p/text()')
    water3 = dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[7]/div[2]/div/p/span/text()')
    if check2(water1) == 'YES!':
        return water2
    elif get_reference_number(soup,url,dom) == 'mbii-bk-jet':
        return  water3
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue':
        return  water3
    elif get_reference_number(soup,url,dom) == 'mbii-bk-orange-bracelet':
        return  water3
    elif get_reference_number(soup,url,dom) == 'mbii-bk-jet-bracelet':
        return  water3
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue-bracelet':
        return  water3
    
    else:
        return water1


# used with get_water_resistance()       
def check2(water1):
    water1_str = str(water1)
    x = re.search(".*crystal", water1_str)
    if x:
        return 'YES!'
    else:
        return 'No'

    
# We must clarify two things in this method
#1-some watches have diffrante paths because the element 'crystal' in a list and sometime the list order is different from watch to other  , we notice that when we used 1 path for all watches some watches that have diffrante path for 'crystal' element it gives me the information of the data below the 'crystal'  , so we use regex to search if it gives me the information of the data below the 'crystal' if yes then use the other path that it works , if no just give me the original path 
#2-we use the elif because these 5 watches have one different path from the others so we call the get_reference_numbe function to get the reference_number for these 5 watches so we can assign there own path to them   
def get_crystal(dom):
    crystal1= dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[6]/div[2]/div/p/span/text()')
    crystal2= dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[6]/div[2]/div/p/text()')
    
    if check_crystal(crystal1) != 'YES!':
        if get_reference_number(soup,url,dom) == 'mbii-bk-jet':
            return  crystal1
        elif get_reference_number(soup,url,dom) == 'mbii-bl-blue':
            return  crystal1
        elif get_reference_number(soup,url,dom) == 'mbii-bk-orange-bracelet':
            return  crystal1
        elif get_reference_number(soup,url,dom) == 'mbii-bk-jet-bracelet':
            return  crystal1
        elif get_reference_number(soup,url,dom) == 'mbii-bl-blue-bracelet':
            return  crystal1
        elif url == 'https://us.bremont.com/products/s300-kaimu' or url == 'https://us.bremont.com/products/s300-vigo' or url =='https://us.bremont.com/products/s300-kaimu-strap' or url =='https://us.bremont.com/products/s300-vigo-strap':
            return ' '
        else:
            return crystal2
    else:
        return ' '



    
     
# used with get_crystal()
def check_crystal(crystal):
    crystal_str = str(crystal)
    x = re.search(".*metres", crystal_str)
    if x:
        return 'YES!'
    else:
        return 'No'



def get_movement(soup):
    movement_details = None
    try:
        prod_content = soup.find('div', class_='prd-TechSpec_Content')
        prod_body_content = prod_content.find('div', attrs={'data-el': 'product-accordions.body'})
        movement_details = prod_body_content.find('p').text
    except AttributeError as e:
        print(e)
    return movement_details
    
def get_caliber(soup):
    movement_details = None
    try:
        prod_content = soup.find('div', class_='prd-TechSpec_Content')
        prod_body_content = prod_content.find('div', attrs={'data-el': 'product-accordions.body'})
        movement_details = prod_body_content.find('p').text
    except AttributeError as e:
        print(e)
    return movement_details

def get_power_reserve(soup):
    movement_details = None
    try:
        prod_content = soup.find('div', class_='prd-TechSpec_Content')
        prod_body_content = prod_content.find('div', attrs={'data-el': 'product-accordions.body'})
        movement_details = prod_body_content.find('p').text
    except AttributeError as e:
        print(e)
    return movement_details

def get_frequency(soup):
    movement_details = None
    try:
        prod_content = soup.find('div', class_='prd-TechSpec_Content')
        prod_body_content = prod_content.find('div', attrs={'data-el': 'product-accordions.body'})
        movement_details = prod_body_content.find('p').text
    except AttributeError as e:
        print(e)
    return movement_details

def get_jewels(soup):
    movement_details = None
    try:
        prod_content = soup.find('div', class_='prd-TechSpec_Content')
        prod_body_content = prod_content.find('div', attrs={'data-el': 'product-accordions.body'})
        movement_details = prod_body_content.find('p').text
    except AttributeError as e:
        print(e)
    return movement_details


# we use the elif because these 5 watches have one different path from the others so we call the get_reference_numbe function to get the reference_number for these 5 watches so we can assign there own path to them   
def get_features(dom):
    features1=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[2]/div[2]/div/p/span/text()')
    features2=dom.xpath('/html/body/main/section[4]/section/div/div/div/div/div[2]/div/div/product-accordions/ul/li[2]/div[2]/div/p/text()')
    if get_reference_number(soup,url,dom) == 'mbii-bk-jet':
        return  features1
    if get_reference_number(soup,url,dom) == 'mbii-bk-orange':
        return  features1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue':
        return  features1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-orange-bracelet':
        return  features1
    elif get_reference_number(soup,url,dom) == 'mbii-bk-jet-bracelet':
        return  features1
    elif get_reference_number(soup,url,dom) == 'mbii-bl-blue-bracelet':
        return  features1
    else:
        return features2




def get_description(dom, soup, url):
    description_map = {
        'https://us.bremont.com/products/rapha-mbiii': '/html/body/main/section[3]/section/div/div/div/section/div/div/div/div[1]/div/div/div/text()',
        'https://us.bremont.com/products/mbii-savanna': '/html/body/main/section[3]/section/div/div/div/section/div/div/div/div[1]/div/div/div/p/text()',
        'https://us.bremont.com/products/bronze-argonaut-blue': '/html/body/main/section[3]/section/div/div/div/section/div/div/div/div[1]/div/div/div/span/text()',
        # Add other URLs and their corresponding XPath or BeautifulSoup selectors here
    }
    
    if url in description_map:
        description = dom.xpath(description_map[url])
    else:
        # If URL not found in the map, use a default selector
        description = soup.find('div', class_='prd-Description_Description rte-RichText fz-14_24').text.strip()
    
    return description
    
def get_reference_number(soup,url,dom):
    reference_number = url.rsplit('/', 1)[-1]
    return reference_number


# In[11]:


# url = 'https://us.bremont.com/products/s502-dlc-bamford-l-s'
# html= requests.get(url)
# soup = BeautifulSoup(html.content, "html.parser")
# dom = etree.HTML(str(soup))


# marketing_name = get_marketing_name(dom)

# marketing_name_string=str(marketing_name)
# marketing_name_without_brackets = marketing_name_string[1:-1]



# print(marketing_name_without_brackets)


# In[3]:


# sea collection
url_ = 'https://us.bremont.com/collections/supermarine'
html = requests.get(url_)
soup_ = BeautifulSoup(html.content, "html.parser")




sea_collections = soup_.find_all('div' , class_ = 'prd-Card prd-Card-grid util-FauxLink')




    

sea_urls = []   
for item in sea_collections:
    a_tag = item.find('a', class_ = 'util-FauxLink_Link')
    href  = a_tag.get('href')
    url = "https://us.bremont.com"+href
    sea_urls.append(url)
    
print(sea_urls)




# In[4]:


#air collection
url_air = 'https://us.bremont.com/collections/altitude'
html = requests.get(url_air)
soup_ = BeautifulSoup(html.content, "html.parser")




air_collections = soup_.find_all('div' , class_ = 'prd-Card prd-Card-grid util-FauxLink')




    

air_urls = []   
for item in air_collections:
    a_tag = item.find('a', class_ = 'util-FauxLink_Link')
    href  = a_tag.get('href')
    url = "https://us.bremont.com"+href
    air_urls.append(url)
    
air_urls


# In[5]:


#land collection
url_ = 'https://us.bremont.com/collections/the-armed-forces-collection'
html = requests.get(url_)
soup_ = BeautifulSoup(html.content, "html.parser")




land_collections = soup_.find_all('div' , class_ = 'prd-Card prd-Card-grid util-FauxLink')


land_urls = []   
for item in land_collections:
    a_tag = item.find('a', class_ = 'util-FauxLink_Link')
    href  = a_tag.get('href')
    url = "https://us.bremont.com"+href
    land_urls.append(url)
    
land_urls


# In[6]:


#for loop to get sea_list
sea_list = []
for url in  sea_urls:
    html= requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    dom = etree.HTML(str(soup))
    


    bracelet_material=get_bracelet_material(dom,url)
    bracelet_color=get_bracelet_color(dom,url)
    clasp_type=get_clasp_type(dom,url)
    water_resistance=get_water_resistance(dom)
    crystal=get_crystal(dom)
    watch_URL = url
    brand = 'Bremont'
    made_in = 'United Kingdom'
    parent = get_parent_model(soup)
    marketing_name = get_marketing_name(dom)
    weight = get_weight(dom)
    currency = get_currency(dom)
    price = get_price(soup)
    image_URL=get_image_URL(soup,url)
    short_description=get_short_description(dom, url)
    case_material=get_case_material(dom,url)
    caseback=get_caseback(dom,url)
    diameter=get_diameter(dom,url)
    between_lugs=get_between_lugs(dom,url)
    lug_to_lug=get_lug_to_lug(dom,url)
    case_thickness=get_case_thickness(dom,url)
    bezel_material=get_bezel_material(dom,url)
    bezel_color=get_bezel_color(dom,url)
    dial_color=get_dial_color(dom,url)
    numerals=get_numerals(dom,url)
    movement=get_movement(soup)
    caliber=get_caliber(soup)
    power_reserve=get_power_reserve(soup)
    frequency=get_frequency(soup)
    jewels=get_jewels(soup)
    features=get_features(dom)
    description=get_description(dom, soup, url)
    reference_number=get_reference_number(soup,url,dom)
    type_ = ' '
    year_introduced =' '
    specific_model = ' '
    nickname = ' '
    style = ' '
    case_shape =' '
    case_finish = ' '
    
    
    marketing_name_string=str(marketing_name)
    marketing_name_without_brackets = marketing_name_string[1:-1]
    weight_string=str(weight)
    weight_without_brackets = weight_string[1:-1]
    parent_string=str(parent)
    parent_without_brackets = parent_string[1:-1]
    currency_string=str(currency)
    currency_without_brackets = currency_string[1:-1]
    case_material_string=str(case_material)
    case_material_without_brackets = case_material_string[1:-1]
    caseback_string=str(caseback)
    caseback_without_brackets = caseback_string[1:-1]
    diameter_string=str(diameter)
    diameter_without_brackets = diameter_string[1:-1]
    between_lugs_string=str(between_lugs)
    between_lugs_without_brackets = between_lugs_string[1:-1]
    case_thickness_string=str(case_thickness)
    case_thickness_without_brackets = case_thickness_string[1:-1]
    lug_to_lug_string=str(lug_to_lug)
    lug_to_lug_without_brackets = lug_to_lug_string[1:-1]
    bezel_material_string=str(bezel_material)
    bezel_material_without_brackets = bezel_material_string[1:-1]
    bezel_color_string=str(bezel_color)
    bezel_color_without_brackets = bezel_color_string[1:-1]
    dial_color_string=str(dial_color)
    dial_color_without_brackets = dial_color_string[1:-1]
    numerals_string=str(numerals)
    numerals_without_brackets = numerals_string[1:-1]
    bracelet_material_string=str(bracelet_material)
    bracelet_material_without_brackets = bracelet_material_string[1:-1]
    bracelet_color_string=str(bracelet_color)
    bracelet_color_without_brackets = bracelet_color_string[1:-1]
    clasp_type_string=str(clasp_type)
    clasp_type_without_brackets = clasp_type_string[1:-1]
    features_string=str(features)
    features_without_brackets = features_string[1:-1]
    water_resistance_string=str(water_resistance)
    water_resistance_without_brackets = water_resistance_string[1:-1]
    crystal_string=str(crystal)
    crystal_without_brackets = crystal_string[1:-1]


    


    
    
    
    
    sea_list.append([reference_number,watch_URL,made_in,brand,parent_without_brackets, marketing_name_without_brackets,weight_without_brackets,currency_without_brackets,price,image_URL, case_material_without_brackets,caseback_without_brackets,diameter_without_brackets,between_lugs_without_brackets,lug_to_lug_without_brackets,case_thickness_without_brackets, bezel_material_without_brackets,bezel_color_without_brackets,dial_color_without_brackets,numerals_without_brackets,bracelet_material_without_brackets,bracelet_color_without_brackets,clasp_type_without_brackets,movement,caliber,power_reserve,frequency,jewels,features_without_brackets,water_resistance_without_brackets,description,short_description,crystal_without_brackets,type_,year_introduced,specific_model,nickname,style,case_shape,case_finish])


# In[7]:


#for loop to get air_list
air_list = []
for url in  air_urls:
    html= requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    dom = etree.HTML(str(soup))
    
    
    bracelet_material=get_bracelet_material(dom,url)
    bracelet_color=get_bracelet_color(dom,url)
    clasp_type=get_clasp_type(dom,url)
    water_resistance=get_water_resistance(dom)
    crystal=get_crystal(dom)
    watch_URL = url
    brand = 'Bremont'
    made_in = 'United Kingdom'
    parent = get_parent_model(soup)
    marketing_name = get_marketing_name(dom)
    weight = get_weight(dom)
    currency = get_currency(dom)
    price = get_price(soup)
    image_URL=get_image_URL(soup,url)
    short_description=get_short_description(dom, url)
    case_material=get_case_material(dom,url)
    caseback=get_caseback(dom,url)
    diameter=get_diameter(dom,url)
    between_lugs=get_between_lugs(dom,url)
    lug_to_lug=get_lug_to_lug(dom,url)
    case_thickness=get_case_thickness(dom,url)
    bezel_material=get_bezel_material(dom,url)
    bezel_color=get_bezel_color(dom,url)
    dial_color=get_dial_color(dom,url)
    numerals=get_numerals(dom,url)
    movement=get_movement(soup)
    caliber=get_caliber(soup)
    power_reserve=get_power_reserve(soup)
    frequency=get_frequency(soup)
    jewels=get_jewels(soup)
    features=get_features(dom)
    description=get_description(dom, soup, url)
    reference_number=get_reference_number(soup,url,dom)
    type_ = ' '
    year_introduced =' '
    specific_model = ' '
    nickname = ' '
    style = ' '
    case_shape =' '
    case_finish = ' '
    
    
    marketing_name_string=str(marketing_name)
    marketing_name_without_brackets = marketing_name_string[1:-1]
    weight_string=str(weight)
    weight_without_brackets = weight_string[1:-1]
    parent_string=str(parent)
    parent_without_brackets = parent_string[1:-1]
    currency_string=str(currency)
    currency_without_brackets = currency_string[1:-1]
    case_material_string=str(case_material)
    case_material_without_brackets = case_material_string[1:-1]
    caseback_string=str(caseback)
    caseback_without_brackets = caseback_string[1:-1]
    diameter_string=str(diameter)
    diameter_without_brackets = diameter_string[1:-1]
    between_lugs_string=str(between_lugs)
    between_lugs_without_brackets = between_lugs_string[1:-1]
    case_thickness_string=str(case_thickness)
    case_thickness_without_brackets = case_thickness_string[1:-1]
    lug_to_lug_string=str(lug_to_lug)
    lug_to_lug_without_brackets = lug_to_lug_string[1:-1]
    bezel_material_string=str(bezel_material)
    bezel_material_without_brackets = bezel_material_string[1:-1]
    bezel_color_string=str(bezel_color)
    bezel_color_without_brackets = bezel_color_string[1:-1]
    dial_color_string=str(dial_color)
    dial_color_without_brackets = dial_color_string[1:-1]
    numerals_string=str(numerals)
    numerals_without_brackets = numerals_string[1:-1]
    bracelet_material_string=str(bracelet_material)
    bracelet_material_without_brackets = bracelet_material_string[1:-1]
    bracelet_color_string=str(bracelet_color)
    bracelet_color_without_brackets = bracelet_color_string[1:-1]
    clasp_type_string=str(clasp_type)
    clasp_type_without_brackets = clasp_type_string[1:-1]
    features_string=str(features)
    features_without_brackets = features_string[1:-1]
    water_resistance_string=str(water_resistance)
    water_resistance_without_brackets = water_resistance_string[1:-1]
    crystal_string=str(crystal)
    crystal_without_brackets = crystal_string[1:-1]
    
    

    
    air_list.append([reference_number,watch_URL,made_in,brand,parent_without_brackets, marketing_name_without_brackets,weight_without_brackets,currency_without_brackets,price,image_URL, case_material_without_brackets,caseback_without_brackets,diameter_without_brackets,between_lugs_without_brackets,lug_to_lug_without_brackets,case_thickness_without_brackets, bezel_material_without_brackets,bezel_color_without_brackets,dial_color_without_brackets,numerals_without_brackets,bracelet_material_without_brackets,bracelet_color_without_brackets,clasp_type_without_brackets,movement,caliber,power_reserve,frequency,jewels,features_without_brackets,water_resistance_without_brackets,description,short_description,crystal_without_brackets,type_,year_introduced,specific_model,nickname,style,case_shape,case_finish])


# In[8]:


#for loop to get land_list 
land_list  = []
for url in  land_urls:
    html= requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    dom = etree.HTML(str(soup))
    
    bracelet_material=get_bracelet_material(dom,url)
    bracelet_color=get_bracelet_color(dom,url)
    clasp_type=get_clasp_type(dom,url)
    water_resistance=get_water_resistance(dom)
    crystal=get_crystal(dom)
    watch_URL = url
    brand = 'Bremont'
    made_in = 'United Kingdom'
    parent = get_parent_model(soup)
    marketing_name = get_marketing_name(dom)
    weight = get_weight(dom)
    currency = get_currency(dom)
    price = get_price(soup)
    image_URL=get_image_URL(soup,url)
    short_description=get_short_description(dom, url)
    case_material=get_case_material(dom,url)
    caseback=get_caseback(dom,url)
    diameter=get_diameter(dom,url)
    between_lugs=get_between_lugs(dom,url)
    lug_to_lug=get_lug_to_lug(dom,url)
    case_thickness=get_case_thickness(dom,url)
    bezel_material=get_bezel_material(dom,url)
    bezel_color=get_bezel_color(dom,url)
    dial_color=get_dial_color(dom,url)
    numerals=get_numerals(dom,url)
    movement=get_movement(soup)
    caliber=get_caliber(soup)
    power_reserve=get_power_reserve(soup)
    frequency=get_frequency(soup)
    jewels=get_jewels(soup)
    features=get_features(dom)
    description=get_description(dom, soup, url)
    reference_number=get_reference_number(soup,url,dom)
    type_ = ' '
    year_introduced =' '
    specific_model = ' '
    nickname = ' '
    style = ' '
    case_shape =' '
    case_finish = ' '
    
    marketing_name_string=str(marketing_name)
    marketing_name_without_brackets = marketing_name_string[1:-1]
    weight_string=str(weight)
    weight_without_brackets = weight_string[1:-1]
    parent_string=str(parent)
    parent_without_brackets = parent_string[1:-1]
    currency_string=str(currency)
    currency_without_brackets = currency_string[1:-1]
    case_material_string=str(case_material)
    case_material_without_brackets = case_material_string[1:-1]
    caseback_string=str(caseback)
    caseback_without_brackets = caseback_string[1:-1]
    diameter_string=str(diameter)
    diameter_without_brackets = diameter_string[1:-1]
    between_lugs_string=str(between_lugs)
    between_lugs_without_brackets = between_lugs_string[1:-1]
    case_thickness_string=str(case_thickness)
    case_thickness_without_brackets = case_thickness_string[1:-1]
    lug_to_lug_string=str(lug_to_lug)
    lug_to_lug_without_brackets = lug_to_lug_string[1:-1]
    bezel_material_string=str(bezel_material)
    bezel_material_without_brackets = bezel_material_string[1:-1]
    bezel_color_string=str(bezel_color)
    bezel_color_without_brackets = bezel_color_string[1:-1]
    dial_color_string=str(dial_color)
    dial_color_without_brackets = dial_color_string[1:-1]
    numerals_string=str(numerals)
    numerals_without_brackets = numerals_string[1:-1]
    bracelet_material_string=str(bracelet_material)
    bracelet_material_without_brackets = bracelet_material_string[1:-1]
    bracelet_color_string=str(bracelet_color)
    bracelet_color_without_brackets = bracelet_color_string[1:-1]
    clasp_type_string=str(clasp_type)
    clasp_type_without_brackets = clasp_type_string[1:-1]
    features_string=str(features)
    features_without_brackets = features_string[1:-1]
    water_resistance_string=str(water_resistance)
    water_resistance_without_brackets = water_resistance_string[1:-1]
    crystal_string=str(crystal)
    crystal_without_brackets = crystal_string[1:-1]
    


   

    


    
    
    
    
    land_list.append([reference_number,watch_URL,made_in,brand,parent_without_brackets, marketing_name_without_brackets,weight_without_brackets,currency_without_brackets,price,image_URL, case_material_without_brackets,caseback_without_brackets,diameter_without_brackets,between_lugs_without_brackets,lug_to_lug_without_brackets,case_thickness_without_brackets, bezel_material_without_brackets,bezel_color_without_brackets,dial_color_without_brackets,numerals_without_brackets,bracelet_material_without_brackets,bracelet_color_without_brackets,clasp_type_without_brackets,movement,caliber,power_reserve,frequency,jewels,features_without_brackets,water_resistance_without_brackets,description,short_description,crystal_without_brackets,type_,year_introduced,specific_model,nickname,style,case_shape,case_finish])


# In[9]:


new_columns =['reference_number','watch_URL','made_in','brand','parent','marketing_name','weight','currency','price','image_URL', 'case_material','caseback','diameter','between_lugs','lug_to_lug','case_thickness','bezel_material','bezel_color','dial_color','numerals','bracelet_material','bracelet_color','clasp_type','movement','caliber','power_reserve','frequency','jewels','features','water_resistance','description','short_description','crystal','type','year_introduced','specific_model','nickname','style','case_shape','case_finish']


# In[10]:


#sea
import csv
file_path = '/Users/shadenalshehri/Documents/final_client_project/sea.csv'
with open(file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sea_list)


# In[11]:


#sea
from pandas import read_csv


sea = read_csv('/Users/shadenalshehri/Documents/final_client_project/sea.csv',header=None)
sea.to_csv('/Users/shadenalshehri/Documents/final_client_project/sea.csv',index=True)


# In[12]:


#air
import csv
file_path = '/Users/shadenalshehri/Documents/final_client_project/air.csv'
with open(file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(air_list)


# In[13]:


#air
from pandas import read_csv     

air = read_csv('/Users/shadenalshehri/Documents/final_client_project/air.csv',header=None)
air.to_csv('/Users/shadenalshehri/Documents/final_client_project/air.csv',index=True)


# In[14]:


#land
import csv
file_path = '/Users/shadenalshehri/Documents/final_client_project/land.csv'
with open(file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(land_list)


# In[15]:


#land
from pandas import read_csv      
land = read_csv('/Users/shadenalshehri/Documents/final_client_project/land.csv',header=None)
land.to_csv('/Users/shadenalshehri/Documents/final_client_project/land.csv',index=True)


# In[16]:


# Concatenate the three DataFrames 'collections'
import pandas as pd
table = [sea, air,land]
sea_air_land = pd.concat(table)

sea_air_land.columns = new_columns
sea_air_land.set_index(sea_air_land.columns[0], inplace=True)


sea_air_land.to_csv('/Users/shadenalshehri/Documents/final_client_project/sea_air_land.csv',index=True)




# In[18]:




sea_air_land = pd.read_csv('/Users/shadenalshehri/Documents/final_client_project/sea_air_land.csv')

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
sea_air_land.to_csv('/Users/shadenalshehri/Documents/final_client_project/sea_air_land_cleaned.csv', index=False)

