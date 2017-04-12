import React from 'react';
import ReactDOM from 'react-dom';
import Relay from 'react-relay';

import App from './App';
import Route from './routes';

import './index.css';

ReactDOM.render(
  <Relay.Renderer
    environment={Relay.Store}
    Container={App}
    queryConfig={new Route()}
  />,
  document.getElementById('root')
);
