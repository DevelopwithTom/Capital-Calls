import React, { Component } from "react";
import "./style.css";
import { Button, Form, FormGroup, Label, Input, FormText } from "reactstrap";
import axios from "axios";
import { Link } from "react-router-dom";

export default class App extends Component {
  state = {
    date: null,
    investmentName: "",
    amount: 0
  };
  update = e => this.setState({ [e.target.name]: e.target.value });

  handleSubmit = e => {
    e.preventDefault();
    const { date, investmentName, amount } = this.state;
    axios
      .post("http://127.0.0.1:8000/api/calls/", {
        date,
        investmentName,
        amount
      })
      .then(response => {
        this.setState({
          date: "",
          investmentName: "",
          amount: 0
        });
        console.log(response);
      })
      .catch(error => {
        console.log(error);
      });
  };

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
    const { date, investmentName, amount, commitments } = this.state;
    return (
      <div className="container">
        <h1 className="example">New Call</h1>
        <Link to="/dashboard" className="btn btn-secondary">
          Dashboard
        </Link>
        <Link to="/newcall" className="btn btn-secondary">
          New Call
        </Link>
        <div className="flex-container">
          <div className="flex-col">
            <Form onSubmit={this.handleSubmit}>
              <FormGroup>
                <Label for="exampleDate">Date</Label>
                <Input
                  type="date"
                  name="date"
                  id="exampleDate"
                  placeholder="date placeholder"
                  value={date}
                  onChange={this.update}
                />
              </FormGroup>
              <FormGroup>
                <Label for="exampleSelect">Rules</Label>
                <Input type="select" name="select" id="exampleSelect">
                  <option>First in first out</option>
                </Input>
              </FormGroup>
              <FormGroup>
                <Label for="exampleText">Investment Name</Label>
                <Input
                  type="text"
                  name="investmentName"
                  id="exampleText"
                  placeholder="Investment Name"
                  value={investmentName}
                  onChange={this.update}
                />
              </FormGroup>
              <FormGroup>
                <Label for="exampleNumber">Amount</Label>
                <Input
                  type="number"
                  name="amount"
                  id="exampleNumber"
                  placeholder="Amount"
                  value={amount}
                  onChange={this.update}
                />
              </FormGroup>
              <Button>Submit</Button>
            </Form>
          </div>
          <div className="flex-col">
            <table className="table">
              <tr>
                <th>Commitment ID</th>
                <th>Fund ID</th>
                <th>Amount</th>
              </tr>
              {commitments.map((commitment, i) => (
                <tr className="Commitment">
                  <td>{commitment.id}</td>
                  <td>{commitment.deposit}</td>
                  <td>{commitment.amount}</td>
                </tr>
              ))}
            </table>
          </div>
        </div>
      </div>
    );
  }
}
