<h1 align="left">Tech News</h1>

###

<p align="left">This project aims to query a website that contains news about technology. To do this, data scraping was used, which is a technique for collecting data from online platforms. The data is captured from the scripts that are generated by the pages and programs that “scrape” the information. After the scraping is finished, the data is saved in a database.<br><br>With the data already saved and structured, the program allows to search by title, date, tags and news category.<br><br>An interactive menu is available so that the user can do the processes more easily.</p>

###

<h2 align="left">Technologies used</h2>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50" width="62" alt="python logo"  />
</div>

###

<h2 align="left">How to use the application</h2>

###

Clone the application using the `git clone` command. After that, enter the project folder using the command `cd-tech-news`.

###

<h2 align="left">How to run the application</h2>

1. Create the virtual environment for the project
- `python3 -m venv .venv && source .venv/bin/activate`

2. Install the dependencies
- `python3 -m pip install -r dev-requirements.txt`

###

<h2 align="left">Running the MongoDB database through Docker 🍃 🐳</h2>

In the root folder of the project, use the command `docker-compose up -d mongodb`.

###


<h2 align="left">Using the menu</h2>

1. In the terminal, use the command:
- `python3 -m tech_news.menu`

This command will bring up the menu, which contains several options on how to view the data that was collected from the scrape.
If this is your first time using the application, first use option `0` on the menu to populate the database.
