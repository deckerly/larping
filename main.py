import requests
import webbrowser

# make it where it saves the data of the limited items and compares the growth between the items from the times you pick it
# this will save the date and time of when you recording your responses to conclude a result

base_url = "https://api.rolimons.com/"

user_settings = {
    "annoying popups": "False",
    "test": "False"
}

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
    response = input("\nDeckerly Awesome Roblox API Lookup!\n-------------\n'1' - Get User Details\n'2' - Get Limited Item Details\n'3' - Soon\n'q' - Quit\n\nResponse: ")
    
    if response == "1":
        user_details = get_user_details()
        if user_details:
            print(f"----------\nName: {user_details['name']}\nValue: {user_details['value']}\nRAP: {user_details['rap']}\nHas Premium: {user_details['premium']}\nTerminated: {user_details['terminated']}\nLast Location: {user_details['last_location']}")
   
    elif response == "2":
        item_details = get_item_details()
        try:
            is_projected = item_data['items'][item_id_input][8]
            if is_projected == 1:
                is_projected = "True"
            else:
                is_projected = "False"
            demand_value = item_data['items'][item_id_input][5]
            demand_thingy = demand_chart.get(demand_value, "Unknown")
            item_value = item_data['items'][item_id_input][3]
            item_value = demand_chart.get(item_value, "N/A")
            if item_details:
                print(f"----------\nItem Name: {item_data['items'][item_id_input][0]}\n"
                    f"Acronym: {item_data['items'][item_id_input][1]}\n"
                    f"RAP: {item_data['items'][item_id_input][2]}\n"
                    f"Value: {item_value}\n"
                    f"Demand: {demand_thingy}\n"
                    f"Is Projected: {is_projected}")
            if user_settings["annoying popups"] == "True":
                choice = input("\nWould you like to access the page for this item? (y/n): ").lower()
                if choice == "y":
                    webbrowser.open(f"https://www.roblox.com/catalog/{item_id_input}")
                elif choice == "n":
                    break
        except:
            print("Use a valid Limited Item ID")

    elif response == "3":
        print("---SETTINGS---\n")
        uhidk = 0
        for key, value in user_settings.items():
            uhidk += 1
            print(f"{uhidk}. {key}: {value}")
        choice = input("\n(b) - Back | Pick a Setting to Toggle: ")
        if choice == "b":
            break
        elif choice == "1" and user_settings["annoying popups"] == "False":
            user_settings["annoying popups"] = "True"
        elif choice == "1" and user_settings["annoying popups"] == "True":
            user_settings["annoying popups"] = "False"
        else:
            print("Not an Option!")
    elif response == "q":
        print("Bye!")
        exit()
    else:
        print("Invalid Response.")
