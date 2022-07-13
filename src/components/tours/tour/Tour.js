import React from 'react';
import './Tour.css';

export default function Tour({ name, image }) {

  return (
    <div className="destination">
      <div>
        <img src={image} alt="" className='image' />
      </div>

      <p className='name'>
        {name}
      </p>
    </div>
  );
}
