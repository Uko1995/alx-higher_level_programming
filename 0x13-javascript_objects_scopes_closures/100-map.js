#!/usr/bin/node

const list = require('./100-data').list;

const mapped = list.map((i, index) => (i * index));

console.log(list);
console.log(mapped);
