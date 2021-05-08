import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class LoginForm extends React.Component {
  state = {
    pk: 0,
    title: "",
    body: "",
    tags: ""
  };

  componentDidMount() {
    if (this.props.student) {
      const { pk, title, body, tags } = this.props.state;
      this.setState({ pk, title, body, tags });
    }
  }

  onChange = e => {
    this.setState({ [e.target.title]: e.target.value });
  };

  sendPost = e => {
    e.preventDefault();
    axios.post(API_URL+'sendPost/', this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    }).catch(console.log('there was an error'));
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.sendPost}>
          <FormGroup>
          <Label for="user_name">Title:</Label>
          <Input
            type="text"
            name="user_name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.title)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="body">Body:</Label>
          <Input
            type="textarea"
            name="body"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.body)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="tags">Tags:</Label>
          <Input
            type="text"
            name="tags"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.tags)}
          />
        </FormGroup>
        <Button>Save</Button>
      </Form>
    );
  }
}

export default LoginForm;