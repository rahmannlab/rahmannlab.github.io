from collections import Counter
import numpy as np


if __name__ == '__main__':
    # Zeilen: fair, unfair, anlocken
    transition = np.array([[0.8, 0.1, 0.1],
                           [0.2, 0.8, 0.0],
                           [0.2, 0.0, 0.8]])
    emission = np.array([[1 / 6] * 6, [1 / 5] * 5 + [0], [1 / 7] * 5 + [2 / 7]])
    log_transition = np.log(transition)
    log_emission = np.log(emission)
    print(log_transition)
    print(log_emission)


    def forward(seq):
        f = log_transition[0] + log_emission[:, seq[0]]
        for x in seq[1:]:
            f_next = []
            for q in range(len(f)):
                q_prev = np.argmax(f + log_transition[:, q])
                logpmax = f[q_prev] + log_transition[q_prev, q]
                probsum = np.sum(np.exp(np.delete(log_transition[:, q], q_prev) - logpmax))
                f_next.append(log_emission[q, x] + logpmax + np.log1p(probsum))
            f = f_next

        i = np.argmax(f)
        return f[i] + np.sum(np.exp(np.delete(f, i) - f[i]))


    sequences = []
    with open('simulation.txt') as f:
        for line in f:
            if line.startswith('sequence:'):
                seq = [int(s) for s in line.split(': ')[1].strip()]
                #print(Counter(seq))
                sequences.append(seq)
    print(len(sequences))

    forward_probs = []
    for s in sequences:
        f=forward(s)
        print(f)
        forward_probs.append(f)
    
    print(np.mean(forward_probs))