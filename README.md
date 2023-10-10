# Property_scraper_

This project is a web application built with Python, Django, MongoDB, and HTML to scrape property data from 99acres.com. It allows users to search for properties based on various criteria and view detailed property information.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Property searching is a common task for individuals looking to buy, rent, or invest in real estate. 99acres.com is a popular real estate website that provides extensive property listings. This project automates the process of collecting property data from 99acres.com using web scraping techniques.

## Features

- Web scraping of property data from 99acres.com
- User-friendly web interface for searching and viewing property listings
- Filter properties based on location, price range, property type, and more
- Detailed property information including images, descriptions, and contact details
- Integration with MongoDB for storing scraped data
- Responsive HTML templates for a pleasant user experience

## Requirements

To run this project, you'll need the following software and packages installed:

- Python 3.x
- Django
- MongoDB
- BeautifulSoup (for web scraping)
- Requests (for making HTTP requests)
- HTML/CSS knowledge for customizing the frontend

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/property-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd property-scraper
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Configure MongoDB:
   - Update the database settings in `settings.py` with your MongoDB connection information.

7. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the web application in your browser at `http://localhost:8000/`.

2. Use the search form to filter properties based on your preferences, such as location, price range, property type, etc.

3. Browse through the property listings, view detailed information, and contact the seller if interested.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Your commit message"
   ```

4. Push your changes to your forked repository:

   ```bash
   git push origin feature-name
   ```

5. Create a pull request on the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy property searching! If you have any questions or issues, please don't hesitate to contact us or open an issue on GitHub.
