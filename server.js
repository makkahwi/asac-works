const express = require('express');
const cors = require('cors');
const axios = require('axios');
let package = require("./package.json");
const { Client } = require('pg');
require('dotenv').config();

const database = process.env.CONNECTION_STRING;

const client = new Client(database);

const server = express();

const port = process.env.PORT || 5050;
const baseURL = "https://api.themoviedb.org/3/"
const APIKey = process.env.API_KEY || "d2bf91e013a81d214c0b1ffc0a698119"

const data = require("./assets/data/data.json");
const endpoints = ["/", "/favorite", "/trending", "/search", "/changes", "/certification", "/addMovie", "/getMovies", "/getMovie/id", "/update/id", "/delete/id"];

server.use(cors());


// Constructors ////////////////////////////////////////////////////////
function Movie({ title, poster_path, overview }) {
  this.title = title;
  this.poster_path = poster_path;
  this.overview = overview;
};

function TMDBMovie({ id, title, release_date, poster_path, overview }) {
  this.id = id;
  this.title = title;
  this.release_date = release_date;
  this.poster_path = poster_path;
  this.overview = overview;
};


// Internal Routes ////////////////////////////////////////////////////////
server.get('/', (req, res) => res.status(200).send(new Movie(data)));

server.get('/favorite', (req, res) => res.status(200).send("Welcome to Favorite Page"));


// TMDB Routes ////////////////////////////////////////////////////////
server.get('/trending', (req, res) => {
  axios.get(`${baseURL}trending/all/week?api_key=${APIKey}&language=en-US`, null)
    .then(data => {
      console.log("Successfully Called Trending Endpoint :)")
      res.status(200).json(data.data.results.map(movie => new TMDBMovie(movie)))
    })
    .catch(e => {
      console.log(`Trending Endpoint Error :( | TMBD says: ${e.response.statusText}`)
      res.status(e.response.status).send(`TMBD says: ${e.response.statusText}`)
    })
});

server.get('/search', (req, res) => {
  axios.get(`${baseURL}search/movie?api_key=${APIKey}&language=en-US&query=${req.query || "spider-man"}`, null)
    .then(data => {
      console.log("Successfully Called Search Endpoint :)")
      res.status(200).json(data.data.results.map(movie => new TMDBMovie(movie)))
    })
    .catch(e => {
      console.log(`Search Endpoint Error :( | TMBD says: ${e.response.statusText}`)
      res.status(e.response.status).send(`TMBD says: ${e.response.statusText}`)
    })
});

server.get('/changes', (req, res) => {
  axios.get(`${baseURL}movie/changes`, null)
    .then(data => {
      console.log("Successfully Called Changes Endpoint :)")
      res.status(200).json(data.data.results.map(movie => new TMDBMovie(movie)))
    })
    .catch(e => {
      console.log(`Changes Endpoint Error :( | TMBD says: ${e.response.statusText}`)
      res.status(e.response.status).send(`TMBD says: ${e.response.statusText}`)
    })
});

server.get('/certification', (req, res) => {
  axios.get(`${baseURL}certification/movie/list`, null)
    .then(data => {
      console.log("Successfully Called Certifications Endpoint :)")
      res.status(200).json(data.data.results.map(movie => new TMDBMovie(movie)))
    })
    .catch(e => {
      console.log(`Certifications Endpoint Error :( | TMBD says: ${e.response.statusText}`)
      res.status(e.response.status).send(`TMBD says: ${e.response.statusText}`)
    })
});


// PG Routes
server.post('/addMovie', (req, res) => {
  client.query(`INSERT INTO movies(${Object.keys(req.query)}) VALUES (${Object.values(req.query)}) RETURNING *`, Object.values(req.query))
    .then(data => {
      res.status(200).json(data || "Movie Was Added, Congrats")
    }).catch(e => {
      res.status(e.response.status).send(`Database says: ${e.response.statusText}`)
    });
});

server.get('/getMovies', (req, res) => {
  client.query(`SELECT ${req.query || "*"} FROM movies;`, null)
    .then(data => {
      res.status(200).json(data || "No movies were found")
    }).catch(e => {
      res.status(e.response.status).send(`Database says: ${e.response.statusText}`)
    });
});

server.get('/getMovie/:id', (req, res) => {
  client.query(`SELECT * FROM movies WHERE id=${req.params.id} ;`, null)
    .then(data => {
      res.status(200).json(data || "No movie was found")
    }).catch(e => {
      res.status(e.response.status).send(`Database says: ${e.response.statusText}`)
    });
});

server.put('/update/:id', (req, res) => {
  client.query(`UPDATE movies SET (${Object.keys(req.body).map(key => `${key} = ${req.body[key]}`)}) WHERE id=${req.params.id} RETURNING *;`, req.body)
    .then(data => {
      res.status(200).json(`Movie ${req.body.title} was updated successfully`)
    }).catch(e => {
      res.status(e.response.status).send(`Database says: ${e.response.statusText}`)
    });
});

server.delete('/delete/:id', (req, res) => {
  client.query(`DELETE FROM movies WHERE id=${req.params.id} RETURNING *;`, req.params)
    .then(data => {
      res.status(200).json(`Movie ${req.body.title} was deleted successfully`)
    }).catch(e => {
      res.status(e.response.status).send(`Database says: ${e.response.statusText}`)
    });
});


// Error Routes ////////////////////////////////////////////////////////
server.use((err, req, res) =>
  res.status(500).send({
    "status": 500,
    "responseText": "Sorry, something went wrong within the local server"
  })
);

server.get('*', (req, res) => res.status(404).send("Requested page isn't found"));


// Listener ////////////////////////////////////////////////////////
client.connect()
  .then(() =>
    server.listen(port, () => {
      console.log(`Hello World War III, this is ${package.author}`)
      console.log(`Listining to server on port ${port}. Here is the list of available endpoints to use...`)
      endpoints.forEach(ep => console.log(`- ${ep}`))
    }));