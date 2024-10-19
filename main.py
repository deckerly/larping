#testing rolimons api!!1111

import requests
base_url = "https://api.rolimons.com/"

demand_chart = {
    -1: "N/A",
    0: "Terrible",
    1: "Low",
    2: "Normal",
    3: "High",
    4: "Amazing!"
}

def get_user_details():
    while True:
        user_id_input = input("Enter a valid roblox userID: ")
        url = f"{base_url}/players/v1/playerinfo/{user_id_input}"
        response = requests.get(url)

        if response.status_code == 200:
            user_data = response.json()
            return user_data
        else:
            print(f"Failed to obtain data\nREASON: {response.status_code}")

def get_item_details():
    global item_id_input, item_data, item_details
    while True:
        try:
            url = f"{base_url}/items/v1/itemdetails"
            response = requests.get(url)
            item_id_input = input("Enter a valid roblox itemID: ")

            if response.status_code == 200:
                item_data = response.json()
                return item_data
            else:
                print(f"Failed to obtain data\nREASON: {response.status_code}")
        except:
            print("\nInvalid Limited Item ID (ex. https://www.roblox.com/catalog/---(1073690)---/JJ5x5s-White-Top-Hat)")

while True:
    response = input("\nDeckerly Awesome Roblox API Lookup!\n-------------\n'1' - Get User Details\n'2' - Get Limited Item Details\n'3' - Soon\n'q' - Quit\n\n Response: ")
    
    if response == "1":
        user_details = get_user_details()
        if user_details:
            print(f"----------\nName: {user_details['name']}\nValue: {user_details['value']}\nRAP: {user_details['rap']}\nHas Premium: {user_details['premium']}\nTerminated: {user_details['terminated']}\nLast Location: {user_details['last_location']}")
   
    elif response == "2":
        item_details = get_item_details()
        try:
            demand_value = item_data['items'][item_id_input][5]
            demand_thingy = demand_chart.get(demand_value, "Unknown")
            if item_details:
                print(f"----------\nItem Name: {item_data['items'][item_id_input][0]}\n"
                    f"Acronym: {item_data['items'][item_id_input][1]}\n"
                    f"RAP: {item_data['items'][item_id_input][2]}\n"
                    f"Value: {item_data['items'][item_id_input][3]}\n"
                    f"Demand: {demand_thingy}")
        except:
            print("Use a valid Limited Item ID")
    elif response == "q":
        print("Bye!")
        exit()
    else:
        print("Invalid Response.")
