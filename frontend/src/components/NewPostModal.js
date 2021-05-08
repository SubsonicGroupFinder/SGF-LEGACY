import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewPostForm from "./NewPostForm";

class LoginModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  render() {
    const create = this.props.create;

    var title = "New Post";

    var button = (
    <Button
        onClick={this.toggle}
        className="start_new_post"
    >
        +
    </Button>
    );

    return (
      <Fragment>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>

          <ModalBody>
            <NewPostForm
              toggle={this.toggle}
              user={this.props.user}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default LoginModal;