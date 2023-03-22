import numpy as np


class HMM:
    """
    HMM model class
    Args:
        A: State transition matrix
        states: list of states
        emissions: list of observations
        B: Emmision probabilites
    """

    def __init__(self, A, states, emissions, pi, B):
        self.A = A
        self.B = B
        self.states = states
        self.emissions = emissions
        self.pi = pi
        self.N = len(states)
        self.M = len(emissions)
        self.make_states_dict()

    def make_states_dict(self):
        """
        Make dictionary mapping between states and indexes
        """
        self.states_dict = dict(zip(self.states, list(range(self.N))))
        self.emissions_dict = dict(
            zip(self.emissions, list(range(self.M))))

    def viterbi_algorithm(self, seq):
        """
        Function implementing the Viterbi algorithm
        Args:
            seq: Observation sequence (list of observations. must be in the emmissions dict)
        Returns:
            nu: Porbability of the hidden state at time t given an obeservation sequence
            hidden_states_sequence: Most likely state sequence 
        """
        # TODO

        #initializing states/arrays
        probability_of_hidden_state = np.zeros((self.N+1, self.N+1))
        t_array = np.zeros((self.N+1, self.N+1), dtype=int)
      
        #initialization
        for i in range(self.N):
            probability_of_hidden_state[0, i] = self.pi[i] * self.B[i, self.emissions_dict[seq[0]]]
            t_array[0, i] = 0

        #recursion
        for i in range(self.N):

            for j in range(self.N):

                max_probability_of_hidden_state = -1
                max_t = -1

                for k in range(self.N):

                    l_probability_of_hidden_state = probability_of_hidden_state[i, k] * self.A[k, j] * (self.B[j, self.emissions_dict[seq[i]]])

                    if l_probability_of_hidden_state > max_probability_of_hidden_state:

                            max_probability_of_hidden_state = l_probability_of_hidden_state
                            max_t = k

                    probability_of_hidden_state[i+1, j] = max_probability_of_hidden_state
                    t_array[i+1, j] = max_t


        max_probability_of_hidden_state = -1
        max_t = -1

        for i in range(self.N):

            l_probability_of_hidden_state = probability_of_hidden_state[self.N, i]

            if l_probability_of_hidden_state > max_probability_of_hidden_state:

                max_probability_of_hidden_state = l_probability_of_hidden_state
                max_t = i

        #reversing states and termination
        states = [max_t]
        for i in range(self.N, 0, -1):
            states.append(t_array[i, states[-1]])

        states.reverse()
        self.states_dict = {a:b for b, a in self.states_dict.items()}

        return [self.states_dict[i] for i in states]
        #pass














































