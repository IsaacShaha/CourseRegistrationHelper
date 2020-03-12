# CourseRegistrationHelper
A program I created to help myself with course registration at UVic. This was created with Python 3 and Selenium WebDriver using Windows. The program regularly checks my specified lab sections without waitlists and sends a text to my phone if there is an available space to register. I chose not use the program to register automatically.

# Virtual Environment Setup
I used pip and virtualenv to create an environment with selenium installed. I used the following commands in the main folder:
- virtualenv WebScrapingEnvironment
- WebScrapingEnvironment\scripts\activate
- pip install selenium

# Automation
Once I had inputted my desired courses, I used the Windows Task Scheduler to run the program every hour after startup. I was able to register for lab sections that I would normally regularly check on for weeks, in just days.
