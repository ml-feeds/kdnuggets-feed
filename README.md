# kdnfeed
This serves a filtered RSS feed for [KDnuggets](https://www.kdnuggets.com/).
As a disclaimer, there is no affiliation of it with KDnuggets.

## Links
* Original unfiltered feed: https://www.kdnuggets.com/feed
* Unofficial filtered feed: https://kdnfeed.now.sh/

## Deployment
Deployment from the `master` branch is automated using https://zeit.co/.
The files required for this automated deployment are [`index.py`](index.py), [`now.json`](now.json), and
[`requirements.txt`](requirements.txt).

The latest deployment is configured to be reachable at the aforementioned link for the unofficial filtered feed.
Older deployments do not delete automatically; they're to be deleted manually.
