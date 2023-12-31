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
- Importation of the asyncio and 0-basic_async_syntax packages that I use to accomplish the task
- Creation of a list of **n** concurrent tasks
```
concurrent_tasks = [asyncio.create_task(wait_random(max_delay))
                        for _ in range(n)]
```
- Insertion the the concurrent tasks in the completed_tasks list according to their completition time.
```
 for task in asyncio.as_completed(concurrent_tasks):
        completed_tasks.append(await task)
```

### Task 3
From the previous file, import wait_n into 2-measure_runtime.py. Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float. Use the time module to measure an approximate elapsed time.  
  
  
**2-main.py**  
```
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
```
#### Task 3 [Solution]
**Featured File** => 2-measure_runtime.py

#### Task 3 [Solution Breakdown]
- Importation of the modules to be used to accomplish the task
- Get start time before running the code in the function
- Run the code in the function  
```asyncio.run(wait_n(n, max_delay))```
- Get the time the process got completed

### Task 4
From the previous file, import wait_n into 2-measure_runtime.py. Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float. Use the time module to measure an approximate elapsed time.


**3-main.py**
```
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```
#### Task 4 [Solution]
**Featured File** => 3-tasks.py

#### Task 4 [Solution Breakdown]
- Importation of the packages I use to achieve the task
- Annotation of the method with a task being expected as the return value  
```
def task_wait_random(max_delay: int) -> asyncio.Task:
```
- Returning of a newly created task
```
return asyncio.create_task(wait_random(max_delay))
```

### Task 5
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.

**4-main.py**
```
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
```
#### Task 5 [Solution]
**Featured File** => 4-tasks.py

#### Task 5 [Solution Breakdown]
- Change of the imported package and method.
- Create a list of n tasks, leaving the work of task creation to the task_wait_random method in the 4-tasks.py module.  
```
concurrent_tasks = [task_wait_random(max_delay)
                        for _ in range(n)]
```
