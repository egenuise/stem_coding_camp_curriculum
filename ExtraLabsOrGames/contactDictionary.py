'''
Lab 5: Phone Contacts
Felecia Hildebran and Zachary Messenger
fah36 and zam48
10/5/17
Section 3
'''

# Creates initially blank dictionary for contacts to be added to
contacts = {}


def create_contact(contacts, first, last, email, age, phone):
    '''Contact Creation Function'''
    # Will create an immutable key using first and last name
    tup = (first, last)
    # Formats the information to add to dictionary
    val = {"Email": email,
           "Age": age,
           "Phone": phone}
    # Adds the information to the dictionary
    contacts[tup] = val


def update_contact_number(contacts, first, last, phone):
    '''Update Contact Phone'''
    # Sets name into tuple to for access key
    tup = (first, last)
    # Actually updates the phone number
    contacts[tup]["Phone"] = phone


def update_contact_email(contacts, first, last, email):
    '''Update Contact Email'''
    # Tuple access key
    tup = (first, last)
    # Updates Email
    contacts[tup]["Email"] = email


def update_contact_age(contacts, first, last, age):
    '''Update Contact Age'''
    # Tuple Access Key
    tup = (first, last)
    # Updates with new age
    contacts[tup]["Age"] = age


def get_contact_number(contacts, first, last):
    '''Get Contact Number'''
    # Tuple access key
    tup = (first, last)
    # Returns the phone number for printing
    return (contacts[tup]["Phone"])


def get_contact_email(contacts, first, last):
    '''Get Contact Email'''
    # Tuple access key
    tup = (first, last)
    # Returns email address for print
    return (contacts[tup]["Email"])


def get_contact_age(contacts, first, last):
    '''Get Contact Age'''
    # Tuple access key
    tup = (first, last)
    # Returns age for printing
    return (contacts[tup]["Age"])


def contains_contact(contacts, first, last):
    '''Contains contacts function'''
    # Tuple access key
    tup = (first, last)
    # Conditional statements check for the contact
    if tup in contacts:
        return True
    else:
        return False


def display(contacts, first, last):
    '''Displays function'''
    # Tuple access key
    tup = (first, last)
    # Checks if function is in contacts then prints it
    if tup in contacts:
        print(first + " " + last)
        print("Email: " + contacts[tup]["Email"])
        print("Phone: " + contacts[tup]["Phone"])
        print("Age: " + str(contacts[tup]["Age"]))
    # If function not in contacts it tells the user this
    else:
        print("Contact for " + first + " " + last + " does not exist.")


def main():
    '''Main function that initiates everything'''
    # Three creation functions here
    create_contact(contacts, "Katie", "Katz", "katie.katz@nau.edu",
                   25, "857-294-2758")
    create_contact(contacts, "Jim", "Jones", "jim.jones@nau.edu",
                   19, "525-866-2749")
    create_contact(contacts, "Sarah", "Sanders", "sarah.sanders@nau.edu",
                   18, "593-026-2532")
    # Displays if the contact was created successfully
    print("Creation of Jim Jones: {}".format(
        "Passed" if contains_contact(contacts, "Jim", "Jones")
        else "Failed"))
    print("Creation of Katie Katz: {}".format(
        "Passed" if contains_contact(contacts, "Katie", "Katz")
        else "Failed"))
    print("Creation of Sarah Sanders: {}".format(
        "Passed" if contains_contact(contacts, "Sarah", "Sanders")
        else "Failed"))
    # Updates a piece of information in each of the three contacts
    update_contact_age(contacts, "Sarah", "Sanders", 19)
    print("Updating Sarah Sanders age to 19: {}".format(
        "Passed"
        if get_contact_age(contacts, "Sarah", "Sanders") == 19
        else "Failed"))
    update_contact_email(contacts, "Jim", "Jones", "jim.jones@gmail.com")
    print("Updating Jim Jones' email: {}".format(
        "Passed"
        if get_contact_email(contacts, "Jim", "Jones") == "jim.jones@gmail.com"
        else "Failed"))
    update_contact_number(contacts, "Katie", "Katz", "907-536-2946")
    print("Updating Katie Katz' number: {}".format(
        "Passed"
        if get_contact_number(contacts, "Katie", "Katz") == "907-536-2946"
        else "Failed"))
    # Displays one real contact and attempts to display one that does not
    # Exist which results in an error to the user
    display(contacts, "Katie", "Katz")
    display(contacts, "George", "Shaw")

# Calls to main and starts everything
main()
