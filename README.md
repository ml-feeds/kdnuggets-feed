# kdnfeed
This serves a filtered RSS feed for [KDnuggets](https://www.kdnuggets.com/).
As a disclaimer, there is no affiliation of it with KDnuggets.

## Links
* Original unfiltered feed: https://www.kdnuggets.com/feed
* Unofficial filtered feed: https://kdnfeed.now.sh/
* Project dashboard: https://zeit.co/dashboard/project/kdnfeed (requires authentication)
* Pproject logs: https://kdnfeed.now.sh/_logs

## Deployment
Deployment from the `master` branch is automated using https://zeit.co/.
The files required for this automated deployment are [`index.py`](index.py), [`now.json`](now.json), and
[`requirements.txt`](requirements.in).

The latest deployment is configured to be reachable at the aforementioned link for the unofficial filtered feed.
Older (unaliased) deployments do not delete automatically; they're to be deleted manually.
Unaliased (older) deployments can be removed using the project website, or via the command `now rm <app> --safe --yes`.
