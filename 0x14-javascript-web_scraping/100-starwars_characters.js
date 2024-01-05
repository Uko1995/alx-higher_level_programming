#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const movie = JSON.parse(body).characters;
  for (const character of movie) {
    request.get(character, (err, res, bd) => {
      if (err) {
        console.error(err);
      }
      const chars = JSON.parse(bd);
      console.log(chars.name);
    });
  }
});
