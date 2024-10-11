### Contents

- [Module 1: Optimal Python Development Lifecycle](#module-1-optimal-python-development-lifecycle)
- [Module 2: Modularization](#module-2-modularization)
- [Module 3: Advanced Object-Oriented Programming](#module-3-advanced-object-oriented-programming)
- [Module 4: Libraries for Advanced Programming](#module-4-libraries-for-advanced-programming)
- [Module 5: Automated Testing](#module-5-automated-testing)
- [Module 6: Functional Programming Paradigm](#module-6-functional-programming-paradigm)
- [Module 7: Multiprocessing and Asynchronous Programming](#module-7-multiprocessing-and-asynchronous-programming)
- [Module 8: Using Clusters](#module-8-using-clusters)
- [Module 9: Web Development](#module-9-web-development)
- [Module 10: Machine Learning](#module-10-machine-learning)
---

## Module 1: Optimal Python Development Lifecycle

### 1. Pick one of the guidelines from the Zen of Python that interests you and write 3-5 sentences about it.
   - I think the guideline "now is better than never" really resonated with me due to the explanation from the reading. Particularly where it was stated "Instead of waiting for perfection, let's start solving the given problem using the information, assumptions, skills, tools, and infrastructure we have." I tend to try for the absolute best way to do something (researching someone else's way and trying to implement even if my understanding is spotty) right off the bat and have had it really come back to bite me when my understanding of a concept is lacking. So from the guideline, I am gonna try to instead of doing something amazing from the start, at least get the best I can from my current understanding and work iteratively to get the better and best solutions over time.

### 2. What are the main elements of a good docstring?
   - placed right after a function or class definition
   - One line summary followed by a more detailed description
   - Strategically uses blank spaces to organize (NOT overusing blank spaces)

### 3. What are the main phases of a typical Python project lifecycle?
   - Requirement analysis
   - Agile development block
   - Deployment

### 4. Which part of the lifecycle discussed in your textbook do you have the least experience with?
   - Deployment
---

## Module 2: Modularization
### 1. What modules in Python exist for interacting with a file system or OS in a cross-platform way? List 3 with a 1-sentence description of what they do.
   - pathlib: Allows you to navigate and perform operations on a machine's file systems.
   - sys: Gives you access to make changes to the system and runtime environment.
   - os: Lets you manage files and environment.
   - shutil: Performs copying, moving, and removing files and directories.

### 2. Where does Python look for modules to load?
   - Depending on if it is a relative, absolute, built-in or some other module name it will look in a few places. From the reading the I believe the primary place it goes to load modules from is sys.path but the places it will look could be the python built-in standard library, current directory or the relative / absolute path provided, or the PYTHONPATH environment variable.

### 3. How can you find out what modules are currently loaded while a program is running?
   - You can use print(globals()) to print the global variable dictionary and the keys with values like "<module '_____' from /_____/____> are the modules loaded into memory.

### 4. What steps happen when you load a module using import?
   - It searches for the module given and then binds the result to a variable name in the local scope of the execution.

### 5. What is the most difficult part of making a shareable package using PyPA guidelines?
   - Creating the package, maintaining it with the setup.py in mind and versioning.
---

## Module 3: Advanced Object-Oriented Programming

### 1. What are the major design patterns of OOP? List them and for each one describe how it's implemented in Python.
   - Encapsulation: Creating classes that handle/have functions and attributes to perform actions that are directly related to that object's plausible behavior and characteristics. The classes will also manage what can or cannot be accessed from those attributes and functions. This is done through setting private (_var_or_method), protected (__var_or_method), and getter/setter methods (function: get_var/set_var, decorator: @property/@_var_or_method.setter)
   - Abstraction: Templating or creating a blueprint class, that inherits from the ABC module in the abc package, full of empty abstract methods (defined method decorated with an @abstractmethod) that other classes will inherit from and require that class objects to implement all of the abstract methods. Thus making them concrete methods within the derived class.
   - Inheritance: A child class (derived class) inherits attributes and methods from a parent class (super class) and is expanded with it's own elements. To inherit you add the parent class in parenthesis when declaring the child class: class ChildClass(ParentClass):
   - Polymorphism: The ability for an object to behave in multiple ways when calling the same method but with different arguments. This is done using method overloading and method overriding. To implement you can either define the same method in multiple classes (method overriding) or have multiple methods defined with the same name but with different parameters with different types (method overloading) (duck typing come into play heavily with method overloading)
### 2. How does Python implement multiple inheritance? What is a case in which it is useful or necessary?
   - Python lets classes inherit from one or more class and will determine what is inherited first via MRO (Method Resolution Order) and is resolved using linearization when a method or attribute is called. This order can be seen by printing the __mro__ dunder or calling the mro() method of the class. Multiple inheritance is best used when an object needs to implement more than one HAS A relationships from multiple classes. GUI's are a great example of a good time to use multiple inheritance.
### 3. List 3 ways Python achieves the effect of operator overloading.
   - Dunder methods
   - Comparison operators
   - type conversion operators
### 4. Explain duck typing with an example.
   - duck typing (dynamic typing) is objects will be defined/typed by their behaviors. Example: if I divide an integer by an integer, python's interpreter will assume we will want a remainder if there is one to be had. So the interpreter will, without prompting, set the return type of the object as a float so it will have the potential for values that are not limited to whole integers instead of losing information by only having static typing to integers.
### 5. Why are context managers useful?
   - Because they allow developers to ensure setup and cleanup operations are handled as expected. Additionally, it ensures resource management to be handled correctly and safely.
### 6. Explain and defend the practice of gradual typing.
   - Gradual typing is a feature that allows devs to use both static and dynamic typing in their programs. Static typing gives us the ability to know exactly what the type of an object is expected to be without have to constantly check, will only change when we explicitly change it, and will throw errors if it is not what we have set it to expect. Dynamic typing takes away the requirement on developers to constantly be casting types to other types and instead allows the interpreter to make a decision based on context of the code and determines the intent. By using gradual typing developers are able to get the benefits of both static and dynamic typing. When done right, devs are able to speed up their workflow by only having to be explicit on typing where it is vital and at all other times let the interpreter make educated decisions on typing based in contextual intent.
---

## Module 4: Libraries for Advanced Programming
### 1. Do you agree with the statement "Generators are better to use than iterators."? Why?
   - I do agree, because of the fact that generators act like iterators but are not required to have the information you are iterating over to be stored in memory. And instead, "generate" the elements on demand.
### 2. Are the libraries and techniques described in Chapter 4 "advanced"? From what perspective is this true? From what perspective is it not true?
   - From the perspective of beginner programmers and some new to python, these data structures would be seen as advanced. This would be due to the fact that lists, dicts, tuples and sets can be confusing at first but are quickly understood with use. While iterators and generators are much more difficult to grasp because you really need to understand data flow.
   - From the perspective of intermediate to advanced programmers this is likely to not seem advanced, due to the fact that all these data structures are fairly common in just about every other high level language and the concepts are easily transferrable between said languages.
### 3. List 3 things you learned from the material in Module 4.
   1. I learned that as of python 3, string objects can no longer hold byte data and now only hold text sequences of Unicode. While they have now created the data type byte to handle byte data.
   2. List comprehensions (uses [] to create) are not generators, but instead are a constructed list object that creates and stores the elements in memory during declaration. While generator expressions (uses () to create) create a generator object of said sequence and will lazily generate one element at a time on demand.
   3. I learned how to adjust the logging format to be changed form log_level:root: to be my own custom format.
### 4. What's the difference between a normal function, a generator and a coroutine?
   - `Function`: (def name(): [optional] return) Used for normal functional task execution.
   - `Generator`: (def name(): [required] yield) Used for iterating memory efficient sequences on demand. It will pause and resume generation and iteration at the keyword yield. It then (implicitly) uses next() to get the next yielded value.
   - `Coroutine`: (async def name(): [optional] return) Similar to a generator but is used for asynchronous operations. Can use yield but normally it will pause and resume at the keyword await. Most use cases for coroutines is related to I/O tasks
---

## Module 5: Automated Testing
### 1. What does white box testing assume?
   - That whoever is performing the tests has knowledge of how the program they are testing works. (White box you can see the insides)
### 2. What does black box testing assume?
   - That whoever is performing the tests has no knowledge of how the program they are testing works. (Black box insides are blocked from being seen)
### 3. What does a test case test?
   - test cases test for expected results from a set of conditions. And they can both test for working cases as well as error cases. The goal is to confirm functionality, error handling, and edge cases. 
### 4. Of the testing frameworks discussed in this chapter which one do you prefer and why?
   - I would say unittest, primarily because I have had previous experience using it so it is more familiar than the others. I will say that I am intrigued by the function use of pytest versus the class use of unittest and wonder how much it would help readability of test cases.
### 5. What's one burning question you have that should have been answered in this chapter but was not?
   - Hmm, as of this point a lot of the stuff this class has been covering has been review of previous classes or previous work I have done, so I am unable to come up with a question at this time. Everything has been pretty clear and concise.
### 6. What are doctests good for?
   - Simple testing of the function where the docstring resides. Hopefully making it more likely to catch when the documentation is out of date in comparison to the code.
---

## Module 6: Functional Programming Paradigm
### 1. What constructs or features for iterating over sequences, collections and infinite streams of data are new to you from this chapter? Whether new or not, list 3 that don't involve a basic sequential for loop.
   - `Compress`: I have never used this. But it allows for selecting items within a collection based off of a selector iterable.
   - `Zip`: while not new to me I think it is very important to have here. It is great for iterating on data of more than one collection in parallel.
   - `Accumulate`: Another I have not used. Which gives the ability for accumulated results from a passed function and an optional operation.
### 2. Why are type annotations useful for functions?
   - They are great for helping developers know what is expected going in and coming out of functions.
   - Most IDE's will use them to signal incorrect usage in regards to static typing.
   - In general it is helpful to prevent bugs.
### 3. Explain what happens when a decorator is used.
   - It basically wraps some functionality up and extends it with more functionality.
### 4. Does using coroutines as explained in this chapter simplify code? Justify your answer.
   - Unless I am completely mistaken, there isn't anything in chapter 6 that explicitly states it is a coroutine. So I am a little lost on how to answer this question. From the chapter summary it seems as though it will be going over multithreading/multiprocessing in the next chapter, which leads me to assume that it will also cover async and concurrency. Meaning next chapter will most likely be going over coroutines, but I may be completely wrong or misunderstood how something in this chapter is a coroutine.
   - After digging in Chapter 7, I would say that it does make code simpler in the fact that it lets you simply wait for asynchronous tasks to occur and are way easier to handle and understand than threading and processes. But it is worth mentioning that it is probably a lot less readable to those who are just beginner coders. 
### 5. Why are partial functions useful?
   - After digging I found that partial is talked about in chapter 7. Partial functions are somewhat similar to lambdas in that both allow you to create more specialized functions without rewriting existing logic. Partial functions pre-fill certain arguments of an existing function, allowing dynamic functionality while hiding unnecessary complexity. This way, you can focus only on the pieces you need, without having to explicitly define all the parameters each time. However, unlike lambdas, which create entirely new inline functions, partial functions retain the underlying function structure with fixed arguments to make their use more specific and efficient.
### 6. Give the acronym for Scope Resolution in Python.
   - `LEGB`: Local, Enclosing, Global, Built-in
### 7. Given a choice, would you rather use Pandas or a database for working with data?
   - Since we have only really explored pandas as of this point, I would say pandas due to having more experience with it, but I am not set in stone.
---

## Module 7: Multiprocessing and Asynchronous Programming
### 1. What are the main differences between multithreading, multiprocessing and asynchronous programming in Python?
#### Synchronous (one operation at a time)
<img src="resources/Synchronous.png" alt="Synchronous" width="450px"><br>
<img src="resources/Synchronous_example.png" alt="Synchronous Example" width="350px">

   - `Concurrency`: the ability to manage multiple tasks at the same time. All three methods (multithreading, multiprocessing, and asynchronous programming) can be considered concurrent in different ways.
   - `Parallelism`: Actually executing multiple tasks at the same time on multiple CPU cores. In python, true parallelism is primarily achieved through multiprocessing.
   - `Asynchronous programming`: Concurrent, but not truly parallel. Different tasks can start, process and finish in overlapping periods of time. It's more like multitasking, where tasks voluntarily yield control to let other tasks run. (asyncio module, async def _(): to create coroutine functions. Must place await keyword in places where it is safe to pause and pass control to another coroutine / awaitable commands. Ex: await asyncio.sleep(3). Run using asyncio.run(...))
   - `Multithreading`: Concurrent but not truly parallel due to GIL. Spreads work out of a task across multiple threads that run concurrently during waiting tasks. Good for IO bound tasks and not CPU bound tasks. Involves running multiple threads within a single process. Threads are like lightweight processes that share the same memory space but can execute code independently. (concurrent.futures module or multipocessing module. concurrent.futures.ThreadPoolExecutor)

#### Multithreading / Asynchronous (when an operation is waiting, another operation can be performed)
<img src="resources/Threading.png" alt="Threading" width="300px"><br>
<img src="resources/Threading_example.png" alt="Threading Example" width="350px">

   - `Multiprocessing`: Parallel and concurrent. Spreads work out of a task across multiple processes and run at the exact same time. Good for CPU bound tasks, not so great for IO bound tasks. Involves creating multiple processes, each with its own memory space. Unlike threads, processes do not share memory directly, making them more isolated and safer from race conditions. On multi-core CPUs each process runs independently in its own memory space, and Python's GIL does not apply to separate processes. Meaning, multiple processes can be executed on different CPU cores simultaneously, but can be at the cost of some memory overhead. (concurrent.futures module or multipocessing module. concurrent.futures.ProcessPoolExecutor)

#### Multiprocessing (runnning in parrallel / at the same time)
<img src="resources/Multiprocessing.png" alt="Multiprocessing" width="350px"><br>
<img src="resources/Multiprocessing_example.png" alt="Multiprocessing Example" width="350px">

### 2. What is the main difference between sequential programming for a single CPU and multicore programming?
   - SPEED / PERFORMANCE
   - `single CPU`: Tasks are executed linearly one after the other and one cannot start until the previous has completed.
   - `multicore`: Tasks that can execute on multiple CPU cores simultaneously. This is done by splitting tasks across multiple cores, allowing parts of the program to run in parallel rather than sequentially.
### 3. Why is The GIL a problem for performance? Is it a problem in reality for most applications that people write? Justify your answer.
   - `GIL`: (Global Interpreter Lock) essentially a mutex (a lock) that protects access to Python objects, ensuring that only one thread executes Python bytecode at a time, even on systems with multiple CPU cores.
   - No, for most programmers they will most likely not run into much of an issue with GIL (unless you're a data analyst dev or performing math operation often) and probably unknowingly get saved by the GIL. This would be due to that fact that a lot of code is more I/O driven than heavy computation driven, leading to threads shining where multiprocessing would most likely be overkill and the GIL would have an adverse affect. Instead and most likely unnoticed, the GIL's reference and memory management is taking a lot of manual work on that the devs would have to handle in another language.
### 4. Can multiprocessing be used for I/O bound tasks in Python?
   - Yes it can be run on both I/O bound and CPU bound tasks. But getting a benefit from doing so will depend on what work you are trying to accomplish and the hardware you are performing it on. And multithreading tends to perform better, as it is better at handling concurrent work while waiting for others to finish.
### 5. What's the difference between and I/O-bound problem and a CPU-bound problem?
   - `I/O-bound`: Performance is bottlenecked by the requirement of waiting for input-output operations / external resource availability (Reading/Writing data from disk, Network operations, downloading, etc.). Multithreading is suitable for I/O-bound problems because threads can be idle while waiting for I/O to complete, allowing other threads to make progress.
   - `CPU-bound`: Data crunching. These are computational heavy operations, that require work to be done through computing (mathematical calculations, image processing, data analysis, machine learning model training, encryption, etc.). Multiprocessing can fully utilize multiple CPU cores, allowing for true parallelism.

---

## Module 8: Using Clusters

---

## Module 9: Web Development

---

## Module 10: Machine Learning

---