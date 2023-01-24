### get-videos-from-html.py
Reads all the HTML files in the HTML folder, extracts all data for each video on that TikTok accounts page, and creates a CSV (spreadsheet) file for each HTML file. 

Each CSV file has 4 columns: `view text`, `view integer`, `caption`, `link`

### Prerequisites
* Python 3.x
* The HTML folder containing all the HTML files that you want to extract video URLs from.

### Running the script
* Add all HTML files into HTML folder (and make sure you fully load page, *scroll down* to bottom, before you copy HTML)
* Open a terminal or command prompt and navigate to this directory
* Run the script:
```python get-videos-from-html.py```
The script will output a CSV file for each of the HTML files.

### HTML
To get HTML for a tiktok account, on desktop search that tiktok account. 
When you're on that page, ex. https://www.tiktok.com/@lizhagearty, right click and click `inspect` to see the HTML. Click the first line (looks like `<html> lang="en"...`) and copy (Command + C). In the HTML folder, make a new HTML file and paste the html you just copied. 

Repeat for as many tiktok accounts as you'd like! The script reads this folder and outputs one CSV file for each HTML file. 

### CSV
the script outputs CSV files (CSV = comma seperate values). So it will look like this: 
```
4.1M,4099999.9999999995,thankfully my hair was down and no one noticed #whoops #bridesmaid ,https://www.tiktok.com/@lizhagearty/video/7180574936572906795
5951,5951.0,@GRiZ 💥 #GranularVelocity #ravetok #edm  ,https://www.tiktok.com/@lizhagearty/video/7177718278503320878
3425,3425.0,"feeling so happy and inspired, wanted to share these thoughts 💘 ",https://www.tiktok.com/@lizhagearty/video/7177171590692506926
```
To view as a spreadsheet on Google Sheets, open a new Sheet and click File --> Import. 
Upload to CSV file you want to add, continue with the Import screen. Select the import location you want (Create new spreadsheet, Insert spreadsheet, Replace spreadsheet, etc.) and import data. 

### Note
 If you want to get all videos an account has ever posted, you need to scroll to the very bottom of the page before copying the HTML. 
 It is assumed that the HTML files are well-formed and you fully loaded the page before copying the HTML.