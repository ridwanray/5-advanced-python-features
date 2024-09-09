# Generator

# def generate_infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1

# gen = generate_infinite_sequence()
# # print(type(gen))

# print(next(gen))
# print(next(gen))

# Iterator

# class RangeIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         else:
#             # Return the current value and then increment it 
#             # for next iteration
#             value = self.current
#             self.current += 1
#             return value
        
# # my_range = RangeIterator(2, 5) 
# # print(next(my_range) )
# # print(next(my_range) )
   
# my_list = [1, 2]
# iterator = iter(my_list)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# Context Managers

# file = open('some_file', 'w')
# file.write('Hello!')
# file.close()

# file = open('some_file', 'w')

# try:    
#     file.write('Hello!')
# except Exception as e:
#     print(f"An error occurred: {e}")    
# finally:
#     file.close()

# with open('some_file', 'w') as file:
#     file.write('Hello!')

# class CustomOpen:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None

#     def __enter__(self):
#         print("Entering the context")
#         # Code to acquire a resource (e.g., opening a file)
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         # Code to release the resource (e.g., closing the file)
#         if self.file:
#             self.file.close()
#             print("File closed in exit")
# #Usage
# with CustomOpen("test.txt", "w") as file_object:
#     file_object.write("Hello!")

# Decorators

# def greet_decorator(func):

# 	def wrapper(user_name):
# 		name = func(user_name)
# 		decorated_name = f"Hi, {name}"
# 		return decorated_name
		
# 	return wrapper

# @greet_decorator
# def greet(name:str):
# 	return name

# # inner = greet_decorator(greet)
# # x = inner("Ray")
# x =  greet("Ridwan")
# print(x)
# Asynchronous programming

async def read_data(db):
    data = await db.fetch('SELECT ...')
 
import asyncio

async def task_one():
    print("Task 1: Starting")
    await asyncio.sleep(4)  # Simulates a non-blocking delay of 2 seconds
    print("Task 1: Completed")

async def task_two():
    print("Task 2: Starting")
    await asyncio.sleep(1)  # Simulates a non-blocking delay of 1 second
    print("Task 2: Completed")

async def main():
    # Schedule both steps to run concurrently
    await asyncio.gather(task_one(), task_two())

# Run the asynchronous event loop
asyncio.run(main())
