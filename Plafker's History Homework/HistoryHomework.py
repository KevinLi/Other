#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-        HistoryHomework.py        -#
#-         Version 1.0.0.0          -#
#-        Written by KevinLi        -#
#-            2011-02-11            -#
#-Public Domain. Knock yourself out!-#
#-         Thanks, symetrik.        -#

#import re                              # I really need to learn regex. Next version, maybe.
import urllib

HtmlDict= {                             # Finally learned how to use dictionaries. They're cool.
    "<strong>"              : ""     ,  "</strong>" : "\n"  ,   # Date
    "<div>"                 : ""     ,  "</div>"    : ""    ,   # Forgot what these do
    "</p><ul><li><div>"     : "\n- " ,  "</li><li>" : "\n- ",   # Bullet points
    "</p>"                  : ""     ,  "<p>"       : "\n"  ,   # Paragraphs
    "</li>"                 : ""     ,  "<li>"      : ""    ,   # lists
    "</ul>"                 : ""     ,  "<ul>"      : ""    ,   # Unordered lists
    "<p/>"                  : "\n"   ,                          # Plafker, what the hell are you doing
    "<em>"                  : ""     ,  "</em>"     : ""    ,   # Italics tag
    "\t"                    : ""     ,                          # Fucking tabs
    " "                     : "\n"   ,  " "         : "\n\n",   # And this is why we can't have ni- UTF-8 FTW
    ""                    : ""     ,                          # Plafker, you have no idea what you're doing, do you.
    "<a href=\""            : "\b"   ,  "\">"       : ""    ,   # Links!
    "\" target=\"_blank\">" : "\n"   ,  "</a>"      : "\n"  ,   # Damn it, Plafker.
    "<br/>"                 : ""     ,                          # What version of HTML are you using...
    "<font color=\"#ff0000" : ""     ,  "</font>"   : ""    ,   # I really, really need to learn regex.
}

# Holy fuck, Plafker. It's too inconsistent to effectively parse. I tried.

def FormatHomework(HtmlDict, Text):
    for key in HtmlDict: Text = Text.replace(key, HtmlDict[key])
    return Text

_url = "http://lovinghistory.org/1st2wkshmwkwh.aspx" # Hopefully the URL doesn't change. :|

if __name__ == '__main__':
    Text = urllib.urlopen(_url).readlines() # Retrieve the HTML
    for line in Text:
        if "<div id=\"IWS_WH_ZoneRowContainer\"><table class=\"MS_WH_ZoneRow\">" in line:
            Text = line # Removing everything but the homework
    Text = Text.split("<div id=\"General_Content\">")[1].split("</td><td style=\"WIDTH: 1%\"")[0]
    Text = FormatHomework(HtmlDict, Text) # Removing tags, mainly.
    print(Text)
