# Jared Radecki
# UIN: 427002698
# Texas A&M University

Scraper.py:
  
scraper works for BidtoArt.com but does not directly sign in. Because of problems run into during creation, the user must navigate to the auction results and change the display amount to 100 (for the most data scraped in one run). Must be specific auction reults of individual art pieces not the collection of auction results. 

The user must then must inspect the page and copy and paste the html locally. The reason for this is when downloading the html, all URLs to pictures disappear.
    
The user must edit two lines in order to properly use the program:

  Line 43: user must change name from "scrape23.html" to the name of the file they saved from copying and pasting
  Line 47: set current ID to the next ID wanted in data acquisition
 
The delay at the end is set to 8 seconds per picture due to website policy of "no spamming"
  
rename.py:

  If a mistake is made when entering the ID, rather than rescraping, this renames all pieces just scraped to the correct ID.
  
datageneralizer.py:
  
  The data received from BidtoArt.com is too specific for machine learning. This code will change specfic mediums to more broad mediums.
  
  
