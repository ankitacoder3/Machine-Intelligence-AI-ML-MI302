import numpy as np


class KMeansClustering:
    """
    K-Means Clustering Model

    Args:
        n_clusters: Number of clusters(int)
    """

    def __init__(self, n_clusters, n_init=10, max_iter=1000, delta=0.001):

        self.n_cluster = n_clusters
        self.n_init = n_init
        self.max_iter = max_iter
        self.delta = delta

    def init_centroids(self, data):
        idx = np.random.choice(
            data.shape[0], size=self.n_cluster, replace=False)
        self.centroids = np.copy(data[idx, :])

    def fit(self, data):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix(M data points with D attributes each)(numpy float)
        Returns:
            The object itself
        """
        if data.shape[0] < self.n_cluster:
            raise ValueError(
                'Number of clusters is grater than number of datapoints')

        best_centroids = None
        m_score = float('inf')

        for _ in range(self.n_init):
            self.init_centroids(data)

            for _ in range(self.max_iter):
                cluster_assign = self.e_step(data)
                old_centroid = np.copy(self.centroids)
                self.m_step(data, cluster_assign)

                if np.abs(old_centroid - self.centroids).sum() < self.delta:
                    break

            cur_score = self.evaluate(data)

            if cur_score < m_score:
                m_score = cur_score
                best_centroids = np.copy(self.centroids)

        self.centroids = best_centroids

        return self

    def e_step(self, data):
        """
        Expectation Step.
        Finding the cluster assignments of all the points in the data passed
        based on the current centroids
        Args:
            data: M x D Matrix (M training samples with D attributes each)(numpy float)
        Returns:
            Cluster assignment of all the samples in the training data
            (M) Vector (M number of samples in the train dataset)(numpy int)
        """
        #TODO
        cluster = []
        data_size=data.shape[0]
        for k in range(data_size):
            value = data[k] - self.centroids
            distance = np.linalg.norm( value , axis=1)
            distance_minimum=np.argmin(distance)
            cluster.append(distance_minimum)
        
        answer= np.array(cluster)   
        return answer
        pass

    def m_step(self, data, cluster_assgn):
        """
        Maximization Step.
        Compute the centroids
        Args:
            data: M x D Matrix(M training samples with D attributes each)(numpy float)
        Change self.centroids
        """
        #TODO
        cluster_size=self.n_cluster
        for v in range(cluster_size):
            cluster_value=data[cluster_assgn == v]
            new_centroid = np.mean(cluster_value, axis=0)
            self.centroids[v] = new_centroid
        pass

    def evaluate(self, data):
        """
        K-Means Objective
        Args:
            data: Test data (M x D) matrix (numpy float)
        Returns:
            metric : (float.)
        """
        #TODO       
        distances=[]
        data_size = len(data)
        no_of_centroids = len(self.centroids)
        for x in range(data_size):
            for y in range(no_of_centroids):
                distance_of_points_from_centroid=self.centroids[y]-data[x]
                distance_array=np.square(distance_of_points_from_centroid)
                distances.append(distance_array)
        distances = np.sum(distances, axis=1)
        sum_of_squared_errors = 0
        for d in distances:
            sum_of_squared_errors += d
        answer= sum_of_squared_errors
        return answer
        pass
