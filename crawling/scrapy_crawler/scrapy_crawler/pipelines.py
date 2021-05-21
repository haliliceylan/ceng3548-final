# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter

class ScrapyCrawlerPipeline:
    def process_item(self, item, spider):
        return item

from urllib.parse import urlparse
import re

class InternalMetricPipeline:
    general_characters = {
        "dot": ".",
        "hyphen": "-",
        "underline": "_",
        "slash": "/",
        "questionmark": "?",
        "equal": "=",
        "at": "@",
        "and": "&",
        "exclamation": "!",
        "space": " ",
        "tilde": "~",
        "comma": ",",
        "plus": "+",
        "asterisk": "*",
        "hashtag": "#",
        "dollar": "$",
        "percent": "%",
    }

    def general_internal_metrics(self, data, postfix=""):
        data = str(data)
        ret_data = {}
        for character_name, character_rep in self.general_characters.items():
            ret_data[f"qty_{character_name}{postfix}"] = data.count(character_rep)
        ret_data[f"length{postfix}"] = len(data)
        return ret_data

    def process_item(self, item, spider):
        new_item = dict(item)
        url = new_item.get("url")
        components_of_url = urlparse(url)
        # calculate all domain Metric
        new_item.update(self.general_internal_metrics(url, "_url"))
        new_item["email_in_url"] = int(bool(re.search("(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}", url)))
        # calculate domain Metrics
        domain = components_of_url.netloc
        new_item.update(self.general_internal_metrics(domain, "_domain"))
        new_item["in_ip_domain"] = int(bool(re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", domain)))
        new_item["server_client_domain"] = int(bool(re.search("(server|client)", domain)))
        # calculate directory Metrics
        path = components_of_url.path
        new_item.update(self.general_internal_metrics(path, "_path"))
        # calculate query Metrics
        query = components_of_url.query
        new_item.update(self.general_internal_metrics(query, "_query"))
        new_item["qty_elements_query"] = query.count("=")
        new_item["tdl_present_query"] = int(bool(domain in query))
        # calculate fragment Metrics
        new_item.update(self.general_internal_metrics(components_of_url.fragment, "_fragment"))
        return new_item;
