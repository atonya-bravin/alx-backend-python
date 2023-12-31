# 0x01. Python - Async
This is a project to build up on the asynchronous python programming.

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
Write a coroutine called async_generator that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.  
  
  
**0-main.py**  

```
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
```
#### Task 1 [Solution]
**Featured File** => 0-async_generator.py

#### Task 1 [Solution Breakdown]
- Importation of packages and methods to use in the solution.
- Defination of a method **async_generator**, which is expected to return a generator object that yields float values. The None represents the type of value that can be sent to the generator using the send() method, and the second None represents the type of value that can be used to raise a StopIteration exception using the throw() method.  
```
async def async_generator() -> Generator[float, None, None]:
```
- Implementation of a 1 second delay before returning a random floating point number

### Task 2
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments. The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.


**1-main.py**

```
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())
```
#### Task 2 [Solution]
**Featured File** => 1-async_comprehension.py

#### Task 2 [Solution Breakdown]
- Importation of packages and methods to use in the solution.
- Defination of a method **async_comprehension** that is expected to collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.
- Use of the async comprehension to iterate over the values produced by the async_generator and assigns them to the variable result. Overall, the async_comprehension function asynchronously waits for the values yielded by the async_generator and collects them into a list, which is then returned.
```
result = [counter async for counter in async_generator()]
```
- Returning of the 10 numbers in a list

### Task 3
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather. measure_runtime should measure the total runtime and return it. Notice that the total runtime is roughly 10 seconds, explain it to yourself.  


**2-main.py**

```
#!/usr/bin/env python3

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
```
#### Task 3 [Solution]
**Featured File** => 2-measure_runtime.py

#### Task 2 [Solution Breakdown]
- Importation of packages and methods to use in the solution.
- Defination of a method **measure_runtime** that  execute async_comprehension four times in parallel using asyncio.gather, then measures and returns the total runtime.
- Capture of the start_time before running the code
- Use of the Python asyncio library to run the async_comprehension() function four times concurrently using the asyncio.gather() method.
```
await asyncio.gather(*(async_comprehension() for _ in range(4)))
```
- Capture of the end_time after running the code, then returning the difference(total runtime).
