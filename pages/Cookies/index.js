import axios from "axios";
import { useEffect, useState } from "react";
import Footer from "../../components/Footer";
import CreateForm from "../../components/Form";
import ReportTable from "../../components/Table";

export default function Cookies({ token }) {
  const [list, setList] = useState([]);
  const [action, setAction] = useState("create");
  const [formData, setFormData] = useState({});

  const getData = async () => {
    const config = {
      header: { "Authoziation": `Bearer ${token}` }
    };

    await axios.get("https://cookie-stand-api-suhaib.herokuapp.com/api/v1/cookie_stands/", config)
      .then(res => {
        setList(res)
        console.log("res", res)
      })
      .catch(e => {
        console.log("GetAll error", e)
      });
  };

  const onSuccess = () => {
    getData();
    setFormData({});
    setAction("create");
    console.log("res", res);
    document.getElementById(`data${list.length}`)?.scrollIntoView({ behavior: 'smooth' });
  };

  const createData = async (data) => {
    const config = {
      header: { "Authoziation": `Bearer ${token}` }
    };

    await axios.post("https://cookie-stand-api-suhaib.herokuapp.com/api/v1/cookie_stands/", config, data)
      .then(res => {
        onSuccess();
        console.log("res", res)
      })
      .catch(e => {
        console.log("Create error", e)
      });
  };

  const updateData = async (id, data) => {
    const config = {
      header: { "Authoziation": `Bearer ${token}` }
    };

    await axios.put("https://cookie-stand-api-suhaib.herokuapp.com/api/v1/cookie_stands/", config, id, data)
      .then(res => {
        onSuccess();
        console.log("res", res)
      })
      .catch(e => {
        console.log("Update error", e)
      });
  };

  const deleteData = async (data) => {
    const config = {
      header: { "Authoziation": `Bearer ${token}` }
    };

    await axios.delete("https://cookie-stand-api-suhaib.herokuapp.com/api/v1/cookie_stands/", config, data)
      .then(res => {
        onSuccess();
        console.log("res", res)
      })
      .catch(e => {
        console.log("Delete error", e)
      });
  };

  useEffect(() => {
    getData()
  }, []);

  const onActionClick = (id, action) => {
    const data = list.find(data => data.id === id);

    action === "duplicate" ? (
      setFormData(data),
      setAction("duplicate"),
      window.scrollTo({ top: 0, left: 0, behavior: 'smooth' })
    ) : action === "view" ? (
      setFormData(data),
      setAction("view"),
      window.scrollTo({ top: 0, left: 0, behavior: 'smooth' })
    ) : action === "update" ? (
      setFormData(data),
      setAction("update"),
      window.scrollTo({ top: 0, left: 0, behavior: 'smooth' })
    ) : action === "delete" && (
      setFormData(data),
      setAction("delete"),
      window.scrollTo({ top: 0, left: 0, behavior: 'smooth' })
    )
  };

  const onActionSubmit = (data) => {
    (action === "duplicate" || action === "create") ? (
      createData(data)
    ) : action === "update" ? (
      updateData(formData)
    ) : action === "delete" && (
      deleteData(formData.id)
    )
  };

  const onReset = () => {
    setFormData({})
    setAction("create")
  };

  const onFormDataChange = (key, value) => {
    let newFormData = { ...formData }
    newFormData[key] = value
    setFormData(newFormData)
  };

  return (
    <>
      <main className="py-10 px-10">
        <CreateForm onSubmit={onActionSubmit} action={action} data={formData} onChange={onFormDataChange} reset={onReset} length={list.length} />
        {list.length ? (<ReportTable data={list} onActionClick={onActionClick} />) : <h2 className="text-center pt-5">No Cookie Stands Available</h2>}
      </main>

      <Footer count={list.length} unique={list.reduce((locations, item) => locations.find(loc => loc === item.location) ? locations : locations = [...locations, item.location], []).length} />
    </>


  )
}
