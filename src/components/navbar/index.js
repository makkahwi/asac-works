import React from 'react';
import { Link } from "react-router-dom";
import logo from '../../assets/images/logo.png';
import './style.css';

export default function NavBar() {

  return (
    <header>
      <ul>
        <li className='li'>
          {/* <img src={logo} alt="" className='logo' /> */}
          NetenFlix
        </li>

        <li className='li'>
          {/* <Link to="/"> */}
          <a href='#'>
            Home
          </a>
          {/* </Link> */}
        </li>

        <li className='li'>
          <a href='#favMovies'>
            Fav Movies
          </a>
        </li>

        <li className='li'>
          <a href='#allMovies'>
            All Movies
          </a>
        </li>
      </ul>
    </header >
  );
}
