import random

def creating_population(size):
    parray=[]
    for i in range(0,100):
        tarray=[]
        for j in range(0,size):
            n=random.randint(0,size-1)
            tarray.append(n)
        parray.append(tarray)
    return parray


maxFitness = 28
def fitness(arr1):    
    nattack=0
    #print("a ",arr1)
    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)):
            if(arr1[i]!=arr1[j] and (abs(i-j)!=abs(arr1[i]-arr1[j]))):
                nattack+=1
    return nattack

def probability(individual, fitness):
    return fitness(individual) / maxFitness

def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
        
def reproduce(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def mutate(x):
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(0, n-1)
    x[c] = m
    return x

def genetic_algo(population, fitness):
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)//2):
        x = random_pick(population, probabilities)
        y = random_pick(population, probabilities)
        child = reproduce(x, y)
        print_individual(child)
        new_population.append(child)
        child = mutate(child)
        print_individual(child)
        new_population.append(child)
        if fitness(child) == 28: break
    return new_population

def print_individual(x):
    print("{},  fitness = {} "
        .format(str(x), fitness(x)))

if __name__ == "__main__":
    population = creating_population(8)
    generation = 1


    while not 28 in [fitness(x) for x in population]:
        print(" For Generation {} ".format(generation))
        population = genetic_algo(population, fitness)
        print("Maximum fitness = {}".format(max([fitness(n) for n in population])))
        generation += 1

    print("Solved in Generation {}!".format(generation-1))
    for x in population:
        if fitness(x) == 28:
            print_individual(x)
            break;
