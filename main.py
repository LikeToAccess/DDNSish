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
import requests
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


def post(url, hostname):
	resp = requests.post(url, data = {"hostname": hostname})
	return resp.text

def put(url, data):
	resp = requests.put(url,
		data={
		"Content-Type": "application/json\" --data '{\"type\":\"A\",\"name\":\"ricotv.gq\",\"content\":\"65.128.148.156\",\"ttl\":auto,\"proxied\":false}'"
		},
		headers={
			"X-Auth-Email": "",
			"X-Auth-Key":   "",
		}
	)
	return resp.text

def main(ddns_url, freenom_url):
	public_ip_address = list(
		filter(
			lambda part: part,
			[
				part if part.replace(".", "").isnumeric() else None \
				for part in post(
					ddns_url, ""
				).split()
			]
		)
	)[0]
	print(public_ip_address)
	print(put("https://api.cloudflare.com/client/v4/zones/", False))
	# scraper = Scraper(minimize=False)
	# scraper.open_link(freenom_url)


if __name__ == "__main__":
	main("http://iplookup.asus.com/nslookup.php", "")
