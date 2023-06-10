# Beating 2048 with python
This project contains two parts:
<ol>
  <li>Recreating the popular game 2048 with python in the terminal with human readable output. The rules of the game are simple. You can move up, down, left, or right and the tiles move that direction and combine if adjacent tile has the same value. The goal is to combine tiles until you get 2048. To try out the game visit https://play2048.co.</li>
  <li>
    Creating an algorithm that suggests moves that can ultimatly beat the game. The algorithm I created beats the game about 30% of the time, which seems likely to be better than many humans. There are some things that could be done to improve the algorithm, but I suspect this within an order of magnitude of what is possible without a widely less effecient algorithm or entirely different approach (e.g., neural net).
  </li>
</ol>
In this README.md file, each of these components are explained in detail along with information about how to run the code on your own machine, and what you should expect to see if everything is working properly.

## Running the code
This section assumes that you have a newer version of python installed on your computer. Outside of that, no extra software is needed.

To run the text user interface for 2048 type the following command into terminal:

    python3 TUI.py
    
This should allow you to play 2048 using nothing but your terminal and keyboard. The initial output when typing the command explains how to make moves useing your keyboard. You should see something like this:

<img width="556" alt="Screenshot 2023-06-04 at 12 06 18 AM" src="https://github.com/zroe1/2048python/assets/114773939/e18bf0b5-4e0f-4b9a-a178-65ba7dc09f64">

## Running my 2048-beating Algorithm
To run my 2048-beating Algorith, type the following command into terminal:

    python3 simulategames.py
    
This runs 1000 games of 2048 (it takes some time) and displays the results of the games in terminal. The output should look something like this:

<img width="293" alt="Screenshot 2023-06-04 at 12 20 21 AM" src="https://github.com/zroe1/2048python/assets/114773939/9bbfb652-329d-4232-b2ab-278f9a39f7cc">

This gives you an idea of how the algorithm I wrote preforms. As you can see, in this batch of games, the algorithm I wrote won 308 out of 1000 games and even got tiles above 2048 in 3 of the games played.

You can change the variable NUM_GAMES in simulategames.py to simulate less or more games. You can also change the method suggest_move in classes2048.py to try your own algorithm and see if you can beat the game. Happy hacking!
## Resources:
Code fommating and documentation loosly follows the Google python formating guide:
https://google.github.io/styleguide/pyguide.html
