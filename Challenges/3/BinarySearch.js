const BinarySearch = (arr, key) => {
  let answer = -1;
  let middle = arr.length % 2 === 0 ? arr.length / 2 : parseInt(arr.length / 2) + 1;
  let newArr = [...arr];

  while (newArr.length > 2) {
    newArr = newArr[middle] > key ? newArr.slice(0, middle) : newArr[middle] < key ? newArr.slice(middle + 1, newArr.length) : newArr[middle] === key ? newArr = [key] : "";
    middle = parseInt(arr.length / 2);
  };

  return answer;
};

BinarySearch([4, 8, 15, 16, 23, 42], 15)