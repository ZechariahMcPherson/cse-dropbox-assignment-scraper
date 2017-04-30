import scrapy
import logging
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

class assignmentSpider(scrapy.Spider):
    #used to call the spider
    name = "assignmentSpider"

    def start_requests(self):
        """sends urls to Request object"""

        #place urls to iterate through
        urls =[
            "https://dropbox.cse.sc.edu"
        ]

        #iterates through given urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,                errback=self.errback_httpbin)

    def parse(self, response):
        """put spider here"""



    #this function is directly copied from https://doc.scrapy.org/en/latest/topics/request-response.html?highlight=errback


    def errback_httpbin(self, failure):
        """handles all of Request object's errors """

        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)
