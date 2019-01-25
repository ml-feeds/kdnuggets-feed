# kdnfeed
*kdnfeed* uses Python 3.7 to serve a filtered RSS feed for [KDnuggets](https://www.kdnuggets.com/).
As a disclaimer, it has no affiliation with KDnuggets.

## Links
* [Project repo](https://github.com/impredicative/kdnfeed)
* [Original unfiltered feed](https://www.kdnuggets.com/feed)
* [Unofficial filtered feed](https://us-east1-ml-feeds.cloudfunctions.net/kdnuggets)

## Deployment
Serverless deployment to [Google Cloud Functions](https://console.cloud.google.com/functions/) is configured.
It requires the the following files:
* requirements.txt
* main.py (having callable `serve(request: flask.Request) -> Tuple[bytes, int, Dict[str, str]]`)

Deployment version updates are not automated.
They can be performed manually by editing and saving the function configuration.

These deployment links require access:
* [Dashboard](https://console.cloud.google.com/functions/details/us-east1/kdnuggets?project=ml-feeds)
* [Logs](https://console.cloud.google.com/logs?service=cloudfunctions.googleapis.com&key1=kdnuggets&key2=us-east1&project=ml-feeds)
* [Repo](https://source.cloud.google.com/ml-feeds/github_impredicative_kdnfeed)
