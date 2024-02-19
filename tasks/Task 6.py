# importing modules
import threading, os, random
 
# path of the current script
path = 'D:/p09s3107 docs/alibaba_bot/'
 
# Before creating
dir_list = os.listdir(path)
print("List of directories and files before creation:")
print(dir_list)
print()
 
randomize = random.randint(100,1000)
# Creates a new file
def generation_numbers(filename='input.txt'):
    with open(filename, encoding='utf8', mode='w+') as fp:
        for i in range(randomize):
            fp.write(str(random.randint(100,1000)))
            fp.write('\n')

def rewritetr():
    pass

generation_numbers()
 
# After creating
dir_list = os.listdir(path)
print("List of directories and files after creation:")
print(dir_list)