
#Airport API Data - Austin
# API endpoint URL
url = "https://aeroapi.flightaware.com/aeroapi/airports/KAUS/routes/KDFW"

# API Key
api_key = "x-apikey"

#Query parameters
query_params = {
    "max_pages": 1
}

# Send the API request
response = requests.get(url, headers={api_key: config.api_key}, params=query_params)

# Check if the API request was successful
if response.status_code == 200:
    #Get the data from the API response
    data = response.json()
    #Print the data
    print(data)
else:
    # Print the error message
    print("Error:", response.text)
    
    
    







passenger_count = {
    "model1": 70,
    "model2": 100,
    "model3": 40,
    "model4": 80,
    "model5": 60
}

plane_models = {}

for planes in austin_data_plane_test['aircraft_type']:
    if austin_data_plane_test['aircraft_type'] != plane_models[planes]:
        plane_models.append(planes['aircraft_type']).unique()



print(plane_models)
#dal_departures
dfw_departures

dal_df = pd.DataFrame(dfw_departures)

dal_df.head()







# Define the API endpoint and the parameters
api_endpoint = "https://api.census.gov/data/"
params = {
    "get": "NAME,B01001_001E",
    "for": "metropolitan%20statistical%20area/micropolitan%20statistical%20area:*"
}

# Define the two metro areas to retrieve data for
metro_areas = [
    "Austin*",
    "Dallas*"
]

# Initialize an empty list to store the data
data = []

# Loop over the years from 2000 to 2019
for year in range(2005, 2020):
    # Replace the year in the API endpoint
    year_endpoint = api_endpoint + str(year) + "/acs" + "/acs1" + "?get=NAME,B01001_001E&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:*"
    
    # Send the API request
    response = requests.get(year_endpoint)
    
    # Convert the response to a list of lists
    response_data = response.json()
    
    # Loop over the data for each metro area
    for metro_area in metro_areas:
        # Find the data for the metro area
        metro_data = [item for item in response_data if item[0] == metro_area]
        
        # If the data for the metro area was found, add it to the data list
        if metro_data:
            data.append([year, metro_area, metro_data[0][1]])

# Convert the data list to a pandas dataframe
df = pd.DataFrame(data, columns=["Year", "Metro Area", "Population"])