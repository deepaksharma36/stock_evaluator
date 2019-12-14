
def simple_dcf_value(cur_cash_flow, growth, discount_rate, period,
                     growth_discount_rate=10):
    dcf_value = 0
    for year_count in range(period):
        growth = growth*(.90)**period
        profit = cur_cash_flow*(1 + growth/100)**year_count
        discount = (1 + discount_rate)**year_count
        dcf_value += profit/discount
    return dcf_value

