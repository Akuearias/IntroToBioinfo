import argparse
import numpy as np
import pandas as pd

def gap_penalty(g,alpha,beta):
    # ... affine gap penalty for gap of length g:
    return 0 if g==0 else -alpha-beta*g

def sigma(a,b,ids,mms):
    # ... simple scoring for identities (ids) and mismatches (mms):
    return ids if a==b else mms


# Function to calculate the optimal SW global alignment score
def score_lSW(A,B,ids,mms,alpha,beta) :
    '''
    Sequence A is of length m (labeling rows)
    Sequence B is of length n (labeling columns)
    '''

    m = len(A)
    n = len(B)

    # Adding a blank space at the beginning of the string:
    A = ' '+A
    B = ' '+B

    # Initializing the score matrix:
    score_matrix = np.zeros([m+1,n+1],dtype=int)

    # Calculations:
    for i in range(1,m+1):
        for j in range(1,n+1):
            d = [score_matrix[i-1,j-1] + sigma(A[i],B[j],ids,mms)]
            h = [score_matrix[i,j-k] + gap_penalty(k,alpha,beta) for k in range(1,j+1)]
            v = [score_matrix[i-l,j] + gap_penalty(l,alpha,beta) for l in range(1,i+1)]
            score_matrix[i,j] = max(d+h+v+[0])

    print("\nlSW score matrix (for debugging):\n")
    smdf = pd.DataFrame(score_matrix)
    smdf.set_axis(list(A),axis=0,inplace=True)
    smdf.set_axis(list(B),axis=1,inplace=True)
    print(smdf)
    print("")

    return score_matrix.max()


if __name__ == '__main__' :

    parser = argparse.ArgumentParser()
    parser.add_argument('-seq1', type=str, default = 'C', help="Sequence 1 (string)")
    parser.add_argument('-seq2', type=str, default = 'CCG', help="Sequence 2 (string)")
    parser.add_argument('-ids', type=int, default = 1, help="Identity score (positive INT)")
    parser.add_argument('-mms', type=int, default = -1, help="Mismatch score (non-positive INT)")
    parser.add_argument('-alpha', type=int, default = 1, help="alpha (non-negative INT)")
    parser.add_argument('-beta', type=int, default = 1, help="beta (non-negative INT)")
    args = parser.parse_args()
    os = score_lSW(args.seq1,args.seq2,args.ids,args.mms,args.alpha,args.beta)

    print("The optimal lSW alignment score of sequences:\n", args.seq1, "\n", args.seq2)
    print("for scoring scheme ids=",args.ids," mms=",args.mms," w(g)=",args.alpha,"-",args.beta,"*g")
    print("is ",os)
