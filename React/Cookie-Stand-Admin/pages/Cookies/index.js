import axios from "axios";
import { useEffect, useState } from "react";
import Footer from "../../components/Footer";
import CreateForm from "../../components/Form";
import Spinner from "../../components/Spinner";
import ReportTable from "../../components/Table";
import { hourly_sales } from "../../data";

export default function Cookies({ token }) {
  const [list, setList] = useState([]);
  const [action, setAction] = useState("create");
  const [formData, setFormData] = useState({});
  const [loading, setLoading] = useState(false)

  const getData = async () => {
    setLoading(true);
    const config = { headers: { "Authorization": `Bearer ${token}` } };

    await axios.get("https://cookie-stand-api-suhaib.herokuapp.com/api/v1/cookie_stands/", config)
      .then(res => {
        setList(res.data)
        console.log("Data", res.data)
      })
      .catch(e => {
        console.log("GetAll error", e)
      })
      .finally(() => {
        setLoading(false);
      })
  };

  const onSuccess = () => {
    getData();
    setFormData({});
    setAction("create");
    document.getElementById(`data${list.length}`)?.scrollIntoView({ behavior: 'smooth' });
  };

  const createData = async (data) => {
    setLoading(true);
    const config = { headers: { "Authorization": `Bearer ${token}`, } };

    await axios.post("https://cookie-stand-api-suhaib.herokuapp.com/api/v1/cookie_stands/", data, config)
      .then(res => {
        onSuccess();
        console.log("Created", res)
      })
      .catch(e => {
        console.log("Create error", e)
      })
      .finally(() => {
        setLoading(false);
      });
  };

  const updateData = async (id, data) => {
    setLoading(true);
    const config = { headers: { "Authorization": `Bearer ${token}` } };

    await axios.put(`https://cookie-stand-api-suhaib.herokuapp.com/api/v1/cookie_stands/${id}`, data, config)
      .then(res => {
        onSuccess();
        console.log("Updated", res)
      })
      .catch(e => {
        console.log("Update error", e)
      })
      .finally(() => {
        setLoading(false);
      });
  };

  const deleteData = async (data) => {
    setLoading(true);
    const config = { headers: { "Authorization": `Bearer ${token}` } };

    await axios.delete(`https://cookie-stand-api-suhaib.herokuapp.com/api/v1/cookie_stands/${data}`, config)
      .then(res => {
        onSuccess();
        console.log("Deleted", res)
      })
      .catch(e => {
        console.log("Delete error", e)
      })
      .finally(() => {
        setLoading(false);
      });
  };

  useEffect(() => {
    getData()
  }, []);

  const onActionClick = (id, action) => {
    const data = list.find(data => data.id === id);

    action === "duplicate" ? (
      setFormData({ ...data, hourly_sales: hourly_sales, description: "Descriping", owner: 1 }),
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

  const onActionSubmit = () => {
    (action === "duplicate" || action === "create") ? (
      createData(formData)
    ) : action === "update" ? (
      updateData(formData.id, formData)
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

        {loading && (
          <div className="text-center py-2">
            <Spinner />
          </div>
        )}

        <ReportTable data={list} onActionClick={onActionClick} />
      </main>



      <Footer count={list.length} unique={list.reduce((locations, item) => locations.find(loc => loc === item.location) ? locations : locations = [...locations, item.location], []).length} />
    </>
  )
}
