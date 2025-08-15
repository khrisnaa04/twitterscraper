# Twitter Scraper
This Twitter Scraper is built using Python 3.x and the `twikit` library to fetch data from Twitter. The script enables automatic data retrieval with error handling for `TooManyRequests`.

## Features
- Uses `twikit` for authentication and data fetching
- Handles errors when `TooManyRequests` occurs
- Saves scraped data in CSV format
- Configurable via `.ini` file

## Requirements
- python 3.x
- twikit 
- asyncio 
- datetime 
- random 
- time 
- configparser
- csv 

## Installation
1. Install Python  
   Download and install Python from the official website: [Python Installation Guide.](https://docs.python.org/3/using/index.html)  
2. Install Requeired Libraries  
   Open a terminal or command prompt and run the following command to install the necessary dependencies:  
   ```sh
   pip install twikit
   ```  
3. Run the Script  
   Ensure the script file is located in the same folder as your working directory. Then, open a terminal or command prompt and execute the script accordingly. 

## File Structure
```sh
📂 twitter-scraper
│─ 📂 asset
   │─ tweets_with_sentiment.csv
│─ 📂 scr
   │─ main.py
   │─ config.ini
   │─ sentimen.py
   │─ tren.py
│─ LICENSE 
│─ README.md
```

## Notes
- Ensure your Twitter account has the necessary API access.
- Use responsibly and comply with Twitter's usage policies. 

## License
- This project is licensed under the MIT License. You are free to use it while providing proper attribution.
