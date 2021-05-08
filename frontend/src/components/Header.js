import React, { Component } from "react";
import NewUserModal from "./NewUserModal";
import LoginModal from "./LoginModal";

class Header extends Component {

    render() {
      return (
        <div className="header">
          <h1 className="header_text">
            Searching for Group
          </h1>
          <ul className="top_menu">
            <li className="menu_item">Find a Group</li>
            <li className="menu_item">My Groups</li>
            <li className="menu_item">Profile</li>
          </ul>
          <div class="action_btns">
            <LoginModal />
            <NewUserModal create={true} />
          </div>
        </div>
      );
    }
  }
  
  export default Header;