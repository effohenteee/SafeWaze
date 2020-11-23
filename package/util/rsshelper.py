import feedparser


class RSSHelper:
    # TODO: Docs and header
    def __init__(self, url):
        self._articles = feedparser.parse(url)

    def __getitem__(self, index):
        return self._articles.entries[index]

    def parse(self, feed):
        self._articles = feedparser.parse(feed)

        return self


if __name__ == '__main__':
    rss = RSSHelper('https://tools.cdc.gov/api/v2/resources/media/404952.rss')
    print('The first item in the feed is:')
    print(rss[0])
