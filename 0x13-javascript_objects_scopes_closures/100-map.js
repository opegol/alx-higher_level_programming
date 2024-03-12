#!/usr/bin/node

let ind = 0;
const list = require('./100-data.js').list;
const newList = list.map((i) => i * ind++);
console.log(list);
console.log(newList);
