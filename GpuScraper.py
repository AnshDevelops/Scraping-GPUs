from baby_soup import Scraper

benchmarks = []


class GPUScraper(Scraper):
    def __init__(self, T_URL):
        self.URL = T_URL
        super(GPUScraper, self).__init__()

    def scrape_gpu_specs(self):
        soap = self.get_soap(self.URL)
        body = soap.body
        table_body = body.find_all("tbody", class_="table__body")[0]
        for row in table_body.find_all("tr"):
            info = row.find_all("td")
            name = info[0].find('a').text
            fhd = info[1].text
            qhd = info[3].text
            fourk = info[4].text
            benchmarks.append([name, fhd, qhd, fourk])


def get_data():
    with GPUScraper('https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html') as GPU:
        GPU.scrape_gpu_specs()
