def taking_data(metro_data):
    lines = {}
    with open(metro_data, "r") as f:
        for i in f:
            i = i.strip()
            if not i or i.startswith("#"):
                continue
            line, cur_station, next_station, travel_time, interchange =i.split(",")
            if line not in lines:
                lines[line] = []
            lines[line].append({"cur_station": cur_station,
                "next": next_station,
                "time": int(travel_time),
                "interchange": interchange=="Yes"})
    return lines

def frequency(t):
    minutes = time(t)
    if minutes in range(480,600) or minutes in range(1020,1140):
        return 4 
    return 8

def time(t):
    hour, minute = map(int, t.split(":"))
    return hour*60 + minute

def minute_to_time(minute):
    hour = minute // 60
    minute = minute % 60
    return f"{hour:02d}:{minute:02d}"

def station_order(line_data):
    stations = []
    for i in line_data:
        s = i.get("cur_station")
        if s and s not in stations:
            stations.append(s)
        nxt = i.get("next")
        if nxt and nxt != "-" and nxt not in stations:
            stations.append(nxt)
    return stations

def calc_travel(line_data, source_station, destination_station):
    stations =station_order(line_data)
    if source_station not in stations or destination_station not in stations:
        return None
    s = stations.index(source_station)
    d = stations.index(destination_station)
    total = 0
    if s < d:
        for i in range(s, d):
            for j in line_data:
                if j["cur_station"] == stations[i]:
                    total += j["time"]
                    break
    else:
        for i in range(d, s):
            for j in line_data:
                if j["cur_station"] == stations[i]:
                    total += j["time"]
                    break
    return total

def next_metro_time(cur_time):
    t =time(cur_time)
    if t < 360 or t >= 1380:  
        return None
    freq= frequency(cur_time)
    rem= t % freq
    return t if rem==0 else t + (freq - rem)

def compute_route(lines, source_station, destination_station, cur_time):
    next_metro = next_metro_time(cur_time)
    if next_metro is None:
        return {"error": "No metro at this time."}
    if source_station == destination_station:
        return {"error": "Both stations can't be same."}
    src_line = None
    dst_line = None
    for line_name, line_data in lines.items():
        station_list = station_order(line_data)
        if source_station in station_list:
            src_line = line_name
        if destination_station in station_list:
            dst_line = line_name
    if src_line is None:
        return {"error": f"'{source_station}' not found."}
    if dst_line is None:
        return {"error": f"'{destination_station}' not found."}
    result ={"routes": []}
    if src_line == dst_line:        
        travel_time = calc_travel(lines[src_line], source_station, destination_station)
        arrival_time = next_metro + travel_time
        if arrival_time>=1380:
            return {"error": "Journey would end after service hours"}
        direct_route = {}
        direct_route["name"] = "Direct Route"
        steps_list = []
        step_1 = f"start at {source_station} ({src_line})"
        step_2 = f"Next metro: {minute_to_time(next_metro)}"
        step_3 = f"Arrive at  {destination_station} at {minute_to_time(arrival_time)}"
        steps_list.append(step_1)
        steps_list.append(step_2)
        steps_list.append(step_3)
        direct_route["steps"] = steps_list
        direct_route["total_time"] = travel_time
        result["routes"].append(direct_route)
        print
        return result
    src_stations = station_order(lines[src_line])
    dst_stations = station_order(lines[dst_line])
    interchanges = set(src_stations).intersection(dst_stations)
    if not interchanges:
        return {"error": "No interchange between these lines."}
    Interchange_time=5
    for interchange in interchanges:       # yes interchange
        time_to_interchange =calc_travel(lines[src_line], source_station, interchange)
        arrival_at_interchange= next_metro + time_to_interchange
        interchange_time= arrival_at_interchange + Interchange_time  
        departure_after_transfer= next_metro_time(minute_to_time(interchange_time))

        if departure_after_transfer is None or departure_after_transfer >= 1380:
            continue  
        travel_to_dst= calc_travel(lines[dst_line], interchange, destination_station)
        final_arrival= departure_after_transfer + travel_to_dst
        if final_arrival >= 1380:
            continue  

        route_details = {}
        route_details["name"] = "Using interchange at " + interchange
        steps = []
        step1 = f" Start at {source_station} ({src_line})"
        step2 = f" Next metro: {minute_to_time(next_metro)}"
        step3 = f" Reach {interchange} at {minute_to_time(arrival_at_interchange)}"
        step4 = f" Walk to {dst_line} Line (5 minutes)"
        step5 = f" Next {dst_line} metro at {minute_to_time(departure_after_transfer)}"
        step6 = f" Arrive at {destination_station} by {minute_to_time(final_arrival)}"
        steps.append(step1)
        steps.append(step2)
        steps.append(step3)
        steps.append(step4)
        steps.append(step5)        
        steps.append(step6)
        route_details["steps"] = steps
        time_taken = final_arrival - next_metro
        route_details["total_time"] = time_taken
        result["routes"].append(route_details)
    return result
    
def handling_time(time_1):
    while True:
        time = input(time_1).strip()
        if ":" not in time:
            print("Invalid time format.")
            continue
        hour, minute =time.split(":")
        if not (hour.isdigit() and minute.isdigit()):
            print("Invalid time.")
            continue
        hour, minute =int(hour), int(minute)
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            print("Invalid time.")
            continue
        return time
    
def handling_stations(time_1, all_stations):
    while True:
        station=input(time_1).strip()
        if not station:
            print("Enter a station name.")
            continue
        a = None
        for s in all_stations:
            if s.lower() == station.lower():
                a = s
                break
        if a is None:
            print(f"Station '{station}' not found. Please check spelling.")
            continue
        return a
    
def main():
    lines=taking_data("metro_data.txt")
    all_stations=[]
    for line_data in lines.values():
        all_stations += station_order(line_data)
    print("1. View upcoming metro schedule")
    print("2. Plan your journey")
    choice =input("Enter choice: ").strip()
    if choice=="1":
        print("\n View upcoming metro schedule")
        station= handling_stations("Enter Station: ", all_stations)
        time= handling_time("Enter current time (HH:MM): ")
        next_station= next_metro_time(time)
        if next_station is None:
            print("No service available now.")
            return
        if next_station >= 1380: 
            print("No more metros today. Last metro has departed.")
            return
        print("Next metro at:", minute_to_time(next_station))
        freq=frequency(time)
        subs=[]
        travel_to_dst= next_station
        for i in range(5):
            travel_to_dst += freq
            if travel_to_dst>=1380:
                break
            subs.append(minute_to_time(travel_to_dst))
            freq = frequency(minute_to_time(travel_to_dst))
        if subs:
            print(f"Subsequent metros at:{', '.join(subs)}")
        return
    elif choice=="2":
        print("\n Plan your journey")
        source_station=handling_stations("Enter Source: ", all_stations)
        destination_station= handling_stations("Enter Destination: ", all_stations)
        time= handling_time("Enter Current Time (HH:MM): ")
        result= compute_route(lines, source_station, destination_station, time)
        if "error" in result:
            print(f"\nError: {result['error']}")
            return
        print("\nAvailable Routes:\n")
        fastest= None
        fastest_time =999999
        len_routes = len(result["routes"])
        for i in range(len_routes):
            route = result["routes"][i]
            print(f"Route {i+1} ({route['name']}):")
            for j in route["steps"]:
                print("  " + j)
            print(f"   Total time: {route['total_time']} minutes")
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
            if route["total_time"] < fastest_time:
                fastest_time = route["total_time"]
                fastest= i+1
        print(f"Fastest Route: Route {fastest}")
        return

    else:
        print("Invalid Choice. Please enter 1 or 2.")
        return



main()
