import csv
import os
import re
from bs4 import BeautifulSoup
from decimal import Decimal

folder_path = './HTML'
file_list = os.listdir(folder_path)

for file in file_list: 
    # Read the contents of the HTML file
    filename = os.path.join('HTML', file)
    with open(filename, 'r') as f:
        html = f.read()

    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the post elements
    divs = soup.find_all("div", {"data-e2e": "user-post-item"})

    # Open a CSV file for writing
    cvsfilename = file.replace('.html', '.csv')
    cvsfilename = os.path.join('CSV', cvsfilename)
    with open(cvsfilename, 'w', newline='') as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile)
        
        # Write the column names
        writer.writerow(['view text', 'view integer', 'caption', 'link' ])
        
        # Iterate over the div elements
        for div in divs:
            # Find the img element and get its alt attribute
            img = div.find('img')
            alt = img['alt']
            href = div.find('a')['href']
            
            # Find the strong element with the given data-e2e attribute
            strong = div.find('strong', {'data-e2e': 'video-views'})
            
            # Get the text within the strong element
            number = strong.text

            match = re.match(r'(\d+\.?\d*)([MK]?)', number)
            value = 0
            
            if match:
                # Convert the numeric part to a float
                value = Decimal(match.group(1))
                
                # Multiply the value by 1000 if the suffix is "k"
                if match.group(2) == "K":
                    value *= 1000
                
                # Multiply the value by 1000000 if the suffix is "M"
                elif match.group(2) == "M":
                    value *= 1000000
            
            # Write the alt text and number to the CSV file
            writer.writerow([number, value, alt, href])
