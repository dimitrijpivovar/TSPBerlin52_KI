# TSP Solver using Evolutionary Algorithm

## Project Overview
This project implements an evolutionary algorithm to solve the Traveling Salesman Problem (TSP) using the `tsplib95` library and the `berlin52` dataset. The goal is to find the shortest possible route that visits each city exactly once and returns to the origin city.

## Features
Visualize graph of the problem
Visualize distance matrix as a table

## Flowchart
![flowchart](./assets/flowchart.PNG)

## To Do
- init pop -> done
- evaluation / fitness
- parent selection
- variation / mutation + cross
- survival selection
- stop condition
- return calculated best outcome

## Installation
To run this project, you need to install the required Python libraries:

```bash
python -m pip install -U pip
pip install tsplib95
pip install matplotlib
pip install networkx
pip install pandas
pip install numpy
