import React, { useState } from 'react';
import './TourDetails.css';
import Data from "../../data/db"
import { useParams } from "react-router-dom";

export default function TourDetails() {
  const { id } = useParams();
  const { name, info, image, price } = Data.find(des => des.id === id);

  const [textMode, setTextMode] = useState(false);

  return (
    <section id="tourDetails">
      <div className="city">
        <img src={image} alt="" className='img' />

        <h2>
          {name}
        </h2>

        <h4>
          {`Price $${price}`}
        </h4>

        <p className={textMode ? "" : "excerpt"}>
          {info}
        </p>
        <span onClick={() => setTextMode(current => !current)} className="showText">
          {textMode ? "Show Less" : "Show More"}
        </span>
      </div>
    </section>
  );
}
