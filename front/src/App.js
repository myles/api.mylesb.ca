import React from 'react';
import Relay from 'react-relay';

import logo from './logo.svg';
import './App.css';

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>{this.about.fullName}</h2>
        </div>
        <p className="App-intro">
          {this.about.firstName} is {this.about.age} years old.
        </p>
      </div>
    );
  }
}

export default Relay.createContainer(App, {
  fragments: {
    viewer: () => Relay.QL`
      query about {
        fullName
        firstName
        age
      }
    `
  }
});
