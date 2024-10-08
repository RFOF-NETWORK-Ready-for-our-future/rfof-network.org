const hre = require("hardhat");

async function main() {
    const Whitelist = await hre.ethers.getContractFactory("Whitelist");
    const whitelist = await Whitelist.deploy();

    await whitelist.deployed();
    console.log("Whitelist Contract deployed to:", whitelist.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
