import urllib2
import re

# Needed for MetroLyrics
import HTMLParser
        
class GetLyrics(object):
    def __init__(self, artist, title, site=None):
        self.Artist = artist
        self.Title = title
        # Order these by preference
        # Current top three Google results for "lyrics"
        # Ordered by correctness of results
        self.Sites = ["MetroLyrics.com","Lyrics.com","AZLyrics.com"]
        # Lyrics Resource:
        # Lyrics.com: LyricFind
        # AZLyrics.com: Manually
        # MetroLyrics: Gracenote
        self.SiteNum = 0
        self.LyricsSite = ""
        self.QueryNextSite()

    def QueryNextSite(self):
        try:
            if self.QuerySite(self.Sites[self.SiteNum]) != 0:
                self.SiteNum += 1
                # Recursion!
                self.QueryNextSite()
        except IndexError:
            pass

    def QuerySite(self, site):
        # Returns status code instead of lyrics.
        if site == "AZLyrics.com":
            # No need to go through the site's search function. Awesome.
            try:
                self.Lyrics = urllib2.urlopen(
                    "http://www.azlyrics.com/lyrics/{0}/{1}.html".format(
                        self.Artist.replace(" ","").lower(),
                        self.Title.replace(" ","").replace("'","").lower()
                    )
                ).read()
            except urllib2.HTTPError:
                return 1
            # Good thing they have these two comments there.
            # Much easier to separate the lyrics from the rest of the page.
            self.Lyrics = re.split("<!-- start of lyrics -->", self.Lyrics)
            self.Lyrics = re.split("<!-- end of lyrics -->", self.Lyrics[1])[0]
            self.Lyrics = self.Lyrics.replace("<br />","\n").strip()
            self.Lyrics = self.Lyrics.replace("\n\n","\n")
            self.LyricsSite = "AZLyrics.com"
            return 0
        if site == "Lyrics.com":
            try:
                self.Lyrics = urllib2.urlopen(
                    "http://www.lyrics.com/{1}-lyrics-{0}.html".format(
                        self.Artist.replace(" ","-").lower(),
                        self.Title.replace(" ","-").replace("'","").lower()
                    )
                ).read()
            except urllib2.HTTPError:
                return 1
            self.Lyrics = re.split("<div id=\"lyric_space\">", self.Lyrics)
            self.Lyrics = re.split("---<br />Lyrics powered by", self.Lyrics[1])[0]
            self.Lyrics = self.Lyrics.replace("<br />","\n").strip()
            self.Lyrics = self.Lyrics.replace("\r\n","\n")
            self.Lyrics = self.Lyrics.replace("\n\n","\n")
            self.LyricsSite = "Lyrics.com"
            return 0
        if site == "MetroLyrics.com":
            htmlparser = HTMLParser.HTMLParser()
            # This one's two-stage because the "Print" page is easier to parse
            try:
                # I probably shouldn't use the same variable a hundred times
                self.Lyrics = urllib2.urlopen(
                    "http://www.metrolyrics.com/{1}-lyrics-{0}.html".format(
                        self.Artist.replace(" ","-").lower(),
                        self.Title.replace(" ","-").replace("'","").lower()
                    )
                ).read()
            except urllib2.HTTPError:
                return 1
            self.Lyrics = re.split("<li class=\"ll-print\"><a href=\"request.php\?lyricid=", self.Lyrics)
            self.Lyrics = re.split("&amp;dothis=printlyrics\"", self.Lyrics[1])[0]
            # self.Lyrics is the id number now
            try:
                self.Lyrics = urllib2.urlopen(
                    "http://www.metrolyrics.com/request.php?lyricid={0}&dothis=printlyrics".format(
                        self.Lyrics
                    )
                ).read()
            except urllib2.HTTPError:
                return 1
            self.Lyrics = re.split("<center><pre>", self.Lyrics)
            self.Lyrics = re.split("</pre></center>", self.Lyrics[1])[0]
            self.Lyrics = htmlparser.unescape(self.Lyrics)
            self.LyricsSite = "MetroLyrics.com"

if __name__ == "__main__":
    artist = raw_input("Artist: ")
    title = raw_input("Title: ")
    out = GetLyrics(
        artist if artist != "" else "rick astley",
        title if title != "" else "never gonna give you up")
    try:
        print("\n" + out.Lyrics)
        print("\n" + out.LyricsSite)
    except TypeError:
        print("Nothing Found!")
