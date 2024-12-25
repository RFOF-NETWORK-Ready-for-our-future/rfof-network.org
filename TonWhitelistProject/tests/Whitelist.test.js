const { expect } = require("chai");

describe("Whitelist Contract", function () {
    let Whitelist;
    let whitelist;
    let owner;
    let addr1;

    beforeEach(async function () {
        Whitelist = await ethers.getContractFactory("Whitelist");
        [owner, addr1] = await ethers.getSigners();
        whitelist = await Whitelist.deploy();
    });

    it("Should add an address to the whitelist", async function () {
        await whitelist.addAddressToWhitelist(addr1.address);
        expect(await whitelist.whitelistedAddresses(addr1.address)).to.equal(true);
    });

    it("Should remove an address from the whitelist", async function () {
        await whitelist.addAddressToWhitelist(addr1.address);
        await whitelist.removeAddressFromWhitelist(addr1.address);
        expect(await whitelist.whitelistedAddresses(addr1.address)).to.equal(false);
    });

    it("Should revert if a non-whitelisted address tries to transact", async function () {
        await expect(whitelist.connect(addr1).transact()).to.be.revertedWith("Nicht autorisierte Adresse");
    });
});
