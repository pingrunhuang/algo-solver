import threading

# # Worker thread 
# def worker(n, sema): 
#     # Wait to be signaled 
#     res = sema.acquire() 
#     # Do some work 
#     print('Working', n, res)
# # Create some threads: counter = release_call - acquire_call + value
# sema = threading.Semaphore(value=0)
# nworkers = 10 
# for n in range(nworkers): 
#     t = threading.Thread(target=worker, args=(n, sema,))
#     t.start()

# sema.release() 
# sema.release()


# Worker thread def worker(n, sema): # Wait to be signaled sema.acquire() # Do some work print('Working', n) # Create some threads sema = threading.Semaphore(0) nworkers = 10 for n in range(nworkers): t = threading.Thread(target=worker, args=(n, sema,)) t.start()


players = [
    "fred",
    "wilma",
    "berney",
    "pebbles",
    "bam bam"
]

def go(players:list):
    import random
    receivers = set()
    givers = [x for x in range(0, len(players))]
    result = []
    for i in range(len(players)):
        pair = [players[i]]
        rand_index = random.randint(0, len(givers)-1)
        while givers[rand_index]==i or givers[rand_index] in receivers:
            rand_index = random.randint(0, len(givers)-1)
        giver_index = givers.pop(rand_index)
        print(receivers, givers)
        receivers.add(giver_index)
        pair.append(players[giver_index])
        result.append(pair)
        
    return result



if __name__ == "__main__":
    # res = supervisor()
    # print(res)
    # main_async()
    print(go(players))