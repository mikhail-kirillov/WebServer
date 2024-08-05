# WebServer Project

## Description

The WebServer project is an example web application created using Flask, designed to demonstrate basic web page handling, Bootstrap styling, and database operations using SQLite via SQLAlchemy. The application allows users to add data to a database, view added records, and demonstrate the basics of pages and error handling.

## Technologies

- **Python 3**: The programming language used to create the server.
- **Flask**: A microframework for creating web applications in Python.
- **SQLAlchemy**: A library for database operations via ORM (Object-Relational Mapping).
- **Bootstrap**: A framework for styling web pages.

## Installation

To run the project, you need Python 3. Make sure it is installed on your system.

1. Clone the repository:

    `git clone https://github.com/kirillov-michael/WebServer.git`

2. Install the necessary dependencies:

    `pip install -r requirements.txt`

3. Run the server:

    `python3 main.py`

## Usage

After starting the server, the web application will be available at [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

- The main page is accessible via the root URL or /index.
- To add data to the database, use /add.html.
- To view added records, go to /get.html.
- The /bootstrap.html page demonstrates the use of Bootstrap.

## Configuration

Configuration parameters such as the application secret key are set in `WebServer/main.py`. To change the port or listening address, modify the corresponding parameters in the `app.run()` function:

```python
def main():
    app.run(port=8080, host='127.0.0.1')
```

---

Date: 24.04.2022
