import React from 'react'
import { Switch, Route } from 'react-router-dom'

import Homepage from './components/HomePage'
import About from './components/About/About'

const RouteHandler = () => (
    <Switch>
         <Route exact path="/" component={Homepage} />
         <Route exact path="/about" component={About} />
    </Switch>
)


export default RouteHandler;
