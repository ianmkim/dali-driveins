# Drive in Movie Scraper
requirements were to scrape all the 500 or so drive-in movie theatres in the continental US and their contact information. This was a small job for OEI Events, a drive in movie & entertainment firm in central Virginia.

# Challenges
Since I needed to complete this job fast rather than do it smartly, I decided to grab a random list of US capitals and their coordinates. Thankfully Vim had my back when converting it all to a format python can understand.

I then iterated through each capital and searched for drive-in movie theaters with max radius. I had to experiment a bit with the request frequency but 5 seconds worked out fine.

# Running the code
Enter in your own API key in the localenv and run "source localenv" then run with python 3.5+.

Install python prereqs with "pip3 install -r requirements.txt --user" or with sudo if you're crazy like that.


