from bs4 import BeautifulSoup
import pandas as pd
import requests 
def get_data(url):
    x = requests.get(url)
    soup = BeautifulSoup(x.text,
                         "lxml")
    books = soup.find_all("div",
                          class_="pic-card")
    
    
    data=[]

    for book in books:

        item={}
        
        link = book.find("a", class_="link")

        if link and 'alt' in link.find("img").attrs:
            item["Name"] = link.find("img").attrs["alt"]
        else:
            item["Name"] = None
        
        # Find the img element and get the src attribute
        img = book.find("img")
        if img and 'src' in img.attrs:
            item["Image URL"] = str("https://theplace-2.com") + str(img.attrs["src"])
        else:
            item["Image URL"] = None

        data.append(item)
        
    
    return data


    
def export_data(data):
    df = pd.DataFrame(data)
    df.to_excel("books.xlsx")
    df.to_csv("books.csv")

if __name__ == '__main__':
    data = get_data("https://theplace-2.com/")
    export_data(data)
    print("Done.")
              

