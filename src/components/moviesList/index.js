import React, { useEffect, useState } from 'react';
import { Row, Container, Col, Spinner } from 'react-bootstrap';
import MoviesApi from "../../api/movies";
import Movie from "./movie";

export default function MoviesList() {

  const [moviesList, setMoviesList] = useState([]);
  const [loading, setLoading] = useState(false);
  const [favs, setFavs] = useState(JSON.parse(localStorage.getItem("favs")) || []);

  useEffect(() => {
    setLoading(true);

    MoviesApi.getAll()
      .then(res => {
        setMoviesList(res);
      })
      .catch(e => {
        setMoviesList([]);
        console.log(e)
      })
      .finally(() => {
        setLoading(false);
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
      <Container id="favMovies" className="w-100 justify-content-md-center my-5">
        <h1 className='py-5 my-5'>
          Fav Movies
        </h1>

        <Row>
          {loading ? (
            <Col className="text-center" xs="12">
              <Spinner animation="border" variant="dark" />
            </Col>
          ) : (
            favs.length ? moviesList.filter(movie => favs.indexOf(movie.id) >= 0).map((movie, i) => {
              const { id } = movie;

              return (
                <Movie data={movie} fav={favs.indexOf(id) >= 0} addToFav={() => addToFavs(id)} removeFromFav={() => removeFromFav(id)} key={i} />
              )
            }) : <Col className="text-center pb-5 mb-5">{"No Fav Movies"}</Col>
          )}
        </Row>
      </Container>

      <Container id="allMovies" className="w-100 justify-content-md-center my-5">
        <h1 className='py-5 my-5'>
          All Movies
        </h1>

        <Row>
          {loading ? (
            <Col className="text-center" xs="12">
              <Spinner animation="border" variant="dark" />
            </Col>
          ) : (
            moviesList.length ? moviesList.map((movie, i) => {
              const { id } = movie;

              return (
                <Movie data={movie} fav={favs.indexOf(id) >= 0} addToFav={() => addToFavs(id)} removeFromFav={() => removeFromFav(id)} key={i} all />
              )
            }) : <Col className="text-center pb-5 mb-5">{"No Movies Retrieved"}</Col>
          )}
        </Row>
      </Container>
    </>
  );
}
