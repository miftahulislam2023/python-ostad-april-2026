names = [
    {
    "first": "Miftahul",
    "last": "Islam"
    },
    {
    "first": "Ridita",
    "last": "Shaila"
    },
    {
    "first": "Tasin",
    "last": "Khan"
    },
    {
    "first": "Zuhan",
    "last": "Hasan"
    },
    {
    "first": "Shihab",
    "last": "Riyaz"
    },
    {
    "first": "Nayeem",
    "last": "Ahasan"
    },
    {
    "first": "Fahim",
    "last": "Alom"
    },
    {
    "first": "Rishat",
    "last": "Hasan"
    },
    {
    "first": "Roni",
    "last": "Ahsan"
    },
    {
    "first": "Shovon",
    "last": "Talukdar"
    }
]

full_names = list(map(lambda name: f"{name['first']} {name['last']}", names))
print(full_names)