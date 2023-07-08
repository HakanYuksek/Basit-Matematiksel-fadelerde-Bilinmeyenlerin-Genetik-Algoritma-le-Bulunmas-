import random
import toPostfix

# This method initialize the population according to given parameters
def initialize(population_size,chromosome_size,postfix_notation,res,is_different_from_zero,variables):
    population = []

    if is_different_from_zero:
        min_point = 1
        max_point = res - 1
    else:
        min_point = 0
        max_point = res
        
    if "/" in postfix_notation:
        max_point = res * 20
        
    for each in range(population_size):
        list1 = []
        for i in range(chromosome_size):
            r = random.randint(min_point, max_point)
            list1.append(r)

        ind = [list1,find_fitness(list1,postfix_notation,res,variables)]

        population.append(ind)

    return population

# This method sorts the given population according to their fitness points
def sort(population):
    sorted_population = population.copy()
    for i in range(len(sorted_population)-1):
        j = i + 1
        k = i
        min = sorted_population[i][1]
        while j < len(sorted_population):
            if sorted_population[j][1] < min:
                min = sorted_population[j][1]
                k = j
            j += 1
        temp = sorted_population[i].copy()
        sorted_population[i] = sorted_population[k].copy()
        sorted_population[k] = temp.copy()

    return sorted_population

# We can use the sequential selection method to select parents by using this method
def selection_sequential(population1):
    
    i = 1
    for j in range(len(population1)):
        population1[j][1] = i
        i += 1
        
    parent1, parent2 = selection(population1)

    return parent1, parent2
        
# This method selects two parents to produce new child for the new population
# Roulette Wheel Selection method is used in here
def selection(population):
    
    fitnesses = []
    for each in population:
        f = 1 / (1+ each[1])
        fitnesses.append(f)

    sum1 = sum(fitnesses)

    probs = []
    i = 0
    for each in population:
        p = fitnesses[i] / sum1
        probs.append(p)

    # For first parent selection
    S = random.random()
    p = 0
    i = 0
    while i < len(probs) and p < S:
        p += probs[i]
        i += 1    
    i -= 1
    
    # For second selection    
    S = random.random()
    p = 0
    j = 0
    while j < len(probs) and p < S:
        p += probs[j]
        j += 1
    j -= 1

    return population[i],population[j]

# We can reproduce childs with uniform cross over method by using this method
def uniform_cross_over(ind1,ind2,postfix_notation,res,variables):
    template = []
    for i in range(len(ind1)):
        r = random.randint(0,1)
        template.append(r)

    child1 = ind1.copy()
    for i in range(len(template)):
        if template[i] == 0:
            temp = child1[0][i]
            child1[0][i] = ind2[0][i]
            ind2[0][i] = temp

    return child1

# This method creates new child from given parents
# This cross over method is order based cross over method
def cross_over(ind1,ind2,postfix_notation,res,variables):
    # cp is cut point, we take first cp points from parent 1
    # then add the other points from parent 2
    cp = random.randint(0,(len(ind1[0])))

    child = []
    i = 0
    while i < cp:
        child.append(ind1[0][i])
        i += 1

    while i < len(list(variables.keys())):
        child.append(ind2[0][i])
        i += 1
        
    child = [child,find_fitness(child,postfix_notation,res,variables)]
    return child

# This method changes the child's random selected value by using randomness
# then recompute the fitness point of the child
def mutation(ind,postfix_notation,res,is_different_from_zero,variables):
    
    if is_different_from_zero:
        min_point = 1
        max_point = res - 1
    else:
        min_point = 0
        max_point = res
        
    i = random.randint(0,len(ind[0])-1)
    new_num = random.randint(min_point,max_point)
    ind[0][i] = new_num

    ind[1] = find_fitness(ind[0],postfix_notation,res,variables)

    return ind
    
# This method finds the fitness point for the given chromosome
# The fitness point is the distance to target number from given equation 
# in this problem
# For example a + b = 30, if a and b are 14, it means our fitness point is 
# 30 - a - b = 30 - 14 - 14 = 2
def find_fitness(ind,postfix_notation,res,variables):
    
    child_variables = {}
    for key,i in zip(variables.keys(),range(len(ind))):
        child_variables[key] = ind[i]
    
    postfix_res = toPostfix.solve_given_equation(child_variables,postfix_notation)
    fitness = abs(postfix_res - res)

    return int(fitness)

# This method finds the choromosome which has the best fitness point
def find_best(population):
    min = 10000
    best = population[0]
    for each in population:
        if each[1] < min:
            min = each[1]
            best = each

    return best

##############################################################################
# The actual part of the program is here
##############################################################################
def run(equation,population_size = 15, mutation_rate = 15,selection_method = "roulette_wheel", cross_over_method = "order_based", max_generation_size = 1000):

    print("Hyper Parameters:")
    print("Population Size :",population_size)
    print("Mutation Rate :",mutation_rate)
    print("Selection Method :",selection_method)
    print("Crossover Method :",cross_over_method)
    print("Max Generation Number :",max_generation_size)
    print("---------------------------------------------------------------")
    
    variables = {}
    res = ""

    for each in equation:
        if each.isalpha():
            # some variables may be duplicated in equation
            if not each in variables.keys():
                # Let's initialize the dictionary
                variables[each] = 0
                
    i = len(equation)-1
    flag = True
    while i >= 0 and flag:
        if equation[i] == "=":
            flag = False
        else:
            res += equation[i]
        i -= 1

    res = list(res)
    if " " in res:
        res.remove(" ")
    res.reverse()
    num = ""
    for each in res:
        num += each

    res = int(num)
    # We obtained the postfix notation of the given equation
    postfix_notation = toPostfix.convert_to_postfix(equation)

    ##############################################################################
    # Parameter initialization
    ##############################################################################

    chromosome_size = len(list(variables.keys()))

    is_different_from_zero = True

    # Let's create the population
    population = initialize(population_size,chromosome_size,postfix_notation,res,is_different_from_zero,variables)
    best = find_best(population)

    generation_size = 0

    if best[1] == 0:
        print("We found the solution")
        print(best)
        flag = False
    else:
        flag = True


    all_best = best.copy()

    old_population = population.copy()

    while generation_size < max_generation_size and flag:

        new_population = []
        for each in range(10):
            best_from_old = find_best(old_population).copy()
            old_population.remove(best_from_old)
            new_population.append(best_from_old)
            
        i = 0
        
        if selection_method != "roulette_wheel":
            population1 = sort(population).copy()
            
        while i < population_size-10:

            if selection_method == "roulette_wheel":
                parent1,parent2 = selection(population)
            else:
                parent1,parent2 = selection_sequential(population1)

            if cross_over_method == "order_based":
                child = cross_over(parent1,parent2,postfix_notation,res,variables)
            else:
                child = uniform_cross_over(parent1,parent2,postfix_notation,res,variables)
                
            pr = random.randint(0,100)

            if pr < mutation_rate:
                child = mutation(child,postfix_notation,res,is_different_from_zero,variables)

            new_population.append(child)

            i += 1

        old_population = population.copy()
        population = new_population.copy()
        best = find_best(population)
        generation_size += 1
        print("Generation-",generation_size)
        print("-----------------------------")
        print("Best ---->",best)

        if best[1] == 0:
            print("We found the solution")
            print(best)
            flag = False
        else:
            flag = True

        if best[1] < all_best[1]:
            all_best = best.copy()
            
    print("-----------------------------")
    print("My answer is--->")

    print(all_best)

    return all_best[0],list(variables.keys()),generation_size







