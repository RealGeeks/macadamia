import datetime
try:
    import urllib2 as url_library
except ImportError:
    import urllib as url_library

def parse_campaign_data(data):
    human_names = {
      "utmcsr": "source",
      "utmcmd": "medium",
      "utmccn": "campaign_name",
      "utmctr": "campaign_keyword",
      "utmcct": "campaign_content",
      "utmgclid": "google_click_id",
    }
    fields = [d.split("=") for d in data.split("|")]
    info = dict((human_names[d[0]] ,url_library.unquote(d[1])) for d in fields)

    return info

def parse_utmz(cookie):
    fields = cookie.split('.')
    return {
        "domain_hash": fields[0],
        "timestamp": datetime.datetime.fromtimestamp(int(fields[1])),
        "session_counter": fields[2],
        "campaign_number": fields[3],
        "campaign_data": parse_campaign_data(".".join(fields[4:])),
    }
