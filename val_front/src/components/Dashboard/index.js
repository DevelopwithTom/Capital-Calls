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
  getRow(call) {
    const cells = [];
    cells.push(<td>{call.id}</td>);
    cells.push(<td>{call.date}</td>);
    this.props.funds.map((item, i) => {
      cells.push(<td key={1}></td>);
    });

    call.drawdown_set.map(item => {
      for (var i = 0; i < this.props.funds.length; i++) {
        const fund = this.props.funds[i];
        if (fund.id == item.commitment.fund) {
          // we have a matching fund
          console.log("Match found");
          console.log(fund);
          cells[i + 2] = <td>{item.amount}</td>;
        }
      }
    });
    return cells;
  }
  render() {
    const { calls } = this.state;

    return (
      <div className="custom-container-dashboard">
        <div>
          <h4>Calls Dashboard</h4>

          <table className="table">
            <tr>
              <th>Call ID</th>
              <th>Date</th>
              {this.props.funds.map(item => (
                <th key={item.id}>{item.name}</th>
              ))}
            </tr>
            {calls.map((call, i) => (
              <tr key={i}>{this.getRow(call)}</tr>
            ))}
          </table>
        </div>
      </div>
    );
  }
}
