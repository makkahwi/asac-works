import 'bootstrap/dist/css/bootstrap.min.css';
import React, { lazy } from 'react';
import { BrowserRouter, Redirect, Route, Switch } from "react-router-dom";
import Footer from '../src/components/footer';
import NavBar from "../src/components/navbar";
import './App.css';

const Home = lazy(() => import('./views/home'));
const All = lazy(() => import('./views/all'));
const Favs = lazy(() => import('./views/favs'));

export default function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <NavBar />

        <Switch>
          <Route path="/" exact name="Home" render={props => <Home {...props} />} />
          <Route path="/all" exact name="All" render={props => <All {...props} />} />
          <Route path="/favs" exact name="Favs" render={props => <Favs {...props} />} />
          <Redirect from="*" to="/" />
        </Switch>

        <Footer />
      </BrowserRouter>
    </div>
  );
};