import scrapy


class RateYourMusicListSpider(scrapy.Spider):
    name = 'rate-your-music-lists'

    start_urls = [
        #'https://rateyourmusic.com/list/huit/complete-john-peel/15/'
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 2] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 3] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 4] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 5] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 6] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 7] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 8] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 9] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 10] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 11] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 12] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 13] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 14] - Rate Your Music.html',
        'file:///home/sam/calliope-bots/bots/peelbot/data/Complete John Peel [Page 15] - Rate Your Music.html',
    ]

    def parse(self, response):
        for artist in response.css('a.list_artist'):
            yield {
                'artist': artist.css('a::text').get()
            }
