from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response: scrapy.http.Response) -> scrapy.http.Request:
        all_peps = response.css("section#numerical-index a")
        for pep in all_peps[1:]:
            pep_url = urljoin(response.url, pep.attrib["href"]) + "/"
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response: scrapy.http.Response) -> PepParseItem:
        number_title = response.css("h1.page-title::text").get().split(" – ")
        status = response.css("section#pep-content abbr::text").get()
        data = {
            "number": int(number_title[0].replace("PEP ", "")),
            "name": number_title[1],
            "status": status,
        }
        yield PepParseItem(data)
