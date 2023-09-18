class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following += 1


# type pass to skip class/function code
# you can create new attributes for an object just by using dot notation !!!
user1 = User('001', 'eljesa')
user2 = User('001', 'emelida')
print(user1.name)

user1.follow(user2)
print(user1.following)
print(user2.followers)