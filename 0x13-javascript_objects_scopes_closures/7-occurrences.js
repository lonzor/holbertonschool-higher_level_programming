#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  const l = list.length;
  for (let i = 0; i < l; i++) {
    if (list[i] === searchElement) {
      occur = occur + 1;
    }
  }
  return occur;
};
