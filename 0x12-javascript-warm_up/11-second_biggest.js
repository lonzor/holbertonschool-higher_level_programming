#!/usr/bin/node
const intList = process.argv;
if (intList.length <= 3) {
  console.log(0);
} else {
  console.log(intList.sort().reverse()[1]);
}
