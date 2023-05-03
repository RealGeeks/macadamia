import datetime
import re

try:
    from urllib2 import unquote
except ImportError:
    from urllib.parse import unquote


def parse_campaign_data(data, prefix="utm"):
    human_names = {
        "%scsr" % prefix: "source",
        "%scmd" % prefix: "medium",
        "%sccn" % prefix: "campaign_name",
        "%sctr" % prefix: "campaign_keyword",
        "%scct" % prefix: "campaign_content",
        "%sgclid" % prefix: "google_click_id",
    }

    fields = [d.split("=") for d in data.split("|")]
    info = dict((human_names[d[0]], unquote(d[1])) for d in fields)

    return info


def parse_cookie(cookie, prefix="utm"):
    fields = re.search(r"^(?:(\d*)\.(\d*)\.(\d*)\.(\d*).)?(.+)$", cookie).groups()
    fields = [field or "" for field in fields]

    if fields[1]:
        timestamp = datetime.datetime.fromtimestamp(int(fields[1]))
    else:
        timestamp = ""

    return {
        "domain_hash": fields[0],
        "timestamp": timestamp,
        "session_counter": fields[2],
        "campaign_number": fields[3],
        "campaign_data": parse_campaign_data(fields[4], prefix),
    }


def parse_utmz(cookie):
    return parse_cookie(cookie, prefix="utm")
