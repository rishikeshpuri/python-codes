amount="32.054,23"
m=amount.maketrans
amount=amount.translate(m(',.','.,'))
print(amount)