import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import PostList from "./PostList";
import NewPostModal from "./NewPostModal";
import { Button } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    posts: []
  };

  componentDidMount() {
    this.resetState();
  }

  getPosts = () => {
    axios.get(API_URL+'getPosts/').then(res => this.setState({ posts: res.data })).catch(function (error) {
        if (error.response) {
          // Request made and server responded
          console.log(error.response.data);
          console.log(error.response.status);
          console.log(error.response.headers);
        } else if (error.request) {
          // The request was made but no response was received
          console.log(error.request);
        } else {
          // Something happened in setting up the request that triggered an Error
          console.log('Error', error.message);
        }
    });
  };

  resetState = () => {
    this.getPosts();
  };

  render() {
    var button = (
    <Button
        onClick={this.toggle}
    >
        Find a Group
    </Button>
    );
    return (
      <Container style={{ marginTop: "20px" }}>
          <div className="new_post">
            <NewPostModal create={true} resetState={this.resetState} />
          </div>
          <div className="post_list">
            <PostList
                posts={this.state.posts}
                resetState={this.resetState}
                />
          </div>
      </Container>
    );
  }
}

export default Home;