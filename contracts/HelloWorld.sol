// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

contract HelloWorld {
    string personName;

    constructor(string memory name){
        personName = name;
    }

    function setName(string memory name) public {
        personName = name;
    }

    function Greeting() public view returns(string memory){
        return string(abi.encodePacked("Hello ", personName));
    }
}