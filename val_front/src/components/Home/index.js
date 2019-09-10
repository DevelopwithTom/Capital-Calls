import React, { Component } from "react";
import { Button } from "reactstrap";
import "./style.css";
import { Link } from "react-router-dom";

export default class App extends Component {
  render() {
    return (
      <div className="container">
        <div className="home-button">
          <Button
            size="lg"
            block
            outline
            color="secondary"
            tag={Link}
            to="/dashboard"
          >
            Capital Calls
          </Button>
        </div>
      </div>
    );
  }
}
