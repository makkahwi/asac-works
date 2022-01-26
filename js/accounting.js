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

const departments = ["Administration", "Marketing", "Development", "Finance"];
const tableheader = ["#", "ID", "name", "Level", "Salary"];

const tablesContainer = document.getElementById("employeesListByDepartment");

const newTableGen = () => {
  let tableEl = document.createElement("table")
  tableEl.className = "table my-4 py-4";

  return tableEl;
};

const newTableHeaderGen = (table, department) => {
  let tableHeadEL = document.createElement("thead");
  let tableTitleRowEL = document.createElement("tr");
  let tableTitleHeadCellEL = document.createElement("th");

  tableTitleHeadCellEL.colSpan = tableheader.length;
  tableTitleHeadCellEL.innerText = `${department} Department`;
  tableTitleRowEL.appendChild(tableTitleHeadCellEL);
  tableHeadEL.appendChild(tableTitleRowEL);

  let tableRowEL = document.createElement("tr");

  tableheader.forEach(header => {
    let tableHeadCellEL = document.createElement("th");

    tableHeadCellEL.innerText = header;
    tableRowEL.appendChild(tableHeadCellEL);
  });

  tableHeadEL.appendChild(tableRowEL);
  table.appendChild(tableHeadEL);
};

let employees = JSON.parse(localStorage.getItem("data")).map(employee => new Employee(employee));

departments.forEach(department => {
  let newTable = newTableGen();
  newTableHeaderGen(newTable, department);

  let tableBodyEL = document.createElement("tbody");
  let tableFootEL = document.createElement("tfoot");
  let tableRowEL = document.createElement("tr");

  const departmentEmployees = employees.filter(employee => employee.department === department);

  departmentEmployees.forEach((employee, i) => {
    let newRow = document.createElement("tr");
    let nocell = document.createElement("td");
    nocell.innerText = i + 1;
    newRow.appendChild(nocell);

    Object.keys(employee).filter(key => key !== "image" && key !== "department").forEach(key => {
      let cell = document.createElement("td");
      cell.innerText = employee[key];

      newRow.appendChild(cell);
    })
    tableBodyEL.appendChild(newRow);
  });

  newTable.appendChild(tableBodyEL);

  const departmentEmployeeSalaries = departmentEmployees.map(employee => employee.salary).reduce((a, b) => a + b);

  const statistics = {
    Number_Of_Employees: departmentEmployees.length,
    Average_Employee_Salary: (departmentEmployeeSalaries / departmentEmployees.length).toFixed(2),
    Total_Salaries: departmentEmployeeSalaries.toFixed(2)
  };

  Object.keys(statistics).forEach(key => {
    let tableCellEL = document.createElement("td");
    tableCellEL.innerHTML = `${key.replaceAll("_", " ")}: ${statistics[key]}`;
    tableFootEL.appendChild(tableCellEL);
  });

  newTable.appendChild(tableFootEL);

  tablesContainer.appendChild(newTable);
});