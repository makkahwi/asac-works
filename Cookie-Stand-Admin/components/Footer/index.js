
export default function Footer({ count, unique }) {
  return (
    <footer className="bg-orange-500">
      <div className="grid grid-cols-2 p-6 text-white">
        <div className="text-left">
          <p>
            {`${unique} Unique Locations Out of Total ${count} Locations Worldwide `}
          </p>
        </div>

        <div className="text-right">
          <p>
            All rights reserved for
            {" "}
            <u>
              <a href="https://Suhaib.dev" target="_blank">
                Suhaib Ahmad
              </a>
            </u>
            {" "}
            &copy; {new Date().getFullYear()}
          </p>
        </div>
      </div>
    </footer>
  )
}