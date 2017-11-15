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

print("")

print("                To suffering souls in Purgatory,")
print("")
print("          I do not want to waste my eternity in Limbo.")
print("             Watching the Glory of the Holy Trinity")
print("                 is infinitely more pleasurable.")
print("                   I will be praying for you.")
print("                             Abraham")
print("                       Bound to Glory inc.")
print("")
        # print(guests[0]): How to centre it as on previous line?

                    # Removing Abraham from list

print("")

cannot_come = guests.pop(0)
print("     Thank you " + cannot_come + " you know how to make everyone happy.")

print("")
print("")

guests.insert(0, "Aquinas")

for guest in guests:
    print("     Dear " + guest + ", come to see your beloved Earth once again.")
    print("     We would like to invite you on a dinner on a mt. Purgatory")
    print("     Please come to visit us in our timely limited suffering.")
    print("")
    print("")

    # Following program is a task 3-6. from Crash Course Python p. 46.

print("             I bought a much bigger dinner table.")
print("")
print("")

guests.insert(0, "Herakleitos")
guests.insert(4, "AbbÃ© Pierre")
guests.insert(9, "C.S. Lewis")
guests.append("Tolkien")

for guest in guests:
    print("     Dear " + guest + ", come to see your beloved Earth once again.")
    print("     We would like to invite you on a dinner on a mt. Purgatory")
    print("     Please come to visit us in our timely limited suffering.")
    print("")
    print("")

    # Following program is a task 3-7. from Crash Course Python p. 46.

print("     I found out that the new bigger table will not arrive on time.")
print("")
print("")

cannot_invite = guests.pop(0)
print("     I am very sorry " + cannot_invite + " but I cannot invite you.")
print("     The table I bought in Purgatory Store will not arrive on time.")
print("")
cannot_invite = guests.pop(0)
print("     I am very sorry " + cannot_invite + " but I cannot invite you.")
print("     The table I bought in Purgatory Store will not arrive on time.")
print("")
cannot_invite = guests.pop(0)
print("     I am very sorry " + cannot_invite + " but I cannot invite you.")
print("     The table I bought in Purgatory Store will not arrive on time.")
print("")
cannot_invite = guests.pop(0)
print("     I am very sorry " + cannot_invite + " but I cannot invite you.")
print("     The table I bought in Purgatory Store will not arrive on time.")
print("")
cannot_invite = guests.pop(0)
print("     I am very sorry " + cannot_invite + " but I cannot invite you.")
print("     The table I bought in Purgatory Store will not arrive on time.")
print("")
cannot_invite = guests.pop(0)
print("     I am very sorry " + cannot_invite + " but I cannot invite you.")
print("     The table I bought in Purgatory Store will not arrive on time.")
print("")
cannot_invite = guests.pop(0)
print("     I am very sorry " + cannot_invite + " but I cannot invite you.")
print("     The table I bought in Purgatory Store will not arrive on time.")
print("")
cannot_invite = guests.pop(0)
print("     I am very sorry " + cannot_invite + " but I cannot invite you.")
print("     The table I bought in Purgatory Store will not arrive on time.")
print("")
cannot_invite = guests.pop(0)
print("     I am very sorry " + cannot_invite + " but I cannot invite you.")
print("     The table I bought in Purgatory Store will not arrive on time.")
print("")

                # Author of the book probably did not expect
                            # such a long list :D
print("")

for guest in guests:
    print("     Dear " + guest + ", although my table is very small")
    print("     you are still invited. Looking forward to see you!")
    print("")


del guests[0]
del guests[0]       # Is there a way how to remove both people
                    # from a list in one line instead of two?
print(guests)
