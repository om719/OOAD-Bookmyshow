import json

data={"admin_Om": {"username": "admin_Om", "password": "hello123", "email": "omomomshreenidhi@gmail.com"}}
# = open('movie_file.json')
#data=json.load(f)

# data["Avengers"]={"name":"Avengers","rating":"5","description":"After half of all life is snapped away by Thanos, the Avengers are left scattered and divided. Now with a way to reverse the damage, the Avengers and their allies must assemble once more and learn to put differences aside in order to work together and set things right. Along the way, the Avengers realize that sacrifices must be made as they prepare for the ultimate final showdown with Thanos, which will result in the heroes fighting the biggest battle they have ever faced."}


#{ "Black Panther": { "name": "Black Panther", "rating": "4", "description": "Follows T'Challa who, after the death of his father, the King who of Wakanda, returns home to the isolated, technologically advanced African nation to succeed to the throne and take his rightful place as king. But when a powerful old enemy reappears, T'Challa's mettle as king and Black Panther is tested when he is drawn into a formidable conflict that puts the fate of Wakanda and the entire world at risk. Faced with treachery and danger, the young king must rally his allies and release the full power of Black Panther to defeat his foes and secure the safety of his people and their way of life.", "image": "black_panther.png" }, "Avengers": { "name": "Avengers", "rating": "5", "description": "After half of all life is snapped away by Thanos, the Avengers are left scattered and divided. Now with a way to reverse the damage, the Avengers and their allies must assemble once more and learn to put differences aside in order to work together and set things right. Along the way, the Avengers realize that sacrifices must be made as they prepare for the ultimate final showdown with Thanos, which will result in the heroes fighting the biggest battle they have ever faced.", "image": "avengers.png" } }

#data= {"Om719" : []}
with open("admin_file.json", "w") as write_file:
    json.dump(data, write_file)