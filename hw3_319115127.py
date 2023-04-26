from functools import reduce

print('###------ Homework 3 ------###')
print('Student: Tony Jubran 319115127')

# Question A.1
print('@----- 1.1')
def display_camel_temp(camel):
    """
     # this function will print the camel’s catalog
     name the camel's temperature in Celsius
    """
    print("Catalog name:",camel[0])
    print("Temperature:",camel[1],"C")
    return

# Question A.2
print('@----- 1.2')
def get_camel_temp_fahr(camel):
    """
    # this function will calculate temprefure of
     camel in Fahrenheit out of temprefure in celsius
    """
    fehr_tempre = camel[1] * (9 / 5) + 32
    cml_num = camel[0]
    number_of_clm = cml_num[4:]
    print("Camel number" , number_of_clm , "-" , camel[1] , "Celsius," , fehr_tempre , "Fahrenheit")
    return fehr_tempre

# Question A.3
print('@----- 1.3')
def camels_temp_fahr(camel_list):
    """
    :param camel_list:
    :return:
    """
    fehr_tempreture_list= list(map(get_camel_temp_fahr,camel_list))
    return fehr_tempreture_list


new_temps = camels_temp_fahr([['cml_1', 38.5], ['cml_2', 36.9], ['cml_3', 39.3], ['cml_4', 35.8]])

def add(a,b):
    return a + b

fehr_tempreture_sum = reduce(add ,new_temps)
print("Temperatures in Fahrenheit summed:" , fehr_tempreture_sum)

# Question B.1
print('@----- 2.1')

inserts = ["GGCTATATAGCGCGATGCTGATCGCGCGCGATGCTAGCTGCTCCGCGCGCGAAT"
    ,"TGAATAGAATTATATAGAATGACGCGCGATGAATCCGCTACGCGATAAGTCCGTAA"
    ,"ACCGCGCTATATAGCGTAAGCTGAATCGCCGCGCGTAAGCTGAATCGCTAGGGGCCGCC"
    ,"TGGTATATACGCGCGCGCCCGCGAATGCTGATCGCCTCGCGCGTAAGATGC"
    ,"CCGTGAATGCCTCGTATATACGCGCTGAATGCCTGCCGCGCGCGCGCGCGCG"]

# Question B.2
print('@----- 2.2')
def lets_find_G(str):
    return str.index("G")
G_indexes = list(map(lets_find_G,inserts))

# Question B.3
print('@----- 2.3')
def TATATA_remover(str):
    return str[str.index("TATATA")+len("TATATA"):]

trimmed_inserts = list(map(TATATA_remover,inserts))

# Question B.4
print('@----- 2.4')
def insert_to_vector(vector, insert):
    first_part = vector[:10]
    last_part = vector[10:]
    sequence = first_part.lower() + insert + last_part.lower()
    seq_len = len(sequence)
    return [sequence, seq_len]

def insert_to_vector_hellper(insert):
    return insert_to_vector(vector, insert)

# Question B.5
print('@----- 2.4')

vector = "CGTACAGCGATCGTACATGCGATCCACTCGGCTATCG"
full_vectors = list(map(insert_to_vector_hellper, inserts))


# Question C.1
print('@----- 3.1')
def seq_Tm(seq):

    A_count = seq.count("A")
    T_count = seq.count("T")
    C_count = seq.count("C")
    G_count = seq.count("G")

    if len(seq)<=13:
        return 2 * (A_count + T_count) + 4 * (C_count + G_count)
    else:
        return (64.9 + ((41 * (G_count + C_count -16.4))/(A_count +T_count +G_count + C_count )))

# Question C.2
print('@----- 3.2')
def  add_with_TACTAC(first, second):

    return first + "TACTAC" + second


def concat_strings_w_TACTAC(seq_list):

    conncted_seq = reduce(add_with_TACTAC,seq_list)

    print(conncted_seq)
    return conncted_seq

# Question C.3
print('@----- 3.3')

part_C3_sequence = [['TTTTTCCCC', 'AAAAA'],
['ATCGGG', 'GACGATCGC', 'CGATCGTGTA', 'CACGTC'],
['CATACCGTCT', 'CGTCTCTAC', 'AACCGCAT'],
['GCATCGATCG', 'AGCTC', 'CCGCTAA', 'GAGC', 'GTAGGAG']]


dna_special_list = list(map(concat_strings_w_TACTAC, part_C3_sequence))
print(dna_special_list)

"""
 i wrote the print with another line just to be sure i have the variable  that 
 iclude the special list, but i can write it all with one line too ( including the print )
print( list(map(concat_strings_w_TACTAC, part_C3_sequence)) )
 but i wont have the special list variable
 """

# Question C.4
print('@----- 3.4')
def add(a,b):
    """ return sum of a and b"""
    return a+b

def melt_temp_for_list(dna_list, sum_or_mean):
    Tm_sum = reduce(add, list(map( seq_Tm , dna_list )))
    """ first i want to calculate the sum of all Tm tempretures, so i map seq_Tm fun on all dna list
    and then add them all using add function and reduce"""
    if sum_or_mean == "sum": # if sum_or_mean equal to "sum" return the sum of the tempretures
        return Tm_sum
    return Tm_sum/len(dna_list) # if sum_or_mean is not equal to "sum" then return mean tempreture

# Question C.5
print('@----- 3.5')

dna_special_Tm_sum = melt_temp_for_list(dna_special_list, "sum")
dna_special_Tm_mean = melt_temp_for_list(dna_special_list, "mean")


# Question *Bonus

print('@----- *Bonus')

def lets_multiply(number, n, multiplication):
    if n==1:
        return multiplication * number
    return lets_multiply(int(number / 10) , n-1 , multiplication * ( number % 10 ))

def lets_add(number, n, sum):
    if n==1:
        return sum + number
    return lets_add(int(number / 10) , n-1 , sum + ( number % 10 ))


def calc_digits(number, n, operation):
    if operation == "add":
        return lets_multiply(number, n , 1)


    elif operation == "multiply":
        return lets_add(number, n, 0)

    else:
        print("calc_digits got an unknown operation")
        return


