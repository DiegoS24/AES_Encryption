# written by Diego Suarez dys0022
# class: CSCE 3550 Section 001
# date due: May 5, 2022
# description: This is an AES implementation that will read out to a file
#              the cycles made throughout the AES process.
# if asked again in an interview about a time you thought outside the box for a project.
# maybe we could mention how you implemented a regex when reading in file input instead of stripping specific characters

# plaintext_file = input("Enter the name of the plaintext input file: ")
# key_file = input("Enter the name of the input key file: ")
# output_file = input("Enter the name of the output ciphertext file: ")

# p_readin = open(plaintext_file, 'r')
# k_readin = open(key_file, 'r')
# o_readout = open(output_file, 'w')

# this is temporary, will need to delete

print("Enter the name of the plaintext input file: input1.txt")
print("Enter the name of the key input file: key1.txt")
print("Enter the name of the output ciphertext file: output1.txt")

p_readin = open('input1.txt', 'r')
k_readin = open('key1.txt', 'r')
o_readout = open('output1.txt', 'w')


plaintext = p_readin.readlines()
key: str = k_readin.readline()

new_plaintext: list[str] = list()

p_readin.close()
k_readin.close()

print("Preprocessing:")
o_readout.write("Preprocessing\n")
for line in plaintext:
    newline = line.replace(" ", "")
    newline = newline.replace(".", "")
    newline = newline.replace(",", "")
    newline = newline.replace("!", "")
    newline = newline.replace("?", "")
    newline = newline.replace("\n", "")
    newline = newline.replace("\t", "")
    new_plaintext.append(newline)
    o_readout.write(newline + '\n')
    print(newline)
# the for loop above 'wastes' time, a regex would be better. optimize this later. gotta brush up on regexs
print(key + '\n')

temp_list = list()

# the code below up until line 77 is the substitution
start = ord('A')
for line in new_plaintext:
    # need to split the message to the length of the key
    i = 0
    split_message = [line[i:i + 16] for i in range(0, 80, 16)]
    temp = list()
    for each_split in split_message:
        for letter, k in zip(each_split, key):
            shift = ord(k) - start
            pos = start + (ord(letter) - start + shift) % 26
            temp.append(chr(pos))
    temp_list.append(temp)

ciphertext = list()

for line in temp_list:
    ciph_temp = ''.join(line)
    ciphertext.append(ciph_temp)

print("Substitution: ")
for line in ciphertext:
    print(line)

o_readout.write("\nSubstitution: \n")
for line in ciphertext:
    o_readout.write(line + '\n')
# write out is working nicely now, this works for files with multiple lines now

# now we have to fix the padding and make sure it writes it out correctly
# make a deep copy for pad_cipher, otherwise you're only making it into a pointer kind of
pad_cipher = list()

for line in ciphertext:
    pad_cipher.append(line)

# this for loop is responsible for the padding added to any string to make it %16 = 0

print("\nInput:")
o_readout.write("\nInput:\n")
for line in ciphertext:
    o_readout.write(line + '\n')
    print(line)

for line_number in range(0, len(pad_cipher)):
    while len(pad_cipher[line_number]) % 16 > 0:
        pad_cipher[line_number] += 'A'

print("\nOutput:")
o_readout.write("\nOutput:\n")
for line in pad_cipher:
    o_readout.write(line + '\n')
    print(line)
# the section below will be part D where we shift rows
# separate the string every 16 characters   CHECK
# then repeat for every four characters.
# dividing it like this should create a 3d matrix with 4 lists
# of 16 chars which are then divided every 4 chars
pre_shift_matrix = list()
print('\n')
for line in pad_cipher:
    i = 0
    line_list = list()
    split_message = [line[i:i + 16] for i in range(0, len(line), 16)]
    for each_split in split_message:
        sub_split = [each_split[i:i + 4] for i in range(0, len(each_split), 4)]
        line_list.append(sub_split)
        # we are getting the correct outcome: we have partitioned every 4 characters, now add these to lists of lists
        # for easier iteration and shift
    pre_shift_matrix.append(line_list)

print(pre_shift_matrix)
# shift matrix is what we will use to do the actual shifting in the rows, we are going to have to use len() and range() to iterate through

shifted_matrix = list()

for line in pre_shift_matrix:
    line_list = list()
    for section_number in range(0,len(line)):
        section_list = list()
        # print(line[section_number][0])
        if section_number == 0:
            for char in range(0, len(line[section_number])):
                section_list.append(line[char][section_number])
            line_list.append(section_list)
        if section_number == 1:
            for char in range(0, len(line[section_number])):
                temp = line[char][section_number][1:] + line[char][section_number][0]
                section_list.append(temp)
            line_list.append(section_list)

        elif section_number == 2:
            for char in range(0, len(line[section_number])):
                temp = line[char][section_number][2:] + line[char][section_number][:2]
                section_list.append(temp)
            line_list.append(section_list)

        elif section_number == 3:
            for char in range(0, len(line[section_number])):
                temp = line[char][section_number][3:] + line[char][section_number][:3]
                section_list.append(temp)
            line_list.append(section_list)
        shifted_matrix.append(line_list)

pre_shift_matrix.clear()
# we need to clear lists we dont need anymore because i am making a lot of lists which is very resource intensive
# so once we are done with a list, lets delete it because we no longer need it
# I now need to write this new shifted list out to the o_readout file

print(shifted_matrix)

            # here we are in the char int of the section object in the line object of the shift matrix



#     i = 0
#     split_message = [line[i:i + 16] for i in range(0, 80, 16)]
#     for each_split in split_message:
#         for letter, k in zip(each_split, key):
#             shift = ord(k) - start
#             pos = start + (ord(letter) - start + shift) % 26
#             temp.append(chr(pos))

o_readout.close()
p_readin.close()
k_readin.close()
