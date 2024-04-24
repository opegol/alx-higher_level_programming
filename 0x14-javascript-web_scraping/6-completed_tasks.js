#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const done = {};
    todos.forEach((todo) => {
      if (todo.completed && done[todo.userId] === undefined) {
        done[todo.userId] = 1;
      } else if (todo.completed) {
        done[todo.userId] += 1;
      }
    });
    console.log(done);
  }
});
