import React, { Component } from 'react';
import RouteHandler from '../routes'
import Header from '../components/Header'

const App = () => (
  <div className="container-fluid">
    <Header />
    <main>
      <RouteHandler />
    </main>
  </div>
)

export default App;
