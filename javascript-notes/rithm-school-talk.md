# Rithm School Talk, May 25: The Tricky Parts of JavaScript #

Before the start, the instructor polled the class and asked to know what people wanted to know.
- Closure
- ES6
- Whatever the hell they meant "tricky parts of JS"
- Hoisting (LET does hoist but you don't get access to what is "let" because it's a temporal dead zone)
	- LET gives us a different issue with hoisting. 
- It's nice to hear that we're all drinking that "React" Kool-aid

##Closures

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

###So when do we use closure?###
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

-Variant known as revealing modular pattern (all functions in outer function, inner function is something compact)


