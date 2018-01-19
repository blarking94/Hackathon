import * as types from '../constants/actionTypes'

export default function (state = {}, action){
    switch(action.type){
        case types.SET_DETAILS_RESPONSE:
            return {...state, chance: action.chance};
        default:
            return state;
    }
}
