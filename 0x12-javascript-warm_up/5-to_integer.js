#!/usr/bin/node
const data = process.argv[2];
if (isNaN(data)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + data);
}
