bicycles = ['tek','cannondale','redline','specialized']
print (bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
# f-strings
message= f"My first bike was a {bicycles[0].title()}."
print(message)
motorcycles = ['honda','yamaha', 'suzuki']
print(motorcycles)
# replace
motorcycles[0] = 'ducati'
print(motorcycles)
# add
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# insert
motorcycles.insert(0,'ducati')
print(motorcycles)
# remove
del motorcycles[0]
print(motorcycles)
# remove with pop  FIFO
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# remove the first element LIFO
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)
# list comprehension
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)
example = list(map(lambda x: x**2, range(10)))
print(example)
example1= [x**2 for x in range(10)]
print(example1)
