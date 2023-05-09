print('###------ Homework 4 ------###')
print('Student: Tony Jubran 319115127')



import math
######### Question 1

print('@----- 1.a')

def Fibonacci(n):
    febo_list=[0,1]                                                           # first 2 indexes of Fibonacci
    for i in range (n-2):
        next_febo = febo_list[-1]+febo_list[-2]                               # finding the next febonacci number
        febo_list.append(next_febo)                                           # adding the next febonacci number to the list
    print(f'Sum of first {n} numbers in Fibonacci series: {sum(febo_list)}')
    return febo_list

print('@----- 1.b')


def hamming_dist(str1, str2):
    hamming= None
    if len(str1) != len(str2):                                                # if the stings have diffrent size return none.
        return hamming
    else:
        hamming =0
        for i in range(len(str2)):
            if str1[i] != str2[i]:                                            # cheking if each index in the strings is not the same to add one.
                hamming += 1

    return hamming

print('@----- 1.c')

def str_overlap(my_string,n):
    if len(my_string) < n:                                                    # if the stingsshorter than n return none.
        return None
    else:
        new_str=[]
        for i in range(len(my_string)-n+1):
            new_str.append(my_string[i:i+n])
    return new_str


######### Question 2

print('@----- 2.a')

def get_string_GC_content(str):
    c_num = str.count('C')
    g_num = str.count('G')
    return (c_num + g_num)/len(str) * 100                                     # finding GC percent out of all the string

print('@----- 2.b')

def get_list_GC_content(list_GC):
    return list(map(get_string_GC_content,list_GC))                           # maping the function for all the list


print('@----- 2.c')

def get_GC_content(strOrList):
    if type(strOrList) == list:                                                # checking if list or just one index to use the appropriate function
        return get_list_GC_content(strOrList)
    else:
        return get_string_GC_content(strOrList)


print('@----- 2.d')
def list_GC_content_max(seq_list):
    max_CG=-1
    length_list = get_GC_content(seq_list)                                     # finding all CG percent of all sentences in the lis
    for i in range(len(length_list)):
        if length_list[i] > max_CG:                                            # if CG percent is larger than prevuse CG biggest percent change them to keep with largest CG percent
            max_CG = length_list[i]
            wanted_index = i

    return [seq_list[wanted_index] , length_list[wanted_index]]                # returning Max CG percent and its sequence


print('@----- 2.e')

def list_GC_content_average_std(DNA_list):
    DNA_CG_con = get_list_GC_content(DNA_list)
    avirage = 0
    for temp in DNA_CG_con:
        avirage = avirage + temp
    avirage = avirage / len(DNA_CG_con)                      # calculating the avirage
    squareOfDiff =0
    for temp in DNA_CG_con:                                  # calculating STD
        squareOfDiff = squareOfDiff + (temp - avirage)**2
    std = math.sqrt(squareOfDiff/(len(DNA_CG_con)-1))
    return [avirage, std]

######### Question 3

print('@----- 3')

def find_var_mutations(ref_seq,query_seq):
    mutation_list= []
    for i in range(len(ref_seq)):
        if ref_seq[i] == query_seq[i]:                      # if both refrence sequance and query sequence are the same then not an mutation, check next index
          continue
        else:                                               # declearation a new mutation in the sequence/
            mutation_list.append([i+1,query_seq[i]])

    return mutation_list                                      



######### Question Bonus

print('@----- Bonus')

index = 0
def find_first_x(protien_seq):
    if len(protien_seq) == 0:             # this mean that we cave been throw all the sequence but didnt find X
        return -1
    if protien_seq[0] == "X" :            # here we finaly found X, so we return 0, its current position
        return 0
    index = find_first_x(protien_seq[1:]) # X is not at the current position, so check next position

    if index == -1:
        return -1                         # if X not found

    return index + 1                      # when we found X all what i will be doing is returning index + 1 for all the times i checked the next position