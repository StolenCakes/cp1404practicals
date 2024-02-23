"""
CP1404/CP5632 - Practical
Program on menus

Use this pattern to create a very simple menu-driven program according to the pseudocode below:

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message

Sample output for this program should look like:

Enter name: Guido
(H)ello
(G)oodbye
(Q)uit
>>> A
Invalid choice
(H)ello
(G)oodbye
(Q)uit
>>> H
Hello Guido
(H)ello
(G)oodbye
(Q)uit
>>> G
Goodbye Guido
(H)ello
(G)oodbye
(Q)uit
>>> Q
Finished.
"""

MENU = """(H)ello
(G)oodbye
(Q)uit"""

user_name = input("Enter name : ")

print(MENU)

choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {user_name}")
    elif choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
