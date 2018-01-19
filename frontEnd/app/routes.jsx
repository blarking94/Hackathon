import React from 'react'
import { Switch, Route } from 'react-router-dom'

import Homepage from './components/HomePage'
import Review from './components/review/Review'

const RouteHandler = () => (
    <Switch>
         <Route exact path="/" component={Homepage} />
         <Route exact path="/review" component={Review} />
    </Switch>
)


export default RouteHandler;
