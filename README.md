# Timestamp Microservice

## What is this?

A small API built on Flask, satisfying the requirements for FreeCodeCamp's Timestamp Microservice project (except in Python).

## Project Specs

<https://www.freecodecamp.org/challenges/timestamp-microservice>

<https://timestamp-ms.herokuapp.com/>

### User stories

1. I can pass a string as a parameter, and it will check to see whether that string contains either a unix timestamp or a natural language date (example: January 1, 2016).

2. If it does, it returns both the Unix timestamp and the natural language form of that date.

3. If it does not contain a date or Unix timestamp, it returns null for those properties.

### Example usage

```url
https://timestamp-ms.herokuapp.com/December%2015,%202015
https://timestamp-ms.herokuapp.com/1450137600
```

### Example output

```json
{ "natural": "December 15, 2015",
  "unix": 1450137600 }
```
