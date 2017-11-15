#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: adam kvitek
# this code is not created by me (gr4viton) i just help to refactor


"""Assignment:

Try It Yourself
The following exercises are a bit more complex than those in Chapter 2, but
they give you an opportunity to use lists in all of the ways described.
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people youÃ¢â‚¬â„¢d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
3-5. Changing Guest List: You just heard that one of your guests canÃ¢â‚¬â„¢t make the
dinner, so you need to send out a new set of invitations. YouÃ¢â‚¬â„¢ll have to think of
someone else to invite.
Ã¢â‚¬Â¢ Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who canÃ¢â‚¬â„¢t make it.
Ã¢â‚¬Â¢ Modify your list, replacing the name of the guest who canÃ¢â‚¬â„¢t make it with
the name of the new person you are inviting.
Ã¢â‚¬Â¢ Print a second set of invitation messages, one for each person who is still
in your list.
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
46     Chapter 3
Ã¢â‚¬Â¢ Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
Ã¢â‚¬Â¢ Use insert() to add one new guest to the beginning of your list.
Ã¢â‚¬Â¢ Use insert() to add one new guest to the middle of your list.
Ã¢â‚¬Â¢ Use append() to add one new guest to the end of your list.
Ã¢â‚¬Â¢ Print a new set of invitation messages, one for each person in your list.
3-7. Shrinking Guest List: You just found out that your new dinner table wonÃ¢â‚¬â„¢t
arrive in time for the dinner, and you have space for only two guests.
Ã¢â‚¬Â¢ Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
Ã¢â‚¬Â¢ Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know youÃ¢â‚¬â„¢re sorry you canÃ¢â‚¬â„¢t invite
them to dinner.
Ã¢â‚¬Â¢ Print a message to each of the two people still on your list, letting them
know theyÃ¢â‚¬â„¢re still invited.
Ã¢â‚¬Â¢ Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
"""

"""This is a program from a book "Crash Course Python" page 46."""

print("")
                # CODE NAME: PRINT A S**T LOUD OF IT
            # Following program is a task 3-4. "Guest List"

guests = ["Abraham", "Isaac", "Isaiah", "Oozes", "Socrates", "Plato", "Aristotle"]

for guest in guests:
    print("     Dear " + guest + ", come to see your beloved Earth once again.")
    print("     We would like to invite you on a dinner on a mt. Purgatory")
    print("     Please come to visit us in our timely limited suffering.")
    print("")

    # Following program is a task 3-5. from Crash Course Python p. 46.

# you can try to go through the Python language course
# in android app called "Learn Python" it's a good course for free

# this is how to print multiline
print("""
                To suffering souls in Purgatory,

          I do not want to waste my eternity in Limbo.
             Watching the Glory of the Holy Trinity
                 is infinitely more pleasurable.
                   I will be praying for you.
                             Abraham
                       Bound to Glory inc.

""")
        # print(guests[0]): How to centre it as on previous line?
txt = guests[0]
width = 80  # fill in your number

# everything is an object - even str
print(txt.center(width))

# you can try print(dir(txt)) to find out what are the functions which can be called on str object

                    # Removing Abraham from list

print()

cannot_come = guests.pop(0)
# print("     Thank you " + cannot_come + " you know how to make everyone happy.")
print("     Thank you {who} you know how to make everyone happy.".format(
    who=cannot_come
))
# str.format() is much better than simple string concatenation

print()

guests.insert(0, "Aquinas")

# also use functions - if you know you gonna print it multiple times create function:
def print_welcome(guest):
    print("""
     Dear {guest}, come to see your beloved Earth once again.
     We would like to invite you on a dinner on a mt. Purgatory
     Please come to visit us in our timely limited suffering.

""".format(guets=guets))

for guest in guests:
    print_welcome(guest)

    # Following program is a task 3-6. from Crash Course Python p. 46.

print("""             I bought a much bigger dinner table.

""")

guests.insert(0, "Herakleitos")
guests.insert(4, "AbbÃ© Pierre")
guests.insert(9, "C.S. Lewis")
guests.append("Tolkien")

for guest in guests:
    print_welcome(guest)

    # Following program is a task 3-7. from Crash Course Python p. 46.

print("""     I found out that the new bigger table will not arrive on time.

""")

def drop_guest(index):

    cannot_invite = guests.pop(index)

    print("""     I am very sorry {nam} but I cannot invite you.
     The table I bought in Purgatory Store will not arrive on time.
""".format(nam=cannot_invite))

# did not read the assignment - you probably want to empty the list one by one?
# `_` can be used when you do not need the value
# - i am not printing `i` variable in the following for loop, so why would i assign it a name
number_to_remove = len(guests) - 2
for _ in range(number_to_remove):
    drop_guest(0)

                # Author of the book probably did not expect
                            # such a long list :D
print("")

for guest in guests:
    print("""     Dear {guest}, although my table is very small
     you are still invited. Looking forward to see you!
""".format(guest=guest))

for _ in range(2):
    del guests[0]

# Is there a way how to remove both people
# from a list in one line instead of two?
# - there is - for loop
print(guests)
