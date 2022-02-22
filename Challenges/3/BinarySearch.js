const BinarySearch = (arr, key) => {
  let answer = -1;
  let middle = arr.length % 2 === 0 ? arr.length / 2 : parseInt(arr.length / 2) + 1;
  let start = 0;
  let end = arr.length - 1;

  while (end - start > 2) {

    if (arr[middle] === key) {
      answer = middle;
      break;
    };

    if (arr[middle] > key) {
      end = parseInt(middle);
      middle = parseInt(middle / 2) % 2 === 0 ? parseInt(middle / 2) : parseInt(middle / 2) + 1;
    }
    else {
      start = parseInt(middle);
      middle = parseInt(middle * 1.5) % 2 === 0 ? parseInt(middle * 1.5) : parseInt(middle * 1.5) + 1;
    };
  };

  return answer;
};