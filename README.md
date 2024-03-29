# Cartomancy 

_cartomancy_ is a project for exploring two efforts:

1. Building a game engine for card games with python
2. Use reinforcement learning to build agents to play card games. 

## Goals
- The games are implemented in such a way as to make it easy to capture _events_ that occur during game play. These events
- Having a uniform way to capture game events so that the RL algorithms implemented can be trained on any game which is implemented with the engine.
- Build a novel card game!

## Progress
### Tech debt
- [ ] use [poetry](https://python-poetry.org/) to manage dependencies.
- [ ] separate the implementation of the games from the engine. (perhaps another repo?)

### Features and Functionality
- [ ] terminal window rendering of games
- [ ] 2d window based rendering of games
- [ ] UI to help users build their own games.

### Games Implemented
See the games [README](https://github.com/joedaws/cartomancy/tree/main/cartomancy/games) for more information.
- [x] go fish
- [ ] magnum opus (a game that I am designing.)

### RL strategies implemented
None yet. Only some rough outlines of how to approach this problem so far. These 
are found in the _brains_ package. 

Currently, only _go fish_ is implemented. This project is structed in such 
a way as to allow for construction of new games for which agents may 
be trained to pay.

## Getting Started

### Dependencies

* python 3.7.x or greater.

### Installing

* Clone this repository.  
* install requirements in a virtual environemnt from `requirements.txt`

### Playing Go Fish on the command line
* Currently, only go fish is implemented. 
* To run a game of GoFish between four players all using random policies use:

```
python -m cartomancy.games.run --game-config cartomancy/games/go_fish/config/random.yaml
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
