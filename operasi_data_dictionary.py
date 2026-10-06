# pengaksesan item
profile = { 
    "id": 2, 
    "name": "mario", 
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"), 
    "is_female": False, 
    } 
print("id:", profile["id"]) 
# output ➜ id: 2 
print("name:", profile.get("name")) 
# output ➜ name: mario

# mengubah isi dictionary
profile = { 
    "id": 2, 
    "name": "mario", 
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"), 
    "is_female": False, 
} 
print("name:", profile["name"])

# menambah item dictionary
profile = { 
    "name": "mario",
} 
print("len:", len(profile), "data:", profile) 
# output ➜ len: 1 data: {'name': 'mario'} 
 
profile["favourite_color"] = "red" 
print("len:", len(profile), "data:", profile) 
# output ➜ len: 2 data: {'name': 'mario', 'favourite_color': 'red'}

#Selain cara tersebut, bisa juga dengan menggunakan method update() . Tulis key dan value baru yang ingin ditambahkan sebagai argument method update() dalam bentuk dictionary.
profile.update({"race": "italian"}) 
print("len:", len(profile), "data:", profile) 
# output ➜ len: 3 data: {'name': 'mario', 'favourite_color': 'red', 'race': 'italian'}


# menghapus item dictonary dengan method pop ()
profile = {
    "id" : 2,
}
# menghapus item dictonary dengan keyword del
del profile["id"]
print[profile]