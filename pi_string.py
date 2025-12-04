filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readline()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

birtday = input("Enter your birthday, in the form mmddyy: ")
if birtday in pi_string:
    print("Your birtday appears in the first million digits of pi!")
else:
    print("Your birtday does not appear in the first million digits of pi.")