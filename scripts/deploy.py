import json
from brownie import accounts, HelloWorld


def deploy_hello_world():
    account = accounts.load("rinkeby1")
    hello_world = HelloWorld.deploy("Jude", {"from": account})
    greeting = hello_world.Greeting()
    print(greeting)
    nameChanged = hello_world.setName("Ben", {"from": account})
    print(hello_world.Greeting())

def main():
    deploy_hello_world()
