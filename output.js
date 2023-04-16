function greet(name) {
    console.log(`"Hello, "${name}"!"`);
}

let names = ["Gabriel", "Ana", "Fernanda", "Alice"];

for (let name of names) {
    greet(name);
}