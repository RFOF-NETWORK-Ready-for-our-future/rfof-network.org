pragma solidity ^0.8.0;

contract Whitelist {
    mapping(address => bool) public whitelistedAddresses;
    address public owner;

    event AddressAdded(address indexed _address);
    event AddressRemoved(address indexed _address);

    constructor() {
        owner = msg.sender; // Der Ersteller des Vertrags ist der Besitzer
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Nicht autorisiert");
        _;
    }

    // Funktion zum Hinzufügen einer Adresse zur Whitelist
    function addAddressToWhitelist(address _address) public onlyOwner {
        require(!whitelistedAddresses[_address], "Adresse ist bereits auf der Whitelist");
        whitelistedAddresses[_address] = true;
        emit AddressAdded(_address);
    }

    // Funktion zum Entfernen einer Adresse von der Whitelist
    function removeAddressFromWhitelist(address _address) public onlyOwner {
        require(whitelistedAddresses[_address], "Adresse ist nicht auf der Whitelist");
        whitelistedAddresses[_address] = false;
        emit AddressRemoved(_address);
    }

    // Beispieltransaktionsfunktion, die die Whitelist überprüft
    function transact() public {
        require(whitelistedAddresses[msg.sender], "Nicht autorisierte Adresse");
        // Transaktionslogik hier
    }
}
