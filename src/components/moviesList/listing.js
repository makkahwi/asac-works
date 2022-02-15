import React from 'react';
import Movie from "./movie";

export default function Listing({ list, favs, comments, addToFavs, removeFromFav, addComment, all }) {

  return (
    <>
      {list.map((movie, i) => {
        const { id } = movie;

        return (
          <Movie data={movie} fav={favs.indexOf(id) >= 0} addToFav={() => addToFavs(id)} removeFromFav={() => removeFromFav(id)} key={i} addComment={addComment} all={all} comments={comments[id]} />
        )
      })}
    </>
  );
}
