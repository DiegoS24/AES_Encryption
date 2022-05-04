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
    # split_message = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))] # start, end, step
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
o_readout.write("\nSubstitution: \n")
for line in ciphertext:
    o_readout.write(line + '\n')
# write out is working nicely now, this works for files with multiple lines now

pad_cipher = ciphertext
for line in ciphertext:
    print(line)
# fixed infinite loop issue
while len(pad_cipher) % 16 > 0:
    pad_cipher += 'A'
pre_shift = list()
# separate the string every 16 characters
# then repeat for every four characters.
# dividing it like this should create a 3d matrix with 4 lists
# of 16 chars which are then divided every 4 chars

# for line in new_plaintext:
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
