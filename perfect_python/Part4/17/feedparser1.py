import feedparser

parsed = feedparser.parse("http://rss.rssad.jp/rss/gihyo/feed/atom")
feed = parsed.feed
print(feed.title)

