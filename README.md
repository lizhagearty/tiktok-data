### get-videos-from-html.py
This script reads all the HTML files in the HTML folder and extracts all data for each video on that TikTok accounts page. 

### Prerequisites
* Python 3.x
* The HTML folder containing all the HTML files that you want to extract video URLs from.

### Running the script
* Make sure that the HTML folder containing the HTML files is in the same directory as the get-videos-from-html.py script.
* Open a terminal or command prompt and navigate to the directory where the script is located.
* Run the script:
```get-videos-from-html.py```
The script will output a CSV file of all videos that it has extracted from the HTML files.

### Note
It is assumed that the HTML files are well-formed and you fully loaded the page before copying the HTML. If you want to get all videos an account has ever posted, you need to scroll to the very bottom of the page before copying the HTML. 