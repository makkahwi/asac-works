import React from 'react';
import { Nav, Navbar, Row } from 'react-bootstrap';
import em from "../../assets/images/icons/em.png";
import fb from "../../assets/images/icons/fb.png";
import gh from "../../assets/images/icons/gh.png";
import hr from "../../assets/images/icons/hr.png";
import ig from "../../assets/images/icons/ig.png";
import li from "../../assets/images/icons/li.png";
import tg from "../../assets/images/icons/tg.png";
import wa from "../../assets/images/icons/wa.png";

export default function Foot() {
  const { Link } = Nav;
  const { Brand } = Navbar;

  const links = [
    {
      link: "https://github.com/makkahwi",
      name: "GH",
      icon: gh
    },
    {
      link: "https://www.hackerrank.com/makkahwi",
      name: "HR",
      icon: hr
    },
    {
      link: "https://linkedin.com/in/makkahwi",
      name: "LI",
      icon: li
    },
    {
      link: "https://facebook.com/makkahwi",
      name: "FB",
      icon: fb
    },
    {
      link: "https://instagram.com/makkahwi",
      name: "IG",
      icon: ig
    },
    {
      link: "mailto:SuhaibAhmadAi@hotmail.com",
      name: "em",
      icon: em
    },
    {
      link: "https://wasap.my/601128094804",
      name: "wa",
      icon: wa
    },
    {
      link: "https://t.me/makkahwi",
      name: "tg",
      icon: tg
    },
  ]

  return (
    <Navbar bg="dark" variant="dark" className='px-4'>
      <Row className="w-100">
        <Brand className='copyright'>
          All Rights Reserved For <a href="https://suhaib.info" target="_blank" rel="noreferrer">Suhaib Ahmad</a> © {(new Date()).getFullYear()}
        </Brand>
      </Row>

      <Row className="w-100">
        <Nav className="float-right">
          {links.map((link, i) => (
            <Link className='Link' href={link.link} target="_blank">
              <img src={link.icon} alt="" width={"25px"} />
            </Link>
          ))}
        </Nav>
      </Row>
    </Navbar>
  );
}
