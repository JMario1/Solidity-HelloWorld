import json
from brownie import accounts, HelloWorld

def get_abi():
    with open("./build/contracts/HelloWorld.json", "r") as file:
        file1 = json.load(file)
        with open("./abi", "w") as file2:
            json.dump(file1["abi"], file2)
        with open("./bin", "w") as file3:
            json.dump(file1["bytecode"], file3)    
            json.dump(file1["deployedBytecode"], file3) 

def deploy_hello_world():
    account = accounts.load("rinkeby1")
    hello_world = HelloWorld.deploy("Jude", {"from": account})
    greeting = hello_world.Greeting()
    print(greeting)
    nameChanged = hello_world.setName("Ben", {"from": account})
    print(hello_world.Greeting())

def main():
    get_abi()
    deploy_hello_world()
