# Game Data Stream Processor & Data Alchemist

## Overview

This project demonstrates Python data processing using:
- generators (`yield`)
- list comprehensions
- dictionary comprehensions
- random data generation

It simulates game-like player events and score analysis.

---

## Features

### 1. Event Generator
- Generates infinite random player actions
- Each event is a tuple: `(player, action)`

### 2. Event Stream Processing
- Prints 1000 generated events
- Uses `next()` with a generator

### 3. Event Collection
- Builds a list of 10 generated events

### 4. Event Consumption
- Randomly removes events from the list
- Uses a generator with `yield`
- Stops when list becomes empty

---

## Data Alchemist Section

### Transformations

- Original list of players contains mixed capitalization
- Creates a fully capitalized version using list comprehension
- Filters only originally capitalized names

### Score System

- Assigns random scores to each player
- Computes average score
- Filters players with scores above average using dictionary comprehension

---

## Concepts Practiced

- Python generators
- `yield` keyword
- `next()` function
- list comprehensions
- dictionary comprehensions
- random module usage
- data filtering and aggregation

---

## How to Run

```bash
python ft_data_stream.py
python ft_data_alchemist.py