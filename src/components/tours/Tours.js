import React from 'react';
import Data from "../../data/db"
import Tour from "./tour/Tour"
import { Link } from "react-router-dom";
import './Tours.css';

export default function Tours() {

  return (
    <section id="tours">
      <h1>
        Available Travels
      </h1>

      <div className="gallery">
        {Data.map((destination, i) => {
          const { id, name, image } = destination;

          return (
            <Link to={`/destination/${id}`}>
              <Tour name={name} image={image} key={i} />
            </Link>
          )
        }
        )}
      </div>
    </section>
  );
}
