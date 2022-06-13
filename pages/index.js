import Head from "next/head";
import { useState } from "react";
import Footer from "../components/Footer";
import CreateForm from "../components/Form";
import Header from "../components/Header";
import ReportTable from "../components/Table";

export default function Home() {
  const [list, setList] = useState([]);

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
        <CreateForm onSubmit={addToList} action={action} data={formData} reset={onReset} />
        {list.length ? (<ReportTable data={list} onAction={onAction} />) : <h2 className="text-center pt-5">No Cookie Stands Available</h2>}
      </main>

      <Footer count={list.length} />
    </>


  )
}
