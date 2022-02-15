import React from 'react';
import { Nav, Navbar } from 'react-bootstrap';

export default function NavBar() {
  const { Brand } = Navbar;
  const { Link } = Nav;

  const links = [
    {
      title: "Home",
      link: "#header"
    },
    {
      title: "Fav Movies",
      link: "#favMovies"
    },
    {
      title: "All Movies",
      link: "#allMovies"
    },
  ];

  return (
    <Navbar fixed="top" bg="dark" variant="dark" className='navbar px-4'>
      <Brand>
        {/* <img src={logo} alt="" className='logo' /> */}
        NetenFlix
      </Brand>

      <Nav>
        {links.map((link, i) => (
          <Link className='link' href={link.link} key={i}>
            {link.title}
          </Link>
        ))}
      </Nav>
    </Navbar>
  );
}
