# EECS_738_Final_Project

This is the final project for EECS 738, Machine Learning. The contributors are Bisher Anadani, Will Duncan, Surabhi Khachar, Andre Kurait, and Vivek Tallavajhala. This project looks at collegiate level basketball datasets and attempts to create game-outcome prediction models using various machine learning algorithms. These algorithms/models were either built from scratch or utilized existing python libraries.

## Project code

Most of the code exists on Jupyter notebooks as they provided a streamlined medium to work with pandas. There is also some Python code, all of which can be found in the 'Notebooks' folder. All the CSV data and output bracket prediction exists in the 'Data' folder.

### Installation

To run the python code, simply download the zip file of this project. The notebooks have embedded outputs of the code that was run previously on kernels.

### Models

The models we used for this included the following:
- Simple, back propagating neural network from scratch: A Neural Net written from scratch that has three layers, input, hidden, and output. Utilized for predicting game outcome.
- Neural Network using Keras: Keras is used here to create a neural network that predicts game outcome. It plays around with different numbers of input layers and hidden layers to see where the best outcome lies.
- Random Forest Regressor: Utilizing the SciKit Learn Python libraries to predict game outcome.
- Markov Model: This model is attempting to predict the seed of the 68 teams that are admitted to the NCAA basketball tournament. To do this, the model needs a transition matrix that rates each team as 'probability of being better' and 'probability of being worse' than each other team in the NCAA. These probabilities are obtained through logistic regression. Once the transition matrix is obtained, the probabilities can be used to seed the bracket. The quality of the bracket is determined by how well the seeds predicted to win do throughout the tournament compared to what actually happened.

Both the neural networks tested with different combinations of input data to find the best features. A lot of feature selection was also done in order to identify which (from the 72 that were given) were actually useful in predicting game outcomes.  

## Data

The data for this project comes from Kaggle and Sports Reference. It includes game data for every NCAA basketball team for every game for however many seasons you'd like. We worked with the most recent 2018-2019 season.

### Results

Results can be shown in the 'Bracket' file for the outcome of game prediction, and in the various notebooks for each of the neural nets.

## References

* [Sports Reference](https://www.sports-reference.com/) - Used for Game Data
* [Kaggle](https://www.kaggle.com/) - Used for Seeding Data

## Libraries Used

* [Scikit Learn](https://scikit-learn.org/stable/) - Random Forest Regressor
