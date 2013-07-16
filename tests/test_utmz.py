import datetime
import pytest
from macadamia import parse_utmz

@pytest.mark.parametrize(("cookie", "expected"),[
    ("44858868.462535200.44.2.utmcsr=localhost:9000|utmccn=(referral)|utmcmd=referral|utmcct=/", {
        "domain_hash": "44858868",
        "timestamp": datetime.datetime(year=1984, month=8, day=28),
        "session_counter": "44",
        "campaign_number": "2",
        "campaign_data": {
            'campaign_content': '/',
            'campaign_name': '(referral)',
            'medium': 'referral',
            'source': 'localhost:9000',
        }
    }),
    ("208940939.1365186784.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)", {
        'campaign_number': '1',
        'domain_hash': '208940939',
        'session_counter': '1',
        'timestamp': datetime.datetime(2013, 4, 5, 8, 33, 4),
        'campaign_data': {
            'campaign_name': '(direct)',
            'medium': '(none)',
            'source': '(direct)'
        },
    }),
])
def test_cookie_split_and_parse(cookie, expected):
    info = parse_utmz(cookie)
    assert info == expected

