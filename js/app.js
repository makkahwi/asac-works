alert('Please bear with us to answer following questions first');

var name = prompt('Please input your name');
console.log(`Input name: ${name}`);

var gender = prompt('Please input your gender, you may copy n paste of the two answers (Male | Female)');
console.log(`Input gender: ${gender}`);

var age = prompt('Please input your age');
console.log(`Input age: ${age}`);

if (age <= 0) {
  alert(`Your input age is ${age}, which is <= 0`)
};

var welcome = prompt('Please select of you wanna see a welcoming message, Type Y for yes or N for No');
console.log(`Input welcome: ${welcome}`);

if (welcome === "Y" || welcome === "y") {
  alert(`Welcome ${gender === "Male" ? "Mr." : gender === "Female" ? "Ms." : ""} ${name} to our system. We like to have a ${age < 40 ? "fresh blood" : `wise ${gender === "Male" ? "gentlemen" : gender === "Female" ? "ladies" : ""}`} of ${age}-year-old visitors at our website`)
}