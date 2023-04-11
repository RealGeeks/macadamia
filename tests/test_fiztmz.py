import datetime
import pytest
from macadamia import parse_cookie


@pytest.mark.parametrize(
    ("cookie", "expected"),
    [
        (
            "44858868.462535200.44.2.fiztmcsr=localhost:9000|fiztmccn=(referral)|fiztmcmd=referral|fiztmcct=/",
            {
                "domain_hash": "44858868",
                "timestamp": datetime.datetime(year=1984, month=8, day=28, hour=10),
                "session_counter": "44",
                "campaign_number": "2",
                "campaign_data": {
                    "campaign_content": "/",
                    "campaign_name": "(referral)",
                    "medium": "referral",
                    "source": "localhost:9000",
                },
            },
        ),
        (
            "208940939.1365186784.1.1.fiztmcsr=(direct)|fiztmccn=(direct)|fiztmcmd=(none)",
            {
                "campaign_number": "1",
                "domain_hash": "208940939",
                "session_counter": "1",
                "timestamp": datetime.datetime(2013, 4, 5, 18, 33, 4),
                "campaign_data": {
                    "campaign_name": "(direct)",
                    "medium": "(none)",
                    "source": "(direct)",
                },
            },
        ),
        (
            "48016369.462535200.1.1.fiztmcsr=realgeeks.com|fiztmccn=(referral)|fiztmcmd=referral|fiztmcct=/clients/lee-cunningham/",
            {
                "campaign_number": "1",
                "domain_hash": "48016369",
                "session_counter": "1",
                "timestamp": datetime.datetime(year=1984, month=8, day=28, hour=10),
                "campaign_data": {
                    "campaign_content": "/clients/lee-cunningham/",
                    "campaign_name": "(referral)",
                    "medium": "referral",
                    "source": "realgeeks.com",
                },
            },
        ),
        (
            "44858868.462535200.71.3.fiztmcsr=google|fiztmccn=(organic)|fiztmcmd=organic|fiztmctr=hawaii%20real%20estate",
            {
                "campaign_number": "3",
                "domain_hash": "44858868",
                "session_counter": "71",
                "timestamp": datetime.datetime(year=1984, month=8, day=28, hour=10),
                "campaign_data": {
                    "campaign_keyword": "hawaii real estate",
                    "campaign_name": "(organic)",
                    "medium": "organic",
                    "source": "google",
                },
            },
        ),
        (
            "112962326.462535200.1.1.fiztmgclid=CMbMrdi_ybgCFWho7AodDyAAvQ|fiztmccn=(not set)|fiztmcmd=(not set)|fiztmctr=real estate for sale in wilmington nc",
            {
                "campaign_number": "1",
                "domain_hash": "112962326",
                "session_counter": "1",
                "timestamp": datetime.datetime(year=1984, month=8, day=28, hour=10),
                "campaign_data": {
                    "campaign_keyword": "real estate for sale in wilmington nc",
                    "campaign_name": "(not set)",
                    "google_click_id": "CMbMrdi_ybgCFWho7AodDyAAvQ",
                    "medium": "(not set)",
                },
            },
        ),
        (
            "fiztmgclid=CMbMrdi_ybgCFWho7AodDyAAvQ|fiztmccn=(not set)|fiztmcmd=(not set)|fiztmctr=real estate for sale in wilmington nc",
            {
                "campaign_number": "",
                "domain_hash": "",
                "session_counter": "",
                "timestamp": "",
                "campaign_data": {
                    "campaign_keyword": "real estate for sale in wilmington nc",
                    "campaign_name": "(not set)",
                    "google_click_id": "CMbMrdi_ybgCFWho7AodDyAAvQ",
                    "medium": "(not set)",
                },
            },
        ),
    ],
)
def test_cookie_split_and_parse(cookie, expected):
    info = parse_cookie(cookie, prefix="fiztm")
    assert info == expected
