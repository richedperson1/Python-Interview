

dist = {
    "FirstName": "Rutvik",
    "Last_name": "Jaiswal",
    "Coding Rank out of 5": 4.5,
    "Programmer": "Best"
}


dist = {f"{key}": f"{val}" for key, val in dist.items()}


# { (some_key if condition else default_key):(something_if_true if condition
#           else something_if_false) for key, value in dict_.items() }


dist2 = {(key if key == "FirstName" else "Patil"): (val)
         for key, val in dist.items()}

print(dist2)
