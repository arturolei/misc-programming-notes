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

### Lists ###

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
- append vs extend
  - append takes an item and adds to it, a list added to a list remains a list. 
  - extend adds an item on the same level; a list extended to list makes the list longer. 

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

### Loops ###

For Loops and Loops in general saves the calculations we have to do. 

More or less **for** each thing **in** a collection, python does something. Yay. 

The body of a loop can contain many statements. Loop variables can be called anything we want. 

Python has a built-in function called **range** that produces a sequence of numbers, the numbers are produced on demand (NOT A LIST, it's OWN CLASS, 'range'). 
- range(N) are the numbers 0.. N-1, keep this in mind if you use the loop variable as an index. 
- range() iterates of a [sequence](https://github.com/dlab-berkeley/python-fundamentals/blob/master/Glossary.md#sequence) of numbers. 

**The Accumulator Pattern**
- Common approach in programming is to initialize an accumulator variable, empty string or empty list 
- Update variable with a collection. 

### Conditionals ###

- An if statemetn (more properly called a conditional statement) controls whether some block of code is executed or not. 
- Structure is similar to For loop, first line opens with if and ends with a colon, body is indented (4 spaces)

**Keypoints from D-labs**
1. Use `if` statements to control whether or not a block of code is executed.
2. Conditionals are often used inside loops.
3. Use `else` to execute a block of code when an `if` condition is *not* true.
4. Use `elif` to specify additional tests.
5. Use boolean operators to make complex statements.
6. Conditions are tested once, in order.

### Functions ###
- Functions are the basic building blocks of programming. 
- Functions are the equivalent of variables for code--->pieces of code, the way variables take string and numbers
- Functions take arguments or parameters (stuff we want them to process or with which to do magic)
- Functions are defined and called in seperate lines. 

Functions can return a result, using 'return':
- print != return
- may occur anywhere in the function but it terminates the function. 
- final result default

**An Interesting Case Study: Order of Operations
```Python

#Why You Call the Function:
def report(pressure):
    print('pressure is', pressure)
    
print('calling', report, 22.5) #you didn't actually call the function, dumbass!

#Again, call the function or else you get nothing
result = print_date(1871, 3, 19)
print('result of call is:', result) 

#using parameter names explicitly to override order:

def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(day=1, month=2, year=2003) #note that the order of the inputs is wrong, we have to explicitly called parameters. 
```
### Scope ###

So, like in JS, variables created in function have a limited place where they can be used... 
So variables created in function cannot be accessed outside that function. 

Running funcitons on mutable datatypes changes mutable datatypes. It might be important to remember this.
Here is a brief list of [the mutable and immutable types.](https://codehabitude.com/2013/12/24/python-objects-mutable-vs-immutable/)

positional/keyword arguments:
- Positional arguments -->be careful of the order in which we put them in
- Keyword arguments-> default value for certain values can be entered. This is for situations where we have a default value. 

```Python
def send(message, recipient, cc=None, bcc=None):
    """ Prints a kind greeting to our input
    returns nothing"""
    print(message, recipient)
    print("CC: ", cc)
    print("BCC: ", bcc)
    
send('Hello','World') #Default value will be none
send ('Hi', 'Mark', 'Lisa', 'Tommy') #Default value will be something. 
```

### Dictionary ####

A dictionary is a collection of key-value pairings...  
dict = {key1: val1, key2: val2}

NB: Dictionaries are indexed by keys. 

Values can be changed but keys cannot be changed.

(dictionary name).keys() returns 
(dictionary name).values() returns 

```Python
new_poets_dict = poets_dict

poets_dict["language"] = "Persian"
print("new dict: ", new_poets_dict["language"])

new_poets_dict["language"] = "Farsi"
print("first dict: ", poets_dict["language"]) #this will say Farsi, the two are linked. 
```

**If you need data to be organized AND ordered, USE A LIST not a dictionary.**
- You index by key with a dicitionary not by some universal indexical value. 
- You use square brackets with a dictionary. 

You can use "in" to see if a key is in the dictionary.
```Python
d = {'apples': 0.49, 'oranges': 0.99, 'pears': 1.49, 'bananas': 0.32}

print('Canada' in l) 
print('grapefruit' in d)
print(0.49 in d)
print('grapefruit' not in d)
```

**Keypoints**
- A python dictionary is a collection of key, value pairs.
- Use dictionary keys to access the values.
- Once a dictionary has been created, you can change the values of the data and assign new keys.
- Dictionaries have their own methods, and you can loop through key/value pairs.
- Dictionaries are different from lists in important ways.

### Files ###
Okay, now we go to terra incognita for me. 

There's the old read(), open(document name, r)
-But don't forget close() or else bad things happen?

Then there is the "with open" way.
- However, use the `with open` syntax and this will automatically close files for you. 
- The `'r'` indicates that you are reading the file, as opposed to, say, writing to it.

```Python
# better code
with open('example.txt', 'r') as my_file:
    text = my_file.read()
    
print(text)
```

Import csv, csv is common file type. 

Review the Juypter notebook for more details. 

```Python
```

### Libraries ###

Use `import` to load a library into memory.
-You must refer to each item with library's name
  -math.cos(pi)

You can use `from` to import specific things. 
`from` math `import` cos,pi

You can create an "alias" for a library when importing to shorting programs.
```Python
import math as m
```

You can also import everything with the * character:
```Python
from math import *
print(pi)
```

To find out stuff about a library, type:
`help`(name of library)
- HOWEVER YOU MUST IMPORT LIBRARY FIRST

**Keypoints**
- "Most of the power of a programming language is in its libraries."
- "A program must import a [library](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#library) in order to use it."
- "Use `help` to find out more about a library's contents."
- "Import specific items from a library to shorten programs."
- "Create an alias for a library when importing it to shorten programs."


### Errors ###
Everybody hurts. Everybody makes mistakes. 

Python tells us the **type or category of error**.
Python reports a **sytax error** when it can't understand a program. Basically, your Python grammar sucks. 

**Traceback** refers to the sequence of errors. They are levels of errors that you can have. 

####FUCKING INDENTATION ERRORS!!!#####
- Tabs or spaces, be consistent. 
- four spaces or tabs, be consistent

A copy and past of some things that they advise:
## Debugging Strategies

### Know what it's supposed to do

The first step in debugging something is to *know what it's supposed to do*. "My program doesn't work" isn't good enough: in order to diagnose and fix problems, we need to be able to tell correct output from incorrect. If we can write a test case for the failing case --- i.e., if we can assert that with *these* inputs, the function should produce *that* result --- then we're ready to start debugging. If we can't, then we need to figure out how we're going to know when we've fixed things.

### Start with a simplified case.

If you're writing a multi-step loop or function, start with one case and get to work. Then ask what you need to do to generalize to many cases.

### Divide and conquer

We want to localize the failure to the smallest possible region of code. The smaller the gap between cause and effect, the easier the connection is to find. Many programmers therefore use a **divide and conquer** strategy to find bugs, i.e., if the output of a function is wrong, they check whether things are OK in the middle, then concentrate on either the first or second half, and so on.

### Change One Thing at a Time, For a Reason

Replacing random chunks of code is unlikely to do much good. (After all, if you got it wrong the first time, you'll probably get it wrong the second and third as well.) Good programmers therefore *change one thing at a time, for a reason*. They are either trying to gather more information ("is the bug still there if we change the order of the loops?") or test a fix ("can we make the bug go away by sorting our data before processing it?").

Every time we make a change, however small, we should re-run our tests immediately, because the more things we change at once, the harder it is to know what's responsible for what.

### Outside Resources

If you've tried everything you can think of to logically fix the error and still don't understand what Python is trying to tell you, now the real searching begins. Go to Google and copy/paste the error, you're probably not the only one who has run into it!

### List Comprehensions ###
Yawn.

### Best Practices ###
Comment on everything.
Remember if you forget the Jedi Code, you can always type `import this`  to get what you want back.
**DOC STRINGS** explain how to use code. Docstrings are '''-'''

**Additional Resources**
* "Code like a Pythonist" http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)
* "Pep Styleguide", https://www.python.org/dev/peps/pep-0008/)
* "Python Objects", Fredrik Lundh, http://www.effbot.org/zone/python-objects.htm
* "Python track: python idioms", http://www.cs.caltech.edu/courses/cs11/material/python/misc/python_idioms.html
* "Be Pythonic", Shalabh Chaturvedi, http://www.cafepy.com/article/be_pythonic/ (PDF version)
* "Python Idioms", http://www.gungfu.de/facts/wiki/Main/PythonIdioms
* "The Hitchhiker’s Guide to Python", http://docs.python-guide.org/en/latest/
* "What is Pythonic?", http://blog.startifact.com/posts/older/what-is-pythonic.html