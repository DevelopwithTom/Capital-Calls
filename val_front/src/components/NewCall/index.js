import React, { Component } from "react";
import "./style.css";
import {
  Button,
  Form,
  FormGroup,
  Label,
  Input,
  FormText,
  Table
} from "reactstrap";
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
          commitments: response.data.map(item => ({
            ...item,
            undrawn: parseFloat(item.undrawn),
            amount: parseFloat(item.amount)
          }))
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
    const { date, investmentName, amount } = this.state;
    let totalAmount = +this.state.amount || 0;

    const commitments = this.state.commitments.map(commitment => {
      let totalDrawdownNotice, remainingAfterDrawdown;

      let nextTotalAmount = totalAmount - commitment.undrawn;
      console.log(
        commitment.undrawn,
        "totalAmount:",
        totalAmount,
        "nextTotalAmount:",
        nextTotalAmount
      );

      totalDrawdownNotice = remainingAfterDrawdown = 0;

      totalDrawdownNotice = totalAmount;
      remainingAfterDrawdown = nextTotalAmount;
      if (nextTotalAmount > 0) {
        totalDrawdownNotice = commitment.undrawn;
      }

      if (remainingAfterDrawdown < 0) {
        remainingAfterDrawdown =
          commitment.undrawn + remainingAfterDrawdown < 0
            ? commitment.undrawn
            : Math.abs(remainingAfterDrawdown);
      } else {
        remainingAfterDrawdown = 0;
      }

      if (totalDrawdownNotice < 0) totalDrawdownNotice = 0;

      totalAmount = nextTotalAmount;

      return {
        ...commitment,
        totalDrawdownNotice,
        remainingAfterDrawdown
      };
    });

    return (
      <div className="custom_container">
        <h1>New Call</h1>

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
            <Table borderless hover>
              <thead>
                <tr>
                  <th style={{ width: "7%" }}>Commit ID</th>
                  <th style={{ width: "7%" }}>Fund ID</th>
                  <th style={{ width: "12%" }}>Date</th>
                  <th>Fund Name</th>
                  <th>Committed Amounts</th>
                  <th>Undrawn Capital before Current Drawdown</th>
                  <th>Drawdown Notice</th>
                  <th>Undrawn Capital after Current Drawdown</th>
                </tr>
              </thead>
              <tbody>
                {commitments.map((commitment, i) => (
                  <tr className="Commitment">
                    <td>{commitment.id}</td>
                    <td>{commitment.fund}</td>
                    <td>{commitment.date}</td>
                    <td>{commitment.fundname}</td>
                    <td>{commitment.amount}</td>
                    <td>{commitment.undrawn}</td>
                    <td>{commitment.totalDrawdownNotice}</td>
                    <td>{commitment.remainingAfterDrawdown}</td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </div>
        </div>
      </div>
    );
  }
}
