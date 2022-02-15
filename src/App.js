import React, { lazy } from 'react';
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";
import Footer from '../src/components/footer/Footer';
import NavBar from "../src/components/navbar/Navbar";
import './App.css';

const Home = lazy(() => import('./components/home/Home'));
const Destination = lazy(() => import('./components/tourDetails/TourDetails'));

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