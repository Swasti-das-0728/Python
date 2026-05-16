# Sample material data (similar to MARA table)

mara = [
    {
        "MATNR": "1001",
        "ERSDA": "2024-01-10",
        "ERNAM": "ADMIN",
        "LAEDA": "2024-05-12",
        "AENAM": "USER1",
        "VPSTA": "K",
        "PSTAT": "A"
    },

    {
        "MATNR": "1002",
        "ERSDA": "2024-02-15",
        "ERNAM": "SAPUSER",
        "LAEDA": "2024-06-20",
        "AENAM": "USER2",
        "VPSTA": "L",
        "PSTAT": "B"
    }
]

# Looping through records and displaying data

for ls_mara in mara:
    print(
        ls_mara["MATNR"],
        ls_mara["ERSDA"],
        ls_mara["ERNAM"],
        ls_mara["LAEDA"],
        ls_mara["AENAM"],
        ls_mara["VPSTA"],
        ls_mara["PSTAT"]
    )