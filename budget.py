class Category:

  def __init__(self, description):
    self.description = description
    self.ledger = []

  def __repr__(self):
    first_line = self.description.center(30, "*") + "\n"
    output = first_line
    for x in self.ledger:
      next_line = '{:<23}'.format(x['description'][:23])
      next_line += '{:>7.2f}'.format(x['amount'])
      output += next_line + '\n'
    output += 'Total: {}'.format(self.get_balance())
    return output

  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=''):
    if amount <= self.get_balance():
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    sum = 0
    for x in self.ledger:
      sum += x['amount']
    return sum

  def transfer(self, amount, transfer_destination):
    if self.withdraw(amount,
                     'Transfer to ' + str(transfer_destination.description)):
      transfer_destination.deposit(amount,
                                   "Transfer from {}".format(self.description))
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True


def create_spend_chart(list_of_categories):
  output = 'Percentage spent by category' + '\n'
  expenditure = []
  longest_word_length = 0
  sum_of_all = 0
  for y in list_of_categories:
    total_amount = 0
    for x in y.ledger:
      if x['amount'] < 0:
        total_amount += abs(x['amount'])
    expenditure.append({"description": y.description, "amount": total_amount})
    sum_of_all += total_amount
    if longest_word_length <= len((y.description)):
      longest_word_length = len((y.description))

  for x in expenditure:
    x['percentage'] = round(x['amount'] / sum_of_all * 100)
    x['description'] = x['description'].capitalize()
  print(expenditure)

  for num in range(10, -1, -1):
    percentage_num = (num) * 10
    output += '{: >3}|'.format(percentage_num)

    for x in expenditure:
      if x['percentage'] >= percentage_num:
        output += ' o '
      else:
        output += '   '
    output += ' \n'
  output += '    ' + '-' * (len(expenditure) * 3 + 1) + '\n'

  for num in range(longest_word_length):
    output += '    '
    for x in expenditure:
      if num < len(x['description']):
        output += x['description'][num].center(3, " ")
      else:
        output += '   '
    if num < longest_word_length - 1:
      output += ' \n'
  output += ' '
  return output
