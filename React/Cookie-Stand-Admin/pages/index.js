import Head from "next/head";
import { useState } from "react";
import Header from "../components/Header";
import Cookies from "./Cookies";
import Landing from "./Landing";

export default function Home() {

  const [jwt, setJWT] = useState("")

  useState(() => {
    // const localStorage = window.localStorage;
    // localStorage.getItem("jwt") !== undefined ? setJWT(localStorage.getItem("jwt")) : ""
  }, [])

  return (
    <>
      <Head>
        <title>Cookie Stand Admin - Suhaib Ahmad</title>
      </Head>

      <Header token={jwt} setToken={setJWT} />

      {jwt.length > 0 ? (
        <Cookies token={jwt} />
      ) : (
        <Landing setToken={setJWT} />
      )}

    </>


  )
}
