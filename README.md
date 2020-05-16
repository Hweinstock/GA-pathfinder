# Genetic-Algorithm-Pathfinding

## Description

A visual illustration of a simple genertic algorithm applied to pathfinding arround obstacles.  

## Purpose 

This project was aimed towards exposing myself to the idea of a genetic algorithm in a simple sense so that hopefully I can build more interesting projects and explore more interesting ideas in the future. 

## Setup

This project is build within the Processing software, but written in Python. In order to run the project, install Processing [here](https://processing.org/download/). As far as I am aware, this project should work on any operating system with Processing installed.   

## Usage 

This project utilizes all of the default Processing functionality for running/stopping and so on.  

In order to add walls, use the following example:   
```
walls = range(4)
walls[0] = wall(0, 200, 250, 50)
walls[1] = wall(350, 200, 300, 50)
walls[2] = wall(0, 400, 150, 50)
walls[3] = wall(200, 400, 300, 50)
```   

`wall(x, y, w, h)`
- **x:** x-coordinate of top left corner of the wall. 
- **y:** y-coordinate of top left corner of the wall. 
- **w:** horizontal width of the wall. 
- **h:** vertical height of the wall. 

Then, in order to change the number of balls, change the first parameter of the initialization of brain.  
  
