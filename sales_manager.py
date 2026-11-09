import calendar
from datetime import date


# ==========================================
# 1. INPUT VALIDATION FUNCTION
# ==========================================

def get_number(prompt, allow_zero=True):
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Value cannot be negative.")

            elif value == 0 and not allow_zero:
                print("Value must be greater than zero.")

            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number.")


# ==========================================
# 2. PROGRAM INTRODUCTION
# ==========================================

print("=" * 45)
print("       MONTHLY SALES MANAGEMENT SYSTEM")
print("=" * 45)


# ==========================================
# 3. COLLECT STORE INFORMATION
# ==========================================

store_name = input("Enter store name: ").strip()
store_code = input("Enter store code: ").strip()


# ==========================================
# 4. COLLECT SALES INFORMATION
# ==========================================

monthly_sales_target = get_number(
    "Enter monthly sales target: ",
    allow_zero=False
)

sales_achieved = get_number(
    "Enter sales achieved so far (up to yesterday): "
)


# ==========================================
# 5. CALENDAR CALCULATIONS
# ==========================================

today = date.today()

days_in_month = calendar.monthrange(
    today.year,
    today.month
)[1]

days_elapsed = today.day - 1

days_remaining = days_in_month - days_elapsed


# ==========================================
# 6. SALES PERFORMANCE CALCULATIONS
# ==========================================

remaining_sales = max(
    monthly_sales_target - sales_achieved,
    0
)

percentage_achieved = (
    sales_achieved / monthly_sales_target
) * 100

if remaining_sales > 0:
    daily_required = remaining_sales / days_remaining
else:
    daily_required = 0


# ==========================================
# 7. PERFORMANCE REPORT
# ==========================================

print("\n" + "=" * 45)
print("             PERFORMANCE REPORT")
print("=" * 45)

print(f"Store name:          {store_name}")
print(f"Store code:          {store_code}")
print(f"Monthly target:      {monthly_sales_target:,.2f}")
print(f"Sales achieved:      {sales_achieved:,.2f}")
print(f"Remaining sales:     {remaining_sales:,.2f}")
print(f"Percentage achieved: {percentage_achieved:.2f}%")


# ==========================================
# 8. TARGET ACHIEVEMENT EVALUATION
# ==========================================

print("\n--- PERFORMANCE STATUS ---")

if percentage_achieved >= 100:
    print("Well done! Target achieved.")

elif percentage_achieved >= 70:
    print("Almost there!")

elif percentage_achieved >= 40:
    print("Keep pushing!")

else:
    print("Performance needs improvement.")


# ==========================================
# 9. EXCESS SALES
# ==========================================

if sales_achieved > monthly_sales_target:
    excess_sales = sales_achieved - monthly_sales_target

    print(f"Excess over target: {excess_sales:,.2f}")


# ==========================================
# 10. DAILY SALES PLAN
# ==========================================

print("\n" + "=" * 45)
print("                DAILY SALES PLAN")
print("=" * 45)

print(f"Days in month:       {days_in_month}")
print(f"Days elapsed:        {days_elapsed}")
print(f"Days remaining:      {days_remaining}")
print(f"Daily sales needed:  {daily_required:,.2f}")


# ==========================================
# 11. SALES FORECASTING
# ==========================================

print("\n--- MONTHLY SALES FORECAST ---")

if days_elapsed > 0:

    daily_average = sales_achieved / days_elapsed

    projected_total = daily_average * days_in_month

    print(f"Current daily average: {daily_average:,.2f}")
    print(f"Projected monthly sales: {projected_total:,.2f}")

    if projected_total >= monthly_sales_target:
        print("Forecast: ON TRACK to meet the monthly target.")

    else:
        print("Forecast: BEHIND the monthly target.")
        print("The store needs to increase its daily sales.")

else:
    print("First day of the month.")
    print("Not enough completed days to calculate a forecast.")


# ==========================================
# 12. FINAL REPORT
# ==========================================

print("\n" + "=" * 45)
print("             END OF SALES REPORT")
print("=" * 45)
