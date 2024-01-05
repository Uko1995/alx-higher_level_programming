#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from command line arguments
const characterId = '18'; // Character ID of Wedge Antilles

// Make a request to fetch films data
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  const films = JSON.parse(body).results;
  const moviesWithWedge = films.filter((film) =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  console.log(`${moviesWithWedge.length}`);
});
