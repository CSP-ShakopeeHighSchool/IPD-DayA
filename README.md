# IPD-DayA - Activity 1.3.9 Tools for Collaboration / Project 1.3.10 Collaborating on a Project
### Computer Science and Software Engineering, PLTW AP CS Principles (c)2014 Project Lead The Way, Inc.


## Running the file 
* To run a tournament, execute `prisoners_dilemma.py`. 
* Place each team's strategy in a file in the same directory as this file.
* Tournament results saved to `tournament.txt` in this directory.
* `play_tournament([team0, team1, team2])` executes a tournament and writes to `tournament.txt`

## Details
* `prisoners_dilemma.py` automates competition among different strategies for the Iterative Prisoners Dilemma, the canonical game of game-theory
* Each strategy is pitted against each other strategy for `100 to 200 rounds`
* The results of all previous rounds within a 100-200 round stretch are known to both players

## Player's files
* Each team's strategy should be coded in their assigned Python file, called a `module`.
* Each player should have their own `.py` file containing three strings team_name, strategy_name, and strategy_description and a function move(my_history, their_history, my_score, their_score)

By default, when executing the `prisoners_dilemma.py` file, `[example0, example1, example2, example3]`, play a tournament. To run the tournament of `[team, team1, team1, example1]:
scores, moves, reports = main_play([team1]*3+[example1])
section0, section1, section2, section3 = reports`
