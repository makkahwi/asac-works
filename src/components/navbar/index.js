import React from 'react';
import { Link } from "react-router-dom";
import logo from '../../assets/images/logo.png';
import './style.css';

export default function NavBar() {

  return (
    <header>
      <ul>
        <li className='li'>
          <img src={logo} alt="" className='logo' />
        </li>

        <li className='li'>
          <Link to="/">
            Home
          </Link>
        </li>
      </ul>
    </header >
  );
}
