# Lab link: https://gist.github.com/jholman-bcit/b2be86f14f0d96f62f48d66ea459bb93 Insertion and Selection Sort

def bubble_sort(seq):
    for j in range(len(seq) - 1, 0, -1):
        for i in range(0, j):
            if (i < j and seq[j] < seq[i]) or (i > j and seq[j] > seq[i]):
                seq[i], seq[j] = seq[j], seq[i]

def selection_sort(seq):
    for j in range(len(seq) - 1):
        best_i = j
        for i in range(j + 1, len(seq)):
            if seq[i] < seq[best_i]: 
                best_i = i    
        #swap
        seq[j], seq[best_i] = seq[best_i], seq[j]

            
def insertion_sort(seq):
    for j in range(1,len(seq)):
        block = j
        for i in range(j):
            if seq[block] < seq[i]:
                seq[block] , seq[i] = seq[i], seq[block]


