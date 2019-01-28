# Web-Scraper-App

Users can enter a havenshop.ca product web address and their email and will receive notification on any changes in stock or price. This information is stored in a MySQL database with a table denoting the product webpage, the user's email, its current price and stock.

## Getting Started

The app.py file runs the web app using flask where users can enter their information.
The poller.py file runs a constant poller that loops over each row in the table in SQL and will check for changes in the corresponding webpage.
The poller.py and app.py files can be run simultaneously and poller will check for new input from the user.

### Prerequisites

MySQL  
Python
