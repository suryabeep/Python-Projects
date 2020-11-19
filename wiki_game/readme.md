# The Wikipedia Game
<b><u>What:</u></b><br>
This lets you play the popular 'Wikipedia Game' in your terminal. Input the two articles you want to try and link, and let the script do the work for you.

<b><u>Why:</u></b><br>
I have to do this for my CS 225 final project but in C++, and I was bored so I decided to do the whole thing on the side in Python instead.

<b><u>Steps to run this on your machine:</u></b><br>
1. Clone this repo to somewhere on your machine. Let's call this 'wiki_game/'
2. Download the wiki-topcats.txt and wiki-topcats-page-names.txt files from http://snap.stanford.edu/data/wiki-topcats.html
3. Place those two files in the wiki_game/data directory
4. Run 'python3 wiki_game.py --names data/wiki-topcats-page-names.txt --edges data/wiki-topcats.txt'

<b><u>To-Do:</u></b><br>
1. Add nearest-match suggestions if the user entered an article that wasn't in the graph.
2. Add function to save the graph on quit and load an existing graph.
