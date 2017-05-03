# Notes on Python (D-Lab Workshops/Seminars) #

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
 
 ###### Why Jupyter? ######
 * Jupyter Notebook lets you run chunks of codes in blocks as you wish as well as tab completion. 
 * You can write comments in handy dandy markdown. 

 **Jupyter Tips and Trivia:**
 * You can press CTRL+ ENTER or CMD+ ENTER will run cell 
 * ln [ ], empty brackets mean that we did not run stuff. 
 * You can merge or split cells/blocks of code as you see fit. 
 * Markdown is a lightweight markup language. It can be easily converted to HTMl. Here is a [markdown cheatsheet.](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
 * By default, Juypter notebook will think you are writing a code cell. You need to click the code segment and change it to Markdown.
 * Variables persist between cells.

 **Python Tips and Trivia**
 - Variables must be created before they are used.
 - Python is case-sensitive. 
 - In Python 3.X, Print() you can string together arguments given to the print function by using commas and the default element between parameters is a space.
 - Use meaningful variable names. Please review the conventions for doing this. 
 - dir() returns a list of the variables

 **An Interesting Case Study of Variable Assignment:**
 
 _NB: Variables only change value when something is assigned to them._
 
 ```Python
lowest = 1.0
highest = 3.0
temp = lowest
lowest = highest
highest = temp #temp still retains the initial assignment value of 1.0.

print (highest) #This should give us 1.0


#This is a similar situation:
initial = "left"
position = initial #NB: POSITION IS NOT TIED TO INTIAL
initial = "right"

print (position) #Position should retain initial assignment value. 
 ```

### Keypoints (According to them), Part 2 of Day 1 ###

1. "Use variables to store values."
2. "Use `print` to display values."
3. "Variables persist between cells."
4. "Variables must be created before they are used."
5. "Python is case-sensitive."
6. "Variables can be used in calculations."
7. "Use meaningful variable names."

 
 **Leaving Jupyter**
 - You can quit by going from File-->"Close and halt", CTRL+ C, then Y to quit in the console.
 - Kernel-->"Restart and clear output", FILE--> "Close and halt"
 - You can also save a checkpoint. So if you #@#@ up you can go back later. 

### Python Data Types ###

#### Types Trivia: Every value has a type. #####
- Every value has a specific type.
- You can use type(var) function to determine type. Yup. 
- Types control what we can do with variables, you can add strings but not subtract them. You can multiply them. 
- You can add floats and integers, but you will produce a float. So 9.0 * 2 = 18.0 NOT 18.00

**Some Cool Functions**
- int(), str() for quick conversion of data types.
- len() gives you length. 


** Some Highlights from the Challenges **
```Python
#You cannot int a string that is a float. You need to float then string.
print("fractional string to int:", int(float("3.4"))) 

#Division of integers produces a float it seems. Multiplication of integers does not. I wonder why. 
print(8/5)
type(8/5)
```
### Strings ###

**Keypoints on Strings**
- You can add/concatenate strings with +
- You can get strings to repeat with *
- Indexing starts at zero. 
- Slicing [start: end-1] or in old timey math notation, [start, end_index_val)

**Strings have methods:**
NB: In ipython, you can use tab completion following '.' to see what methods an object has. Yipee skipee.
- ipython also lets you append a '?' to a method without parenthesis to get a description of what it does, e.g. str.upper? returns a brief description. 
- Calling certain string methods does not change value of the original string-->REASSIGN if you want to change the original string. 
- strip(substring) takes away the last instance.
- replace(substring_old, substring_new) replaces all instances. 

```Python
print(str(2).upper()) #Python likes this but does not change anything, as youu cannot uppercase a number.
```


**Closing Comments on Strings**
- Some mathematical operators can be used on strings
- Strings can be indexed, Python indexing always starts at 0!
- Strings, and other types, have their own methods, which are called using dots after the variable, and then the method name.
- Using a function is "calling it", we "pass arguments" to a function

### Built-In Functions ###

**Notes on Functions**
- Functions take arguments
- There are some built-in functions like max, min, round (this rounds a number to an integer or specified number)
-Functions may work

## The Jupyter Notebook has two ways to get help.##
- Place the cursor inside the parenthesis of the function,
  - Hold down `shift`,
  - and press `tab`.
- Or type a function name with a question mark after it.

## Difference between Function, Method, Object ##
  
A **function** is a piece of code that is called by name. It can be passed data to operate on (ie. the parameters) and can optionally return data (the return value).

A **method** is a function which is tied to a particular object. Each of an object's methods typically implements one of the things it can do, or one of the questions it can answer. It is called using the dot notation: e.g. `object.method()`. Objects have methods. 

An **object** is a collection of conceptually related grouping of variables (called "members") and functions using those variables (called "methods"). Every [object](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#object) is an instance of a `class`, which is like a blueprint for an object. 

  - Everything that exists is an object.
  - Everything that happens is a function call.
  
Read more about objects, classes and methods [here](https://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming)

Check out our Python glossary [here](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md).

## Python Fundamentals, Day 2/3 ##

### Lists ####

Lists are ordered collections of data. Indexing begins at zero. Yadda

You can use slicing notation on lists. 
```Python
#Holy cow, this works!
country_list = ['Surinam', 'Vietnam', 'Denmark', 'Andorra']
print(country_list[1:3])
```

Strings are **immutable**! Lists are **mutable** ; they can be changed on the fly.  
- Changing a list item changes the original list.
- NB: TO COPY AN ENTIRE LIST-->USE SLICING

**List methods:**
- del list[3]-->del method deletes element from list. 
- append(item) is a useful method that lets you append things. 
- index(value) is useful, returns index for content.

**Slices of Slice: Tidbits**
- list[start:end (or rather the index before which we stop) :stride/step length]
- list[::-1] is a good quick formula for reverse a list.
- list[:] is copying

**Keypoints (cribbed from them)**
1. A list stores many values in a single structure.
2. Use an item’s index to fetch it from a list.
3. Lists’ values can be replaced by assigning to them.
4. Appending items to a list lengthens it.
5. Use del to remove items from a list entirely.
6. The empty list contains no values.
7. Lists may contain values of different types.
8. Character strings are immutable.
9. Indexing beyond the end of the collection is an error.