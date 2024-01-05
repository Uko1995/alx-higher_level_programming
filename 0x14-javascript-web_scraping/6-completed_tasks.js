#!/usr/bin/node

const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const tasks = JSON.parse(body);

  const completedTasks = tasks.filter(task => task.completed === true);
  const results = completedTasks.reduce((acc, task) => {
    const userId = task.userId;
    if (acc[userId]) {
      acc[userId]++;
    } else {
      acc[userId] = 1;
    }
    return acc;
  }, {});

  console.log(results);
});
