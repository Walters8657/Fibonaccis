function fib(n) {
    f1 = 0, f2 = 1;

    if(n < 1) {
        return;
    }

    console.log(f1);
    
    for (var i = 1; i < n; i++) {
        console.log(f2);
        next = f1 + f2;
        f1 = f2;
        f2 = next;
    }
}

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("How many numbers do you want? ", function(name) {
    num = parseInt(name);
    fib(num);
    rl.close();
});

rl.on("close", function() {
    process.exit(0);
});
