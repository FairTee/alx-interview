#!/usr/bin/node

const request = require('request-promise');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

async function fetchCharacterNames () {
  try {
    const filmData = await request({ uri: apiUrl, json: true });
    const characterUrls = filmData.characters;

    // Fetch all character details in order
    const characterPromises = characterUrls.map(url => request({ uri: url, json: true }));
    const characters = await Promise.all(characterPromises);

    // Print character names in the same order as the list
    characters.forEach(character => {
      console.log(character.name);
    });
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchCharacterNames();
