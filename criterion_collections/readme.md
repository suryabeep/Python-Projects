# Your Favorite Filmmaker's Favorite Films
'Art for Artists' is kind of hard to find. Maybe it's just me but I certainly have a hard time finding good examples. Luckily, the Criterion Collection asked a bunch of capital-A Artists what their favorite movies were, and posted their responses on its website. This simple python script collects all the movies mentioned, along with who chose them and how many times they were chosen. <br>

### Usage:
Run 'python3 main.py' with at least one of --count and --info <br>
--count: Prints movies that were picked by \<count> or more people<br>
--info: Prints information on the chosen film. eg: 'python3 main.py --info 'A Woman Under the Influence' --count 20'

### Todo:
Create some sort of basic web page to display this information. <br>
DONE - Convert this to use Selenium so I can scrape all the lists possible, not just the first one. 