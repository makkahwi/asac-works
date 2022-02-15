import React, { useState } from 'react';
import './style.css';
import star from "../../../assets/images/icons/star.png"
import Modal from "../../modal"

export default function Movie({ data, fav, addToFav, removeFromFav, all }) {
  const { title, poster_path, overview } = data;

  const [modal, setModal] = useState(false);

  return (
    <div className="movie">
      <div>
        <img src={poster_path ? `https://image.tmdb.org/t/p/original/${poster_path}` : "https://executionconsulting.com/wp-content/uploads/2016/05/ef3-placeholder-image.jpg"} alt="" className='image' />
      </div>

      <h4 className='name'>
        {(all && fav) && <img src={star} alt="" width={"15px"} />}
        {(all && fav) && ' '}
        {title || "No Title"}
      </h4>

      <p className='desc'>
        {overview}
      </p>

      <button className='favButton' onClick={fav ? removeFromFav : addToFav}>
        {fav ? "Remove From Favorites" : "Add To Favorites"}
      </button>

      <button className='modalButton' onClick={() => setModal(current => !current)}>
        {"Show Details"}
      </button>

      {modal ? <Modal data={data} /> : ""}
    </div>
  );
}
