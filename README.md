
# 🚊 Delhi Metro Route and Schedule Simulator

A command-line Python application that simulates **Delhi Metro schedules, routes, interchanges, and fares** using Blue Line (Dwarka Sector 21 ↔ Noida Electronic City / Vaishali) and Magenta Line (Janakpuri West ↔ Botanical Garden) datasets.

---
# 📘 Project Overview

The **Delhi Metro Route and Schedule Simulator** allows you to:

- View next metro timings  
- Plan journeys between stations  
- Get multiple routes with interchanges  
- Calculate travel time and fares  
- Identify the fastest route  

Uses `metro_data.txt` to build a complete metro graph.

---

# 🧩 Features

- Schedule view  
- Multi-route journey planner  
- Interchange detection  
- Walking time added between lines  
- Fare calculation  
- Automatic fastest-route identification  

---

# 📂 Project Structure

```
2025103_metro_simulator.py
metro_data.txt
README.md
```
- "metro_data.txt" is for storage of data of stations,line,travel time and other things.
- "2025103_metro_simulator.py" is the main program in python.
- "README.md" is documentation of project.

---
## 💿 Dataset Format
Each line in `metro_data.txt` looks like:
```
LineName,CurrentStation,NextStation,TravelTime,Interchange(Yes/No)
```

Example:
```
Blue,Rajiv Chowk,Ramakrishna Ashram Marg,2,No
```

---
# ▶️ How to Run

```
1. Keep both files ("metro_data.txt" and "2025103_metro_simulator.py") in same folder 
2. Run: 2025103_metro_simulator.py file  
```

---

# 🧭 Installation

## 💻 Windows  
```
python3 2025103_metro_simulator.py
```

## 💻 Mac / Linux  
```
python3 2025103_metro_simulator.py
```

---

## 📸 Screenshots 

### 🕒 Upcoming Metro Schedule
### Input1

![alt text](<Screenshot 2025-11-24 at 8.10.21 PM.png>)
---
### Input2
![alt text](<Screenshot 2025-11-24 at 8.10.41 PM.png>)
### 🚇 Route Planning Examples
### Input1
![alt text](<Screenshot 2025-11-24 at 8.11.05 PM.png>)
---
### Input2
![alt text](<Screenshot 2025-11-24 at 8.11.47 PM.png>)
---




# 🧠 Internal Working

## Which Function is for what Thing
- taking_data(): This function extracts data from "metro_data.txt" file by opening it in read mode storing each data in diffrent variable.

- frequency(): It checks metro comes in which frequency, between 08:00AM to 10:00AM and between 05:00PM to 7:00PM metro will come in every 4 minutes otherwise 8 minutes.

- time(): It will convert manual time to minutes.

- minute_to_time(): It will convert minutes in manual time.
- station_order(): it adds all stations provided in file to list.

- calc_travel: It check for whether both entered stations are valid or not then return total time required to travel between those stations and it works in both direction.

- next_metro_time(): It calculates the next metro departure time.

- compute_routes(): It calculates all possible routes to travel between two stations whether both are on same line or diffrent line. 

- handling_time():It handles error in time.

- handling_station: It handles error in station.

- main(): This function is used for calling other function and calculating fare and giving final output. 


## Data Loading
Builds a dictionary of metro line → stations.

## Station Ordering  
Reconstructs direction-wise travel order.

## Schedule Analyzer  
Service Hours: 
	06:00-23:00 

    Peak: 08:00-10:00 and 17:00-19:00   (4 minutes frequency) 
	Off-peak: 8 minutes frequency 


## Route Planner  
- Traverse line  
- Add interchange walking time  
- Compute next arrival metro  
- Compute travel and total time  
- Compute fare  

---


# 💭 Assumptions
    - I had implemented here time in 24 hours format.
    - I had taken random time (2 or 3 minutes) between two station.
    - I had taken line interchange time = 5 minutes which passenger will take to change line from Blue to Magenta or from Magenta to Blue 



# 🚀 Future Improvements

- Add all metro lines  
- GUI version  
- Real DMRC data integration  
- Live delay simulation  

---

# 👤 Author

**Arpit Prakash Gupta**  
GitHub: https://github.com/arpitprakashgupta

---
