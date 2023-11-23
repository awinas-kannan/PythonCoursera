from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_list = r.generate_users(10)
name = r.get_full_name()
print(name)
for user in some_list:
    print(user.get_full_name(), " ", user.get_email())

for user in some_list:
    print(user.get_picture())


def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        user_X = {"Name": user.get_full_name(), "Gender": user.get_gender(), "City": user.get_city(),
                  "State": user.get_state(), "Email": user.get_email(), "DOB": user.get_dob(),
                  "Picture": user.get_picture()}
        print(user_X)
        users.append(user_X)

    return pd.DataFrame(users)


df1 = get_users()
print(df1)
df1 = pd.DataFrame(get_users())
print(df1)
