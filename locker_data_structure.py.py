# Start with an empty data structure
lockers = []

# Add hardcoded locker records to the data structure

# Adding locker 1
lockers.append({
    "id": "L01",
    "occupied": True,
    "mobile": "1122334455",
    "passcode": "ABXY11",
    "time": 5
})

# Adding locker 2
lockers.append({
    "id": "L02",
    "occupied": False,
    "mobile": None,
    "passcode": None,
    "time": 0
})

# Adding locker 3
lockers.append({
    "id": "L03",
    "occupied": True,
    "mobile": "9988776655",
    "passcode": "BC012",
    "time": 12
})

# Adding locker 4
lockers.append({
    "id": "L04",
    "occupied": True,
    "mobile": "2244668800",
    "passcode": "OXD33",
    "time": 2
})

# Adding locker 5
lockers.append({
    "id": "L05",
    "occupied": False,
    "mobile": None,
    "passcode": None,
    "time": 0
})

# Adding locker 6
lockers.append({
    "id": "L06",
    "occupied": True,
    "mobile": "3311557799",
    "passcode": "L1O21",
    "time": 2
})

# Adding Locker 7
lockers.append({
    "id": "L07",
    "occupied": True,
    "mobile": "4422668810",
    "passcode": "IUV66",
    "time": 2
})

# Display all locker records and their details

print("\n")
print("═" * 60)
print("DISPLAYING ALL THE LOCKERS AND ITS DETAILS".center(60))
print("═" * 60)

for locker in lockers:
    print(f"Locker ID  :  {locker['id']}")
    print(f"Occupied   :  {locker['occupied']}")
    print(f"Mobile     :  {locker['mobile']}")
    print(f"Passcode   :  {locker['passcode']}")
    print(f"Time       :  {locker['time']} hours")
    print("─" * 60)

print("\n\n\n")

# Display lockers that are currently occupied

print("═" * 60)
print("DISPLAYING THE OCCUPIED LOCKERS".center(60))
print("═" * 60)

for locker in lockers:
    if locker["occupied"]:
        print(f"Locker ID  :  {locker['id']}")
        print(f"Mobile     :  {locker['mobile']}")
        print(f"Passcode   :  {locker['passcode']}")
        print(f"Time       :  {locker['time']} hours")
        print("─" * 60)

print("\n\n\n")

# Display lockers that are currently available

print("═" * 60)
print("DISPLAYING THE AVAILABLE(EMPTY) LOCKERS".center(60))
print("═" * 60)

for locker in lockers:
    if not locker["occupied"]:
        print(f"Locker ID  :  {locker['id']}")
        print(f"Occupied   :  {locker['occupied']}")
        print("─" * 60)

print("\n\n\n")

# Change an available locker to occupied and assign details

print("═" * 60)
print("CHANGING A LOCKER FROM EMPTY TO OCCUPIED".center(60))
print("═" * 60)

print("\n")

print("BEFORE")
print("─" * 60)

for locker in lockers:
    if locker["id"] == "L02":
        print(f"Locker ID  :  {locker['id']}")
        print(f"Occupied   :  {locker['occupied']}")
        print(f"Mobile     :  {locker['mobile']}")
        print(f"Passcode   :  {locker['passcode']}")
        print(f"Time       :  {locker['time']} hours")
        print("─" * 60)

for locker in lockers:
    if locker["id"] == "L02":
        locker["occupied"] = True
        locker["mobile"] = "5544668811"
        locker["passcode"] = "B45C"
        locker["time"] = 1
        break

print("\nAFTER")
print("─" * 60)

for locker in lockers:
    if locker["id"] == "L02":
        print(f"Locker ID  :  {locker['id']}")
        print(f"Occupied   :  {locker['occupied']}")
        print(f"Mobile     :  {locker['mobile']}")
        print(f"Passcode   :  {locker['passcode']}")
        print(f"Time       :  {locker['time']} hours")
        print("─" * 60)

print("\n\n\n")

# Free an occupied locker by removing customer information

print("═" * 60)
print("FREEING A LOCKER".center(60))
print("═" * 60)

print("\n")

print("BEFORE")
print("─" * 60)

for locker in lockers:
    if locker["id"] == "L03":
        print(f"Locker ID  :  {locker['id']}")
        print(f"Occupied   :  {locker['occupied']}")
        print(f"Mobile     :  {locker['mobile']}")
        print(f"Passcode   :  {locker['passcode']}")
        print(f"Time       :  {locker['time']} hours")
        print("─" * 60)

for locker in lockers:
    if locker["id"] == "L03":
        locker["occupied"] = False
        locker["mobile"] = None
        locker["passcode"] = None
        locker["time"] = 0
        break

print("\nAFTER")
print("─" * 60)

for locker in lockers:
    if locker["id"] == "L03":
        print(f"Locker ID  :  {locker['id']}")
        print(f"Occupied   :  {locker['occupied']}")
        print(f"Mobile     :  {locker['mobile']}")
        print(f"Passcode   :  {locker['passcode']}")
        print(f"Time       :  {locker['time']} hours")
        print("─" * 60)

print("\n\n\n")

# Update the occupied time of a locker

print("═" * 60)
print("UPDATING THE OCCUPIED TIME".center(60))
print("═" * 60)

print("\n")

print("BEFORE")
print("─" * 60)

for locker in lockers:
    if locker["id"] == "L04":
        print(f"Locker ID  :  {locker['id']}")
        print(f"Occupied   :  {locker['occupied']}")
        print(f"Mobile     :  {locker['mobile']}")
        print(f"Passcode   :  {locker['passcode']}")
        print(f"Time       :  {locker['time']} hours")
        print("─" * 60)

for locker in lockers:
    if locker["id"] == "L04":
        locker["time"] += 3
        break

print("\nAFTER")
print("─" * 60)

for locker in lockers:
    if locker["id"] == "L04":
        print(f"Locker ID  :  {locker['id']}")
        print(f"Occupied   :  {locker['occupied']}")
        print(f"Mobile     :  {locker['mobile']}")
        print(f"Passcode   :  {locker['passcode']}")
        print(f"Time       :  {locker['time']} hours")
        print("─" * 60)

print("\n\n\n")

# Search for a locker using its unique identifier

print("═" * 60)
print("SEARCHING THE LOCKER".center(60))
print("═" * 60)

search_id = "L01"

found = False

for locker in lockers:
    if locker["id"] == search_id:
        print("Locker Found!")
        print(f"Locker ID  :  {locker['id']}")
        print(f"Occupied   :  {locker['occupied']}")
        print(f"Mobile     :  {locker['mobile']}")
        print(f"Passcode   :  {locker['passcode']}")
        print(f"Time       :  {locker['time']} hours")
        print("─" * 60)
        found = True
        break

if not found:
    print(f"Locker {search_id} not found.")

print("\n\n\n")

# Count total, occupied, and available lockers

print("═" * 60)
print("LOCKER STATUS REPORT".center(60))
print("═" * 60)

total_lockers = len(lockers)
occupied_count = 0
available_count = 0

for locker in lockers:
    if locker["occupied"]:
        occupied_count += 1
    else:
        available_count += 1

print(f"Total Lockers      :  {total_lockers}")
print(f"Occupied Lockers   :  {occupied_count}")
print(f"Available Lockers  :  {available_count}")
print("─" * 60)

print("\n\n\n")

# Update multiple details of an existing locker record

print("═" * 60)
print("UPDATING THE LOCKER DETAILS".center(60))
print("═" * 60)

print("\n")

print("BEFORE")
print("─" * 60)

for locker in lockers:
    if locker["id"] == "L06":
        print(f"Locker ID  :  {locker['id']}")
        print(f"Occupied   :  {locker['occupied']}")
        print(f"Mobile     :  {locker['mobile']}")
        print(f"Passcode   :  {locker['passcode']}")
        print(f"Time       :  {locker['time']} hours")
        print("─" * 60)

for locker in lockers:
    if locker["id"] == "L06":
        locker["mobile"] = "7766554433"
        locker["passcode"] = "Y1Z23"
        locker["time"] = 8
        break

print("\nAFTER")
print("─" * 60)

for locker in lockers:
    if locker["id"] == "L06":
        print(f"Locker ID  :  {locker['id']}")
        print(f"Occupied   :  {locker['occupied']}")
        print(f"Mobile     :  {locker['mobile']}")
        print(f"Passcode   :  {locker['passcode']}")
        print(f"Time       :  {locker['time']} hours")
        print("─" * 60)

print("\n\n\n")

# Change the passcode of a locker

print("═" * 60)
print("CHANGING THE PASSCODE".center(60))
print("═" * 60)

print("\n")

locker_id = "L04"

print("BEFORE")
print("─" * 60)

for locker in lockers:
    if locker["id"] == locker_id:
        print(f"Locker ID  :  {locker['id']}")
        print(f"Passcode   :  {locker['passcode']}")
        print("─" * 60)

new_passcode = "7STAR"

for locker in lockers:
    if locker["id"] == locker_id:
        locker["passcode"] = new_passcode
        break

print("\nAFTER")
print("─" * 60)

for locker in lockers:
    if locker["id"] == locker_id:
        print(f"Locker ID  :  {locker['id']}")
        print(f"Passcode   :  {locker['passcode']}")
        print("─" * 60)

print("\n\n\n")

# Update the customer's mobile number associated with a locker

print("═" * 60)
print("UPDATING THE MOBILE NUMBER".center(60))
print("═" * 60)

print("\n")

locker_id = "L01"

print("BEFORE")
print("─" * 60)

for locker in lockers:
    if locker["id"] == locker_id:
        print(f"Locker ID  :  {locker['id']}")
        print(f"Mobile     :  {locker['mobile']}")
        print("─" * 60)

new_mobile = "9753123466"

for locker in lockers:
    if locker["id"] == locker_id:
        locker["mobile"] = new_mobile
        break

print("\nAFTER")
print("─" * 60)

for locker in lockers:
    if locker["id"] == locker_id:
        print(f"Locker ID  :  {locker['id']}")
        print(f"Mobile     :  {locker['mobile']}")
        print("─" * 60)

print("\n\n\n")

#Display Customer Mobile Numbers of Occupied Lockers

print("═" * 60)
print("Occupied Locker Customer Mobile Numbers".center(60))
print("═" * 60)
print()


for locker in lockers:

    if locker["occupied"] == True:
        print(
            "Locker ID:",
            locker["id"],
            "| Mobile Number:",
            locker["mobile"]
        )

        found = True

    if found == False:
        print("No occupied lockers found.")