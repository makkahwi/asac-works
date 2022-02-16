import React from 'react';
import Movie from "./movie";

export default function Listing({ list, favs, addToFavs, updateFav, removeFav, all }) {

  return (
    <>
      {list.map((movie, i) => {
        const { id } = movie;

        return (
          <Movie data={movie} fav={favs?.find(movi => movi.id === id)} addToFav={addToFavs} updateFav={updateFav} removeFav={removeFav} key={i} all={all} />
        )
      })}
    </>
  );
}
