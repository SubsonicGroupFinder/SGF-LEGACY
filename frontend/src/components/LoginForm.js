import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class LoginForm extends React.Component {
  state = {
    pk: 0,
    username: "",
    password: ""
  };

  componentDidMount() {
    if (this.props.student) {
      const { pk, username, password } = this.props.user;
      this.setState({ pk, username, password });
    }
  }

  onChange = e => {
    this.setState({ [e.target.username]: e.target.value });
  };

  loginUser = e => {
    e.preventDefault();
    axios.post(API_URL+'custom/login/', this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.loginUser}>
          <FormGroup>
          <Label for="user_name">Username:</Label>
          <Input
            type="text"
            name="user_name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.username)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="password">Password:</Label>
          <Input
            type="password"
            name="password"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.password)}
          />
        </FormGroup>
        <Button>Login</Button>
      </Form>
    );
  }
}

export default LoginForm;