import React from 'react';
import Data from "../../data/db"
import './style.css';

export default function Tours() {

  return (
    <section id="tours">
      <div className="gallery">
        {Data.map((destination, i) => {
          const { name, image } = destination;

          return (
            <div className="destination">
              <div>
                <img src={image} alt="" />
              </div>

              <p className='desc'>
                {`${i + 1}- ${name}`}
              </p>
            </div>
          )
        }
        )}
      </div>
    </section>
  );
}
