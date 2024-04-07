#Day17 of learning Creating of our OWN classes

class User:
    '''this is way of creating constructor, constructor is used to initialize the attributes'''
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers+=1
        self.following+=1
    
user1 = User('001','darshil')
user2 = User('002','jenil')
# print(user1.id)
# print(user1.username)
# print(user1.followers)
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)