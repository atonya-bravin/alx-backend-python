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
#### Task 1 [Solution]
**Featured File** => 0-basic_async_syntax.py

#### Task 1 [Solution Breakdown]
- In the begining of the file i imported asyncio and random, the packages that i require to solve the task.
- I then defined a coroutine `async def wait_random(max_delay: int = 10) -> float:` which uses the python anotation. The method takes in a max_delay which is an integer and defaults to 10, returning a float.
- I then get a random number between 0 and 10, returning that number from the function.

### Task 2
Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay. wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.


**1-main.py**
```
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
```
#### Task 2 [Solution]
First implementation without concurrency
```
#!/usr/bin/env python3
"""This module contains the wait_n function"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This method takes in two integers, n and max_delay,
    then spawns the wait_random function, n number of times,
    with a max_delay.
    """

    randoms = []

    for counter in range(n):
        # call the wait_random method while awaiting on it
        random_value = await wait_random(max_delay)

        #just insert the value in the list index 0 if empty
        if len(randoms) == 0:
            randoms.insert(0, random_value)

        #if value is greter than or equal to last value, append it
        elif random_value >= randoms[len(randoms) - 1]:
            randoms.append(random_value)

        #go through the list, inserting the value in corect index in the list
        else:
            for index in range(len(randoms)):
                if random_value < randoms[index]:
                    randoms.insert(index, random_value)
                    break
    return randoms
```
  
  
**Featured File** => 1-concurrent_coroutines.py

#### Task 2 [Solution Breakdown]

