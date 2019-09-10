import React, { Component } from "react";
import { Button } from "reactstrap";
import "./style.css";
import axios from "axios";
import { Link } from "react-router-dom";

export default class App extends Component {
  state = {
    calls: []
  };

  componentDidMount() {
    axios
      .get("http://127.0.0.1:8000/api/calls/")
      .then(response => {
        // handle success
        console.log(response);
        this.setState({
          calls: response.data
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
    const { calls } = this.state;

    return (
      <div className="container">
        <div>
          <h4>Dashboard</h4>

          <table className="table">
            <tr>
              <th>Date</th>
              <th>Call ID</th>
              <th>Fund 1</th>
              <th>Fund 2</th>
              <th>Fund 3</th>
              <th>Fund 4</th>
            </tr>
            {calls.map((call, i) => (
              <tr>
                <td>{call.date}</td>
                <td>{call.id}</td>
                <td>{call.amount}</td>
                <td>{call.amount}</td>
                <td>{call.amount}</td>
                <td>{call.amount}</td>
              </tr>
            ))}
          </table>
        </div>
      </div>
    );
  }
}
