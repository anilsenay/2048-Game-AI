# CSE4082 Project 2 - Artificial Intelligence for 2048 Game 

## Aim of the Project
This project aims to implement 4 different heuristics on the “2048 Game” to get indicated results. These heuristics include;
1. The tile with the highest value is on the corner + The distribution of the tiles is near to the corner.
2. The number of possible mergeable tiles + The possibility of the highest value of tiles to merge
3. Monotonicity
4. The tiles are ordered like snake-shaped

## Explanation of the Heuristics
### Heuristic 1
The purpose of this heuristic is to collect the tiles with the higher value on the corner. We combined two heuristics to get better results in the game. In this heuristic, we take the power of every tile with a selected number (weight) based on its location on the board. This weight is 3 on the corners which is the highest one we give because we want the tiles with the highest value to be at the corner. The evaluation function is given in the equation below. weight[i][j] could be 3, 2, 1 based on the location i, j. board[i][j] is the value of that tile in the position i, j.

<img src="https://i.ibb.co/dQFQxR1/image.png" data-canonical-src="https://i.ibb.co/dQFQxR1/image.png" width="400" />

The figure in the below shows the weight matrix of heuristic 1. x is the value of the tile.

<img src="https://i.ibb.co/gvJK7nM/image.png" data-canonical-src="https://i.ibb.co/gvJK7nM/image.png" width="400" />


### Heuristic 2

The purpose of this heuristic is to make tiles to be merged. We take the square of the value of the tile. By doing this, we ensure the merge of the highest value, because we want the higher tiles to be merged. Also, we multiply the empty tiles with a constant which is 4190304, by doing this we make the game do more merge which is available because we want to have as empty tiles as possible.

### Heuristic 3

This heuristic makes the game collect tiles with decreasing order from one corner to another.
Heuristic tries to ensure that the tiles with the highest values should be clustered in a corner and decrease along with the right&down or left&down or left&up or right&up directions. In this way, we keep the board organized and we prevent the tiles with smaller values from getting orphaned. The figure shows the weight matrix of the heuristic. The corner has the highest weight and the given weight decreases as shown. The evaluation function is given in equation 2, weight[i][j] could be 7, 6,1.

<img src="https://i.ibb.co/jJp6btH/image.png" data-canonical-src="https://i.ibb.co/jJp6btH/image.png" width="400" />


The below figure shows the weight matrix of heuristic 4. x is the value of the tile.

<img src="https://i.ibb.co/Dg01N9p/image.png" data-canonical-src="https://i.ibb.co/Dg01N9p/image.png" width="400" />


### Heuristic 4

The aim of this heuristic is to order squares from highest value to lowest value in the shape of a snake. This is our best-performed heuristic. We give weight values from 15 to 0. In the evaluation function below, we multiply board value in position i, j with 4weight[i][j]. The figure shows the values of 4weight[i][j].

<img src="https://i.ibb.co/sQVkKpG/image.png" data-canonical-src="https://i.ibb.co/sQVkKpG/image.png" width="400" />

## Best Plays for each configuration

![](https://i.ibb.co/NKhDv4P/image.png)
