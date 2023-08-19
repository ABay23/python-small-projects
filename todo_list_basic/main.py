# print("Enter a todo:")
# text_inp = input()
# print(f'You have a new to do: {text_inp}!')

# u_prompt = "Enter a To Do "

# tod1 = input(u_prompt)
# tod2 = input(u_prompt)
# tod3 = input(u_prompt)

# tods = [todo1, todo2, todo3]

# print(tods)

# print(type(tods))

# Create a program that can get a title of a book and return the length of the title.
# intro = "Enter the title of your book: "
# book = str(input(intro))

# len = (len(book))
# print(f"The lenght of the title with spaces is {len}.")

# List with a loop
# user_prompt = "Enter a todo: "
# todx= []

# while True:
#     todx = input(user_prompt)
#     todxs.append(todx)
#     print(todxs)

# tod = []

while True:
    user_input = input("Enter add, show, edit or exit ")
    user_input = user_input.lower().strip()
    match user_input:
        case 'add':
            todx = input("Enter a todo: ") + "\n"

            file = open('todo.txt', 'r')
            tod = file.readlines()
            file.close()

            tod.append(todx)
            file = open('todo.txt', 'w')
            file.writelines(tod)
            file.close()

        case 'show':
            file = open('todo.txt', 'r')
            tod = file.readlines()
            file.close()

            for index, item in enumerate(tod):
                print(f"{index +1} - {item}")
        case 'edit':
            read = open('todo.txt', 'r')
            tod = read.readlines()

            print("Enter the number you want to edit from the list\n")
            for item in tod:
                print(f"Number:{int(tod.index(item))+1} - {item}\n")

            ed = int(input("Enter the number to edit, Number? \n")) - 1
            msg = str(input("Updated to do: ") + "\n")
            tod[ed] = msg

            file = open('todo.txt', 'w')
            file.writelines(tod)
            file.close()

        case 'exit':
            break
