import base64
from abc import ABCMeta
from typing import Literal, Union
from requests import Session

from bs4 import BeautifulSoup


class Scraper(metaclass=ABCMeta):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62",
        "X-Amzn-Trace-Id": "Root=1-61acac03-6279b8a6274777eb44d81aae",
        "X-Client-Data": "CJW2yQEIpLbJAQjEtskBCKmdygEIuevKAQjr8ssBCOaEzAEItoXMAQjLicwBCKyOzAEI3I7MARiOnssB"
    }

    def __init__(self):
        self.Se: Union["Session", None] = None

    def __enter__(self):
        self.Se = Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Se.close()
        self.Se = None

    def get_soap(self, URL, type_: Literal["GET", "POST"] = "GET", payload_=None) -> BeautifulSoup:
        if type_ == "GET":
            response = self.Se.get(URL, headers=self.HEADERS)
        elif type_ == "POST":
            response = self.Se.post(URL, data=payload_, headers=self.HEADERS)
        else:
            raise ValueError(f"invalid {type_=}")
        return BeautifulSoup(response.content, 'html.parser')

    def get_img(self, URL) -> bytes:
        return base64.encodebytes(self.Se.get(URL).content)
