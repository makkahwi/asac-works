import Head from "next/head";
import { useState } from "react";
import Footer from "../components/Footer";
import Form from "../components/Form";
import Header from "../components/Header";
import List from "../components/List";

export default function Home() {
  const [list, setList] = useState([
    {
      location: "Amman",
      minCustomers: 1,
      maxCustomers: 2,
      avgCookies: 3
    }
  ]);

  const [action, setAction] = useState("create")

  const [formData, setFormData] = useState({})

  const onAction = (id, action) => {
    action === "duplicate" ? (
      setFormData(list[id]),
      setAction("duplicate"),
      console.log("duplicate")
    ) : action === "view" ? (
      setFormData(list[id]),
      setAction("view"),
      console.log("view")
    ) : action === "update" ? (
      setFormData(list[id]),
      setAction("update"),
      console.log("update")
    ) : action === "delete" && (
      setFormData(list[id]),
      setAction("delete"),
      console.log("delete")
    )
  };

  const onReset = () => {
    setFormData({})
    setAction("create")
  }

  const addToList = formData => setList(current => [...current, formData]);

  return (
    <>
      <Head>
        <title>Cookie Stand Admin - Suhaib Ahmad</title>
      </Head>

      <Header />

      <main className="py-10 px-10">
        <Form onSubmit={addToList} action={action} data={formData} reset={onReset} />
        <List data={list} onAction={onAction} />
      </main>

      <Footer />
    </>


  )
}
