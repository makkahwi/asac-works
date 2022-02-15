import React, { lazy } from 'react';
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";
import Footer from '../src/components/footer';
import NavBar from "../src/components/navbar";
import './App.css';

const Home = lazy(() => import('./views/home'));

export default function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <NavBar />

        <Switch>
          <Route path="/" exact name="Home" render={props => <Home {...props} />} />
          <Redirect from="*" to="/" />
        </Switch>

        <Footer />
      </BrowserRouter>
    </div>
  );
};