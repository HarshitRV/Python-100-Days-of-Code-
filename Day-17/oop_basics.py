# class Car:
#     def __init__ (self,model,seats):
#         self.model = model
#         self.top_speed = 80
#         self.seats = seats


# maruti = Car("800",4)

# print(maruti.top_speed)

# maruti.top_speed = 110

# print(maruti.top_speed)

class User:
    def __init__(self,user_id,username):
        self.user_id = user_id
        self.usename = username
        self.follower = 0
        self.following = 0
    
    def follow(self,user):
        user.follower += 1
        self.following += 1

user_1 = User(1,"wolverine")
user_2 = User(2,"logan")

user_1.follow(user_2)

print(f"Following of {user_1.usename} = {user_1.following}")
print(f"Follower of {user_1.usename} = {user_1.follower}")
print(f"Following of {user_2.usename} = {user_2.following}")
print(f"Follower of {user_2.usename} = {user_2.follower}")


            