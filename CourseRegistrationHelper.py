#COMMENT:	I created an encryption program so that I would not have to type my
#			real password into the passwordEncrypted variable when showing
#			others my code.

#from Encryption import encrypt, decrypt

#passwordEncrypted = "my encrypted password was here"
#password = decrypt(passwordEncrypted)

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from smtplib import SMTP

class Email:
	def __init__(self):
		self.body = ""
	def append(self, text):
		self.body += text

class Class:
	def __init__(self, course, section, semester):
		self.course = course
		self.section = section
		self.semester = semester

class Request:
	def __init__(self, email):
		self.email = email
		self.classes = []
	def addClass(self, course, section, semester):
		self.classes.append(Class(course, section, semester))
	def process(self):
		self.message = Email()
		for entry in self.classes:
			if (checkAvailability(entry)):
				self.message.append(entry.course+" "+entry.section+" is available!\n")
				print(entry.course+" "+entry.section+" in "+entry.semester+" is available!\n")
			else:
				print(entry.course+" "+entry.section+" in "+entry.semester+" is not available.\n")
		if (self.message.body != ""):
			self.sendEmail()
	def sendEmail(self):
		#print("Sending a message to " + self.email + ".")
		server.sendmail("coursealerts1@gmail.com", self.email, self.message.body)

def getElement(argument):
	while True:
		#print("getElement on " + argument)
		try:
			return driver.find_element_by_xpath(argument)
		except NoSuchElementException:
			continue

def Click(element):
	while True:
		#print("Click")
		try:
			element.click()
			break
		except ElementNotVisibleException:
			continue

def sendKeys(element, keys):
	while True:
		try:
			element.send_keys(keys)
			break
		except ElementNotVisibleException:
			continue

def printElement(element):
	print(element.get_attribute('outerHTML'))

def logIntoUvic():
	driver.get("https://www.uvic.ca/BAN1P/bwskfcls.p_sel_crse_search")
	sendKeys(getElement("//input[@name='username']"), "ishaha")
	sendKeys(getElement("//input[@name='password']"), password)
	Click(getElement("//input[@name='form-submit']"))

def checkAvailability(entry):
	subject, courseNumber = entry.course.split()
	section = entry.section
	semester = entry.semester
	driver.get("https://www.uvic.ca/BAN1P/bwskfcls.p_sel_crse_search")
	Click(getElement("//option[@value='"+semester+"']"))
	Click(getElement("//input[@value='Submit']"))
	Click(getElement("//option[@value='"+subject+"']"))
	Click(getElement("//input[@value='Course Search']"))
	Click(getElement("//td[contains(text(), '"+courseNumber+"')]/..//input[@value='View Sections']"))
	actual = int(getElement("//td[contains(text(), '"+section+"')]/../td[12]").text)
	capacity = int(getElement("//td[contains(text(), '"+section+"')]/../td[11]").text)
	return True if actual < capacity else False

def logIntoEmail():
	server.starttls()
	server.login("coursealerts1@gmail.com", encrypt("CourseAlerts"))

def main():

	logIntoUvic()
	logIntoEmail()
	
	isaac = Request("6044466463@vmobile.ca")
	isaac.addClass("SENG 275", "B02", "201905")
	isaac.addClass("SENG 275", "B03", "201905")
	isaac.process()

if (__name__ == "__main__"):
	#Set Up Chrome.
	options = Options()
	#options.add_argument("--headless")
	#options.add_argument("--disable-gpu")
	driver = webdriver.Chrome(options=options, executable_path="C:/Users/isaac/Programming/chromedriver")
	driver.maximize_window()
	server = SMTP("smtp.gmail.com", 587)
	main()
	print("Done.")
	driver.quit()
	server.quit()

exit()