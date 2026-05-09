#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']

apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]
peaches = fruit[3]

plt.bar(people, apples, width=0.5, color='red', label='apples')

plt.bar(
    people,
    bananas,
    width=0.5,
    bottom=apples,
    color='yellow',
    label='bananas'
)

plt.bar(
    people,
    oranges,
    width=0.5,
    bottom=apples + bananas,
    color='#ff8000',
    label='oranges'
)

plt.bar(
    people,
    peaches,
    width=0.5,
    bottom=apples + bananas + oranges,
    color='#ffe5b4',
    label='peaches'
)

plt.ylabel('Quantity of Fruit')

plt.yticks(range(0, 81, 10))
plt.ylim(0, 80)

plt.title('Number of Fruit per Person')

plt.legend()

plt.show()