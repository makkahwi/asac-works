import React, { useEffect, useState } from 'react';
import { Row } from 'react-bootstrap';
import MoviesApi from "../../api/movies";
import Movie from "./movie";
import './style.css';

export default function MoviesList() {

  const [moviesList, setMoviesList] = useState([]);
  const [favs, setFavs] = useState(JSON.parse(localStorage.getItem("favs")) || []);

  useEffect(() => {
    MoviesApi.getAll()
      .then(res => {
        setMoviesList(res);
      })
      .catch(e => {
        setMoviesList([]);
        console.log(e)
      })
  }, [])

  const addToFavs = id => {
    const newFavs = [...favs, id]
    setFavs(newFavs);
    localStorage.setItem("favs", JSON.stringify(newFavs));
  };

  const removeFromFav = id => {
    const newFavs = favs.filter(movie => movie !== id);
    setFavs(newFavs);
    localStorage.setItem("favs", JSON.stringify(newFavs));
  };

  return (
    <>
      <section id="favMovies">
        <h1>
          Fav Movies
        </h1>

        <Row>
          {favs.length ? moviesList.filter(movie => favs.indexOf(movie.id) >= 0).map((movie, i) => {
            const { id } = movie;

            return (
              <Movie data={movie} fav={favs.indexOf(id) >= 0} addToFav={() => addToFavs(id)} removeFromFav={() => removeFromFav(id)} key={i} />
            )
          }
          ) : "No Fav Movies"}
        </Row>
      </section>

      <div style={{ height: "50vh" }} />

      <section id="allMovies">
        <h1>
          All Movies
        </h1>

        <Row>
          {moviesList.map((movie, i) => {
            const { id } = movie;

            return (
              <Movie data={movie} fav={favs.indexOf(id) >= 0} addToFav={() => addToFavs(id)} removeFromFav={() => removeFromFav(id)} key={i} all />
            )
          }
          )}
        </Row>
      </section>
    </>
  );
}
