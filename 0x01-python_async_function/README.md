# 0x01. Python - Async
This is a project that tries to build on the skill of creation of asynchronous applications.

## Objectives
This project is posed with the aim of achiving knowledge in;
1. async and await syntax
2. How to execute an async program with asyncio
3. How to run concurrent coroutines
4. How to create asyncio tasks
5. How to use the random module

## Requirements
Some of the main requirements in this particular project include;
1. A README.md file, at the root of the folder of the project, is mandatory
2. Allowed editors: vi, vim, emacs
3. All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
4. All your files should end with a new line
5. All your files must be executable
6. The length of your files will be tested using wc
7. The first line of all your files should be exactly `#!/usr/bin/env python3`
8. Your code should use the pycodestyle style (version 2.5.x)
9. All your functions and coroutines must be type-annotated.
10. All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
11. All your functions should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'`
12. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Featured tasks and solutions
### Task 1
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it. Use the random module.  
  
  
**0-main.py**  
```
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```
### Task 1 [Solution]

