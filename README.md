# kdnfeed
This serves a filtered RSS feed for [KDnuggets](https://www.kdnuggets.com/).
As a disclaimer, there is no affiliation of it with KDnuggets.

## Links
* [Project repo](https://github.com/impredicative/kdnfeed)
* [Project repo (deployment mirror)](https://source.cloud.google.com/kdnfeed/github_impredicative_kdnfeed) (requires access)
* [Project dashboard](https://console.cloud.google.com/functions/details/us-east1/kdnfeed?project=kdnfeed) (requires access)
* [Original unfiltered feed](https://www.kdnuggets.com/feed)
* [Unofficial filtered feed](https://us-east1-kdnfeed.cloudfunctions.net/kdnfeed)

## Deployment
Deployment to [Google Cloud Functions](https://console.cloud.google.com/functions/) is configured.
It requires the existence of the following files:
* requirements.txt
* main.py (having callable `serve(request: flask.Request) -> bytes`)

Deployment version updates are performed manually, such as by editing and saving the function configuration.
