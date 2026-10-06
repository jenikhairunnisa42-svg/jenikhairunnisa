#menggunakan {}
profile = { 
    "id": 2, 
    "name": "john wick", 
    "hobbies": ["playing with pencil"], 
    "is_female":False,
}

#menggunakan fungsi dict() dengan argumen key_value
profile = dict( 
    identifier="set", 
    name="john wick",
    hobbies=["playing with pencil"], 
    is_female=False,
)

#menggunakan fungsi dist() dengan isi list tuple
profile = dict([ 
    ('identifier', "set"), 
    ('name', "john wick"),
    ('hobbies', ["playing with pencil"]), 
    ('is_female', False)
])

#Sedangkan untuk membuat dictionary tanpa item atau kosong, bisa cukup menggunakan dict() atau {} :
profile = dict() 
print(profile) # output ➜ {} profile = {} 
print(profile) # output ➜ {} profile = {} 