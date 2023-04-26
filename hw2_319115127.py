print('###------ Homework 2 ------###')
print('Student: Tony Jubran 319115127')

######### Question 1

spike30 = "MFVFLVLLPLVSSQCVNLTTRTQLPPAYTN"

print('@----- 1.1')
spike30_length = len(spike30)
print(spike30_length)

print('@----- 1.2')
print(spike30[spike30_length-2])

print('@----- 1.3')
print(spike30[-2])

print('@----- 1.4')
print(spike30[:8:2])

print('@----- 1.5')
spike = spike30+ 'SFTRGVYYPDKVFRSS'
print(spike[::-1])

print('@----- 1.6')
print(len(spike)-len(spike30))

######### Question 2

rna_seq = 'GGACUCGAUGUUCCCAUUAGUACCCAAGG'
print('@----- 2.1')
repsOfU = rna_seq.count('U')
print(repsOfU)

print('@----- 2.2')
allNucleotides=len(rna_seq)
print(100*(repsOfU/allNucleotides))

print('@----- 2.3')
first_AUG = rna_seq.find("AUG")
print(first_AUG)

print('@----- 2.4')
first_UAG = rna_seq.find("UAG")
translated_region = rna_seq[first_AUG+3:first_UAG]
print(translated_region)

print('@----- 2.5')
first_second_CCCA = rna_seq.find("CCCA",first_UAG)
print(first_second_CCCA-first_UAG-3) # the +3 presents the length of UAG

print('@----- 2.6')
rna_seq_new = rna_seq[:first_second_CCCA] + rna_seq[first_second_CCCA+4:]
print(rna_seq_new)

######### Question 3
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print('@----- 3.1')
print(fibonacci[-1] + fibonacci[-2])

print('@----- 3.2')
evenNumbers1To30 = list(range(2,30,2))
print(evenNumbers1To30)

print('@----- 3.3')
myNewList = evenNumbers1To30 + fibonacci
print(myNewList)
print(myNewList[2] * myNewList[19] )

print('@----- 3.4')
# listFor3_4 = myNewList[:5] + myNewList[-5:] + 'python_2021'

print('@----- 3.5')
my_list = [1, 12, 2, 10, 3, 8, 4, 6, 5, 4]
goingUp = my_list[::2]
goingDown = my_list[1::2]
print(goingUp)
print(goingDown)

######### Question 4


print('@----- 4.1')
mutated_seq = "AAAAGGGGGTATAGTCCTTCCCCCAAAAAGGGGGGAAAATTGTATAGTT"
print(mutated_seq.count("GTATAG"))

print('@----- 4.2')
unmutated_seq = mutated_seq.replace("GTATAG", "CCACCG")
print(unmutated_seq)

print('@----- 4.3')
firstT = unmutated_seq.find('T')
secondT = unmutated_seq.find('T',firstT+1)
print(secondT)

print('@----- 4.4 *Bonus')
first_CCACCG = unmutated_seq.find('CCACCG')
second_CCACCG = unmutated_seq.find('CCACCG',first_CCACCG + 1)
nonmutatedAsnumber = unmutated_seq.count("A")
middleOfNonmutated = unmutated_seq[first_CCACCG+6:second_CCACCG]
middleNonmutatedAsnumber = middleOfNonmutated.count("A")
print(100 * (middleNonmutatedAsnumber / nonmutatedAsnumber),"%")


