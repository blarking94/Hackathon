import * as types from './actionTypes'

export function submitDetails(roleTitle, roleLevel, industryExpetise, technologyExpetise, gallup, certifications){
    return {
        type: types.SUBMIT_DETAILS, roleTitle, roleLevel, industryExpetise, technologyExpetise, gallup, certifications
    };
}
