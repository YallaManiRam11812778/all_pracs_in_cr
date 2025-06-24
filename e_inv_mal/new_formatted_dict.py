states_dict = {
    0: "All States",
    1: "Johor",
    2: "Kedah",
    3: "Kelantan",
    4: "Melaka",
    5: "Negeri Sembilan",
    6: "Pahang",
    7: "Pulau Pinang",
    8: "Perak",
    9: "Perlis",
    10: "Selangor",
    11: "Terengganu",
    12: "Sabah",
    13: "Sarawak",
    14: "Wilayah Persekutuan Kuala Lumpur",
    15: "Wilayah Persekutuan Labuan",
    16: "Wilayah Persekutuan Putrajaya",
    17: "Not Applicable"
}
 
# Transform the dictionary
transformed_dict = [
    {"statecode": key, "state": value} for key, value in states_dict.items()
]
 
# Output the result
print(transformed_dict)