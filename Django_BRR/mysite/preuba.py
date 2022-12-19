from dotenv import dotenv_values

config = dotenv_values("Django_BRR\mysite\credentials.env")

print(config["USER_PASSWORD"])