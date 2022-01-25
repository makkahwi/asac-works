"use strict";

const tax = 7.5 / 100;

const netSalary = salary => {
  return salary - (salary * tax)
};

const salary = ({ max, min }) => {
  return Math.floor(Math.random() * (max - min)) + min;
};

const limits = level => {
  switch (level) {
    case "Senior": return salary({ max: 2000, min: 1500 });
    case "Mid-Senior": return salary({ max: 1500, min: 1000 });
    case "Junior": return salary({ max: 1000, min: 500 });
    default: return salary({ max: 0, min: 0 });
  }
};

function Employee([id, n, d, l, i]) {
  this.id = id;
  this.name = n;
  this.department = d;
  this.level = l;
  this.salary = netSalary(limits(l));
};

const employees = [
  [1000, "Ghazi Samer", "Administration", "Senior"],
  [1001, "Lana Ali", "Finance", "Senior"],
  [1002, "Tamara Ayoub", "Marketing", "Senior"],
  [1003, "Safi Walid", "Administration", "Mid-Senior"],
  [1004, "Omar Zaid", "Development", "Senior"],
  [1005, "Rana Saleh", "Development", "Junior"],
  [1006, "Hadi Ahmad", "Finance", "Mid-Senior"]
];

const employeesList = () => {
  const mytable = document.getElementById("employeeTable");
  employees.forEach(employee => {
    let newRow = document.createElement("tr");
    Object.values(new Employee(employee)).forEach((value) => {
      let cell = document.createElement("td");
      cell.innerText = value;
      newRow.appendChild(cell);
    })
    mytable.appendChild(newRow);
  });
}

const employeeId = () => Math.floor(Math.random() * (9999 - 1000)) + 1000

employeesList();