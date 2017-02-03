base_meal = float(raw_input())
tip_percent = float(raw_input())
tax_percent = float(raw_input())
tip = base_meal * (tip_percent/100)
tax = base_meal * (tax_percent/100)
total_cost = int(round(base_meal+tip+tax))
print 'The total meal cost is', total_cost, 'dollars.'
