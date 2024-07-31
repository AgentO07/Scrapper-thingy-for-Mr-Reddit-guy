import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import os

def download_images(csv_file, save_directory):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Create directory to save images if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Download and save each image
    for index, row in df.iterrows():
        name = row['Name']
        url = row['Image URL']
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            image = Image.open(BytesIO(response.content))
            
            # Clean the name to be a valid filename
            clean_name = "".join([c if c.isalnum() else "_" for c in name])
            image_path = os.path.join(save_directory, f"{clean_name}.jpg")
            
            image.save(image_path)
            print(f"Saved {name} as {image_path}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {url}: {e}")
        except Exception as e:
            print(f"Failed to save {name}: {e}")

if __name__ == '__main__':
    csv_file = 'books.csv'  # Path to your CSV file
    save_directory = 'downloaded_images'  # Directory to save images
    download_images(csv_file, save_directory)
    print("Done.")
