function checkprime(n) {
  var max = Math.sqrt(n);
  for (var i = 2; i <= max; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

do {
  var random = Math.floor(Math.random() * 7000 + 1024);
  if (checkprime(random)) {
    var prime = random;
  }
} while (!checkprime(random));

function gcd(a, b) {
  if (a === 0) return b;
  return gcd(b % a, a);
}
var generators = [];
function creategenerate(n) {
  for (i = 1; i <= n; i++) {
    if (gcd(i, n) == 1) generators.push(i);
  }
}
console.log("Generated Prime Number :" + prime);
creategenerate(prime);
var generator = generators[Math.floor(Math.random() * 10)];
console.log("Generator of a prime number is " + generator);
var private_a = Math.floor(Math.random() * 8);
var private_b = Math.floor(Math.random() * 8);
console.log("--------------------------------");
console.log("private key of A =  " + private_a);
console.log("private key of B =  " + private_b);
console.log("--------------------------------");
var public_a = generator ** private_a % prime;
var public_b = generator ** private_b % prime;
console.log("public key of A =  " + public_a);
console.log("public key of B =  " + public_b);
console.log("--------------------------------");
//------------after exchange

var shared_a = public_b ** private_a % prime;
var shared_b = public_a ** private_b % prime;
console.log("Shared Secret key of A =  " + shared_a);
console.log("Shared Secret key of B =  " + shared_b);
console.log("--------------------------------");
console.log("exchange key authnticated");
