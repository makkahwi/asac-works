const insertShiftArray = (arr, num) => {
  const middle = arr.length % 2 === 0 ? arr.length / 2 : parseInt(arr.length / 2) + 1;
  const newArr = [];

  let i = 0;

  while (i < arr.length) {
    (i === middle && newArr[newArr.length - 1] !== num) ? newArr.push(num) : newArr.push(arr[i++]);
  };

  return newArr;
};