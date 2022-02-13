import React, { Suspense, lazy } from 'react';
import './App.css';

const Home = lazy(() => import('./views/home'));

function App() {
  return (
    <div className="App">
      <Suspense fallback={"Loading"}>
        <Home />
      </Suspense>
    </div>
  );
}

export default App;
