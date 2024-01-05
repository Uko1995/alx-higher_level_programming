#!/usr/bin/node
// get the status code of GET request

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  if (response.statusCode !== 200) {
    console.log('Failed to fetch data');
  }
  const movie = JSON.parse(body);
  console.log(`${movie.title}`); });
