# Monthly Sales Management System

A Python command-line tool that helps a retail store manager track progress toward a monthly sales target. It calculates performance, the daily sales still needed, and whether the store is on track to hit its target by month end.

Built as a practical step from learning Python syntax to solving a real retail business problem.

## Business problem

A retail company sets each store a monthly sales target. A store manager needs to know:

1. How much of the target has been achieved?
2. How much is left to sell?
3. How much must the store sell **every day** for the rest of the month?
4. At the current pace, will the store reach its target?

## Features

- Collects store name, store code, monthly target and sales achieved
- Calculates remaining sales and percentage achieved (2 decimal places)
- Shows a performance message based on the percentage
- Shows the excess amount when sales exceed the target
- Detects the number of days in the current month, including leap years
- Calculates the daily sales required for the remaining days
- Forecasts month-end sales from the current daily average and reports ON TRACK or BEHIND
- Validates all numeric input, so the program never crashes on bad entries

## How to run

Requires Python 3.8 or later. No external libraries.

```bash
python sales_manager.py
```

## Sample run

Run on 9 November, with a target of 60,000 and 14,500 sold up to yesterday:

```
=============================================
       MONTHLY SALES MANAGEMENT SYSTEM
=============================================
Enter store name: Salmiya Branch
Enter store code: S01
Enter monthly sales target: 60000
Enter sales achieved so far (up to yesterday): 14500

=============================================
             PERFORMANCE REPORT
=============================================
Store name:          Salmiya Branch
Store code:          S01
Monthly target:      60,000.00
Sales achieved:      14,500.00
Remaining sales:     45,500.00
Percentage achieved: 24.17%

--- PERFORMANCE STATUS ---
Performance needs improvement.

=============================================
                DAILY SALES PLAN
=============================================
Days in month:       30
Days elapsed:        8
Days remaining:      22
Daily sales needed:  2,068.18

--- MONTHLY SALES FORECAST ---
Current daily average: 1,812.50
Projected monthly sales: 54,375.00
Forecast: BEHIND the monthly target.
The store needs to increase its daily sales.
```

## Logic

**Assumptions**
- "Sales achieved" means sales up to the end of yesterday.
- "Days remaining" includes today, because the store still trades today.

**Formulas**

```
days_elapsed        = today's date - 1
days_remaining      = days_in_month - days_elapsed
remaining_sales     = max(target - achieved, 0)
percentage_achieved = achieved / target x 100
daily_required      = remaining_sales / days_remaining
daily_average       = achieved / days_elapsed
projected_total     = daily_average x days_in_month
on track            = projected_total >= target
```

**Performance messages**

| Percentage achieved | Message |
|---|---|
| 100% or above | Well done! Target achieved. |
| 70% to below 100% | Almost there! |
| 40% to below 70% | Keep pushing! |
| Below 40% | Performance needs improvement. |

The checks run from highest to lowest, so each lower check needs only a lower bound and no percentage falls into a gap.

**Input validation**

```
LOOP:
  try to convert input to a number
      fails            -> ValueError caught -> message -> ask again
  value < 0            -> message -> ask again
  value == 0 and the field does not allow zero -> message -> ask again
  otherwise            -> accept and exit loop
```

The same `get_number()` function validates both numbers. Target must be greater than zero. Sales may be zero but never negative.

## Edge cases handled

| Scenario | Behaviour |
|---|---|
| Target is 0 or negative | Rejected, which also prevents divide-by-zero |
| Sales are negative | Rejected |
| Text such as "abc" | `ValueError` caught, user asked again |
| Sales above target | Remaining shows 0.00 and the excess is displayed |
| Target already reached | Daily sales needed shows 0.00 |
| 1st of the month | No days elapsed, so the forecast is skipped |
| Last day of the month | Days remaining is 1, so the full remainder is needed today |
| February in a leap year | `calendar.monthrange()` returns 29 days |

## Python concepts practised

- Functions and reusable input validation
- `while True` loops with `try` / `except ValueError`
- Conditional logic with `if` / `elif` / `else`
- f-string formatting (`:,.2f` for two decimals and thousands separators)
- `calendar.monthrange()` and `datetime.date.today()`
- Structuring a program in clearly labelled sections

## Possible improvements

- Loop to check several stores in one session
- Save each report to a CSV file to keep a history
- Read targets and sales from an Excel file for many stores
- Unit tests for the calculation logic

## Author

Joe, IT and cybersecurity learner and retail supervisor, building practical projects from real business problems.
