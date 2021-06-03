#!/usr/bin/node
exports.converter = function (base) {
  function itConverts(number) {
    return number.toString(base);
  }
  return itConverts;
}
