import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class LoginForm extends React.Component {
  state = {
    pk: 0,
    title: "",
    body: "",
    tags: "",
    platform: "",
    game: ""
  };

  componentDidMount() {
    if (this.props.user) {
      const { pk, title, body, tags, platform, game } = this.props.state;
      this.setState({ pk, title, body, tags, platform, game });
    }
  }

  onChange = e => {
    // this.setState({ [e.target.title]: e.target.value });
    if (e.target.name === "user_name"){
      this.setState({
        title: e.target.value
      })
    }

    if (e.target.name === "game"){
      this.setState({
        game: e.target.value
      })
    }

    if (e.target.name === "platform"){
      this.setState({
        platform: e.target.value
      })
    }

    if (e.target.name === "body"){
      this.setState({
        body: e.target.value
      })
    }

    if (e.target.name === "tags"){
      this.setState({
        tags: e.target.value
      })
    }


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
          <Label for="game">Game:</Label>
          <Input
            type="text"
            name="game"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.game)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="platform">Platform:</Label>
          <Input
            type="text"
            name="platform"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.platform)}
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