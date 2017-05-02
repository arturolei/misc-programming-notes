#Notes on Python (D-Lab Workshops/Seminars)#

## Webscraping with Python, 4/24 and 4/28 ##
There are two ways of getting data:
1. Webscraping--> Every scraping job you do is inefficient, relies on downloading a lot of data-->generally encourage people not to do this especially if there is another way
2. API (Application Programming Interface)--->Get structured data back, JSON--->Please see if there's an API
  *API data access might be limited

### Rule of Thumb: ###
If no API, you have to scrape-->Etiquette for scraping? API's furnish structured data. 
* Check to see if they let you. 

Webscraping most of the time, we can find what we want through HTML, sometimes we can find this through CSS. 

CSS makes finding key elements that we want. 

Markdown and HTML integrated with code, things look a lot more presentable... Things can look nice when you program. 
Specific can run-->You can save stages within your kernel. Better than writing 

Need request library, bs4-->Import Beautiful soup.

JS Problem-->Some sites do not populate elements until things happy. 

BeautifulSoup(src, 'lxml'), src exq

**DO NOT FORGET** time.sleep(x) where x is positive integer. **DO NOT FORGET TO SLEEP** or given Python speed, you could get blocked by the server (constantly pulling data)

Please take a timestamp photo
- If you do scraping, write code to create a text so that you have all the original data... 
- You never want to scrape things twice or multiple times because you forgot to do something the first time around. Better to have than not have. 

## Python Fundamentals, 2 May 2017 ##

[Here are the notes for this course.](https://github.com/dlab-berkeley/python-fundamentals/blob/master/Day_1/00_Intro.md)

#### A definition of programming: #### knowing how to program and programming languages could perhaps be considered as *different things*. 
* Most programmers know how to program in more than one language, but it's because they know *how to program*. Concepts are universal. Everything else is a matter of 
syntax.
* What language you should you learn? It depends on what you are trying to accomplish.  

#### What is programming like? ####
* Most of your time will be spent de-bugging (StackOverflow is spice. Spice is life.)
* Most of your time will be spent reading documentation and attempting to decipher it. 
* Most of your time will be spent googling errors. 
* Most of your time will be spent writing print statements. 

### Running Python ###

#### Running Python in the shell ####

**Simple Way:** just type 'python' in the shell. This is **interactive mode**.
  * Probably not the best for trying to write code. 

**Other Simple Way:** Normal Mode
  *Just type python (prog name).py

**NB: You can tell which version of python you have by typing which python in the console.**

**IDEs and Other Tools**
- IDEs offer you an integrated development environment where you can compile, interpret, and debug. All nice looking.
  -You can also manage packages with those. 

 ##### Jupyter Notebook ####
 Jupyter Nteobook is included in the Anaconda distribution. Notebook files have the extension. "ipynb"
 
 ###### Why Juypter? ######
 * Jupyter Notebook lets you run chunks of codes in blocks as you wish as well as tab completion. 
 * You can write comments in handy dandy markdown. 

 Tips:
 * You can press CTRL+ ENTER or CMD+ ENTER will run cell 
 * ln [ ], empty brackets mean that we did not run stuff. 
 * You can merge or split cells/blocks of code as you see fit. 
 * Markdown is a lightweight markup language. It can be easily converted to HTMl. Here is a [markdown cheatsheet.](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

 By default, Juypter notebook will think you are writing a code cell. You need to click the code segment. 





