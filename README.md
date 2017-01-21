# Sudoku Solver
A simple python code which reduces the Sudoku to SAT and solves it using minisat SAT solver.

# Requirements
0. Python 3  
0. minisat solver from https://github.com/niklasso/minisat  
0. tkinter with dependencies

> Note: Complete installation instructions for MiniSat Solver are mentioned in it's respective repository but in short:

0. clone minisat `git clone https://github.com/niklasso/minisat.git`
0. cd to minisat directory `cd minisat`
0. install using `sudo make install`

# Input Format
The Sudoku is input block wise, the first row of puzzle array contains the first block of Sudoku, and so on. The blanks in Sudoku are replaced by zeros(0).
