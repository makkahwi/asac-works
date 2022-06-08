export default function Header() {
  const links = [
    {
      title: "Home",
      link: "/"
    }
  ];

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
                <a href={link.link} className="block lg:inline-block text-md font-bold  text-white-500  sm:hover:border-white-400  mx-2 focus:text-blue-500  p-1 hover:bg-gray-300 sm:hover:bg-transparent rounded-lg" key={i}>
                  {link.title}
                </a>
              ))}
            </div>
          </div>
        </nav>
      </div>
    </header>
  )
}