import numpy as np
from random import shuffle
from Queen import *

def getDiagnoal(Queen):

    board = Queen.board
    for position in Queen.x_and_y_location:

        x = position[0]
        y = position[1]
        more_conflict_ignore = False

        while x <8 or y <8:
            x += 1
            y += 1
            if x < 8:
                if y < 8:
                    if board[y][x] == 1 and not more_conflict_ignore:
                        if board[y][x] == 1:
                            Queen.conflict += 1
                            more_conflict_ignore = True

        x = position[0]
        y = position[1]

        while (x < 8 or y > 0) and not more_conflict_ignore :
            x+= 1
            y -= 1
            if (x < 8):
                if (y >= 0):
                    if (board[y][x] == 1 and not more_conflict_ignore):
                        more_conflict_ignore = True
                        Queen.conflict += 1

        x = position[0]
        y = position[1]

        while (x >=0 or y >=0):
            x-= 1
            y-= 1
            if (x>=0):
                if (y>=0):
                    if (board[y][x] == 1 and not more_conflict_ignore):
                        Queen.conflict += 1
                        more_conflict_ignore = True

        x = position[0]
        y = position[1]

        while ((x >=0 or y <7)  and not more_conflict_ignore):
            x-= 1
            y+= 1
            if (x>=0):
                if (y<=7):
                    if (board[y][x] == 1 and not more_conflict_ignore):
                        Queen.conflict += 1
                        more_conflict_ignore = True

        x=0
        more_than_one= 0
        while (x < len(board[position[1]]) and not more_conflict_ignore):
            if board[position[1]][x]==1:
                more_than_one += 1
            if more_than_one==2:
                more_conflict_ignore = True
                Queen.conflict += 1
            x+= 1

        x=0
        more_than_one= 0
        while (x < len(board[:,position[1]]) and not more_conflict_ignore):
            if board[x][position[1]]==1:
                more_than_one += 1
            if more_than_one==2:
                more_conflict_ignore = True
                Queen.conflict += 1
            x += 1

    Queen.fitness =  (8- Queen.conflict)*3.5

def crossover(select_chromo,mutate,num_of_itr):

    new = sorted(Queen.Queen_objects, key=lambda q: q.fitness, reverse=True)
    new_select_best = new[0:int(select_chromo)]

    if num_of_itr=='-1':
        num_of_itr= '99999999999999999999999999999999999999999999999999999'

    for itr in range (0,int(num_of_itr)):

        for queen in range(len(new_select_best)-1):
            rand = np.random.randint(1, 8)
            best_fit_1 = new_select_best[queen].chromosome
            best_fit_2 = new_select_best[queen+1].chromosome
            child1 = best_fit_1[0:rand]+best_fit_2[rand:]
            child2 = best_fit_2[0:rand] + best_fit_1[rand:]
            complete = mutation(child1, int(mutate))
            if complete.fitness ==28: return complete , itr+1
            complete =mutation(child2, int(mutate))
            if complete.fitness ==28: return complete, itr+1


        mergeChild()
        shuffle(Queen.Queen_objects)
        new = sorted(Queen.Queen_objects, key=lambda q: q.fitness, reverse=True)
        new_select_best = new[0:int(select_chromo)]

    return (new_select_best[0], num_of_itr)

def two_crossover(select_chromo,mutate,num_of_itr):

    new = sorted(Queen.Queen_objects, key=lambda q: q.fitness, reverse=True)
    new_select_best = new[0:int(select_chromo)]

    if num_of_itr=='-1':
        num_of_itr= 999999999999999999999999999999999999999999999

    for itr in range (0,int(num_of_itr)):

        for queen in range(len(new_select_best)-1):
            randstart = np.random.randint(1, 8)
            randend = np.random.randint(randstart, 8)
            best_fit_1 = new_select_best[queen].chromosome
            best_fit_2 = new_select_best[queen+1].chromosome
            child1 = best_fit_1[:randstart] + best_fit_2[randstart:randend] + best_fit_1[randend:]
            child2 = best_fit_2[:randstart] + best_fit_1[randstart:randend] + best_fit_2[randend:]
            complete = mutation(child1, int(mutate))
            if complete.fitness ==28: return (complete , itr+1)
            complete =mutation(child2, int(mutate))
            if complete.fitness ==28: return (complete, itr+1)

        mergeChild()
        shuffle(Queen.Queen_objects)
        new = sorted(Queen.Queen_objects, key=lambda q: q.fitness, reverse=True)
        new_select_best = new[0:int(select_chromo)]

    return (new_select_best[0], num_of_itr)

def cut_and_splice(select_chromo,mutate,num_of_itr):
    new = sorted(Queen.Queen_objects, key=lambda q: q.fitness, reverse=True)
    new_select_best = new[0:int(select_chromo)]

    if num_of_itr == '-1':
        num_of_itr = 999999999999999999999999999999999999999999999

    for itr in range(0, int(num_of_itr)):

        for queen in range(len(new_select_best) - 1):
            rand_1 = np.random.randint(1, 8)
            rand_2 = np.random.randint(1, 8)
            best_fit_1 = new_select_best[queen].chromosome
            best_fit_2 = new_select_best[queen + 1].chromosome
            child1 = best_fit_1[0:rand_1] + best_fit_2[rand_1:]
            child2 = best_fit_2[0:rand_2] + best_fit_1[rand_2:]
            complete = mutation(child1, int(mutate))
            if complete.fitness == 28: return complete, itr + 1
            complete = mutation(child2, int(mutate))
            if complete.fitness == 28: return complete, itr + 1

        mergeChild()
        shuffle(Queen.Queen_objects)
        new = sorted(Queen.Queen_objects, key=lambda q: q.fitness, reverse=True)
        new_select_best = new[0:int(select_chromo)]

    return (new_select_best[0], num_of_itr)

def uniform_crossover(select_chromo,mutate,num_of_itr):
    new = sorted(Queen.Queen_objects, key=lambda q: q.fitness, reverse=True)
    new_select_best = new[0:int(select_chromo)]

    if num_of_itr == '-1':
        num_of_itr = 9999999999999999999999999999999999999999999999

    for itr in range(0, int(num_of_itr)):

        for queen in range(len(new_select_best) - 1):

            best_fit_1 = new_select_best[queen].chromosome
            best_fit_2 = new_select_best[queen + 1].chromosome
            child1 = [0] * 8
            child2 = [0] * 8
            for index in range(8):
                rand = np.random.uniform(0, 1)
                if rand > 0.7:
                    child1[index] = best_fit_2[index]
                    child2[index] = best_fit_1[index]
                else:
                    child1[index] = best_fit_1[index]
                    child2[index] = best_fit_2[index]
            complete = mutation(child1, int(mutate))
            if complete.fitness == 28: return complete, itr + 1
            complete = mutation(child2, int(mutate))
            if complete.fitness == 28: return complete, itr + 1

        mergeChild()
        shuffle(Queen.Queen_objects)
        new = sorted(Queen.Queen_objects, key=lambda q: q.fitness, reverse=True)
        new_select_best = new[0:int(select_chromo)]

    return (new_select_best[0], num_of_itr)

def mutation(chromosome, number_of_mutation):

    for v in range(number_of_mutation):
        location = np.random.randint(0, 8)
        mutate = np.random.randint(0, 8)

        chromosome[location]= mutate

    new_queen = Queen()
    new_queen.setBoard(chromosome)
    getDiagnoal(new_queen)
    if (new_queen.fitness > 7.5):
        Queen.Queen_child_temp.append(new_queen)
    return new_queen


def population_generator(size):

    Queen.Queen_objects=[]
    Queen.Queen_child_temp = []
    for x in range(size):
        pop = Queen()
        for y in range(8):
            rand = np.random.randint(0, 8)
            #Put Queen in place
            pop.board[rand][y]=1
            pop.x_and_y_location.append([])
            pop.x_and_y_location[y].append(y)
            pop.x_and_y_location[y].append(rand)
            pop.chromosome.append(rand)

        getDiagnoal(pop)
        Queen.Queen_objects.append(pop)
        Queen.only_pop.append(pop)

def question1():
    print("Eight Queen Gene Algorithm\n\nPlease enter the following information:\n\t1. Population Size\n"
          "\t2. Number of Chromosomes for each iteration\n"
          "\t3. Mutation Rate\n"
          "\t4. Number of Iteration to run (-1 for unlimited trials)\n"
          "Enter E to exit")

    answer = input("Enter information with space separator\n")
    answer = answer.split(" ")

    if len(answer)==1:
        if answer[0]=='E' or answer[0]=='e':
            print ("Program Exit")
            exit(0)
        else:
            print("Missing values\nPlease enter 4 values with space separator")
            return None
    elif len(answer)==4:
        if (answer[0]=='0' or answer[0]=='1'):
            print ('Population has to be 2 or larger.')
            return None
        elif (answer[1]=='0'):
            print ('Iteration has to be 1 or larger.')
            return None
        return answer
    else:
        print ("Missing values\nPlease enter 4 values with space separator")
        return None

def question2():

    print("Choose method:\n"
          "1. Single Point Crossover\n"
          "2. Two Point Crossover\n"
          "3. Cut and Splice\n"
          "4. Uniform Crossover")

    user = input("Select Option:")
    user = int(user)

    if user >4 or user <1:
        print ("Please choose between 1-4")
        return None
    else:
        return user

def mergeChild():

    Queen.Queen_objects = Queen.Queen_objects + Queen.Queen_child_temp
    Queen.Queen_child_temp = []

def main():


    population = 250
    select_chromo = 20
    mutate = 3
    num_of_itr = '-1'

    choice =1

    while True:


        if choice ==1:
            userinformation_one = None
            while userinformation_one==None:
                userinformation_one = question1()
            population = userinformation_one[0]
            select_chromo = userinformation_one[1]
            mutate = userinformation_one[2]
            num_of_itr = userinformation_one[3]
            population_generator(int(population))

        else:
            Queen.Queen_child_temp=[]
            Queen.Queen_objects = []
            Queen.Queen_objects = Queen.only_pop.copy()


        userinformation_two = None
        while userinformation_two==None:
            userinformation_two = question2()

        if userinformation_two ==1:
            result = crossover(select_chromo,mutate,num_of_itr)
        elif (userinformation_two ==2):
            result = two_crossover(select_chromo,mutate,num_of_itr)
        elif (userinformation_two == 3):
            result = cut_and_splice(select_chromo,mutate,num_of_itr)
        elif (userinformation_two == 4):
            result =uniform_crossover(select_chromo,mutate,num_of_itr)

        print ("(<Population:{}>, <Chromosomes per iteration:{}>, <Mutate:{}>, <Iteration:{}>)".format(
            population,select_chromo,mutate,'Unlimited' if num_of_itr=='-1' else num_of_itr
        ))
        print ("Number of iterations: {}".format(result[1]))

        print ("Final state reached {}".format([x+1 for x in result[0].chromosome]))
        print ("Board:")
        print (np.flip(result[0].board,0))
        print ("Final state fitness {}".format(result[0].fitness))

        same_values = 0
        while (same_values < 1 or same_values >3):
            same_values = input ("Use same initial values:\n1.Yes\n"
                                 "2.No\n"
                                 "3.Exit\n"
                                 "Choice: ")
            same_values =int(same_values)


        if same_values == 1:
            choice = 0
        elif (same_values== 2):
            choice =1
        elif( same_values== 3):
            exit(0)

main()