import { combineReducers } from 'redux'
import { routerReducer } from 'react-router-redux'

// Combines all reducers to a single reducer function
export default combineReducers({
     router: routerReducer
});