import React, { lazy } from 'react';
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";
import Footer from '../src/components/footer';
import NavBar from "../src/components/navbar";
import './App.css';

const Home = lazy(() => import('./views/home'));
const Destination = lazy(() => import('./views/tourDetails'));

export default function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <NavBar />

        <Switch>
          <Route path="/" exact name="Home" render={props => <Home {...props} />} />
          <Route path="/destination/:id" exact name="Destinations" render={props => <Destination {...props} />} />
          <Redirect from="*" to="/" />
        </Switch>

        <Footer />
      </BrowserRouter>
    </div>
  );
};