import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import Home from "./components/Home";
import Dashboard from "./components/Dashboard";
import NewCall from "./components/NewCall";

const Routes = props => (
  <Router>
    <Route exact path="/" component={Home} />
    <Route exact path="/dashboard" component={Dashboard} />
    <Route exact path="/newcall" component={NewCall} />
  </Router>
);

export default Routes;
