import numpy as np
from numpy.lib.function_base import disp


class KNN:
    """
    K Nearest Neighbours model
    Args:
        k_neigh: Number of neighbours to take for prediction
        weighted: Boolean flag to indicate if the nieghbours contribution
                  is weighted as an inverse of the distance measure
        p: Parameter of Minkowski distance
    """

    def __init__(self, k_neigh, weighted=False, p=2):

        self.weighted = weighted
        self.k_neigh = k_neigh
        self.p = p

    def fit(self, data, target):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix( M data points with D attributes each)(float)
            target: Vector of length M (Target class for all the data points as int)
        Returns:
            The object itself
        """

        self.data = data
        self.target = target.astype(np.int64)
        return self

    def find_distance(self, x):
        """
        Find the Minkowski distance to all the points in the train dataset x
        Args:
            x: N x D Matrix (N inputs with D attributes each)(float)
        Returns:
            Distance between each input to every data point in the train dataset
            (N x M) Matrix (N Number of inputs, M number of samples in the train dataset)(float)
        """

        # TODO    
        data = self.data
        p = self.p
        Minkowski_distance = []
        for n in range(len(x)):
            Minkowski_distance_temp=[]
            for d1 in range(len(data)):
                val = 0
                for d2 in range(len(data[d1])):
                    val+= abs(x[n][d2]-data[d1][d2])**p
                Minkowski_distance_temp.append(val**(1/p))
            Minkowski_distance.append(Minkowski_distance_temp)
        return Minkowski_distance
        pass

    def k_neighbours(self, x):
        """
        Find K nearest neighbours of each point in train dataset x
        Note that the point itself is not to be included in the set of k Nearest Neighbours
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            k nearest neighbours as a list of (neigh_dists, idx_of_neigh)
            neigh_dists -> N x k Matrix(float) - Dist of all input points to its k closest neighbours.
            idx_of_neigh -> N x k Matrix(int) - The (row index in the dataset) of the k closest neighbours of each input
            Note that each row of both neigh_dists and idx_of_neigh must be SORTED in increasing order of distance
        """

        # TODO
        k_neigh = self.k_neigh
        Distances = self.find_distance(x)
        Neighbours = []
        Index=[]
        for distance in Distances:
            Neighbours.append((sorted(distance)[:k_neigh]))
        for dist in range(len(Distances)):
            Index_temp=[]
            for neigh in Neighbours[dist]:
                for dist2 in range(len(Distances[dist])):
                    if neigh == Distances[dist][dist2]:
                        Index_temp.append(dist2)
                        break
            Index.append(Index_temp)
        return tuple([Neighbours,Index])
        pass

    def predict(self, x):
        """
        Predict the target value of the inputs.
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            pred: Vector of length N (Predicted target value for each input)(int)
        """

        # TODO
        k_neighbours=self.k_neighbours(x)
        target = self.target
        weighted = self.weighted
        result=[]
        weight_temp={}
        
        for neigh in range (len(k_neighbours[0])):
            if(weighted):
                for neigh2 in range (len(k_neighbours[0][0])):
                    if(target[k_neighbours[1][neigh][neigh2]] in weight_temp):
                        weight_temp[target[k_neighbours[1][neigh][neigh2]]]+=(1/(k_neighbours[0][neigh][neigh2]+0.00000001))
                    else:
                        weight_temp[target[k_neighbours[1][neigh][neigh2]]]=(1/(k_neighbours[0][neigh][neigh2]+0.00000001))
                temp1=list(weight_temp.values())[0]
                temp2=list(weight_temp.keys())[0]
                for key,val in weight_temp.items():
                    if(val>temp1):
                        temp1=val
                        temp2=key
            else:
                for neigh2 in range (len(k_neighbours[0][0])):
                    if(target[k_neighbours[1][neigh][neigh2]] in weight_temp):
                        weight_temp[target[k_neighbours[1][neigh][neigh2]]]+=1
                    else:
                        weight_temp[target[k_neighbours[1][neigh][neigh2]]]=1
                temp1=list(weight_temp.values())[0]
                temp2=list(weight_temp.keys())[0]
                for key,val in weight_temp.items():
                    if(val>temp1):
                        temp1=val
                        temp2=key 
            result.append(temp2)
        return result
        pass

    def evaluate(self, x, y):
        """
        Evaluate Model on test data using 
            classification: accuracy metric
        Args:
            x: Test data (N x D) matrix(float)
            y: True target of test data(int)
        Returns:
            accuracy : (float.)
        """

        # TODO
        predict=self.predict(x)
        Correctly_predicted_instances=0
        Total_instances=0
        for instance in range(len(y)):
            Total_instances+=1
            if(predict[instance]==y[instance]):
                Correctly_predicted_instances+=1
        result = (Correctly_predicted_instances/Total_instances)*100
        return result
        pass

