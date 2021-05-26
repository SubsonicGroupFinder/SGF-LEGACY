import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewUserForm extends React.Component {
  state = {
    pk: 0,
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    password1: "",
    password2: ""
  };

  componentDidMount() {
    if (this.props.student) {
      const { pk, username, first_name, last_name, password2, password1, email } = this.props.user;
      this.setState({ pk, username, first_name, last_name, password2, password1, email });
    }
  }

  onChange = e => {
    // this.setState({ [e.target.username]: e.target.value });
    if ( e.target.name === "user_name")
      this.setState({ username: e.target.value})
    if ( e.target.name === "first_name")
      this.setState({ first_name: e.target.value})
    if ( e.target.name === "last_name")
      this.setState({ last_name: e.target.value})
    if ( e.target.name === "email")
      this.setState({ email: e.target.value})
    if ( e.target.name === "password")
      this.setState({ password1: e.target.value})
    if ( e.target.name === "confirm_password")
      this.setState({ password2: e.target.value})
    
  };

  createUser = e => {
    e.preventDefault();
    axios.post(API_URL+'custom/register/', this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editUser = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.user ? this.editUser : this.createUser}>
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
          <Label for="first_name">First Name:</Label>
          <Input
            type="text"
            name="first_name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.first_name)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="last_name">Last Name:</Label>
          <Input
            type="text"
            name="last_name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.last_name)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="email">Email:</Label>
          <Input
            type="email"
            name="email"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.email)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="password">Password:</Label>
          <Input
            type="password"
            name="password"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.password1)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="confirm_password">Confirm Password:</Label>
          <Input
            type="password"
            name="confirm_password"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.password2)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewUserForm;