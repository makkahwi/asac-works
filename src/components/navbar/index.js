import React from 'react';
import { Nav, Navbar } from 'react-bootstrap';
import { Link as RouterLink } from 'react-router-dom';

export default function NavBar() {
  const { Brand } = Navbar;
  const { Link } = Nav;

  const links = [
    {
      title: "Home",
      link: "/"
    },
    {
      title: "All Movies",
      link: "/all"
    },
    {
      title: "Fav Movies",
      link: "/favs"
    }
  ];

  return (
    <Navbar fixed="top" bg="dark" variant="dark" className='navbar px-4'>
      <Brand>
        {/* <img src={logo} alt="" className='logo' /> */}
        NetenFlix
      </Brand>

      <Nav>
        {links.map((link, i) => (
          <Link className='link' key={i}>
            <RouterLink to={link.link} >
              {link.title}
            </RouterLink>
          </Link>
        ))}
      </Nav>
    </Navbar>
  );
}
