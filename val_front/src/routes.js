import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import axios from "axios";
import Home from "./components/Home";
import Dashboard from "./components/Dashboard";
import NewCall from "./components/NewCall";
import { Navigation } from "./components/Navbar/index.js";

import { Nav } from "reactstrap";

class Routes extends React.Component {
  constructor(props) {
    super(props);
    this.state = { funds: [] };
  }

  componentDidMount() {
    axios
      .get("http://127.0.0.1:8000/api/funds/")
      .then(response => {
        // handle success
        this.setState({
          funds: response.data
        });
      })
      .catch(error => {
        // handle error
        console.log(error);
      })
      .finally(() => {
        // always executed
      });
  }
  render() {
    return (
      <Router>
        <Navigation />
        <Route exact path="/" component={Home} />
        <Route
          exact
          path="/dashboard"
          render={() => <Dashboard funds={this.state.funds} />}
        />
        <Route exact path="/newcall" component={NewCall} />
      </Router>
    );
  }
}

export default Routes;
