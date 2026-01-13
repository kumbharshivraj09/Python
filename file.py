with open('user_info.txt','w') as  file:
    file.write("this is my first text using python\n")


with open('user_info.txt','a') as file:
    file.write("this is second text\n")
    file.write("this is third text\n")
    file.write("sham\n")
    file.write("sujal\n")
    file.write("shubham\n")
    file.write("ram\n")


with open ('user_info.txt','r') as file:
    content=file.readlines()
print(content)

for line in content:
    print(f'wellcome {line.rstrip()}')
