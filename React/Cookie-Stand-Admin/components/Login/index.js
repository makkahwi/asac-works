import axios from "axios";
import { useState } from "react";
import Spinner from "../Spinner";

export default function Login({ setReg, setToken }) {

  const [loading, setLoading] = useState(false)

  const onLogin = async (e) => {
    e.preventDefault();

    setLoading(true)

    const formData = {
      username: "admin" || e.target.username.value,
      password: "123" || e.target.password.value,
    };

    await axios.post("https://cookie-stand-api-suhaib.herokuapp.com/api/token/", formData)
      .then(res => {
        setToken(res.data.access)
        localStorage.setItem("jwt", res.data.access)
        console.log("token", res.data.access)
      })
      .catch(e => {
        console.log("login error", e)
      })
      .finally(() => {
        setLoading(false)
      })
  };

  return (
    <div className="flex items-center justify-center py-2 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Sign in</h2>
        </div>

        <form onSubmit={onLogin} className="mt-8 space-y-6">
          <input type="hidden" name="remember" value="true" />

          <div className="shadow-sm -space-y-px">
            <div className="grid grid-cols-2">
              <div>
                <input name="username" defaultValue={"admin"} type="text" required className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-l-md focus:outline-none focus:ring-orange-500 focus:border-orange-500 focus:z-10 sm:text-sm" placeholder="Username" />
              </div>

              <div>
                <input name="password" defaultValue={"123"} type="password" autoComplete="current-password" required className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-r-md focus:outline-none focus:ring-orange-500 focus:border-orange-500 focus:z-10 sm:text-sm" placeholder="Password" />
              </div>
            </div>
          </div>

          <div>
            <button type="submit" disabled={loading} className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">
              Sign in
            </button>

            {loading && (
              <div className="text-center py-2">
                <Spinner />
              </div>
            )}
          </div>
        </form>

        <div className="flex items-center justify-between">
          <div className="text-sm">
            <a className="font-medium text-orange-600 hover:text-orange-500"> Forgot your password? </a>
          </div>

          {/* <div className="text-sm">
            <button onClick={() => setReg(true)} className="bg-transparent hover:bg-orange-500 text-orange-700 font-semibold hover:text-white py-2 px-4 border border-orange-500 hover:border-transparent rounded">
              Sign Up
            </button>
          </div> */}
        </div>
      </div>
    </div>
  )
}