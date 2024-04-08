usernames = ["user1", "user2", "user3"]
passwords = ("pass1", "pass2", "pass3")
login_date = ["1/1/2021", "1/1/2022", "1/1/2023"]

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)
