import { createStore, applyMiddleware } from 'redux'
import { routerMiddleware } from 'react-router-redux'
import createHistory from 'history/createBrowserHistory'
import createSagaMiddleware from 'redux-saga'
import combineReducers from './reducers'
import sagas from './sagas'

let middlewares = []

// Create Middleware
const sagaMiddleware = createSagaMiddleware()
middlewares.push(sagaMiddleware)

const history = createHistory()
const routingMiddleware = routerMiddleware(history)
middlewares.push(routingMiddleware)

let middleware = applyMiddleware(...middlewares)

const store = createStore(combineReducers, middleware);

sagaMiddleware.run(sagas);

export { store, history }
