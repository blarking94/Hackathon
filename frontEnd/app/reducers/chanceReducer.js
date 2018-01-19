import * as types from '../constants/actionTypes'

export default function (state = {}, action){
    switch(action.type){
        case types.SET_DETAILS_RESPONSE:
            console.log("in reducer")
            console.log(action)
            return {...state, chance: action.chance};
        default:
            return state;
    }
}
