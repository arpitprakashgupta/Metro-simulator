# 🚊 Delhi Metro Route and Schedule Simulator

A command-line Python application that simulates **Delhi Metro schedules, routes, interchanges, and fares** using Blue Line (Dwarka Sector 21 ↔ Noida Electronic City / Vaishali) and Magenta Line (Janakpuri West ↔ Botanical Garden) datasets.

# 💸 Extra Feature (Fair Calculation)

| Time (min) | Fare |
|-----------|------|
| 0–10      | ₹10  |
| 11–20     | ₹20  |
| 21–30     | ₹30  |
| 31–40     | ₹40  |
| 41–50     | ₹50  |
| 51–999    | ₹60  |


In main function named main():
i had written some line of code which outputs total fare of journey based on travel time.
~~~
if int(route['total_time']) in range(0,11):
    print(f"   Total Fare: 10rupees\n")
elif int(route['total_time']) in range(11,21):
    print(f"   Total Fare: 20rupees\n")
elif int(route['total_time']) in range(21,31):
    print(f"   Total Fare: 30rupees\n")
elif int(route['total_time']) in range(31,41):
    print(f"   Total Fare: 40rupees\n")
elif int(route['total_time']) in range(41,51):
    print(f"   Total Fare: 50rupees\n")
elif int(route['total_time']) in range(51,999):
    print(f"   Total Fare: 60rupees\n")
~~~
---
# 👤 Author

**Arpit Prakash Gupta**  
GitHub: https://github.com/arpitprakashgupta

---