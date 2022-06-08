
function Footer() {
  return (
    <footer className="bg-orange-500">
      <div className="py-6 lg:mx-4 xl:mx-12 text-white">
        <p>
          All rights reserved for
          {" "}
          <a href="https://Suhaib.dev" target="_blank">
            Suhaib Ahmad
          </a>
          {" "}
          &copy; {new Date().getFullYear()}
        </p>
      </div>
    </footer>
  )
}

export default Footer