#!/usr/bin/node

exports.converter = function (base) {
  return (c) => c.toString(base);
};
