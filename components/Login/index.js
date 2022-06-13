export default function Login({ setReg }) {
  return (
    <div className="flex items-center justify-center py-2 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Sign in</h2>
        </div>

        <form className="mt-8 space-y-6">
          <input type="hidden" name="remember" value="true" />

          <div className="shadow-sm -space-y-px">
            <div className="grid grid-cols-2">
              <div>
                <input name="username" type="text" required className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-l-md focus:outline-none focus:ring-orange-500 focus:border-orange-500 focus:z-10 sm:text-sm" placeholder="Username" />
              </div>

              <div>
                <input name="password" type="password" autocomplete="current-password" required className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-r-md focus:outline-none focus:ring-orange-500 focus:border-orange-500 focus:z-10 sm:text-sm" placeholder="Password" />
              </div>
            </div>
          </div>

          <div>
            <button type="submit" className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">
              Sign in
            </button>
          </div>
        </form>

        <div className="flex items-center justify-between">
          <div className="text-sm">
            <a className="font-medium text-orange-600 hover:text-orange-500"> Forgot your password? </a>
          </div>

          <div className="text-sm">
            <button onClick={() => setReg(true)} className="bg-transparent hover:bg-orange-500 text-orange-700 font-semibold hover:text-white py-2 px-4 border border-orange-500 hover:border-transparent rounded">
              Sign Up
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}