import scrapy

from pep_parse.items import PepParseItem


stat_count = {}


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response: scrapy.http.Response) -> scrapy.http.Request:
        all_peps = response.css("section#numerical-index a")
        for pep in all_peps[1:]:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response: scrapy.http.Response) -> PepParseItem:
        num_tit = response.css("h1.page-title::text").get().split(" – ")
        status = response.css("section#pep-content abbr::text").get()
        data = {
            "number": int(num_tit[0].replace("PEP ", "")),
            "name": num_tit[1],
            "status": status,
        }
        stat_count[status] = stat_count.get(status, 0) + 1
        yield PepParseItem(data)
