const missingPersons = [
    { name: "Mohamed", age: 28, location: "Chennai" },
    { name: "Rahul Singh", age: 35, location: "Bangalore" },
    { name: "Suresh", age: 42, location: "Hyderabad" }
];

function searchPersonByName(name) {
    const result = missingPersons.find(
        person => person.name.toLowerCase() === name.toLowerCase()
    );

    if (result) {
        console.log("Match Found:");
        console.log(result);
    } else {
        console.log("No matching person found.");
    }
}

searchPersonByName("Mohamed");
