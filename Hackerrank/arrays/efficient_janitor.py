"""
selecting number of bags that together do not weight more than 3 pounds to dump in the outside trash can and return to school
given a number of plastic bags n, the weights of each bag, determine the minimum number of trips the janitor has to make

constraints: all weights are between 1.01-3 inclucsive, and each groups sum is at max 3

note: this is a transformation of 2 sum, but the constraints here is vital
"""

def efficientJanitor(weights:list)->int:
    n = len(weights)
    i = 0
    j = n-1
    target = 3
    count = 0
    weights.sort()
    while j>0:
        if weights[j]<=1.99 and weights[i]+weights[j]<=target:
            # since min(weights)>=1.01, therefore one trip can take no more than 3 bags
            i+=1
        count+=1
        if i>=j:
            break
        j-=1
    return count


if __name__ == "__main__":
    assert 3==efficientJanitor([1.01, 1.99, 2.5, 1.5, 1.01])