/*import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
*/

import React, { Component, Fragment } from "react";
import Header from "./components/Header";
import Home from "./components/Home";

import { API_URL } from "./constants/index";

class App extends Component {
    state = {
    posts: []
  };

  async componentDidMount() {
    // try {
    //   const res = await fetch(API_URL);
    //   const posts = await res.json();
    //   console.log(posts);
    //   this.setState({
    //     posts
    //   });
    // } catch (e) {
    //   console.log(e);
    // }
  }

  render() {
    return (
      <Fragment>
        <Header />
        <Home />
      </Fragment>
    );
  }
}

export default App;
