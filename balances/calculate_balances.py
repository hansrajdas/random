import json


def balance_expenses(expenses, per_head):
    print('\nTransactions required')
    print('---------------------')
    if all(v[1] == per_head for v in expenses):
        print('* No transaction required')
        return None
    start = 0
    end = len(expenses) - 1
    while start < end:
        balance = per_head - expenses[start][1]
        if balance < expenses[end][1] - per_head:
            print('* %s should give %.2f to %s' % (expenses[start][0],
                                                 balance,
                                                 expenses[end][0]))
            expenses[start][1] = per_head
            expenses[end][1] = expenses[end][1] - balance
            start += 1
        elif balance > expenses[end][1] - per_head:
            print('* %s should give %.2f to %s' % (expenses[start][0],
                                                 expenses[end][1] - per_head,
                                                 expenses[end][0]))
            expenses[start][1] = (
                expenses[start][1] + expenses[end][1] - per_head)
            expenses[end][1] = per_head
            end -= 1
        else:
            print('* %s should give %.2f to %s' % (expenses[start][0],
                                                 balance,
                                                 expenses[end][0]))
            expenses[start][1] = per_head
            expenses[end][1] = per_head
            start += 1
            end -= 1

def sort_dict_with_value(data):
    """Returns list of dictionaries, sorted based on values."""
    return [[k, v] for k, v in sorted(data.items(), key=lambda item: item[1])]

def get_details_map():
    f = open('details.json', 'r')
    return json.loads(f.read(), strict=False)

def main():
    details = get_details_map()

    total = 0
    count = 0
    expenses = {}
    for user in details:
        expenses[user] = sum(details[user])
        total += expenses[user]
        count += 1

    sorted_expenses = sort_dict_with_value(expenses)
    for expense in sorted_expenses:
        print('%s spend: %.2f' % (expense[0], expense[1]))

    per_head = total / count
    print('\nTotal expense: %.2f' % total)
    print('Per head share: %.2f' % per_head)
    balance_expenses(sorted_expenses, per_head)


if __name__ == '__main__':
    main()
