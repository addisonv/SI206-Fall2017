import facebook 
import urllib3
import requests

token = "EAALj5ZCoLn6YBAMsuoJj5tDjgEihh6VZBFkxPY3bK8yIk6PfzV6MCSH7bYdfiZBLegWW5XBSa74TfiBsoH9JP7qAcetDZAYeEwlcJ8SxlNuFEofEMVAZBz1JpQHbmIzsE0z0DRKh1Y5bmByKvzQpfIPZA7TrQrGYLiwq62dvDlvAZDZD"
graph = facebook.GraphAPI(access_token=token, version = 2.7)
events = graph.request("/search?q=Poetry&type=event&limit=10000")
eventList = events["data"]
print(eventList)