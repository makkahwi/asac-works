const reverseArray = arr => {
  const revArr = [];

  for (let i = arr.length - 1; i >= 0; i--) {
    revArr.push(arr[i])
  };

  return revArr;
};