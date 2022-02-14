import React from 'react';
import logo from '../../logo.svg';
import './style.css';

export default function NavBar() {

  return (
    <header>
      <ul>
        <li>
          <img src={logo} alt="" height="20px" />
        </li>

        <li>
          Suhaib's Travel Destination
        </li>

        <li>
          <a href="#home">Home</a>
        </li>

        <li>
          <a href="#tours">Tours</a>
        </li>
      </ul>
    </header>
  );
}
