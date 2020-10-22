# ChatEvents


## Purpose
This challenge aims to see how you approach a problem and design a solution. The problem will also be a basis to have an interesting discussion about the various approaches and design patterns that could be explored. The challenge consists of a programming problem described below. After this, we will review your solution and then discuss it with you in person or over a call (if done remotely).
We're especially interested in:<br>

what paradigms (e.g. OOP, FP) you use in your code
using appropriate data structures
the overall design of your solution
unit tests
challenges you faced in your implementation
areas of your code that you would go back to and improve on
In total, the challenge should take about 1 hour to complete. Please don't spend more time on it - we think that amount of time will give us plenty to discuss.
Before you start
Some quick admin about the challenge:
You need to do the challenge in python
Do not use external libraries, use only basic language functionality
Challenge
University Response Time
The challenge focuses on modeling and manipulating chat related data to calculate statistics about them. The data is provided as an event stream in a text file, the format of which is described below. To do the calculations, you will first need to parse the data from the text file.
Your goal is to design a system that parses the event stream and computes the average response time of a university in seconds. That means the average time that an applicant is going to wait if they message that university.
The response time is the amount of time it takes for a mentor to send a message after an applicant sends a message.
For example, if an applicant sends a message at 1 pm and a mentor responds at 2 pm on the same day, then the mentor's response time is 1 hour.
The file stream.txt contains a sequence of events that have taken place.
Each line in the file represents an event. An event contains a series of values, separated by a | (pipe) character. The first value is always the event type
The table below shows the format of each event.
```
Notes:
Applicants don't have a universityName field since they can send messages to many universities, however, a mentor can only be part of one university.
The sentTime is given in seconds.
Calculate the mean response time of Edinburgh university.
Messages which do not have a response should be ignored. Print the result to standard output.
```
