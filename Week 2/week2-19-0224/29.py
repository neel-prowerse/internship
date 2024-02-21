# Opening Files : 
open('example.txt','r') #read mode (DEFAULT)
open('example.txt','w') #write mode, if the file already exists erase its whole data then insert data, create a new file if the file does not exist then insert data.
# open('example.txt','x') #exclusive creation mode, this method fails, if the file already exists.
open('example.txt','a') #append mode, inserts data at the end of the file without erasing the previous data of the file and creates a new file does not exist.
# open('example.txt','t') #text mode (DEFAULT)
# open('example.txt','b') #binary mode

# Writing to Files :
with open('example1.txt','w') as f:
    f.write('Hello World!\n')
    f.write('HI!\tTHIS IS EXAMPLE TEXT FILE...')

# Reading Files : 
f = open('example1.txt','r')
file_data = f.read()
print(file_data) 
# Closing Files : 
f.close()

# Append Mode : 
f = open('example1.txt','a')
f.write('\nMy Name is NEEL\n')
f.close()
print('\n------------ALL THE FUNCTION IN FILE HANDLING-------------')
# IMPLEMENTING ALL THE FUNCTIONS IN FILE HANDLING : 
import os 

# method for file creation
def file_creation(file_name):
    try:
        with open(file_name,'w') as file:
            file.write("HI!!! WELCOME...")
        print(f"\n{file_name} CREATED SUCCESSFULLY...")
    except IOError:
        print(f'E\nRROR! {file_name} CREATION FAILED...')

# method for reading data from the file 
def file_reading(file_name):
    try:
        with open(file_name,'r') as file:
            file_content = file.read()
            print(file_content)
    except IOError:
        print(f"\nERROR! {file_name} NOT FOUND...")

# method for appending data into the file
def data_appending(file_name,data):
    try:
        with open(file_name,"a") as file:
            file.write(data)
        print(f"\nDATA APPENDED SUCCESSFULLY... IN {file_name}")
    except IOError:
        print("\nERROR! OCCURED WHILE APPENDING THE FILE...")

# method for renaming file 
def file_renaming(file_name,new_name):
    try:
        os.rename(file_name,new_name)
        print('\nFILE RENAMING SUCCESSFULLY !')
    except IOError:
        print('\nERROR OCCURED WHILE RENAMING THE FILE !')

# method for deletion of file 
def file_deletion(file_name):
    try:
        os.remove(file_name)
        print('\nFILE DELETED SUCCESSFULLY...')
    except IOError:
        print('\nERROR! OCCURED WHILE DELETING THE FILE...')
if __name__ == '__main__':
    file_name = 'example1.txt'
    new_name = 'example2.txt'
    file_creation(file_name)
    file_reading(file_name)
    data_appending(file_name,"\nThis is an additional line.")
    file_reading(file_name)
    file_renaming(file_name,new_name)
    file_reading(new_name)
    file_deletion(new_name)