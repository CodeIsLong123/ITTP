

beatles_container1 = [
    ("Paul McCartney", "bass guitar"),
    ("John Lennon", "rhythm guitar"),
    ("George Harrison", "lead guitar"),
    ("Ringo Starr", "drums")
]

beatles_container2 = {name: instrument for name, instrument in beatles_container1}



def beatle_lookup(name):
    if name not in beatles_container2: 
        return f"ERROR. Name '{name}' not found. Available names: {beatles_container2.keys()}"
    else:
        return beatles_container2[name]
    
    
    
print(beatle_lookup("mick Jagger"))



