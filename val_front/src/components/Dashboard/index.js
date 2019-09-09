import React, { Component } from "react";
import { Button } from "reactstrap";
import "./style.css";
import axios from "axios";
import { Link } from "react-router-dom";

export default class App extends Component {
  state = {
    commitments: []
  };

  componentDidMount() {
    axios
      .get("http://127.0.0.1:8000/api/commitments/")
      .then(response => {
        // handle success
        console.log(response);
        this.setState({
          commitments: response.data
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
    const { commitments } = this.state;

    return (
      <div className="container">
        <div className="Commitments">
          <h1 className="example">Dashboard</h1>
          <Link to="/dashboard" className="btn btn-secondary">
            Dashboard
          </Link>
          <Link to="/newcall" className="btn btn-secondary">
            New Call
          </Link>

          <table className="table">
            <tr>
              <th>index</th>
              <th>Date</th>
              <th>Amount</th>
            </tr>
            {commitments.map((commitment, i) => (
              <tr className="Commitment">
                <td>{i + 1}</td>
                <td>{commitment.date}</td>
                <td>{commitment.amount}</td>
              </tr>
            ))}
          </table>
        </div>
      </div>
    );
  }
}
