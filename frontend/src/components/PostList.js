import React, { Component } from "react";
import {
    Card, CardImg, CardText, CardBody,
    CardTitle, CardSubtitle, Button
} from "reactstrap";

class PostList extends Component {
  render() {
    const posts = this.props.posts;
    return (
        <div>
          {!posts || posts.length <= 0 ? (
            <div className="no_posts">
                <h3>Oops, no one is looking for a group at the moment.</h3>
                <h3>Please try again later</h3>
            </div>
            ) : (
                posts.map(post => (
                    <Card className="post" key={post.key}>
                        {/* <CardImg top width="100%" src="/assets/318x180.svg" alt="Card image cap" /> */}
                        <CardBody>
                            <CardTitle className="post_title" tag="h5">{post.title}</CardTitle>
                            <CardText className="post_text">{post.body}</CardText>
                            <CardSubtitle tag="h6" className="post_tags">{post.tags}</CardSubtitle>
                        </CardBody>
                    </Card>
                ))
            )}
        </div>
    );
  }
}

export default PostList;