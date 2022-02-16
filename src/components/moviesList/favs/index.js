import React, { useEffect, useState } from 'react';
import { Col, Container, Row, Spinner } from 'react-bootstrap';
import MoviesApi from "../../../api/tmdbData";
import Listing from "../listing";

export default function MoviesList() {

  const [moviesList, setMoviesList] = useState([]);
  const [loading, setLoading] = useState(false);
  const [favsList, setFavsList] = useState([]);

  const getFavs = () => {
    setLoading(true);

    MoviesApi.getFavs()
      .then(res => {
        setFavsList(res);
      })
      .catch(e => {
        console.log("Get Favs Error", e)
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    setLoading(true);

    MoviesApi.getAll()
      .then(res => {
        setMoviesList(res);
        getFavs();
      })
      .catch(e => {
        console.log("Get All Error", e)
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  const addToFavs = data => {
    setLoading(true);

    MoviesApi.createFav(data)
      .then(res => {
        getFavs();
      })
      .catch(e => {
        console.log("Create Favs Error", e)
      })
      .finally(() => {
        setLoading(false);
      });
  };

  const updateFav = data => {
    setLoading(true);

    MoviesApi.updateFav(data.id, data)
      .then(res => {
        getFavs();
      })
      .catch(e => {
        console.log("Update Favs Error", e)
      })
      .finally(() => {
        setLoading(false);
      });
  };

  const removeFav = id => {
    setLoading(true);

    MoviesApi.removeFav(id)
      .then(res => {
        getFavs();
      })
      .catch(e => {
        console.log("Delete Favs Error", e)
      })
      .finally(() => {
        setLoading(false);
      });
  };

  return (
    <Container id="favMovies" className="min-vh-100 w-100 justify-content-md-center my-5">
      <h1 className='py-5 my-5'>
        Fav Movies
      </h1>

      <Row>
        {loading ? (
          <Col className="text-center" xs="12">
            <Spinner animation="border" variant="dark" />
          </Col>
        ) : (
          favsList?.length ? (
            <Listing
              list={moviesList.filter(movie => favsList.indexOf(movie.id) >= 0)}
              favs={favsList}
              addToFavs={addToFavs}
              updateFav={updateFav}
              removeFav={removeFav}
            />
          ) : <Col className="text-center pb-5 mb-5">{"No Fav Movies"}</Col>
        )}
      </Row>
    </Container>
  );
}
