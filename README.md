# kdnfeed
This serves a filtered RSS feed for [KDnuggets](https://www.kdnuggets.com/).
As a disclaimer, there is no affiliation of it with KDnuggets.

## Links
* [Project repo](https://github.com/impredicative/kdnfeed)
* [Original unfiltered feed](https://www.kdnuggets.com/feed)
* [Unofficial filtered feed](https://us-east1-ml-feeds.cloudfunctions.net/kdnuggets)

## Deployment
Serverless deployment to [Google Cloud Functions](https://console.cloud.google.com/functions/) is configured.
It requires the the following files:
* requirements.txt
* main.py (having callable `serve(request: flask.Request) -> Tuple[bytes, int, Dict[str, str]]`)

Deployment version updates are performed manually, such as by editing and saving the function configuration.

These deployment links require access.
* [Function repo](https://source.cloud.google.com/ml-feeds/github_impredicative_kdnfeed)
* [Function dashboard](https://console.cloud.google.com/functions/details/us-east1/kdnuggets?project=ml-feeds)
