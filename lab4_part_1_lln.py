#Lab: https://gist.github.com/jholman-bcit/8353f5f853e067510d6cd8f92f0052d2

#Part 1: LinkedListNode

#part1_lln.py
class LLN:
    def __init__(self, contents):
        self.contents = contents
        self.next = None

    def __repr__(self):
        # This isn't the greatest implementation ever, but I don't want to give too much away
        return f"LLN({str(self.contents)})"

    def addAfter(self, contents):
        # This function should made a new LLN, and it should attach that LLN after the current one
        #   ... and it should return the new one.
        # If there was already a node after the current one, don't destroy it, just bump it over!
        node = LLN(contents)
        node.next = self.next
        self.next = node
        return node

    def toList(self):
        # This function is not supposed to print!
        # It should return a list, with all the contents from the Linked List
        current = self
        lst = [current.contents]
        while current.next != None:
            current = current.next
            lst.append(current.contents)
        return lst
    
    def findLast(self):
        # This should return the LLN that is last in the LL
        current = self
        while current.next != None:
            current = current.next
        return current

    def findAfter(self, needle):
        # This should return the LLN that has the needle as its contents
        #   But only if it's at-or-later-than the current self
        #   And if there are two, return the first one, just like how `.index` does.

        if self.next == None:
            if self.contents == needle:
                return self
            else:
                raise KeyError(needle)
        elif self.next.contents == needle:
            return self.next
        else:
            return self.next.findAfter(needle)



def main():
    print("\n** init and repr **")
    first = LLN("alice")
    print("first should have a repr() (or a str()) so that it can be printed:", first)

    print("\n** addAfter **")
    second = first.addAfter("bob")
    print("now second should exist too:", second)
    print("\n** toList **")
    print("I'd like to be able to print them out in a normal list")
    print("Everything (as a list) starting from second:", second.toList())
    print("Everything (as a list) starting from first:", first.toList())
    print("Let me prove that it's a list.  What's the type?  It's:", type(first.toList()))

    print("\n** more checking of longer LinkedLists **")
    third = second.addAfter("dog")
    print("we just added 'dog' after the second node")
    print("the whole linked list (as a list):", first.toList())
    print("starting at second:", second.toList())
    print("starting at third:", third.toList())

    print("\n** findLast **")
    print("this should get the dog (which is last): ", first.findLast())

    print("\n** inserting works in the middle **")
    twopointfive = second.addAfter("cat")
    print("I added a cat after bob, it should appear before the dog:", first.toList())

    print("\n** findAfter **")
    print("I can find bob after the alice:", first.findAfter("bob"))
    print("But if I try to find alice after bob, I get an exception")
    try:
        print(second.findAfter("alice"))
    except KeyError as ke:
        print("KEY ERROR", ke)
    print("Similarly I cannot find cat AFTER cat, I get an exception")
    try:
        print(twopointfive.findAfter("cat"))
    except KeyError as ke:
        print("KEY ERROR", ke)
    print("But the dog is after the cat, that's fine:", twopointfive.findAfter("dog"))




    ### This whole main() function has this output, for me:
#     """
# ** init and repr **
# first should have a repr() (or a str()) so that it can be printed: LLN(alice)
# ** addAfter **
# now second should exist too: LLN(bob)
# ** toList **
# I'd like to be able to print them out in a normal list
# Everything (as a list) starting from second: ['bob']
# Everything (as a list) starting from first: ['alice', 'bob']
# Let me prove that it's a list.  What's the type?  It's: <class 'list'>
# ** more checking of longer LinkedLists **
# we just added 'dog' after the second node
# the whole linked list (as a list): ['alice', 'bob', 'dog']
# starting at second: ['bob', 'dog']
# starting at third: ['dog']
# ** findLast **
# this should get the dog (which is last):  LLN(dog)
# ** inserting works in the middle **
# I added a cat after bob, it should appear before the dog: ['alice', 'bob', 'cat', 'dog']
# ** findAfter **
# I can find bob after the alice: LLN(bob)
# But if I try to find alice after bob, I get an exception
# KEY ERROR 'alice'
# Similarly I cannot find cat AFTER cat, I get an exception
# KEY ERROR 'cat'
# But the dog is after the cat, that's fine: LLN(dog)
#     """


if __name__ == "__main__":
    main()