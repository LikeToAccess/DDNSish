# -*- coding: utf-8 -*-
# filename          : main.py
# description       : 
# author            : LikeToAccess
# email             : liketoaccess@protonmail.com
# date              : 12-07-2021
# version           : v1.0
# usage             : python main.py
# notes             :
# license           : MIT
# py version        : 3.9.7 (must run on 3.6 or higher)
#==============================================================================
import os
import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Scraper:
	def __init__(
		self,
		minimize=True,
		user_data_dir=os.path.abspath("selenium_data"),
		executable = "chromedriver.exe" if os.name == "nt" else "chromedriver",
		headers = {
			"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
		},
	):
		options = Options()
		options.add_argument(f"user-data-dir={user_data_dir}")
		options.add_argument("log-level=3")
		self.executable = executable
		self.driver = webdriver.Chrome(executable_path=os.path.abspath(self.executable), options=options)
		self.headers = headers
		if minimize: self.driver.minimize_window()

	def open_link(self, url):
		self.driver.get(url)

	def close(self):
		self.driver.close()

	def current_url(self):
		return self.driver.current_url


def main(freenom_url):
	scraper = Scraper(minimize=False)
	scraper.open_link(url)

if __name__ == "__main__":
	scraper = 
