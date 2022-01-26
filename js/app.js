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
  this.image = i;
};

let employees = [
  [1000, "Ghazi Samer", "Administration", "Senior"],
  [1001, "Lana Ali", "Finance", "Senior"],
  [1002, "Tamara Ayoub", "Marketing", "Senior"],
  [1003, "Safi Walid", "Administration", "Mid-Senior"],
  [1004, "Omar Zaid", "Development", "Senior"],
  [1005, "Rana Saleh", "Development", "Junior"],
  [1006, "Hadi Ahmad", "Finance", "Mid-Senior"]
];

const employeesListing = () => {
  const employeeTable = document.getElementById("employeeTable");
  employeeTable.innerHTML = "";

  employees.forEach(employee => {
    let newRow = document.createElement("tr");

    Object.keys(new Employee(employee)).forEach(key => {
      let cell = document.createElement("td");
      let link = document.createElement("a");

      if (key === "image") {
        if (new Employee(employee)[key]) {
          link.href = new Employee(employee)[key];
          link.target = "_blank";
          link.innerText = "Img Link";
          cell.appendChild(link);
        }
        else {
          cell.innerText = "No Img";
        }
      }
      else {
        cell.innerText = new Employee(employee)[key];
      }

      newRow.appendChild(cell);
    })
    employeeTable.appendChild(newRow);
  });
};

const employeeId = () => Math.floor(Math.random() * (9999 - 1000)) + 1000;

const employeesGriding = () => {
  const employeesGrid = document.getElementById("employeesGrid");
  employeesGrid.innerHTML = "";

  employees.forEach(employee => {
    const employ = new Employee(employee);

    let p = document.createElement("p");
    p.className = "card-text text-light";

    Object.keys(employ).forEach(key => {
      if (key !== 'image') {
        let span = document.createElement("span");
        let br = document.createElement("br");
        span.innerText = `${key.charAt(0).toUpperCase() + key.slice(1)}: ${employ[key]}`;
        p.appendChild(span)
        p.appendChild(br)
      }
    });

    let div3 = document.createElement("div");
    div3.className = "card-body";

    div3.appendChild(p);

    let img = document.createElement("img");
    img.className = "p-2";
    img.src = employ.image || `img/${employ.name}.jpg`;

    let div2 = document.createElement("div");
    div2.className = "card shadow-sm bg-success";

    div2.appendChild(img);
    div2.appendChild(div3);

    let div1 = document.createElement("div");
    div1.className = "col my-4";

    div1.appendChild(div2);

    employeesGrid.appendChild(div1);
  });
};

let addEmployeeForm = document.getElementById("addEmployeeForm");

const addEmployee = e => {
  e.preventDefault();
  const { name, department, level, img } = e.target;
  employees.push([employeeId(), name.value, department.value, level.value, img.value]);
  employeesGriding();
  employeesListing();
  addEmployeeForm.reset();
};

addEmployeeForm.addEventListener('submit', addEmployee);

employeesListing();
employeesGriding();