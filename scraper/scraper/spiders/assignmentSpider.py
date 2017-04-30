import scrapy
import logging

class assignmentSpider(scrapy.Spider):
    #used to call the spider
    name = "assignmentSpider"

    def start_requests(self):
        """sends urls to Request object"""

        #urls to iterate through
        urls =["https://dropbox.cse.sc.edu"]

        #iterates through given urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,                errback=self.error)

    def parse(self, response):
        self.logger.info("Opened: %s", response.url)

    def error(self, error):
        """handles Request object's errors"""
