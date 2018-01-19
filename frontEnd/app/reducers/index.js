import { combineReducers } from 'redux'
import { routerReducer } from 'react-router-redux'
import chanceReducer from './chanceReducer'

// Combines all reducers to a single reducer function
export default combineReducers({
     router: routerReducer,
     chance : chanceReducer
});
