#!/usr/bin/env python2


class UnknownPersonError(Exception):
    def __init__(self, message):
        self.message = message


def splitwise(expenses):
    total = reduce(lambda a, b: a + b, expenses.values())
    per_person_expense = total / len(expenses)
    for key in expenses.keys():
        expenses[key] -= per_person_expense
    extra_amount = total % len(expenses)
    expenses[1] -= extra_amount
    return expenses


def main():
    expense_count, friends_count = map(int, raw_input().split(" "))
    expenses = {}
    for _ in xrange(1, friends_count + 1):
        expenses[_] = 0
    for _ in xrange(expense_count):
        payer, expense = map(int, raw_input().split(" "))
        try:
            expenses[payer] += expense
        except KeyError:
            raise UnknownPersonError("This Person was not on the trip")
    for person, owes in splitwise(expenses).items():
        print person, owes


if __name__ == '__main__':
    main()
