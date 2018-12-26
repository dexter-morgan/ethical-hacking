#!/usr/bin/env python

import requests, re, urlparse


target_url = "http://10.0.2.10"
target_links = []


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)


def crawl(url):
    hyper_links = extract_links_from(url)
    for link in hyper_links:
        link = urlparse.urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]
        if url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)
print(len(target_links))
