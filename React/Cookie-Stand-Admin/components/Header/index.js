import links from "../../Routes/_nav";

export default function Header({ token, setToken }) {
  return (
    <header className="bg-orange-500">
      <div className="py-6 lg:mx-4 xl:mx-12">
        <nav className="flex items-center justify-between flex-wrap">
          <div className="flex items-center flex-no-shrink text-white mr-6">
            <h2 className="text-2xl text-white">
              Cookie Stand Admin
            </h2>
          </div>

          <div id="main-nav" className="w-full flex-grow lg:flex items-center lg:w-auto hidden">
            <div className="text-sm lg:flex-grow mt-2 animated jackinthebox xl:mx-8">
              {links.map((link, i) => (
                <button href={link.link} className="block lg:inline-block text-md font-bold  text-white-500  sm:hover:border-white-400  mx-2 focus:text-blue-500  p-1 hover:bg-gray-300 sm:hover:bg-transparent rounded-lg" key={i}>
                  {link.title}
                </button>
              ))}

              {token.length > 0 ? (
                <button onClick={() => { setToken(""), localStorage.setItem("jwt", null) }} className="block lg:inline-block text-md font-bold  text-white-500  sm:hover:border-white-400  mx-2 focus:text-blue-500  p-1 hover:bg-gray-300 sm:hover:bg-transparent rounded-lg">
                  Sign Out
                </button>
              ) : (
                <button className="block lg:inline-block text-md font-bold  text-white-500  sm:hover:border-white-400  mx-2 focus:text-blue-500  p-1 hover:bg-gray-300 sm:hover:bg-transparent rounded-lg">
                  Sign In
                </button>
              )}
            </div>
          </div>
        </nav>
      </div>
    </header>
  )
}