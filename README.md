# Conway's Game of Life

A single-celled organism simulator

## Background
The	playing	field	for	Conway’s	game	of	life	consists	of	a	two	dimensional	grid	of	
cells.	Each	cell	is	identified	as	either	alive	or	dead.	For	this	exercise,	let’s	assume	the	
playing	field	is	an 8x6	grid	of	cells	(i.e.	8	columns,	6	rows).
The	challenge	is	to	calculate	the	next	state	of	the	playing	field	given	any	initial	grid	
state.	To	find	the	next	state,	follow	these	rules:

Rules of the game:
1. Any	live	cell	with	fewer	than two	live	neighbors	dies,	as	if	caused	by	underpopulation.
2. Any	live	cell	with	more	than	three	live	neighbors	dies,	as	if	by	overcrowding.
3. Any	live	cell	with	two	or	three	live	neighbors	lives	on	to	the	next	generation.
4. Any	dead	cell	with	exactly	three	live neighbors	becomes	a	live	cell.
5. A	cell’s	neighbors	are	those	cells	which	are	horizontally,	vertically	or	
diagonally	adjacent.	Most	cells	will	have	eight	neighbors.	Cells	placed	on	the	
edge	of	the	grid	will	have	fewer.
## Setup
Python 3.5 or greater is the only requirement. No outside libraries or packages are needed. 

**Using zip file:**
    
Unzip and open the extracted directory
    
**Using git:**
 
 `git clone https://github.com/blthree/kata`

## Running the simulation

This simulator runs as a Command-line application
```
>python kata.py -c 1 sample_board.txt

INFO: Running simulation for 1 cycle(s) using file: 'sample_board.txt' as starting board
Initial Board State:
......O.
OOO...O.
......O.
........
...OO...
...OO...

Final Board State:
.O......
.O...OOO
.O......
........
...OO...
...OO...

```
### Options
```
usage: kata.py [-h] [-v] [-c CYCLES] BOARD_FILE
Conway's Game of Life Simulator

positional arguments:
  BOARD_FILE            File containing game board

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         displays intermediate board states as well as starting
                        and final states
  -c CYCLES, --cycles CYCLES
                        # of simulation cycles, defaults to 1 if omitted

```

```
BOARD_FILE            File containing game board
```
The board file should be a plain-text file containing any number of rows of equal widths (can be with or without newline at end of file). An example board is provided in `sample_board.txt`:
```
......O.
OOO...O.
......O.
........
...OO...
...OO...
```

```
-h, --help            show this help message and exit
```
```
-v, --verbose          -v, --verbose         displays intermediate board states as well as starting and final states
```
Displays starting and intermediate board states as well as the final state.
```
-c CYCLES, --cycles CYCLES
                        # of simulation cycles, defaults to 1 if omitted
```
Number of cycles to run the simulation. 
## Unit Tests
To run unit tests (from project directory):
`python -m unittest tests`       