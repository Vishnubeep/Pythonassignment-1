# Cost calculations for hosting provider

hourly_rate = 0.51
daily_rate = 24 * hourly_rate
weekly_rate = 7 * daily_rate
monthly_rate = 4 * weekly_rate   # assuming 4 weeks per month

account_balance = 918

operating_days = account_balance / daily_rate

print("Cost per day: $", daily_rate)
print("Cost per week: $", weekly_rate)
print("Cost per month: $", monthly_rate)
print("Number of days you can operate with $918:", operating_days)
