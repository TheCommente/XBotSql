
# XbotApp - Twitter Bot

XbotApp is a Python-based Twitter automation application that uses Selenium to log in to Twitter and post tweets with optional images. The application reads tweets from a MySQL database and marks them as posted after tweeting. When all tweets have been posted, the application resets them for reposting.

## Features
- Automatically logs in to Twitter using Selenium.
- Posts tweets with optional images.
- Reads tweet content from a MySQL database.
- Resets tweet statuses after all tweets are posted.

## Project Structure
```
XbotApp/
│
├── .env                         # Environment variables for sensitive data
├── chromedriver/                # Directory for ChromeDriver
│   └── chromedriver.exe         # ChromeDriver executable
├── config/
│   └── database.py              # Database configuration and connection
├── services/
│   ├── twitter_service.py       # Service for Twitter-related functions
│   └── tweet_manager.py         # Logic for managing tweets
├── models/
│   └── tweet.sql                # SQL file to create the tweets table
├── main.py                      # Main entry point to run the application
└── requirements.txt             # Python dependencies
```

## Prerequisites
- Python 3.x installed
- Google Chrome installed
- ChromeDriver (match the version of your Chrome installation)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TheCommente/XbotApp.git
   cd XbotApp
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the .env file**:
   Create a `.env` file in the project root directory with the following content:
   ```
   # Database configuration
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_database_password
   DB_NAME=twitter_bot

   # Twitter login credentials
   TWITTER_USERNAME=your_twitter_username
   TWITTER_PASSWORD=your_twitter_password

   # Path to ChromeDriver
   CHROMEDRIVER_PATH=chromedriver/chromedriver.exe
   ```

   **Note**: Replace `your_database_password`, `your_twitter_username`, and `your_twitter_password` with your actual database and Twitter credentials.

4. **Create the database and table**:
   - Import the `models/tweet.sql` file to create the `tweets` table in your MySQL database:
     ```bash
     mysql -u root -p twitter_bot < models/tweet.sql
     ```

5. **Add tweet data**:
   - Manually insert some tweets into the `tweets` table for testing:
     ```sql
     INSERT INTO tweets (content, image_path, posted) VALUES 
     ('Hello, world!', 'C:\path_to_image\image.png', FALSE);
     ```

6. **Run the application**:
   ```bash
   python main.py
   ```

## Troubleshooting
- Ensure that the ChromeDriver version matches your installed Chrome version.
- Verify the `.env` file configuration for correct credentials.
- Make sure the MySQL database is running.

## License
This project is licensed under the MIT License.
