import React from 'react';
import './Footer.css';
import gh from "../../assets/images/icons/gh.png"
import hr from "../../assets/images/icons/hr.png"
import li from "../../assets/images/icons/li.png"
import fb from "../../assets/images/icons/fb.png"
import ig from "../../assets/images/icons/ig.png"
import em from "../../assets/images/icons/em.png"
import wa from "../../assets/images/icons/wa.png"
import tg from "../../assets/images/icons/tg.png"

export default function Footer() {

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
    <footer>
      All Rights Reserved For <a href="https://suhaib.info" target="_blank" rel="noreferrer">Suhaib Ahmad</a> © {(new Date()).getFullYear()}

      <ul>
        {links.map((link, i) => (
          <li stlye={{ width: `${1 / link.length * 100}%` }}>
            <a href={link.link} target="_blank" rel="noreferrer" key={i}>
              <img src={link.icon} alt="" width={"25px"} />
            </a>
          </li>
        ))}
      </ul>
    </footer>
  );
}
