# Macadamia

![yummy](http://i.imgur.com/qWDTNcg.jpg)

Named after the most delicious kind of cookie, this is a parser for Google Analytics cookies.

Really I just care about the `__utmz` cookie, so that is all that this parser can parse for now.  But if it turns out there is something interesting in the other cookies, I'll add to this parser to support them too.

## Installation

```bash
pip install macadamia
```

## Usage

```python
>>> from macadamia import parse_utmz
>>> cookie_to_parse = "208940939.1365186784.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"
>>> parsed_cookie = parse_utmz(cookie_to_parse)
{'domain_hash': '208940939', 'campaign_number': '1', 'campaign_data': {'source': '(direct)', 'campaign_name': '(direct)', 'medium': '(none)'}, 'timestamp': datetime.datetime(2013, 4, 5, 8, 33, 4), 'session_counter': '1'}
```

```python
>>> from macadamia import parse_cookie
>>> cookie_to_parse = "208940939.1365186784.1.1.fiztmcsr=(direct)|fiztmccn=(direct)|fiztmcmd=(none)"
>>> parsed_cookie = parse_cookie(cookie_to_parse, prefix="fiztm")
>>> {'domain_hash': '208940939', 'campaign_number': '1', 'campaign_data': {'source': '(direct)', 'campaign_name': '(direct)', 'medium': '(none)'}, 'timestamp': datetime.datetime(2013, 4, 5, 8, 33, 4), 'session_counter': '1'}
```

## The future of google analytics cookies

Google has deprecated this cookie format and now GA4 stores a cookie incompatible with Macadamia.  If you would like to continue using Macadamia, version `0.2.0` adds support for parsing cookies created by [the included utmz cookie replicator javascript](https://github.com/RealGeeks/macadamia/blob/master/utmz-cookie.js)

###__utma Visitor Cookie (lasts 2 years)
Used to distinguish users and sessions. The cookie is created when the javascript library executes and no existing __utma cookies exists. The cookie is updated every time data is sent to Google Analytics.

Each group is separated by a period character. All times stored are UNIX timest­amps. For new visits the three times in this cookie will all be the same.

Has the following info:
  * domain_hash
  * random_id
  * first_visit_at
  * previous_visit_at
  * current_visit_at
  * session_counter

### `__utmb` Session Cookie (lasts 30 minutes)
Used to determine new sessions/visits. The cookie is created when the javascript library executes and no existing __utmb cookies exists. The cookie is updated every time data is sent to Google Analytics.

Has the following fields:
  * domain_hash
  * pageviews
  * tokens_available
  * time_of_session

Each group is separated by a period character. All times stored are UNIX timestamps. The token bucket stores how many requests are being made to GA at once. This number will decrease for each request, any requests sent while the bucket is empty will be discarded.

### `__utmc` (lasts until browser is closed)
Deprecated.  Still set for backwards compability sometimes.

### `__utmz` (lasts 6 months)
Stores the traffic source or campaign that explains how the user reached your site. The cookie is created when the javascript library executes and is updated every time data is sent to Google Analytics.

Has the following fields:

* domain_hash
* timestamp
* session_counter
* campaign_number
* campaign_data

Nested Inside campaign_data are the following fields, separated by `|` characters.

| value name | human-readable name | example values |
| ---------- | ------------------- | -------------- |
| utmcsr  | source | google, yahoo, bing (if organic) or example.com if referral |
| utmcmd  | medium | referral, organic, direct |
| utnccn  | campaign name | (direct), (referral) |
| utmctr  | campaign keyword | ? |
| utmcct  | campaign content | the relative page URL of the referring site if a referral |
| utmgclid | google click ID | ? |

`utmgclid` will only be set for AutoTagged AdWords visits. If set, other parameters will be unset, as utmgclid is a hash of the campaign values and is used instead.

## Rare variables

### `__utmv` (lasts 2 years)
Used to store visitor-level custom variable data. 

  * domain_hash
  * custom variable value

Each group is separated by a period character. This cookie can only be created by using Google Analytics' deprecated _setVar() method. Calling this method sets this cookie and automa­tically sends the data to Google Analytics via a __utm.gif request.  Values sent in this manner appear in the "User Define­d" report, unless otherwise interc­epted with profile filters.

### `__utmx`
Used by Website Optimizer.  Now used by "Content Experiments?"

### `__utmk`
Digest hashes of utm values

Sources:
  * [Google Analytics v2 cheatsheet](http://www.cheatography.com/jay-taylor/cheat-sheets/google-analytics-cookies-v2/)
  * [Google UTMZ Cookie Parser](http://daleconboy.com/portfolio/code/google-utmz-cookie-parser)
  * [Python GA Cookie Parser](https://github.com/ryonlife/Python-Google-Analytics-Cookie-Parser)
  * [Official GA Cookie Documentation](https://developers.google.com/analytics/devguides/collection/analyticsjs/cookie-usage)

## Running tests via tox and docker
```bash
make test
```

## Changelog

* 0.2.0: Support cookies missing the leading fields, as created by some `_utmz` replicator scripts.
* 0.1.0: Support cookies shaped like `_utmz` but with a different name
* 0.0.7: Actually add Python 3 compatibility and upgrade Dockerfile base image to test against Python 3.7
* 0.0.6: Python 3 compatibility and add Dockerfile for development
* 0.0.5: Fix typo parsing `utmgclid` cookie value
* 0.0.4: URLDecode cookie information
* 0.0.3: Fix bug where the . in a referring domain name was causing the `campaign_data` field to be cut off
* 0.0.2: Remove accidential PyYAML dependency
* 0.0.1: initial release

## License (MIT)
The MIT License (MIT)

Copyright (c) 2013-2023 Kevin McCarthy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

