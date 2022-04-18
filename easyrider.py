import json
# import re


input_data = json.loads(input())
# Stage 6. Check that all the departure points, final stops, and transfer stations are not "On-demand".
stop_dict = {}
wrong_o_stops = []

for stop in input_data:
    if stop["stop_name"] not in stop_dict:
        stop_dict[stop["stop_name"]] = []
    stop_dict[stop["stop_name"]].append(stop["stop_type"])

    if "O" in stop_dict[stop["stop_name"]] and len(stop_dict[stop["stop_name"]]) > 1:
        wrong_o_stops.append(stop['stop_name'])
print("On demand stops test:")
print(f'Wrong stop type: {sorted(wrong_o_stops) if wrong_o_stops else "OK"}')

"""# Stage 5. Check on arrival time to the next stops of bus line
bus_time_dict = {}
time_check = True
print("Arrival time test:")

# Create a Dictionary {bus_id : [time at stop with formatting HHMM, stop name]}
for stop in input_data:    
    if stop["bus_id"] not in bus_time_dict:
        bus_time_dict[stop["bus_id"]] = []
    stop_tuple = "".join(stop["a_time"].split(":")), stop["stop_name"]
    bus_time_dict[stop["bus_id"]].append(stop_tuple)

# Check for errors on the line
for bus in bus_time_dict:
    for n in range(len(bus_time_dict[bus]) - 1):
        if bus_time_dict[bus][n][0] < bus_time_dict[bus][n + 1][0]:
            pass
        else:
            print(f"bus_id line {bus}: wrong time on station {bus_time_dict[bus][n+1][1]}")
            time_check = False
            break
else:
    if time_check:
        print("OK")
"""
""" 
# Stages 1-4 Type and Data check with regex, error count. Count and check issues on start, transfer, finish stops
dict_for_errors = {'bus_id': 0, 'stop_id': 0, 'stop_name': 0, 'next_stop': 0, 'stop_type': 0, 'a_time': 0}
types = {'bus_id': 0, 'stop_id': 0, 'stop_name': "[proper name][suffix]",
         'next_stop': 0, 'stop_type': "S/O/F", 'a_time': "HH:MM"}
bus_id_dict = {}
start_stops = []
all_stops = []
transfer_stops = set()
finish_stops = []


def type_check(key, obj, ref_obj):
    if key in ["stop_name"]:
        return re.match(r"[A-Z][a-z]+[ \w]* (Street|Boulevard|Avenue|Road)$", obj) is not None
    if key == 'a_time':
        return re.match(r"[0-2]\d:[0-5]\d$", obj) is not None
    if key == 'stop_type':
        return obj in ['', 'S', 'O', 'F']
    return type(obj) == type(ref_obj)


def update_stops_dict(stop_name, stop_type):
    if stop_type == "S":
        start_stops.append(stop_name)
    elif stop_type == "F":
        finish_stops.append(stop_name)

    if stop_name not in all_stops:
        all_stops.append(stop_name)
    else:
        transfer_stops.add(stop_name)


for stop in input_data:
    for field in stop:
        # Error counter.
        if not type_check(field, stop[field], types[field]):
            dict_for_errors[field] += 1
            
    # Stage 4
    # Create set for each bus_id, add stop_types
    if type(stop["bus_id"]) is int:
        if stop["bus_id"] not in bus_id_dict:
            bus_id_dict[stop["bus_id"]] = set()
        if stop["stop_type"] in ["S", "F"] and stop["stop_type"] not in bus_id_dict[stop["bus_id"]]:
            bus_id_dict[stop["bus_id"]].add(stop["stop_type"])
        # elif stop["stop_type"] in bus_id_dict[stop["bus_id"]]:
            # print(stop["stop_name"])
        update_stops_dict(stop["stop_name"], stop["stop_type"])

for bus in bus_id_dict:
    if {'S', 'F'} != bus_id_dict[bus]:
        print(f"There is no start or end stop for the line: {bus}.")
        break
else:
    print("Start stops:", len(start_stops), sorted(list(set(start_stops))))
    print("Transfer stops:", len(transfer_stops), sorted(list(transfer_stops)))
    print("Finish stops:", len(set(finish_stops)), sorted(list(finish_stops)))
"""
"""
print("Line names and number of stops:")
for bus_id in bus_id_dict:
    print(f"bus_id: {bus_id}, stops: {bus_id_dict[bus_id]}")
"""
"""
print(f'Type and required field validation: {sum(dict_for_errors.values())} errors')
for data in dict_for_errors:
    if data in ["stop_name", "stop_type", "a_time"]:
            print(data, dict_for_errors[data], sep=': ')
"""
