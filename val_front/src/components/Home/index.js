import React, { Component } from "react";
import { Button } from "reactstrap";
import "./style.css";
import { Link } from "react-router-dom";

export default class App extends Component {
  render() {
    return (
      <div>
        <Link to="/dashboard" className="btn btn-secondary">
          Capital Call
        </Link>
      </div>
    );
  }
}
