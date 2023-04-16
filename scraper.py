import csv
import requests
import os

# Set the directory to save the images
SAVE_DIR = 'images'
total_rows = 16578

# Create the save directory if it does not exist
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

progress_bar = 0

# Open the CSV file with the list of image URLs
with open('fitzpatrick17k.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader) # Get the header row if there is one
    
    # Check if the first row is a header
    if header[7] == 'url':
        # Skip the header row
        next(reader)

    http_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

    # Loop through each row of the CSV file
    for row in reader:
        url = row[7]  # Assuming the URLs are in the 8th column of the CSV file

        if len(url) == 0:
            continue
        # print(f'downloading from url: {url}')
        filename = os.path.join(SAVE_DIR,row[0] + '.jpg')  # Get the filename from the URL

        if not os.path.exists(filename):
            # Send a request to download the image
            response = requests.get(url, headers=http_headers)

            if response.status_code == 200:
                with open(filename,'wb') as f:
                    f.write(response.content)
                # print('Image sucessfully Downloaded: ',filename)
            # else:
                # print('Image Could not be retrieved: ', filename)

        progress_bar += 1
        print(f"{progress_bar} rows processed")




