# Rithm School Talk, May 25: The Tricky Parts of JavaScript #

Before the start, the instructor polled the class and asked to know what people wanted to know.
- Closure
- ES6
- Whatever the hell they meant "tricky parts of JS"
- Hoisting (LET does hoist but you don't get access to what is "let" because it's a temporal dead zone)
	- LET gives us a different issue with hoisting. 
- It's nice to hear that we're all drinking that "React" Kool-aid

## Closures

**Scope** = things can't be called outside of a domain, variables are limited 
- Scopes can be created by functions
- There is a global scope. 
  - PROBLEM: GLOBAL IS GLOBAL, global variables can easily be overwritten. 
- ES2015 has an idea of something called "block scope"

```javascript

function():{
	return function(){
		return "Hello Class"
	}
}

```

- A function that returns a function which returns "Hello Class"

The idea of closure = inner functions that make use of variables defined in outer functions when those outer functions have returned. JS only remmebers 
the variable it needs to remember. **This idea is unique to JS**
- Variables defined in outer functions that are used in inner function even when those outer functions have been returned. 

### So when do we use closure?###
- In order to write programs in a functional style, we need to use closure. Haskell, React, Redux (combine reducers)
- Common purpose of using closure-->Maintaining state requires that people don't modify that state, that people don't mess with our code, protecting information or certain bits of information from the outside (similar to the notion of private or public variables.)

Case Study:

'''
function counter(){
	var count = 0
	return function inner(){
		count++
		return count
}
}
c1()
```

c1= counter() returns inner(), count variable effectively is a private variable. 

function classRoom(){
	var instructors = ['Tim', 'Matt', 'Elie'];
	return {
		getInstructors: function(){
		return instructors;
	}
		addInstructors: function(string){
		instructors.push(string);
		return instructors;
	}

	}
}

Closure can return an object that contains two functions, those inner two functions can still access variables.

Cfr. "module" pattern-->Design pattern common in JS-->Design patterns are universally structured way of doing things. 
- Make use of closure and wrapped code in module. 
	- Instead of making classroom in global scope, I have made a variable called module. 
- NB: Libraries often assigned to some module you have made. 

- Variant known as revealing modular pattern (all functions in outer function, inner function is something compact, ES2015 allows for more extreme 
refactoring)

- See "Revealing Module Pattern", for cleaning up code. 

- _Key Thing: Variables defined in outer functions being used inner functions when those outer functions have already been returned._
  - This leads to a potential "memory leak" problem with private/outer variables accumulating. 

- JS Compiler will perform some sort of garbage collection on its own. 

- Rithm school emphasizes smaller class size and paid developer experience, job stuff. 

## Hoisting

Variables defined with var keyword lifts variable declaration to the top of its scope. 
- What is diff between declaration and assignment? 
	- Declaration creates a space in memory but necessary a value (var thing; creates a variable with 'undefined')
- Var declaration is lifted to the top of its scope.

``` function sayHi(){
	var elie;// undefined
	return elie
	elie = "Instructor"
}

sayHi()
```

Two ways of writing functions in JS:
1. **function declaration**, just using function keyword.
	- function() sayHello(){}
2. function expression, lefthand stuff
	- We will use var, as in var firstFunction  = function(){return "HI"}

What's the difference? 
- Hoisting? Function declarations always hoist--> you can call a function before it is defined in the JS document.
- Function expression, (create a sayHello), hoisting a var. 
	- Why does this exist if possibly problematic? 
	- It's really stylistic.


The crux of the matter is that we should not freak out if we were to see 
``` 
function foo(){
	var first, last, 
}
```

There are lots of bad things you can do in language; it's loosely or dynamically typed. 

In ES5, they came up with something called "use strict" mode; 
- Let's make things fail loudly instead of silently.  ESLINT, 
- This should be a default configuration you should set up. 

## ES2015/ES6: Let/Const ##

ES6 allowed for two types, const and let.

const DOES NOT mean immutability. 
- const just blocks reassignment. 
	- const numbers = [1,2, 3, 4]-->You can use push on numbers and add a valable. 
	- However, you cannot reassign numbers.

- let gives you a new kind of scope. 
```
var instructor = "Elie";
if (instructor == "Elie"){
	let fact = true;
}
fact 
```
This returns a Reference error, fact exists only in the scope of the IF statement. 
Some have even gone so far as to allow call for let being used instead of 'var'

**let** does hoist but does not have access to its declaration, but not initiziaiton, see documentation for more clues. 

-Advise use of ```let``` in loops. 

##ES2016/6: Class##

What's a class? It collects data and functionality. 
We create copies of that class. 

JS has no notion of class. JS has objects and functions. 


You can create a factory function which produces/makes objects. 

```
function createStudent(first,last){
	return {
		first: first,
		last: last
	}
}

function Student(first,last){
	this.first = first;
	this.last = last;
}

Student('Tim', 'Garcia');-->Undefined
```

However, new Student('Time', 'Garcia'); returns something akin to an object.

What does "new" do?
1. Creates {}
2. assign this ={}
3. return this 

This is not really a class or instance; it's a link. 

See object-oriented programming on the rithm school website. 

To use ```class, we can do this. 

```
class Person{
	constructor(first, last){
	this.first= first;
	this.last = last;
}
}
```

typeof Person --> returns function. 
