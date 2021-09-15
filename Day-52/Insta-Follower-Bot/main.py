from insta import Instagram
import os

path = "/Users/harshitkrvishwakarma/Devlopment/chromedriver"
email = os.environ.get("email")
password = os.environ.get("password")

insta = Instagram(webdriver_path=path, email=email, pass_=password)
insta.login()

# Searching a specific account with similiar content like mine and following the people who
# who follows that account
insta.search_accounts(account_username="python.hub")
insta.scroll_and_follow(scroll_limit=10)
print(insta.people_followed)

# unfollows every one I am following
insta.unfollow()

insta.close_window()