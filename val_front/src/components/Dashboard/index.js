import React, { Component } from "react";
import { Button } from "reactstrap";
import "./style.css";
import axios from "axios";
import { Link } from "react-router-dom";

export default class App extends Component {
  state = {
    drawdowns: []
  };

  componentDidMount() {
    axios
      .get("http://127.0.0.1:8000/api/drawdowns/")
      .then(response => {
        // handle success
        console.log(response);
        this.setState({
          drawdowns: response.data
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
    const { drawdowns } = this.state;

    return (
      <div className="container">
        <div className="Drawdowns">
          <h1 className="example">Dashboard</h1>

          <table className="table">
            <tr>
              <th>index</th>
              <th>Date</th>
              <th>Amount</th>
            </tr>
            {drawdowns.map((drawdown, i) => (
              <tr className="Commitment">
                <td>{i + 1}</td>
                <td>{drawdown.date}</td>
                <td>{drawdown.amount}</td>
              </tr>
            ))}
          </table>
        </div>
      </div>
    );
  }
}
